import json
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import (
    r2_score, mean_squared_error, accuracy_score,
    confusion_matrix, precision_score, recall_score, f1_score,
    silhouette_score
)
from mlxtend.frequent_patterns import apriori, association_rules

print("Step 1: Loading Online Retail.xlsx...")
df = pd.read_excel('Online Retail.xlsx')
raw_rows = len(df)
print(f"Raw rows: {raw_rows}")

# Cleaning pipeline (Labs 3, 4, 6)
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df_clean = df[~df['InvoiceNo'].astype(str).str.startswith('C')].copy()
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['UnitPrice'] > 0)].copy()
df_clean['SalesAmount'] = df_clean['Quantity'] * df_clean['UnitPrice']
df_clean['Month'] = df_clean['InvoiceDate'].dt.month
df_clean['Year'] = df_clean['InvoiceDate'].dt.year
df_clean['Period'] = df_clean['Year'].astype(str) + '-' + df_clean['Month'].astype(str).str.zfill(2)
df_clean['Date'] = df_clean['InvoiceDate'].dt.date.astype(str)
df_clean['DayOfWeek'] = df_clean['InvoiceDate'].dt.day_name()
df_clean['Hour'] = df_clean['InvoiceDate'].dt.hour.astype(str)

cleaned_rows = len(df_clean)
total_revenue = float(df_clean['SalesAmount'].sum())
unique_invoices = int(df_clean['InvoiceNo'].nunique())
unique_products = int(df_clean['Description'].dropna().nunique())
unique_countries = int(df_clean['Country'].nunique())
unique_customers = int(df_clean['CustomerID'].dropna().nunique())

q1 = float(df_clean['SalesAmount'].quantile(1/3))
q2 = float(df_clean['SalesAmount'].quantile(2/3))
print(f"Cleaned rows: {cleaned_rows}, Revenue: £{total_revenue:,.2f}, q1: {q1}, q2: {q2}")

# LAB 3: EDA Aggregations
print("Step 2: Processing Lab 3 EDA Aggregations...")
top_products_rev = (
    df_clean.groupby('Description')['SalesAmount']
    .agg(['sum', 'count'])
    .rename(columns={'sum': 'revenue', 'count': 'orders'})
    .sort_values('revenue', ascending=False)
    .head(50)
)
top_products_qty = (
    df_clean.groupby('Description')['Quantity']
    .sum()
    .sort_values(ascending=False)
    .head(50)
)
# Combined product summary for top 100
prod_agg = df_clean.groupby('Description').agg(
    revenue=('SalesAmount', 'sum'),
    quantity=('Quantity', 'sum'),
    orders=('InvoiceNo', 'nunique')
).sort_values('revenue', ascending=False)
prod_list = [
    [idx, round(row['revenue'], 2), int(row['quantity']), int(row['orders'])]
    for idx, row in prod_agg.head(50).iterrows()
]

country_agg = df_clean.groupby('Country').agg(
    revenue=('SalesAmount', 'sum'),
    quantity=('Quantity', 'sum'),
    orders=('InvoiceNo', 'nunique')
).sort_values('revenue', ascending=False)
country_list = [
    [idx, round(row['revenue'], 2), int(row['quantity']), int(row['orders'])]
    for idx, row in country_agg.iterrows()
]

# Monthly trend
monthly_agg = df_clean.groupby('Period').agg(
    revenue=('SalesAmount', 'sum'),
    quantity=('Quantity', 'sum'),
    orders=('InvoiceNo', 'nunique')
).sort_values('Period')
monthly_list = [
    [idx, round(row['revenue'], 2), int(row['quantity']), int(row['orders'])]
    for idx, row in monthly_agg.iterrows()
]

# Day of week
dow_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Sunday']
dow_agg = df_clean.groupby('DayOfWeek').agg(
    revenue=('SalesAmount', 'sum'),
    quantity=('Quantity', 'sum'),
    orders=('InvoiceNo', 'nunique')
).reindex(dow_order).dropna()
dow_list = [
    [idx, round(row['revenue'], 2), int(row['quantity']), int(row['orders'])]
    for idx, row in dow_agg.iterrows()
]

# Hour of day
hour_agg = df_clean.groupby('Hour').agg(
    revenue=('SalesAmount', 'sum'),
    quantity=('Quantity', 'sum'),
    orders=('InvoiceNo', 'nunique')
)
hour_list = [
    [int(idx), round(row['revenue'], 2), int(row['quantity']), int(row['orders'])]
    for idx, row in hour_agg.iterrows()
]
hour_list.sort(key=lambda x: x[0])

# Top customers
cust_clean = df_clean.dropna(subset=['CustomerID'])
cust_agg = cust_clean.groupby('CustomerID').agg(
    revenue=('SalesAmount', 'sum'),
    quantity=('Quantity', 'sum'),
    orders=('InvoiceNo', 'nunique')
).sort_values('revenue', ascending=False)
cust_list = [
    [str(int(idx)), round(row['revenue'], 2), int(row['quantity']), int(row['orders'])]
    for idx, row in cust_agg.head(50).iterrows()
]

# Value distribution (histogram bins log-scaled)
hist_counts, hist_edges = np.histogram(np.log10(df_clean['SalesAmount']), bins=12)
hist_data = [int(c) for c in hist_counts]

# LAB 4: Regression
print("Step 3: Training Lab 4 Regression Models...")
# Features: Quantity, UnitPrice, Month -> SalesAmount
reg_df = df_clean[['Quantity', 'UnitPrice', 'Month', 'SalesAmount']].copy()

# SLR (Quantity -> SalesAmount)
X_slr = reg_df[['Quantity']]
y_slr = reg_df['SalesAmount']
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(
    X_slr, y_slr, test_size=0.2, random_state=42
)
slr_model = LinearRegression().fit(X_train_s, y_train_s)
y_pred_s = slr_model.predict(X_test_s)
slr_r2 = float(r2_score(y_test_s, y_pred_s))
slr_mse = float(mean_squared_error(y_test_s, y_pred_s))
slr_coef = float(slr_model.coef_[0])
slr_intercept = float(slr_model.intercept_)

# MLR (Quantity, UnitPrice, Month -> SalesAmount)
X_mlr = reg_df[['Quantity', 'UnitPrice', 'Month']]
y_mlr = reg_df['SalesAmount']
X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(
    X_mlr, y_mlr, test_size=0.2, random_state=42
)
mlr_model = LinearRegression().fit(X_train_m, y_train_m)
y_pred_m = mlr_model.predict(X_test_m)
mlr_r2 = float(r2_score(y_test_m, y_pred_m))
mlr_mse = float(mean_squared_error(y_test_m, y_pred_m))
mlr_coefs = {col: float(coef) for col, coef in zip(X_mlr.columns, mlr_model.coef_)}
mlr_intercept = float(mlr_model.intercept_)

# Sample actual vs predicted for visualization (500 points)
sample_idx = np.random.RandomState(42).choice(len(X_test_m), size=500, replace=False)
actual_vs_pred = [
    [round(float(y_test_m.iloc[i]), 2), round(float(y_pred_m[i]), 2), float(X_test_m.iloc[i]['Quantity'])]
    for i in sample_idx
]

# LAB 5: Decision Tree Classification
print("Step 4: Training Lab 5 Decision Tree Classifier...")
def assign_category(val):
    if val <= q1: return 'Low'
    elif val <= q2: return 'Medium'
    else: return 'High'

df_clean['Sales_Category'] = df_clean['SalesAmount'].apply(assign_category)
clf_df = df_clean[['Quantity', 'UnitPrice', 'Month', 'Sales_Category']].copy()

X_dt = clf_df[['Quantity', 'UnitPrice', 'Month']]
y_dt = clf_df['Sales_Category']
X_train_dt, X_test_dt, y_train_dt, y_test_dt = train_test_split(
    X_dt, y_dt, test_size=0.2, random_state=42, stratify=y_dt
)

dt_model = DecisionTreeClassifier(
    criterion='entropy',
    max_depth=5,
    random_state=42
).fit(X_train_dt, y_train_dt)

y_pred_dt = dt_model.predict(X_test_dt)
dt_acc = float(accuracy_score(y_test_dt, y_pred_dt))
dt_cm = confusion_matrix(y_test_dt, y_pred_dt, labels=['Low', 'Medium', 'High']).tolist()
dt_prec = float(precision_score(y_test_dt, y_pred_dt, average='weighted'))
dt_rec = float(recall_score(y_test_dt, y_pred_dt, average='weighted'))
dt_f1 = float(f1_score(y_test_dt, y_pred_dt, average='weighted'))
dt_feat_imp = {col: float(imp) for col, imp in zip(X_dt.columns, dt_model.feature_importances_)}

# Export simplified decision tree representation for client-side scoring
def serialize_tree(tree, feature_names, class_names):
    def recurse(node):
        if tree.children_left[node] == tree.children_right[node]: # Leaf
            val = tree.value[node][0]
            pred_idx = int(np.argmax(val))
            return {
                'leaf': True,
                'class': class_names[pred_idx],
                'prob': [float(v / sum(val)) for v in val]
            }
        else:
            feat_idx = tree.feature[node]
            return {
                'leaf': False,
                'feature': feature_names[feat_idx],
                'threshold': float(tree.threshold[node]),
                'left': recurse(tree.children_left[node]),
                'right': recurse(tree.children_right[node])
            }
    return recurse(0)

dt_serialized = serialize_tree(dt_model.tree_, list(X_dt.columns), list(dt_model.classes_))

# LAB 6: Gaussian Naive Bayes Classification
print("Step 5: Training Lab 6 Gaussian Naive Bayes Classifier...")
X_train_nb, X_test_nb, y_train_nb, y_test_nb = train_test_split(
    X_dt, y_dt, test_size=0.3, random_state=42, stratify=y_dt
)
nb_model = GaussianNB().fit(X_train_nb, y_train_nb)
y_pred_nb = nb_model.predict(X_test_nb)
nb_acc = float(accuracy_score(y_test_nb, y_pred_nb))
nb_cm = confusion_matrix(y_test_nb, y_pred_nb, labels=['Low', 'Medium', 'High']).tolist()
nb_prec = float(precision_score(y_test_nb, y_pred_nb, average='weighted'))
nb_rec = float(recall_score(y_test_nb, y_pred_nb, average='weighted'))
nb_f1 = float(f1_score(y_test_nb, y_pred_nb, average='weighted'))

# Class statistics for in-browser exact scoring
nb_params = {
    'classes': list(nb_model.classes_),
    'priors': [float(p) for p in nb_model.class_prior_],
    'theta': [[float(m) for m in row] for row in nb_model.theta_], # means per class per feature
    'var': [[float(v) for v in row] for row in nb_model.var_],     # variances per class per feature
    'features': list(X_dt.columns)
}

# LAB 7: K-Means Customer Clustering
print("Step 6: Executing Lab 7 Customer Clustering...")
customer_df = df_clean.dropna(subset=['CustomerID']).groupby('CustomerID').agg(
    TotalSpending=('SalesAmount', 'sum'),
    TotalOrders=('InvoiceNo', 'nunique'),
    TotalQuantity=('Quantity', 'sum'),
    AverageOrderValue=('SalesAmount', lambda x: x.sum() / df_clean.loc[x.index, 'InvoiceNo'].nunique()),
    UniqueProducts=('StockCode', 'nunique')
).reset_index()

cluster_features = ['TotalSpending', 'TotalOrders', 'TotalQuantity', 'AverageOrderValue', 'UniqueProducts']
cust_X = customer_df[cluster_features].copy()
cust_X_log = np.log1p(cust_X)

scaler = StandardScaler()
cust_X_scaled = scaler.fit_transform(cust_X_log)

# Elbow method WCSS for K=1..10
wcss_list = []
for k in range(1, 11):
    km = KMeans(n_clusters=k, random_state=42, n_init=10).fit(cust_X_scaled)
    wcss_list.append(float(km.inertia_))

# Optimal K=3
km3 = KMeans(n_clusters=3, random_state=42, n_init=10).fit(cust_X_scaled)
customer_df['Cluster_K3'] = km3.labels_
k3_silhouette = float(silhouette_score(cust_X_scaled, km3.labels_))
k3_sizes = [int(c) for c in pd.Series(km3.labels_).value_counts().sort_index()]

k3_profiles = []
for c in range(3):
    sub = customer_df[customer_df['Cluster_K3'] == c]
    k3_profiles.append({
        'cluster': c + 1,
        'size': len(sub),
        'avg_spending': round(float(sub['TotalSpending'].mean()), 2),
        'avg_orders': round(float(sub['TotalOrders'].mean()), 2),
        'avg_quantity': round(float(sub['TotalQuantity'].mean()), 2),
        'avg_order_value': round(float(sub['AverageOrderValue'].mean()), 2),
        'avg_unique_products': round(float(sub['UniqueProducts'].mean()), 2)
    })

# Customer points sample for interactive scatter chart (800 customers)
rng_cust = np.random.RandomState(42)
sample_cust_idx = rng_cust.choice(len(customer_df), size=800, replace=False)
cust_scatter_sample = [
    {
        'id': int(customer_df.iloc[i]['CustomerID']),
        'spending': round(float(customer_df.iloc[i]['TotalSpending']), 2),
        'orders': int(customer_df.iloc[i]['TotalOrders']),
        'quantity': int(customer_df.iloc[i]['TotalQuantity']),
        'order_value': round(float(customer_df.iloc[i]['AverageOrderValue']), 2),
        'unique_prods': int(customer_df.iloc[i]['UniqueProducts']),
        'cluster': int(customer_df.iloc[i]['Cluster_K3'])
    }
    for i in sample_cust_idx
]

# Normalization parameters for client-side scaling
scaler_means = [float(m) for m in scaler.mean_]
scaler_stds = [float(s) for s in scaler.scale_]

# LAB 8: Hierarchical Clustering Comparison
print("Step 7: Executing Lab 8 Hierarchical Clustering Benchmark...")
# Subsample 1,000 customers for fast & stable linkage comparison
h_sample_size = min(1000, len(cust_X_scaled))
h_idx = np.random.RandomState(42).choice(len(cust_X_scaled), size=h_sample_size, replace=False)
X_h_sample = cust_X_scaled[h_idx]
cust_h_sub = customer_df.iloc[h_idx].copy().reset_index(drop=True)

linkages = ['ward', 'complete', 'average', 'single']
hier_benchmark = []
hier_labels = {}

for link in linkages:
    agg = AgglomerativeClustering(n_clusters=4, linkage=link).fit(X_h_sample)
    sil = float(silhouette_score(X_h_sample, agg.labels_))
    sizes = [int(x) for x in pd.Series(agg.labels_).value_counts().sort_index()]
    hier_labels[link] = [int(lbl) for lbl in agg.labels_]
    hier_benchmark.append({
        'linkage': link.capitalize(),
        'silhouette': round(sil, 4),
        'clusters': 4,
        'sizes': sizes
    })

# Profiles for Ward linkage (recommended in Lab 8)
cust_h_sub['Ward_Cluster'] = hier_labels['ward']
ward_profiles = []
for c in range(4):
    sub = cust_h_sub[cust_h_sub['Ward_Cluster'] == c]
    ward_profiles.append({
        'cluster': c + 1,
        'size': len(sub),
        'avg_spending': round(float(sub['TotalSpending'].mean()), 2),
        'avg_orders': round(float(sub['TotalOrders'].mean()), 2),
        'avg_quantity': round(float(sub['TotalQuantity'].mean()), 2),
        'avg_order_value': round(float(sub['AverageOrderValue'].mean()), 2)
    })

hier_sample_points = [
    {
        'spending': round(float(cust_h_sub.iloc[i]['TotalSpending']), 2),
        'orders': int(cust_h_sub.iloc[i]['TotalOrders']),
        'ward': int(hier_labels['ward'][i]),
        'complete': int(hier_labels['complete'][i]),
        'average': int(hier_labels['average'][i]),
        'single': int(hier_labels['single'][i])
    }
    for i in range(len(cust_h_sub))
]

# LAB 9: Apriori Association Rule Mining
print("Step 8: Executing Lab 9 Apriori Association Rules...")
# Top 50 products by unique invoices
df_apriori = df_clean.dropna(subset=['Description']).copy()
df_apriori['Description'] = df_apriori['Description'].astype(str).str.strip()
df_apriori = df_apriori[df_apriori['Description'] != ''].copy()

top50_items = (
    df_apriori.groupby('Description')['InvoiceNo']
    .nunique()
    .sort_values(ascending=False)
    .head(50)
    .index
)
apriori_filtered = df_apriori[df_apriori['Description'].isin(top50_items)].copy()
basket = (
    apriori_filtered.groupby(['InvoiceNo', 'Description'])['Quantity']
    .sum()
    .unstack(fill_value=0)
)
basket_binary = (basket > 0).astype(bool)

frequent_itemsets = apriori(basket_binary, min_support=0.02, use_colnames=True)
frequent_itemsets['size'] = frequent_itemsets['itemsets'].apply(len)
itemset_size_dist = {str(k): int(v) for k, v in frequent_itemsets['size'].value_counts().items()}

rules = association_rules(
    frequent_itemsets.drop(columns='size'),
    metric='confidence',
    min_threshold=0.30
)
rules['Antecedent'] = rules['antecedents'].apply(lambda x: ', '.join(sorted(x)))
rules['Consequent'] = rules['consequents'].apply(lambda x: ', '.join(sorted(x)))
rules = rules[['Antecedent', 'Consequent', 'support', 'confidence', 'lift']].sort_values('lift', ascending=False)

top_rules_lift = [
    {
        'ant': row['Antecedent'],
        'con': row['Consequent'],
        'support': round(float(row['support']), 4),
        'confidence': round(float(row['confidence']), 4),
        'lift': round(float(row['lift']), 2)
    }
    for _, row in rules.head(20).iterrows()
]

# Consolidate complete dashboard payload
dashboard_payload = {
    'meta': {
        'title': 'DWM Online Retail Analytics Dashboard',
        'dataset': 'Online Retail (UCI / Dec 2010 - Dec 2011)',
        'raw_rows': raw_rows,
        'cleaned_rows': cleaned_rows,
        'total_revenue': total_revenue,
        'invoices': unique_invoices,
        'products': unique_products,
        'countries': unique_countries,
        'customers': unique_customers,
        'q1_tertile': q1,
        'q2_tertile': q2
    },
    'lab3_eda': {
        'products': prod_list,
        'countries': country_list,
        'monthly': monthly_list,
        'day_of_week': dow_list,
        'hours': hour_list,
        'customers': cust_list,
        'value_histogram': hist_data
    },
    'lab4_regression': {
        'slr': {
            'feature': 'Quantity',
            'target': 'SalesAmount',
            'r2': slr_r2,
            'mse': slr_mse,
            'coef': slr_coef,
            'intercept': slr_intercept
        },
        'mlr': {
            'features': ['Quantity', 'UnitPrice', 'Month'],
            'target': 'SalesAmount',
            'r2': mlr_r2,
            'mse': mlr_mse,
            'coefs': mlr_coefs,
            'intercept': mlr_intercept
        },
        'actual_vs_pred': actual_vs_pred,
        'sample_prediction_lab': {
            'inputs': {'Quantity': 10, 'UnitPrice': 5, 'Month': 12},
            'predicted_sales': round(float(mlr_model.predict([[10, 5, 12]])[0]), 2)
        }
    },
    'lab5_decision_tree': {
        'target': 'Sales_Category',
        'classes': ['Low', 'Medium', 'High'],
        'criterion': 'entropy',
        'max_depth': 5,
        'accuracy': dt_acc,
        'precision': dt_prec,
        'recall': dt_rec,
        'f1': dt_f1,
        'confusion_matrix': dt_cm,
        'feature_importance': dt_feat_imp,
        'tree_structure': dt_serialized,
        'sample_prediction_lab': {
            'inputs': {'Quantity': 10, 'UnitPrice': 5, 'Month': 12},
            'predicted_category': str(dt_model.predict([[10, 5, 12]])[0])
        }
    },
    'lab6_naive_bayes': {
        'target': 'Sales_Category',
        'classes': ['Low', 'Medium', 'High'],
        'accuracy': nb_acc,
        'precision': nb_prec,
        'recall': nb_rec,
        'f1': nb_f1,
        'confusion_matrix': nb_cm,
        'model_parameters': nb_params,
        'sample_prediction_lab': {
            'inputs': {'Quantity': 10, 'UnitPrice': 5, 'Month': 12},
            'predicted_category': str(nb_model.predict([[10, 5, 12]])[0]),
            'probabilities': {cls: round(float(prob), 4) for cls, prob in zip(nb_model.classes_, nb_model.predict_proba([[10, 5, 12]])[0])}
        }
    },
    'lab7_kmeans': {
        'features': cluster_features,
        'optimal_k': 3,
        'wcss': wcss_list,
        'silhouette': k3_silhouette,
        'cluster_sizes': k3_sizes,
        'profiles': k3_profiles,
        'scatter_sample': cust_scatter_sample,
        'scaler_means': scaler_means,
        'scaler_stds': scaler_stds
    },
    'lab8_hierarchical': {
        'linkages_benchmark': hier_benchmark,
        'ward_profiles': ward_profiles,
        'sample_points': hier_sample_points
    },
    'lab9_apriori': {
        'min_support': 0.02,
        'min_confidence': 0.30,
        'itemset_sizes': itemset_size_dist,
        'top_rules': top_rules_lift,
        'total_rules': len(rules)
    }
}

print("Step 9: Writing dashboard_data.json...")
with open('dashboard_data.json', 'w', encoding='utf-8') as f:
    json.dump(dashboard_payload, f, indent=2)

print("SUCCESS: Data processing and ML pipelines completed successfully!")
