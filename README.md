# DWM Retail Analytics Dashboard

A modern, high-performance Data Warehousing & Mining (DWM) retail intelligence dashboard built from the **Online Retail** dataset (541,909 raw records &rarr; 530,104 verified cleaned transactions). 

The platform features an executive analytics interface and end-to-end implementations of classic data mining and machine learning algorithms:

1. **Executive Overview**: High-level revenue (£10.67M), customer count (4,338), catalog metrics, dimensional performance slicing, and dataset audit verification.
2. **Exploratory Analysis**: Pareto distributions, monthly seasonality curves, hourly peak traffic, and transaction tertiles.
3. **Linear Regression**: Simple (SLR) and Multiple Linear Regression (MLR, $R^2 = 0.6898$), actual vs. predicted diagnostics with reference fit line, and real-time sales price prediction.
4. **Decision Tree Classification**: Information Gain entropy minimization (Accuracy: 94.3%), feature importance ranking, full confusion matrix, and interactive rule classification.
5. **Naive Bayes Classification**: Gaussian continuous likelihood estimation ($P(X \mid C)$), class means ($\mu$), and real-time posterior probability calculator.
6. **K-Means Clustering**: Unsupervised customer segmentation with log-scaled order and spend features, verified Elbow bend ($K=3$), Silhouette separation (0.304), and interactive PCA scatter.
7. **Hierarchical Clustering**: Agglomerative clustering benchmark across Ward, Complete, Average, and Single linkages, step progression curve, and segment balance analysis.
8. **Market Basket Analysis**: Apriori association rule mining across 14,291 multi-item baskets, interactive lift-filtered rule tables, and support vs. confidence distributions.

---

## 🎨 Theme & UI Architecture

- **Palette**: Premium matte-black & charcoal interface (`#09090B`, `#0D0D12`, `#15151D`, `#1C1C27`, `#2B2B38`).
- **Accents**: Violet (`#8B5CF6`) for primary navigation and actions; Teal (`#14B8A6`) for positive outcomes and top metrics; Amber (`#F59E0B`), Coral (`#F97373`), and Cyan (`#22D3EE`) for multi-series charts.
- **Icons**: Clean monochrome SVG line icons with zero emojis and clean titles.
- **Theme Toggle**: Instant switching between Dark and Light mode without page reloading.
- **Zero Heavy Dependencies**: Pure HTML5, CSS3, Vanilla JavaScript, and Chart.js 4.4.1.

---

## 🚀 Running Locally

You can launch the dashboard locally with any static web server:

### Using Python:
```bash
# In the repository root:
python -m http.server 8000
```
Then open: **`http://localhost:8000/`**

### Direct Browser Access:
Alternatively, double-click **`index.html`** or **`Retail Analytics Dashboard.html`** to open directly in Google Chrome, Microsoft Edge, or Safari.

---

## 🌐 Deploy to GitHub Pages (Access Anywhere)

To access your live dashboard from any phone, laptop, or browser without installing Python:

1. Push this repository to GitHub.
2. In your GitHub repository, go to **Settings** &rarr; **Pages**.
3. Under **Build and deployment**:
   - **Source**: Deploy from a branch
   - **Branch**: `main` / `root`
   - Click **Save**.
4. Within 1 minute, your dashboard will be live at:
   `https://<your-username>.github.io/<your-repository-name>/`

---

## 📁 Repository Structure

```
├── index.html                       # Main dashboard entrypoint (ready for GitHub Pages)
├── Retail Analytics Dashboard.html  # Standalone analytics dashboard application
├── Retail Analytics Dashboard.md    # Complete academic project documentation & proofs
├── dashboard_data.json              # Verified precomputed data assets & model weights
├── build_data_assets_native.py      # Resilient native Python ETL and ML extraction pipeline
├── build_data_assets.py             # Scikit-learn data extraction script
├── generate_dashboard_html.py       # Dashboard generator and HTML builder
├── Online Retail.xlsx               # Source UCI Online Retail dataset (541,909 rows)
└── notebooks/                       # Academic Lab 3 through Lab 9 Jupyter notebooks
    ├── DWM_Lab_3_Online_Retail (1).ipynb
    ├── DWM_Lab_4_Online_Retail.ipynb
    ├── DWM_Lab_5_Online_Retail.ipynb
    ├── DWM_Lab_6_Online_Retail.ipynb
    ├── DWM_Lab_7_Online_Retail.ipynb
    ├── DWM_Lab_8_Online_Retail.ipynb
    └── DWM_Lab_9_Online_Retail.ipynb
```
