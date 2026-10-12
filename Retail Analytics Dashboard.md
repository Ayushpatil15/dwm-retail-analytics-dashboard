# DWM Online Retail Analytics Dashboard
**Data Warehousing and Mining (DWM) — Complete Laboratory Reference & Analytics Suite**

[![Dataset](https://img.shields.io/badge/Dataset-UCI%20Online%20Retail-blue.svg)](#dataset-profile)
[![Cleaned Records](https://img.shields.io/badge/Cleaned%20Rows-530%2C104-emerald.svg)](#data-cleaning--preprocessing-pipeline)
[![Revenue](https://img.shields.io/badge/Cleaned%20Revenue-%C2%A310.67M-indigo.svg)](#dataset-profile)
[![Coverage](https://img.shields.io/badge/Labs%20Covered-Labs%203%E2%80%939-purple.svg)](#laboratory-modules--algorithms)

---

## 1. Executive Summary

This project delivers an interactive, end-to-end Data Warehousing and Data Mining (DWM) analytics suite based on the authentic **UCI Online Retail dataset** (transacted between December 1, 2010 and December 9, 2011). 

The platform translates theoretical and practical data mining methodologies developed across **DWM Labs 3 through 9** into a unified, high-performance web dashboard application ([Retail Analytics Dashboard.html](file:///f:/dwm%20prj/Retail%20Analytics%20Dashboard.html)).

All analytical models, parameters, clustering centroids, association rules, and evaluative benchmarks are mathematically verified directly from `Online Retail.xlsx` without hardcoded fabrications.

---

## 2. Dataset Profile & Verified Schema

### 2.1 Raw Attribute Schema
The raw dataset contains **541,909 records** across 8 transactional attributes:

| Column | Data Type | Missing Count | Description / Role |
| :--- | :--- | :--- | :--- |
| `InvoiceNo` | `object` | 0 | 6-digit invoice identifier. Cancellations start with the character `'C'`. |
| `StockCode` | `object` | 0 | Distinct product item identifier. |
| `Description`| `object` | 1,454 | Product description string. |
| `Quantity` | `int64` | 0 | Units per transaction line item. Negative values indicate cancellations/adjustments. |
| `InvoiceDate`| `datetime64[us]` | 0 | Timestamp of transaction generation. |
| `UnitPrice` | `float64` | 0 | Price per unit in Sterling (£). Zero/negative values indicate administrative fees. |
| `CustomerID` | `float64` | 135,080 | 5-digit unique customer code. Missing for guest checkout. |
| `Country` | `str` | 0 | Country of client residence. |

### 2.2 Data Cleaning & Preprocessing Pipeline
Across Labs 3, 4, 6, 7, and 9, the following standardized filtering rules are applied:
1. **Cancellation Removal**: Filter out all rows where `InvoiceNo` starts with `'C'` (9,288 rows removed).
2. **Positive Transaction Retention**: Retain line items where `Quantity > 0` and `UnitPrice > 0` (13,141 non-positive rows removed).
3. **Derived Feature Computation**:
   $$\text{SalesAmount} = \text{Quantity} \times \text{UnitPrice}$$
4. **Target Discretization (Tertiles)**:
   - Tertile cutoffs: $q_1 = \text{quantile}(1/3) = £5.00$, $q_2 = \text{quantile}(2/3) = £15.00$.
   - **Low**: $\text{SalesAmount} \le £5.00$
   - **Medium**: $£5.00 < \text{SalesAmount} \le £15.00$
   - **High**: $\text{SalesAmount} > £15.00$

### 2.3 Verified Cleaned Baseline Metrics
- **Cleaned Transaction Records**: **530,104**
- **Cleaned Total Revenue**: **£10,666,684.54** (~£10.67M)
- **Distinct Invoices**: **19,960**
- **Distinct Catalog Products**: **4,026**
- **Distinct Geographic Markets**: **38**
- **Distinct Registered Customers**: **4,338**

---

## 3. Laboratory Modules & Algorithms

### Lab 3 — Exploratory Data Analysis & Dimensional OLAP
- **Objective**: Multi-dimensional transactional aggregation across business dimensions.
- **Dimensional Slices**:
  - **Products**: Top 50 products ranked by sales revenue, unit quantity, and transaction count.
  - **Countries**: Global revenue distribution across 38 countries (United Kingdom $>85\%$, followed by Germany, France, EIRE).
  - **Temporal Seasonality**: 13-month timeline showing the massive holiday volume surge in October–November 2011.
  - **Day-of-Week Patterns**: Sunday through Friday trading trends (store closed Saturdays).
  - **Hourly Patterns**: Distinct midday e-commerce shopping peak between 12:00 PM and 3:00 PM.
  - **Value Distribution**: Logarithmic ($\log_{10}$) frequency distribution of basket line item values.

---

### Lab 4 — Simple & Multiple Linear Regression
- **Objective**: Quantitative modeling of transaction revenue ($\text{SalesAmount}$) using ordinary least squares (OLS) regression on an 80/20 train/test split (`random_state=42`).
- **Simple Linear Regression (SLR)**:
  - Feature: `Quantity`
  - Formula: $\text{SalesAmount} \approx 3.3542 + 1.5810 \times \text{Quantity}$
  - Performance: $R^2 = 0.2038$, $\text{MSE} = 6,221.58$
- **Multiple Linear Regression (MLR)**:
  - Features: `Quantity`, `UnitPrice`, `Month`
  - Formula: $\text{SalesAmount} \approx -2.4599 + 1.5818 \times \text{Quantity} + 1.1346 \times \text{UnitPrice} + 0.1931 \times \text{Month}$
  - Performance: $R^2 = 0.6898$, $\text{MSE} = 2,423.82$
- **Interactive Verification**:
  - Test Case: $\text{Quantity} = 10, \text{UnitPrice} = £5.00, \text{Month} = 12$
  - Model Output: **£21.35** (Notebook Benchmark: **£21.31**).

---

### Lab 5 — Decision Tree Classification
- **Objective**: Non-linear supervised classification into value categories (`Low`, `Medium`, `High`) using an entropy-based decision tree with maximum depth 5 on an 80/20 stratified split.
- **Impurity Metric**: Information Gain via Shannon Entropy:
  $$H(S) = -\sum_{c \in \{L, M, H\}} p_c \log_2(p_c)$$
- **Model Results**:
  - Test Accuracy: **94.34%**
  - Primary Split Feature: `Quantity` (Threshold: $\le 2.5$ units vs $> 2.5$ units).
  - Secondary Split Feature: `UnitPrice` (Thresholds: $£2.55$ and $£1.65$).
- **Interactive Verification**:
  - Test Case: $\text{Quantity} = 10, \text{UnitPrice} = £5.00, \text{Month} = 12$ ($\text{SalesAmount} = £50.00$) $\rightarrow$ Class **High**.

---

### Lab 6 — Gaussian Naive Bayes Classification
- **Objective**: Probabilistic classification into `Low`, `Medium`, and `High` tiers using Bayes' theorem on a 70/30 stratified train/test partition:
  $$P(C \mid X) \propto P(C) \prod_{j=1}^{3} \frac{1}{\sqrt{2\pi\sigma_{C,j}^2}} \exp\left(-\frac{(x_j - \mu_{C,j})^2}{2\sigma_{C,j}^2}\right)$$
- **Model Results**:
  - Test Accuracy: **56.21%**
  - Balanced Class Priors: $P(\text{Low}) = 0.333$, $P(\text{Medium}) = 0.333$, $P(\text{High}) = 0.333$.
  - Continuous likelihoods model the overlapping variances in basket combinations.
- **Interactive Verification**:
  - Test Case: $\text{Quantity} = 10, \text{UnitPrice} = £5.00, \text{Month} = 12$
  - Posterior Probabilities: Low = $2.2\%$, Medium = $97.6\%$, High = $0.2\%$ $\rightarrow$ Class **Medium**.

---

### Lab 7 — K-Means Customer Clustering
- **Objective**: Unsupervised behavioral customer segmentation across 4,338 clients.
- **Feature Vector**:
  1. `TotalSpending`: Aggregate transaction value
  2. `TotalOrders`: Distinct invoices placed
  3. `TotalQuantity`: Aggregate unit volume purchased
  4. `AverageOrderValue`: $\text{TotalSpending} / \text{TotalOrders}$
  5. `UniqueProducts`: Distinct catalog stock items purchased
- **Transformations**: $\log(1 + x)$ non-linear skew reduction followed by `StandardScaler` $z$-score normalization:
  $$z = \frac{\log(1 + x) - \mu}{\sigma}$$
- **Optimal $K$ Evaluation**:
  - **Elbow Curve (WCSS)**: Clear inflection point at **$K = 3$**.
  - **Silhouette Coefficient**: **0.304** for $K = 3$.
- **Cluster Profiles ($K = 3$)**:
  - **Cluster 1 (High-Value / Wholesale)**: 1,170 clients, Average Spend: £5,188, Average Orders: 12.3.
  - **Cluster 2 (Occasional Shoppers)**: 1,180 clients, Average Spend: £1,245, Average Orders: 3.1.
  - **Cluster 3 (Low-Volume / Casual)**: 1,988 clients, Average Spend: £378, Average Orders: 1.4.

---

### Lab 8 — Agglomerative Hierarchical Clustering
- **Objective**: Dendrogram hierarchical clustering comparing all 4 linkage criteria on the standardized customer feature space cut at $K = 4$ clusters.
- **Comparative Benchmark**:
  | Linkage Method | Distance Formula | Silhouette Score ($K=4$) | Cluster Distribution | Practical Evaluation |
  | :--- | :--- | :--- | :--- | :--- |
  | **Ward (Recommended)** | Minimum within-cluster variance increase | **0.1971** | 64 · 21 · 92 · 123 | **Most balanced, actionable customer segments** |
  | **Complete** | Maximum pairwise distance | **0.2345** | 60 · 201 · 18 · 21 | Compact clusters, uneven density |
  | **Average** | Mean pairwise distance | **0.2830** | 1 · 2 · 288 · 9 | Severe chaining, outlier isolation |
  | **Single** | Minimum pairwise distance | **0.5436** | 1 · 1 · 3 · 295 | Severe chaining effect, 1-point outliers |

---

### Lab 9 — Apriori Association Rule Mining
- **Objective**: Market basket analysis identifying frequent itemsets and co-purchasing affinity across 14,291 multi-item invoices.
- **Universe Reduction**: Top 50 catalog items by invoice frequency (matching notebook dimensionality reduction).
- **Thresholds**: Minimum Support $\ge 2.0\%$ (`min_support = 0.02`), Minimum Confidence $\ge 30.0\%$ (`min_threshold = 0.30`).
- **Core Metrics**:
  $$\text{Support}(A \rightarrow B) = P(A \cap B)$$
  $$\text{Confidence}(A \rightarrow B) = \frac{P(A \cap B)}{P(A)}$$
  $$\text{Lift}(A \rightarrow B) = \frac{\text{Confidence}(A \rightarrow B)}{\text{Support}(B)}$$
- **Top Discovered Rules**:
  - `ALARM CLOCK BAKELIKE GREEN` $\rightarrow$ `ALARM CLOCK BAKELIKE RED`: Support = $3.29\%$, Confidence = $77.8\%$, **Lift = 15.11×**
  - `ROSES REGENCY TEACUP AND SAUCER` $\rightarrow$ `GREEN REGENCY TEACUP AND SAUCER`: Support = $2.91\%$, Confidence = $71.4\%$, **Lift = 14.32×**
  - `JUMBO BAG PINK POLKADOT` $\rightarrow$ `JUMBO BAG RED RETROSPOT`: Support = $4.18\%$, Confidence = $67.5\%$, **Lift = 6.42×**

---

## 4. Frontend Architecture & Technology Stack

The client dashboard is implemented in [Retail Analytics Dashboard.html](file:///f:/dwm%20prj/Retail%20Analytics%20Dashboard.html) as a standalone single-page application:
- **Core Structure**: Semantic HTML5.
- **Styling**: Vanilla CSS3 custom properties with automatic dark/light theme switcher (`data-theme="dark"` / `data-theme="light"`).
- **Typography**: Google Fonts Inter and Outfit.
- **Charting Engine**: Chart.js 4.4.1 (UMD) with custom dark-mode tooltips, smooth bezier splines, scatter maps, and donut cutouts.
- **Interactive Tools**: Real-time regression predictor, Decision Tree rule explorer, Gaussian probability calculator, K-Means axis selector, and live Apriori search filter.

---

## 5. File Inventory & Pipeline Reproducibility

| File | Purpose |
| :--- | :--- |
| [Retail Analytics Dashboard.html](file:///f:/dwm%20prj/Retail%20Analytics%20Dashboard.html) | Complete interactive web dashboard (open directly in any browser) |
| [Retail Analytics Dashboard.md](file:///f:/dwm%20prj/Retail%20Analytics%20Dashboard.md) | Comprehensive academic and technical reference documentation |
| [dashboard_data.json](file:///f:/dwm%20prj/dashboard_data.json) | Cleaned data and verified model assets extracted directly from Excel |
| [build_data_assets_native.py](file:///f:/dwm%20prj/build_data_assets_native.py) | Native NumPy & Pandas pipeline script executing Labs 3–9 |
| [Online Retail.xlsx](file:///f:/dwm%20prj/Online%20Retail.xlsx) | Primary raw transactional dataset (541,909 records) |
| [notebooks/](file:///f:/dwm%20prj/notebooks/) | Reference Jupyter Notebooks (DWM Labs 3 through 9) |

To recompute all data assets directly from `Online Retail.xlsx`, execute:
```bash
python build_data_assets_native.py
python generate_dashboard_html.py
```