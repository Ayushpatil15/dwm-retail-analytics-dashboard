import json

with open('dashboard_data.json', 'r', encoding='utf-8') as f:
    data_json = f.read()

html_template = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>DWM Retail Analytics Suite | Online Retail Intelligence</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
  <style>
    :root, [data-theme="dark"] {
      --bg: #09090B;
      --sb: #0D0D12;
      --card: #15151D;
      --card-hover: #191924;
      --panel: #1C1C27;
      --panel-hover: #222230;
      --tx: #F4F4F5;
      --tx-dim: #A1A1AA;
      --tx-muted: #71717A;
      --bd: #2B2B38;
      --bd-light: rgba(255, 255, 255, 0.06);
      --bd-focus: #8B5CF6;
      --ac: #8B5CF6;
      --ac-hover: #7C3AED;
      --ac-light: rgba(139, 92, 246, 0.12);
      --teal: #14B8A6;
      --teal-hover: #0D9488;
      --teal-light: rgba(20, 184, 166, 0.12);
      --amber: #F59E0B;
      --amber-light: rgba(245, 158, 11, 0.12);
      --coral: #F97373;
      --coral-light: rgba(249, 115, 115, 0.12);
      --cyan: #22D3EE;
      --cyan-light: rgba(34, 211, 238, 0.12);
      --grid-line: rgba(255, 255, 255, 0.05);
      --radius: 10px;
      --radius-sm: 6px;
      --shadow: 0 4px 18px rgba(0, 0, 0, 0.45);
    }

    [data-theme="light"] {
      --bg: #F8FAFC;
      --sb: #18181B;
      --card: #FFFFFF;
      --card-hover: #F8FAFC;
      --panel: #F1F5F9;
      --panel-hover: #E2E8F0;
      --tx: #09090B;
      --tx-dim: #52525B;
      --tx-muted: #71717A;
      --bd: #E2E8F0;
      --bd-light: #CBD5E1;
      --bd-focus: #7C3AED;
      --ac: #7C3AED;
      --ac-hover: #6D28D9;
      --ac-light: rgba(124, 58, 237, 0.08);
      --teal: #0D9488;
      --teal-hover: #0F766E;
      --teal-light: rgba(13, 148, 136, 0.08);
      --amber: #D97706;
      --amber-light: rgba(217, 119, 6, 0.08);
      --coral: #E11D48;
      --coral-light: rgba(225, 29, 72, 0.08);
      --cyan: #0284C7;
      --cyan-light: rgba(2, 132, 199, 0.08);
      --grid-line: rgba(0, 0, 0, 0.05);
      --radius: 10px;
      --radius-sm: 6px;
      --shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    html, body { height: 100%; font-family: 'Inter', -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif; }
    body {
      background: var(--bg);
      color: var(--tx);
      display: flex;
      font-size: 13.5px;
      line-height: 1.5;
      overflow: hidden;
      transition: background 0.15s ease, color 0.15s ease;
    }

    /* Scrollbars */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb { background: rgba(161, 161, 170, 0.2); border-radius: 99px; }
    ::-webkit-scrollbar-thumb:hover { background: rgba(161, 161, 170, 0.4); }

    /* SIDEBAR */
    aside {
      width: 260px;
      background: var(--sb);
      color: #E4E4E7;
      display: flex;
      flex-direction: column;
      flex-shrink: 0;
      border-right: 1px solid var(--bd);
      padding: 18px 12px;
      overflow-y: auto;
      z-index: 20;
    }
    .brand {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 2px 8px 16px;
      border-bottom: 1px solid var(--bd);
      margin-bottom: 12px;
    }
    .brand-icon {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: var(--panel);
      border: 1px solid var(--bd);
      display: grid;
      place-items: center;
      color: var(--ac);
      flex-shrink: 0;
    }
    .brand-text h2 {
      font-family: 'Outfit', sans-serif;
      font-size: 15px;
      font-weight: 700;
      letter-spacing: -0.3px;
      color: var(--tx);
    }
    .brand-text p {
      font-size: 11px;
      color: var(--tx-dim);
    }

    .nav-section-title {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.8px;
      color: var(--tx-muted);
      padding: 10px 10px 4px;
    }
    nav { display: flex; flex-direction: column; gap: 2px; }
    nav button {
      all: unset;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 12px;
      border-radius: var(--radius-sm);
      font-size: 12.5px;
      font-weight: 500;
      color: #A1A1AA;
      border-left: 3px solid transparent;
      transition: all 0.12s ease;
    }
    nav button:hover {
      background: rgba(255, 255, 255, 0.04);
      color: #F4F4F5;
    }
    nav button.active {
      background: var(--ac-light);
      border-left-color: var(--ac);
      color: #F4F4F5;
      font-weight: 600;
    }
    nav button.active .nav-svg { color: var(--ac); }
    nav button .nav-svg {
      width: 16px;
      height: 16px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--tx-muted);
      flex-shrink: 0;
      transition: color 0.12s;
    }
    nav button:hover .nav-svg { color: var(--tx); }

    .aside-footer {
      margin-top: auto;
      padding-top: 14px;
      border-top: 1px solid var(--bd);
      display: flex;
      flex-direction: column;
      gap: 8px;
    }
    .theme-toggle-btn {
      all: unset;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 7px 12px;
      border-radius: var(--radius-sm);
      background: var(--panel);
      border: 1px solid var(--bd);
      font-size: 12px;
      color: var(--tx-dim);
      transition: background 0.12s;
    }
    .theme-toggle-btn:hover { background: var(--panel-hover); color: var(--tx); }
    .status-badge {
      font-size: 11px;
      color: var(--tx-muted);
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 2px 4px;
    }
    .status-dot {
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--teal);
    }

    /* MAIN VIEWPORT */
    main {
      flex: 1;
      display: flex;
      flex-direction: column;
      min-width: 0;
      overflow-y: auto;
      background: var(--bg);
      padding: 24px 28px;
    }
    .top-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 18px;
      flex-wrap: wrap;
      gap: 12px;
    }
    .header-titles h1 {
      font-family: 'Outfit', sans-serif;
      font-size: 22px;
      font-weight: 700;
      letter-spacing: -0.3px;
      color: var(--tx);
    }
    .header-titles p {
      color: var(--tx-dim);
      font-size: 13px;
      margin-top: 2px;
    }
    .section-badge {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: var(--panel);
      border: 1px solid var(--bd);
      color: var(--tx-dim);
      font-size: 11px;
      font-weight: 600;
      padding: 4px 10px;
      border-radius: 6px;
      text-transform: uppercase;
      letter-spacing: 0.5px;
    }

    /* CONTROLS TOOLBAR */
    .toolbar {
      background: var(--card);
      border: 1px solid var(--bd);
      border-radius: var(--radius);
      padding: 10px 16px;
      margin-bottom: 16px;
      display: flex;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
      box-shadow: var(--shadow);
    }
    .control-item {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .control-item label {
      font-size: 10px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--tx-muted);
    }
    .control-item select, .control-item input[type="number"], .control-item input[type="text"] {
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--bd);
      background: var(--panel);
      color: var(--tx);
      font-size: 12.5px;
      font-family: inherit;
      outline: none;
      transition: border 0.12s;
      min-width: 120px;
    }
    .control-item select:focus, .control-item input:focus {
      border-color: var(--bd-focus);
    }

    /* KPI CARDS GRID */
    .kpi-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
      gap: 14px;
      margin-bottom: 16px;
    }
    .kpi-card {
      background: var(--card);
      border: 1px solid var(--bd);
      border-radius: var(--radius);
      padding: 14px 16px;
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      gap: 3px;
      transition: border-color 0.12s ease;
    }
    .kpi-card:hover {
      border-color: rgba(139, 92, 246, 0.4);
    }
    .kpi-card .kpi-label {
      font-size: 10.5px;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      color: var(--tx-muted);
    }
    .kpi-card .kpi-val {
      font-family: 'Outfit', sans-serif;
      font-size: 23px;
      font-weight: 700;
      color: var(--tx);
      letter-spacing: -0.4px;
    }
    .kpi-card .kpi-sub {
      font-size: 11px;
      color: var(--tx-dim);
    }

    /* CARDS & GRIDS */
    .cards-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(min(100%, 460px), 1fr));
      gap: 16px;
    }
    .card {
      background: var(--card);
      border: 1px solid var(--bd);
      border-radius: var(--radius);
      padding: 16px 18px;
      box-shadow: var(--shadow);
      display: flex;
      flex-direction: column;
      min-width: 0;
    }
    .card.wide { grid-column: 1 / -1; }
    .card-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 12px;
    }
    .card-header h3 {
      font-family: 'Outfit', sans-serif;
      font-size: 14.5px;
      font-weight: 700;
      color: var(--tx);
      letter-spacing: -0.2px;
    }
    .card-header p {
      font-size: 11.5px;
      color: var(--tx-muted);
      margin-top: 1px;
    }
    .chart-container {
      position: relative;
      height: 290px;
      width: 100%;
    }
    .chart-container.tall { height: 350px; }
    .chart-container.short { height: 210px; }

    /* TABLES */
    .table-container {
      overflow-x: auto;
      margin-top: 8px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--bd);
      background: var(--panel);
    }
    table {
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
      text-align: left;
    }
    th {
      background: var(--panel);
      color: var(--tx-dim);
      font-weight: 600;
      padding: 8px 12px;
      border-bottom: 1px solid var(--bd);
      text-transform: uppercase;
      font-size: 10.5px;
      letter-spacing: 0.4px;
      white-space: nowrap;
    }
    td {
      padding: 8px 12px;
      border-bottom: 1px solid var(--bd);
      color: var(--tx);
      white-space: nowrap;
    }
    tr:last-child td { border-bottom: none; }
    tr:hover td { background: rgba(255, 255, 255, 0.02); }

    /* CALLOUT BOXES */
    .callout {
      background: var(--panel);
      border-left: 3px solid var(--ac);
      border-radius: 2px var(--radius-sm) var(--radius-sm) 2px;
      padding: 10px 14px;
      font-size: 12px;
      color: var(--tx-dim);
      margin-top: 12px;
      line-height: 1.45;
    }
    .callout b { color: var(--tx); }
    .callout.teal { border-left-color: var(--teal); }
    .callout.amber { border-left-color: var(--amber); }

    /* INTERACTIVE PREDICTOR WIDGET */
    .predictor-box {
      background: var(--panel);
      border: 1px solid var(--bd);
      border-radius: var(--radius-sm);
      padding: 14px 16px;
      margin-bottom: 12px;
      display: flex;
      flex-direction: column;
      gap: 12px;
    }
    .predictor-inputs {
      display: flex;
      gap: 16px;
      flex-wrap: wrap;
      align-items: flex-end;
    }
    .pred-field {
      display: flex;
      flex-direction: column;
      gap: 3px;
    }
    .pred-field label {
      font-size: 10.5px;
      font-weight: 600;
      text-transform: uppercase;
      color: var(--tx-muted);
    }
    .pred-field input {
      padding: 6px 10px;
      border-radius: var(--radius-sm);
      border: 1px solid var(--bd);
      background: var(--card);
      color: var(--tx);
      font-size: 12.5px;
      width: 110px;
      outline: none;
    }
    .pred-field input:focus { border-color: var(--bd-focus); }
    .pred-result-card {
      display: flex;
      align-items: center;
      gap: 14px;
      padding: 8px 14px;
      border-radius: var(--radius-sm);
      background: var(--card);
      border: 1px solid var(--bd);
    }
    .pred-badge {
      font-family: 'Outfit', sans-serif;
      font-size: 17px;
      font-weight: 700;
      color: var(--ac);
    }

    /* CONFUSION MATRIX HEATMAP */
    .cm-grid {
      display: grid;
      grid-template-columns: 80px repeat(3, 1fr);
      gap: 4px;
      max-width: 440px;
      margin: 10px auto;
      text-align: center;
      font-size: 12px;
    }
    .cm-cell {
      padding: 10px 8px;
      border-radius: var(--radius-sm);
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border: 1px solid var(--bd-light);
    }
    .cm-cell.header {
      background: transparent;
      border: none;
      font-weight: 600;
      color: var(--tx-muted);
      text-transform: uppercase;
      font-size: 10.5px;
    }
    .cm-val {
      font-weight: 700;
      font-size: 13.5px;
      color: var(--tx);
    }

    /* TREE VISUALIZER */
    .tree-diagram {
      background: var(--panel);
      border: 1px solid var(--bd);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      font-family: monospace;
      font-size: 11px;
      line-height: 1.6;
      max-height: 280px;
      overflow-y: auto;
      color: var(--tx-dim);
    }
    .tree-node-line {
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .tree-branch { color: var(--ac); font-weight: bold; }
    .tree-leaf-high { color: var(--teal); font-weight: bold; }
    .tree-leaf-med { color: var(--amber); font-weight: bold; }
    .tree-leaf-low { color: var(--coral); font-weight: bold; }

    /* RESPONSIVE */
    @media (max-width: 900px) {
      body { flex-direction: column; overflow-y: auto; }
      aside { width: 100%; border-right: none; border-bottom: 1px solid var(--bd); padding: 12px; }
      nav { flex-direction: row; overflow-x: auto; padding-bottom: 4px; }
      nav button { white-space: nowrap; }
      .brand, .aside-footer { display: none; }
      main { padding: 16px; overflow: visible; }
      .cards-grid { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>

  <!-- SIDEBAR NAVIGATION -->
  <aside>
    <div class="brand">
      <div class="brand-icon">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="18" y1="20" x2="18" y2="10"></line>
          <line x1="12" y1="20" x2="12" y2="4"></line>
          <line x1="6" y1="20" x2="6" y2="14"></line>
        </svg>
      </div>
      <div class="brand-text">
        <h2>Retail Analytics</h2>
        <p>Online Retail Intelligence</p>
      </div>
    </div>

    <div class="nav-section-title">Overview & Exploration</div>
    <nav>
      <button data-tab="overview" class="active">
        <span class="nav-svg">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="3" width="7" height="7"></rect>
            <rect x="14" y="3" width="7" height="7"></rect>
            <rect x="14" y="14" width="7" height="7"></rect>
            <rect x="3" y="14" width="7" height="7"></rect>
          </svg>
        </span>
        <span>Executive Overview</span>
      </button>
      <button data-tab="eda">
        <span class="nav-svg">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="4" y1="21" x2="4" y2="14"></line>
            <line x1="4" y1="10" x2="4" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="12"></line>
            <line x1="12" y1="8" x2="12" y2="3"></line>
            <line x1="20" y1="21" x2="20" y2="16"></line>
            <line x1="20" y1="12" x2="20" y2="3"></line>
            <line x1="1" y1="14" x2="7" y2="14"></line>
            <line x1="9" y1="8" x2="15" y2="8"></line>
            <line x1="17" y1="16" x2="23" y2="16"></line>
          </svg>
        </span>
        <span>Exploratory Analysis</span>
      </button>
    </nav>

    <div class="nav-section-title">Predictive Models</div>
    <nav>
      <button data-tab="regression">
        <span class="nav-svg">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="23 6 13.5 15.5 8.5 10.5 1 18"></polyline>
            <polyline points="17 6 23 6 23 12"></polyline>
          </svg>
        </span>
        <span>Linear Regression</span>
      </button>
      <button data-tab="decision_tree">
        <span class="nav-svg">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="6" y1="3" x2="6" y2="15"></line>
            <circle cx="18" cy="6" r="3"></circle>
            <circle cx="6" cy="18" r="3"></circle>
            <path d="M18 9a9 9 0 0 1-9 9"></path>
          </svg>
        </span>
        <span>Decision Tree</span>
      </button>
      <button data-tab="naive_bayes">
        <span class="nav-svg">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"></circle>
            <circle cx="12" cy="12" r="6"></circle>
            <circle cx="12" cy="12" r="2"></circle>
          </svg>
        </span>
        <span>Naive Bayes</span>
      </button>
    </nav>

    <div class="nav-section-title">Pattern Discovery</div>
    <nav>
      <button data-tab="kmeans">
        <span class="nav-svg">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
            <circle cx="9" cy="7" r="4"></circle>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
          </svg>
        </span>
        <span>K-Means Clustering</span>
      </button>
      <button data-tab="hierarchical">
        <span class="nav-svg">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="5" r="3"></circle>
            <line x1="12" y1="8" x2="12" y2="12"></line>
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <line x1="5" y1="12" x2="5" y2="16"></line>
            <line x1="19" y1="12" x2="19" y2="16"></line>
            <circle cx="5" cy="19" r="3"></circle>
            <circle cx="19" cy="19" r="3"></circle>
          </svg>
        </span>
        <span>Hierarchical Clustering</span>
      </button>
      <button data-tab="apriori">
        <span class="nav-svg">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="9" cy="21" r="1"></circle>
            <circle cx="20" cy="21" r="1"></circle>
            <path d="M1 1h4l2.68 13.39a2 2 0 0 0 2 1.61h9.72a2 2 0 0 0 2-1.61L23 6H6"></path>
          </svg>
        </span>
        <span>Market Basket Analysis</span>
      </button>
    </nav>

    <div class="aside-footer">
      <button class="theme-toggle-btn" id="themeBtn">
        <span>Display Theme</span>
        <span id="themeLabel" style="font-weight:600">Dark</span>
      </button>
      <div class="status-badge">
        <div class="status-dot"></div>
        <span>530,104 Cleaned Records</span>
      </div>
    </div>
  </aside>

  <!-- MAIN VIEWPORT -->
  <main>
    <div class="top-header">
      <div class="header-titles">
        <h1 id="pageTitle">Executive Overview</h1>
        <p id="pageDesc">High-level transactional volume, market concentrations, and verified dataset profile.</p>
      </div>
      <div class="section-badge" id="sectionBadge">
        <span>Enterprise Overview</span>
      </div>
    </div>

    <!-- CONTROLS TOOLBAR -->
    <div class="toolbar" id="toolbar"></div>

    <!-- KPI METRICS GRID -->
    <div class="kpi-grid" id="kpiGrid"></div>

    <!-- MAIN CARDS GRID -->
    <div class="cards-grid" id="cardsGrid"></div>
  </main>

  <script>
    const D = {
  "meta": {
    "title": "DWM Online Retail Analytics Dashboard",
    "dataset": "Online Retail (UCI / Dec 2010 - Dec 2011)",
    "raw_rows": 541909,
    "cleaned_rows": 530104,
    "total_revenue": 10666684.54,
    "invoices": 19960,
    "products": 4026,
    "countries": 38,
    "customers": 4338,
    "q1_tertile": 5.0,
    "q2_tertile": 15.0
  },
  "lab3_eda": {
    "products": [
      [
        "DOTCOM POSTAGE",
        206248.77,
        706,
        706
      ],
      [
        "REGENCY CAKESTAND 3 TIER",
        174484.74,
        13879,
        1988
      ],
      [
        "PAPER CRAFT , LITTLE BIRDIE",
        168469.6,
        80995,
        1
      ],
      [
        "WHITE HANGING HEART T-LIGHT HOLDER",
        106292.77,
        37891,
        2256
      ],
      [
        "PARTY BUNTING",
        99504.33,
        18295,
        1685
      ],
      [
        "JUMBO BAG RED RETROSPOT",
        94340.05,
        48474,
        2089
      ],
      [
        "MEDIUM CERAMIC TOP STORAGE JAR",
        81700.92,
        78033,
        247
      ],
      [
        "Manual",
        78112.82,
        7225,
        290
      ],
      [
        "POSTAGE",
        78101.88,
        3150,
        1126
      ],
      [
        "RABBIT NIGHT LIGHT",
        66964.99,
        30788,
        994
      ],
      [
        "PAPER CHAIN KIT 50'S CHRISTMAS",
        64952.29,
        19355,
        1160
      ],
      [
        "ASSORTED COLOUR BIRD ORNAMENT",
        59094.93,
        36461,
        1455
      ],
      [
        "CHILLI LIGHTS",
        54117.76,
        10306,
        661
      ],
      [
        "SPOTTY BUNTING",
        42548.13,
        8327,
        1140
      ],
      [
        "JUMBO BAG PINK POLKADOT",
        42436.24,
        21465,
        1218
      ],
      [
        "BLACK RECORD COVER FRAME",
        40652.13,
        11656,
        375
      ],
      [
        "PICNIC BASKET WICKER 60 PIECES",
        39619.5,
        61,
        2
      ],
      [
        "DOORMAT KEEP CALM AND COME IN",
        38166.64,
        5491,
        728
      ],
      [
        "SET OF 3 CAKE TINS PANTRY DESIGN",
        38158.39,
        7493,
        1385
      ],
      [
        "JAM MAKING SET WITH JARS",
        37128.88,
        8706,
        1132
      ],
      [
        "WOOD BLACK BOARD ANT WHITE FINISH",
        36030.22,
        6020,
        685
      ],
      [
        "LUNCH BAG RED RETROSPOT",
        35752.01,
        19353,
        1564
      ],
      [
        "POPCORN HOLDER",
        34298.87,
        36761,
        803
      ],
      [
        "VICTORIAN GLASS HANGING T-LIGHT",
        33187.97,
        24304,
        1037
      ],
      [
        "HOT WATER BOTTLE TEA AND SYMPATHY",
        33002.59,
        5747,
        643
      ],
      [
        "PAPER CHAIN KIT VINTAGE CHRISTMAS",
        32873.34,
        10604,
        820
      ],
      [
        "CHOCOLATE HOT WATER BOTTLE",
        32866.18,
        6025,
        858
      ],
      [
        "JUMBO BAG STRAWBERRY",
        32802.53,
        17319,
        822
      ],
      [
        "HEART OF WICKER SMALL",
        32107.8,
        17971,
        1201
      ],
      [
        "SET OF 3 REGENCY CAKE TINS",
        31177.95,
        6357,
        873
      ],
      [
        "JUMBO STORAGE BAG SUKI",
        30770.12,
        13654,
        1184
      ],
      [
        "ALARM CLOCK BAKELIKE RED",
        30701.12,
        7815,
        1051
      ],
      [
        "JUMBO BAG APPLES",
        30475.65,
        14920,
        978
      ],
      [
        "HEART OF WICKER LARGE",
        30139.41,
        9901,
        925
      ],
      [
        "CHARLOTTE BAG SUKI DESIGN",
        29277.95,
        18152,
        882
      ],
      [
        "ROSES REGENCY TEACUP AND SAUCER",
        29095.27,
        9877,
        1065
      ],
      [
        "HOT WATER BOTTLE KEEP CALM",
        28842.55,
        5841,
        782
      ],
      [
        "JUMBO SHOPPER VINTAGE RED PAISLEY",
        28634.95,
        12602,
        1175
      ],
      [
        "NATURAL SLATE HEART CHALKBOARD",
        28147.96,
        9172,
        1249
      ],
      [
        "JUMBO  BAG BAROQUE BLACK WHITE",
        28092.2,
        13922,
        933
      ],
      [
        "DOORMAT RED RETROSPOT",
        28082.54,
        4092,
        696
      ],
      [
        "JUMBO BAG ALPHABET",
        27890.17,
        13379,
        906
      ],
      [
        "ALARM CLOCK BAKELIKE GREEN",
        27196.53,
        6430,
        980
      ],
      [
        "ROTATING SILVER ANGELS T-LIGHT HLDR",
        26463.83,
        9476,
        449
      ],
      [
        "RED  HARMONICA IN BOX",
        26331.58,
        21933,
        661
      ],
      [
        "RECIPE BOX PANTRY YELLOW DESIGN",
        26240.6,
        8276,
        1111
      ],
      [
        "GIN + TONIC DIET METAL SIGN",
        25836.57,
        11727,
        759
      ],
      [
        "SPACEBOY LUNCH BOX",
        25740.47,
        14260,
        900
      ],
      [
        "JAM MAKING SET PRINTED",
        25660.98,
        16412,
        1162
      ],
      [
        "DOORMAT UNION FLAG",
        25609.6,
        3762,
        616
      ]
    ],
    "countries": [
      [
        "United Kingdom",
        9025222.08,
        4662390,
        18019
      ],
      [
        "Netherlands",
        285446.34,
        200361,
        94
      ],
      [
        "EIRE",
        283453.96,
        147173,
        288
      ],
      [
        "Germany",
        228867.14,
        119261,
        457
      ],
      [
        "France",
        209715.11,
        112103,
        392
      ],
      [
        "Australia",
        138521.31,
        83901,
        57
      ],
      [
        "Spain",
        61577.11,
        27940,
        90
      ],
      [
        "Switzerland",
        57089.9,
        30629,
        54
      ],
      [
        "Belgium",
        41196.34,
        23237,
        98
      ],
      [
        "Sweden",
        38378.33,
        36083,
        36
      ],
      [
        "Japan",
        37416.37,
        26016,
        19
      ],
      [
        "Norway",
        36165.44,
        19336,
        36
      ],
      [
        "Portugal",
        33747.1,
        16258,
        58
      ],
      [
        "Finland",
        22546.08,
        10704,
        41
      ],
      [
        "Singapore",
        21279.29,
        5241,
        7
      ],
      [
        "Channel Islands",
        20450.44,
        9491,
        26
      ],
      [
        "Denmark",
        18955.34,
        8235,
        18
      ],
      [
        "Italy",
        17483.24,
        8112,
        38
      ],
      [
        "Hong Kong",
        15691.8,
        4773,
        11
      ],
      [
        "Cyprus",
        13590.38,
        6361,
        16
      ],
      [
        "Austria",
        10198.68,
        4881,
        17
      ],
      [
        "Israel",
        8135.26,
        4409,
        8
      ],
      [
        "Poland",
        7334.65,
        3684,
        19
      ],
      [
        "Greece",
        4760.52,
        1557,
        5
      ],
      [
        "Unspecified",
        4749.79,
        3300,
        13
      ],
      [
        "Iceland",
        4310.0,
        2458,
        7
      ],
      [
        "Canada",
        3666.38,
        2763,
        6
      ],
      [
        "USA",
        3580.39,
        2458,
        5
      ],
      [
        "Malta",
        2725.59,
        970,
        5
      ],
      [
        "United Arab Emirates",
        1902.28,
        982,
        3
      ],
      [
        "Lebanon",
        1693.88,
        386,
        1
      ],
      [
        "Lithuania",
        1661.06,
        652,
        4
      ],
      [
        "European Community",
        1300.25,
        499,
        4
      ],
      [
        "Brazil",
        1143.6,
        356,
        1
      ],
      [
        "RSA",
        1002.31,
        351,
        1
      ],
      [
        "Czech Republic",
        826.74,
        671,
        2
      ],
      [
        "Bahrain",
        754.14,
        314,
        3
      ],
      [
        "Saudi Arabia",
        145.92,
        80,
        1
      ]
    ],
    "monthly": [
      [
        "2010-12",
        823746.14,
        359239,
        1559
      ],
      [
        "2011-01",
        691364.56,
        387785,
        1086
      ],
      [
        "2011-02",
        523631.89,
        283555,
        1100
      ],
      [
        "2011-03",
        717639.36,
        377526,
        1454
      ],
      [
        "2011-04",
        537808.62,
        308815,
        1246
      ],
      [
        "2011-05",
        770536.02,
        395738,
        1681
      ],
      [
        "2011-06",
        761739.9,
        389213,
        1533
      ],
      [
        "2011-07",
        719221.19,
        401759,
        1475
      ],
      [
        "2011-08",
        759138.38,
        421770,
        1361
      ],
      [
        "2011-09",
        1058590.17,
        570820,
        1837
      ],
      [
        "2011-10",
        1154979.3,
        623401,
        2040
      ],
      [
        "2011-11",
        1509496.33,
        754507,
        2769
      ],
      [
        "2011-12",
        638792.68,
        314248,
        819
      ]
    ],
    "day_of_week": [
      [
        "Monday",
        1779575.04,
        873332,
        3126
      ],
      [
        "Tuesday",
        2178632.61,
        1115208,
        3554
      ],
      [
        "Wednesday",
        1851147.81,
        1027431,
        3690
      ],
      [
        "Thursday",
        2203161.24,
        1209617,
        4246
      ],
      [
        "Friday",
        1840340.23,
        891784,
        3140
      ],
      [
        "Sunday",
        813827.61,
        471004,
        2204
      ]
    ],
    "hours": [
      [
        6,
        4.25,
        1,
        1
      ],
      [
        7,
        31059.21,
        15370,
        29
      ],
      [
        8,
        283868.52,
        159097,
        566
      ],
      [
        9,
        990267.82,
        518098,
        1484
      ],
      [
        10,
        1446742.7,
        813805,
        2361
      ],
      [
        11,
        1239954.44,
        674682,
        2396
      ],
      [
        12,
        1444245.88,
        839523,
        3220
      ],
      [
        13,
        1265736.3,
        706285,
        2753
      ],
      [
        14,
        1181812.37,
        599220,
        2457
      ],
      [
        15,
        1352972.18,
        628564,
        2336
      ],
      [
        16,
        754006.56,
        331487,
        1335
      ],
      [
        17,
        461603.49,
        192975,
        667
      ],
      [
        18,
        144813.05,
        66578,
        192
      ],
      [
        19,
        50665.01,
        33104,
        146
      ],
      [
        20,
        18932.76,
        9587,
        18
      ]
    ],
    "customers": [
      [
        "14646",
        280206.02,
        196915,
        73
      ],
      [
        "18102",
        259657.3,
        64124,
        60
      ],
      [
        "17450",
        194550.79,
        69993,
        46
      ],
      [
        "16446",
        168472.5,
        80997,
        2
      ],
      [
        "14911",
        143825.06,
        80265,
        201
      ],
      [
        "12415",
        124914.53,
        77374,
        21
      ],
      [
        "14156",
        117379.63,
        57885,
        55
      ],
      [
        "17511",
        91062.38,
        64549,
        31
      ],
      [
        "16029",
        81024.84,
        40208,
        63
      ],
      [
        "12346",
        77183.6,
        74215,
        1
      ],
      [
        "16684",
        66653.56,
        50255,
        28
      ],
      [
        "14096",
        65164.79,
        16352,
        17
      ],
      [
        "13694",
        65039.62,
        63312,
        50
      ],
      [
        "15311",
        60767.9,
        38194,
        91
      ],
      [
        "13089",
        58825.83,
        31070,
        97
      ],
      [
        "17949",
        58510.48,
        30546,
        45
      ],
      [
        "15769",
        56252.72,
        29672,
        26
      ],
      [
        "15061",
        54534.14,
        28920,
        48
      ],
      [
        "14298",
        51527.3,
        58343,
        44
      ],
      [
        "14088",
        50491.81,
        12665,
        13
      ],
      [
        "15749",
        44534.3,
        18028,
        3
      ],
      [
        "12931",
        42055.96,
        28004,
        15
      ],
      [
        "17841",
        40991.57,
        23071,
        124
      ],
      [
        "15098",
        39916.5,
        121,
        3
      ],
      [
        "13798",
        37153.85,
        23948,
        57
      ],
      [
        "16013",
        37130.6,
        15536,
        47
      ],
      [
        "16422",
        34684.4,
        33704,
        51
      ],
      [
        "12748",
        33719.73,
        25747,
        209
      ],
      [
        "15838",
        33643.08,
        18368,
        19
      ],
      [
        "17404",
        31906.82,
        32748,
        15
      ],
      [
        "17389",
        31833.68,
        7612,
        34
      ],
      [
        "13098",
        28882.44,
        15968,
        28
      ],
      [
        "14680",
        28754.11,
        13476,
        16
      ],
      [
        "13081",
        28337.38,
        19068,
        11
      ],
      [
        "13408",
        28117.04,
        16232,
        62
      ],
      [
        "17857",
        26879.04,
        19256,
        23
      ],
      [
        "16333",
        26626.8,
        32184,
        22
      ],
      [
        "13777",
        25977.16,
        12897,
        33
      ],
      [
        "12753",
        21429.39,
        11421,
        6
      ],
      [
        "12744",
        21279.29,
        5241,
        7
      ],
      [
        "16210",
        21086.3,
        7559,
        18
      ],
      [
        "17675",
        20374.28,
        8360,
        31
      ],
      [
        "17381",
        20275.61,
        25649,
        29
      ],
      [
        "15039",
        19914.44,
        9209,
        47
      ],
      [
        "12471",
        19824.05,
        8212,
        30
      ],
      [
        "12731",
        18895.91,
        8437,
        12
      ],
      [
        "15159",
        18641.01,
        11441,
        30
      ],
      [
        "12901",
        17654.54,
        23075,
        28
      ],
      [
        "12678",
        17628.46,
        10923,
        12
      ],
      [
        "14031",
        17286.86,
        5788,
        19
      ]
    ],
    "value_histogram": [
      4,
      0,
      6,
      5742,
      89406,
      221712,
      188978,
      21766,
      2293,
      191,
      3,
      3
    ]
  },
  "lab4_regression": {
    "slr": {
      "feature": "Quantity",
      "target": "SalesAmount",
      "r2": 0.2038,
      "mse": 6221.58,
      "coef": 1.581,
      "intercept": 3.3542
    },
    "mlr": {
      "features": [
        "Quantity",
        "UnitPrice",
        "Month"
      ],
      "target": "SalesAmount",
      "r2": 0.6898,
      "mse": 2423.82,
      "coefs": {
        "Quantity": 1.5818,
        "UnitPrice": 1.1346,
        "Month": 0.1931
      },
      "intercept": -2.4599
    },
    "actual_vs_pred": [
      [
        5.91,
        8.14,
        1.0
      ],
      [
        16.5,
        10.64,
        2.0
      ],
      [
        30.0,
        15.8,
        8.0
      ],
      [
        8.5,
        14.52,
        10.0
      ],
      [
        2.51,
        4.29,
        1.0
      ],
      [
        2.1,
        3.44,
        1.0
      ],
      [
        0.42,
        1.72,
        1.0
      ],
      [
        50.0,
        63.58,
        40.0
      ],
      [
        41.76,
        227.0,
        144.0
      ],
      [
        16.5,
        16.97,
        10.0
      ],
      [
        5.95,
        7.61,
        1.0
      ],
      [
        4.15,
        5.95,
        1.0
      ],
      [
        16.5,
        16.77,
        10.0
      ],
      [
        6.8,
        12.9,
        8.0
      ],
      [
        13.2,
        37.09,
        24.0
      ],
      [
        1.65,
        4.26,
        3.0
      ],
      [
        5.95,
        8.0,
        1.0
      ],
      [
        24.78,
        13.84,
        6.0
      ],
      [
        1.71,
        13.73,
        9.0
      ],
      [
        40.56,
        39.54,
        24.0
      ],
      [
        31.8,
        14.24,
        4.0
      ],
      [
        5.1,
        4.56,
        2.0
      ],
      [
        8.26,
        6.74,
        2.0
      ],
      [
        9.9,
        11.03,
        6.0
      ],
      [
        2.46,
        2.49,
        1.0
      ],
      [
        1.45,
        2.7,
        1.0
      ],
      [
        60.0,
        29.42,
        16.0
      ],
      [
        16.5,
        16.39,
        10.0
      ],
      [
        8.5,
        15.09,
        10.0
      ],
      [
        13.2,
        37.09,
        24.0
      ],
      [
        10.0,
        13.35,
        8.0
      ],
      [
        290.0,
        167.15,
        2.0
      ],
      [
        2.55,
        3.17,
        1.0
      ],
      [
        15.0,
        19.87,
        12.0
      ],
      [
        26.4,
        75.63,
        48.0
      ],
      [
        44.55,
        19.52,
        9.0
      ],
      [
        4.92,
        4.46,
        2.0
      ],
      [
        0.85,
        2.21,
        1.0
      ],
      [
        8.26,
        6.93,
        2.0
      ],
      [
        15.0,
        10.44,
        4.0
      ],
      [
        11.7,
        11.37,
        6.0
      ],
      [
        31.8,
        15.2,
        4.0
      ],
      [
        30.0,
        37.69,
        24.0
      ],
      [
        10.2,
        19.22,
        12.0
      ],
      [
        61.2,
        39.36,
        24.0
      ],
      [
        4.95,
        6.86,
        1.0
      ],
      [
        1.63,
        3.1,
        1.0
      ],
      [
        30.0,
        38.27,
        24.0
      ],
      [
        3.75,
        4.15,
        1.0
      ],
      [
        59.52,
        24.27,
        12.0
      ],
      [
        4.92,
        5.62,
        2.0
      ],
      [
        4.13,
        5.74,
        1.0
      ],
      [
        8.4,
        7.41,
        4.0
      ],
      [
        2.46,
        3.84,
        1.0
      ],
      [
        4.25,
        6.07,
        1.0
      ],
      [
        16.8,
        12.77,
        8.0
      ],
      [
        34.8,
        39.47,
        24.0
      ],
      [
        3.29,
        4.59,
        1.0
      ],
      [
        1.58,
        3.53,
        2.0
      ],
      [
        4.25,
        5.68,
        1.0
      ],
      [
        6.5,
        14.48,
        10.0
      ],
      [
        30.0,
        16.38,
        8.0
      ],
      [
        0.42,
        1.53,
        1.0
      ],
      [
        2.9,
        2.93,
        2.0
      ],
      [
        19.8,
        19.94,
        12.0
      ],
      [
        24.96,
        27.63,
        1.0
      ],
      [
        1.1,
        1.91,
        2.0
      ],
      [
        9.9,
        9.87,
        6.0
      ],
      [
        4.95,
        6.86,
        1.0
      ],
      [
        4.2,
        4.82,
        2.0
      ],
      [
        0.83,
        1.8,
        1.0
      ],
      [
        1.25,
        0.93,
        1.0
      ],
      [
        10.5,
        39.69,
        25.0
      ],
      [
        34.0,
        15.83,
        4.0
      ],
      [
        31.2,
        76.13,
        48.0
      ],
      [
        75.78,
        33.11,
        18.0
      ],
      [
        6.6,
        6.13,
        4.0
      ],
      [
        17.7,
        12.31,
        6.0
      ],
      [
        1.95,
        4.18,
        3.0
      ],
      [
        20.65,
        11.49,
        5.0
      ],
      [
        15.0,
        19.87,
        12.0
      ],
      [
        17.7,
        10.76,
        6.0
      ],
      [
        6.25,
        8.61,
        5.0
      ],
      [
        92.16,
        202.37,
        128.0
      ],
      [
        20.8,
        17.46,
        10.0
      ],
      [
        20.8,
        17.26,
        10.0
      ],
      [
        39.6,
        39.11,
        24.0
      ],
      [
        2.5,
        3.86,
        2.0
      ],
      [
        33.2,
        16.83,
        8.0
      ],
      [
        30.6,
        56.61,
        36.0
      ],
      [
        1.65,
        3.12,
        1.0
      ],
      [
        21.0,
        17.67,
        10.0
      ],
      [
        17.4,
        20.1,
        12.0
      ],
      [
        8.26,
        6.74,
        2.0
      ],
      [
        102.0,
        65.83,
        40.0
      ],
      [
        3.26,
        4.87,
        2.0
      ],
      [
        15.8,
        9.51,
        4.0
      ],
      [
        18.75,
        10.54,
        3.0
      ],
      [
        1.25,
        2.86,
        1.0
      ],
      [
        135.0,
        38.19,
        20.0
      ],
      [
        10.2,
        17.68,
        12.0
      ],
      [
        1.95,
        7.82,
        5.0
      ],
      [
        23.4,
        19.12,
        12.0
      ],
      [
        7.8,
        6.27,
        4.0
      ],
      [
        4.92,
        4.65,
        2.0
      ],
      [
        16.5,
        11.61,
        2.0
      ],
      [
        1.25,
        2.47,
        1.0
      ],
      [
        5.79,
        7.04,
        1.0
      ],
      [
        35.4,
        20.25,
        12.0
      ],
      [
        16.63,
        18.57,
        1.0
      ],
      [
        9.36,
        37.88,
        24.0
      ],
      [
        12.5,
        16.51,
        10.0
      ],
      [
        33.2,
        17.03,
        8.0
      ],
      [
        1.63,
        2.71,
        1.0
      ],
      [
        10.79,
        19.24,
        13.0
      ],
      [
        1.66,
        3.32,
        1.0
      ],
      [
        17.7,
        12.5,
        6.0
      ],
      [
        61.2,
        39.17,
        24.0
      ],
      [
        17.0,
        10.81,
        4.0
      ],
      [
        16.95,
        20.09,
        1.0
      ],
      [
        4.2,
        5.21,
        2.0
      ],
      [
        0.95,
        0.97,
        1.0
      ],
      [
        4.13,
        4.19,
        1.0
      ],
      [
        7.8,
        17.45,
        12.0
      ],
      [
        21.9,
        13.9,
        2.0
      ],
      [
        37.9,
        24.33,
        2.0
      ],
      [
        14.75,
        8.99,
        5.0
      ],
      [
        7.65,
        5.76,
        3.0
      ],
      [
        5.1,
        4.37,
        2.0
      ],
      [
        1.95,
        3.65,
        1.0
      ],
      [
        4.15,
        4.99,
        1.0
      ],
      [
        16.52,
        10.87,
        4.0
      ],
      [
        2.46,
        3.07,
        1.0
      ],
      [
        2.95,
        4.79,
        1.0
      ],
      [
        4.65,
        5.36,
        1.0
      ],
      [
        4.13,
        5.74,
        1.0
      ],
      [
        9.96,
        18.43,
        12.0
      ],
      [
        4.13,
        4.97,
        1.0
      ],
      [
        2.08,
        2.06,
        1.0
      ],
      [
        1.66,
        3.32,
        1.0
      ],
      [
        4.2,
        5.4,
        2.0
      ],
      [
        66.0,
        63.26,
        40.0
      ],
      [
        19.8,
        19.55,
        12.0
      ],
      [
        10.2,
        18.07,
        12.0
      ],
      [
        2.46,
        3.07,
        1.0
      ],
      [
        51.0,
        18.03,
        6.0
      ],
      [
        7.5,
        5.34,
        2.0
      ],
      [
        3.32,
        2.78,
        2.0
      ],
      [
        30.0,
        15.99,
        8.0
      ],
      [
        2.95,
        4.79,
        1.0
      ],
      [
        30.0,
        37.89,
        24.0
      ],
      [
        2.5,
        3.67,
        2.0
      ],
      [
        1.25,
        2.47,
        1.0
      ],
      [
        3.4,
        5.02,
        4.0
      ],
      [
        19.5,
        15.76,
        10.0
      ],
      [
        5.0,
        5.86,
        4.0
      ],
      [
        1.9,
        2.75,
        2.0
      ],
      [
        33.0,
        13.81,
        4.0
      ],
      [
        3.75,
        5.5,
        1.0
      ],
      [
        2.08,
        3.22,
        1.0
      ],
      [
        2.1,
        3.44,
        1.0
      ],
      [
        31.8,
        19.72,
        12.0
      ],
      [
        2.95,
        3.05,
        1.0
      ],
      [
        5.04,
        17.96,
        12.0
      ],
      [
        6.6,
        18.88,
        12.0
      ],
      [
        81.36,
        41.09,
        24.0
      ],
      [
        8.29,
        10.07,
        1.0
      ],
      [
        15.0,
        9.86,
        4.0
      ],
      [
        20.8,
        17.46,
        10.0
      ],
      [
        50.88,
        75.44,
        48.0
      ],
      [
        7.5,
        7.28,
        2.0
      ],
      [
        10.5,
        39.88,
        25.0
      ],
      [
        2.5,
        4.25,
        2.0
      ],
      [
        3.26,
        4.68,
        2.0
      ],
      [
        0.85,
        2.21,
        1.0
      ],
      [
        1.65,
        1.77,
        1.0
      ],
      [
        15.0,
        20.26,
        12.0
      ],
      [
        4.2,
        5.4,
        2.0
      ],
      [
        8.3,
        7.54,
        2.0
      ],
      [
        25.0,
        32.72,
        20.0
      ],
      [
        2.46,
        3.26,
        1.0
      ],
      [
        34.72,
        16.17,
        7.0
      ],
      [
        19.8,
        11.8,
        4.0
      ],
      [
        51.0,
        22.89,
        12.0
      ],
      [
        1.63,
        1.36,
        1.0
      ],
      [
        316.8,
        303.31,
        192.0
      ],
      [
        31.6,
        16.61,
        8.0
      ],
      [
        1.63,
        1.94,
        1.0
      ],
      [
        2.5,
        2.89,
        2.0
      ],
      [
        2.1,
        3.82,
        1.0
      ],
      [
        19.92,
        14.56,
        8.0
      ],
      [
        5.04,
        17.38,
        12.0
      ],
      [
        15.0,
        18.33,
        12.0
      ],
      [
        4.89,
        5.29,
        3.0
      ],
      [
        30.6,
        57.57,
        36.0
      ],
      [
        4.89,
        6.07,
        3.0
      ],
      [
        4.2,
        4.05,
        2.0
      ],
      [
        5.04,
        18.54,
        12.0
      ],
      [
        14.85,
        8.48,
        3.0
      ],
      [
        6.63,
        6.84,
        1.0
      ],
      [
        0.84,
        3.3,
        2.0
      ],
      [
        9.84,
        6.85,
        4.0
      ],
      [
        20.8,
        16.68,
        10.0
      ],
      [
        0.85,
        2.21,
        1.0
      ],
      [
        51.0,
        22.89,
        12.0
      ],
      [
        3.38,
        3.59,
        2.0
      ],
      [
        5.9,
        5.02,
        2.0
      ],
      [
        1.25,
        1.89,
        1.0
      ],
      [
        2.34,
        9.79,
        6.0
      ],
      [
        1.63,
        2.9,
        1.0
      ],
      [
        15.8,
        9.12,
        4.0
      ],
      [
        3.3,
        9.01,
        6.0
      ],
      [
        14.85,
        15.58,
        9.0
      ],
      [
        72.0,
        156.73,
        100.0
      ],
      [
        2.88,
        37.38,
        24.0
      ],
      [
        7.95,
        10.07,
        1.0
      ],
      [
        1241.98,
        1409.2,
        1.0
      ],
      [
        25.2,
        20.84,
        12.0
      ],
      [
        4.2,
        3.67,
        2.0
      ],
      [
        1.65,
        2.54,
        1.0
      ],
      [
        7.8,
        18.61,
        12.0
      ],
      [
        5.06,
        7.18,
        1.0
      ],
      [
        19.5,
        12.07,
        6.0
      ],
      [
        8.7,
        10.99,
        6.0
      ],
      [
        23.12,
        14.83,
        8.0
      ],
      [
        8.25,
        9.64,
        1.0
      ],
      [
        74.88,
        114.73,
        72.0
      ],
      [
        10.79,
        11.94,
        1.0
      ],
      [
        33.26,
        21.89,
        2.0
      ],
      [
        20.8,
        17.07,
        10.0
      ],
      [
        16.5,
        10.64,
        2.0
      ],
      [
        15.0,
        19.68,
        12.0
      ],
      [
        1.25,
        1.7,
        1.0
      ],
      [
        10.79,
        11.94,
        1.0
      ],
      [
        15.9,
        11.27,
        2.0
      ],
      [
        67.8,
        25.42,
        4.0
      ],
      [
        67.7,
        23.36,
        10.0
      ],
      [
        9.9,
        7.29,
        2.0
      ],
      [
        45.0,
        57.25,
        36.0
      ],
      [
        1.63,
        1.55,
        1.0
      ],
      [
        16.58,
        11.85,
        2.0
      ],
      [
        10.5,
        38.91,
        25.0
      ],
      [
        40.8,
        76.75,
        48.0
      ],
      [
        11.8,
        7.6,
        4.0
      ],
      [
        1.66,
        3.38,
        2.0
      ],
      [
        14.22,
        28.26,
        18.0
      ],
      [
        19.8,
        10.06,
        4.0
      ],
      [
        30.6,
        20.19,
        12.0
      ],
      [
        17.0,
        12.28,
        2.0
      ],
      [
        68.0,
        314.86,
        200.0
      ],
      [
        17.4,
        20.29,
        12.0
      ],
      [
        15.0,
        10.18,
        2.0
      ],
      [
        4.25,
        7.19,
        5.0
      ],
      [
        7.8,
        17.65,
        12.0
      ],
      [
        2.5,
        3.47,
        2.0
      ],
      [
        26.4,
        26.07,
        16.0
      ],
      [
        1.7,
        2.63,
        2.0
      ],
      [
        19.8,
        19.36,
        12.0
      ],
      [
        5.79,
        6.85,
        1.0
      ],
      [
        15.0,
        8.31,
        4.0
      ],
      [
        4.15,
        5.57,
        1.0
      ],
      [
        47.7,
        17.98,
        6.0
      ],
      [
        72.0,
        26.41,
        4.0
      ],
      [
        119.51,
        136.26,
        1.0
      ],
      [
        39.84,
        76.15,
        48.0
      ],
      [
        6.5,
        16.22,
        10.0
      ],
      [
        15.9,
        10.3,
        2.0
      ],
      [
        4.95,
        6.67,
        1.0
      ],
      [
        7.95,
        10.46,
        1.0
      ],
      [
        3.3,
        3.54,
        2.0
      ],
      [
        10.2,
        19.03,
        12.0
      ],
      [
        17.7,
        12.5,
        6.0
      ],
      [
        8.4,
        8.18,
        4.0
      ],
      [
        15.9,
        11.65,
        2.0
      ],
      [
        1.7,
        3.21,
        2.0
      ],
      [
        11.7,
        9.82,
        6.0
      ],
      [
        19.8,
        10.84,
        4.0
      ],
      [
        6.25,
        7.64,
        5.0
      ],
      [
        3.4,
        5.02,
        4.0
      ],
      [
        5.79,
        6.85,
        1.0
      ],
      [
        19.8,
        20.32,
        12.0
      ],
      [
        10.79,
        12.33,
        1.0
      ],
      [
        14.04,
        56.47,
        36.0
      ],
      [
        8.29,
        8.91,
        1.0
      ],
      [
        1.63,
        2.32,
        1.0
      ],
      [
        207.36,
        909.82,
        576.0
      ],
      [
        3.75,
        5.83,
        3.0
      ],
      [
        30.0,
        37.69,
        24.0
      ],
      [
        23.4,
        18.93,
        12.0
      ],
      [
        5.9,
        5.79,
        2.0
      ],
      [
        5.04,
        17.38,
        12.0
      ],
      [
        11.63,
        13.09,
        1.0
      ],
      [
        4.16,
        4.8,
        2.0
      ],
      [
        25.2,
        19.1,
        12.0
      ],
      [
        13.5,
        9.91,
        2.0
      ],
      [
        4.16,
        4.61,
        2.0
      ],
      [
        3.3,
        9.59,
        6.0
      ],
      [
        6.3,
        6.79,
        3.0
      ],
      [
        2.51,
        4.29,
        1.0
      ],
      [
        1.66,
        3.19,
        2.0
      ],
      [
        157.44,
        103.88,
        64.0
      ],
      [
        1.56,
        6.43,
        4.0
      ],
      [
        4.96,
        6.68,
        1.0
      ],
      [
        133.12,
        202.73,
        128.0
      ],
      [
        19.8,
        18.97,
        12.0
      ],
      [
        7.5,
        9.41,
        6.0
      ],
      [
        88.8,
        77.3,
        48.0
      ],
      [
        2.46,
        3.07,
        1.0
      ],
      [
        15.12,
        55.35,
        36.0
      ],
      [
        12.48,
        11.13,
        6.0
      ],
      [
        15.9,
        10.11,
        2.0
      ],
      [
        3.95,
        5.73,
        1.0
      ],
      [
        39.8,
        16.89,
        4.0
      ],
      [
        10.5,
        9.96,
        5.0
      ],
      [
        0.83,
        1.22,
        1.0
      ],
      [
        25.5,
        13.78,
        6.0
      ],
      [
        20.4,
        38.59,
        24.0
      ],
      [
        15.3,
        10.5,
        6.0
      ],
      [
        12.5,
        15.93,
        10.0
      ],
      [
        2.46,
        2.69,
        1.0
      ],
      [
        4.95,
        6.86,
        1.0
      ],
      [
        7.65,
        6.53,
        3.0
      ],
      [
        6.6,
        7.09,
        4.0
      ],
      [
        67.5,
        22.17,
        10.0
      ],
      [
        17.0,
        10.54,
        2.0
      ],
      [
        6.96,
        36.22,
        24.0
      ],
      [
        10.4,
        25.52,
        16.0
      ],
      [
        17.7,
        12.12,
        6.0
      ],
      [
        21.97,
        22.34,
        13.0
      ],
      [
        17.0,
        11.89,
        2.0
      ],
      [
        15.0,
        19.48,
        12.0
      ],
      [
        15.0,
        18.52,
        12.0
      ],
      [
        99.6,
        42.34,
        24.0
      ],
      [
        4.98,
        9.32,
        6.0
      ],
      [
        4.35,
        6.06,
        3.0
      ],
      [
        38.25,
        16.94,
        3.0
      ],
      [
        5.78,
        5.91,
        2.0
      ],
      [
        2.52,
        8.67,
        6.0
      ],
      [
        0.84,
        2.73,
        2.0
      ],
      [
        5.04,
        19.32,
        12.0
      ],
      [
        6.58,
        6.17,
        2.0
      ],
      [
        8.15,
        9.42,
        5.0
      ],
      [
        12.6,
        11.54,
        6.0
      ],
      [
        16.52,
        9.52,
        4.0
      ],
      [
        67.5,
        32.58,
        18.0
      ],
      [
        10.0,
        13.54,
        8.0
      ],
      [
        15.9,
        10.88,
        2.0
      ],
      [
        7.5,
        10.77,
        6.0
      ],
      [
        39.6,
        38.53,
        24.0
      ],
      [
        17.4,
        19.33,
        12.0
      ],
      [
        1.65,
        2.15,
        1.0
      ],
      [
        3.26,
        3.52,
        2.0
      ],
      [
        19.92,
        13.36,
        2.0
      ],
      [
        17.4,
        18.94,
        12.0
      ],
      [
        21.58,
        15.07,
        2.0
      ],
      [
        18.72,
        75.65,
        48.0
      ],
      [
        2.95,
        4.59,
        1.0
      ],
      [
        4.13,
        4.39,
        1.0
      ],
      [
        0.39,
        1.11,
        1.0
      ],
      [
        10.5,
        38.72,
        25.0
      ],
      [
        19.8,
        11.8,
        4.0
      ],
      [
        1.95,
        3.65,
        1.0
      ],
      [
        2.95,
        4.59,
        1.0
      ],
      [
        26.0,
        62.9,
        40.0
      ],
      [
        1.65,
        1.19,
        1.0
      ],
      [
        5.06,
        7.18,
        1.0
      ],
      [
        6.5,
        14.67,
        10.0
      ],
      [
        17.4,
        19.52,
        12.0
      ],
      [
        2.5,
        3.67,
        2.0
      ],
      [
        2.51,
        4.29,
        1.0
      ],
      [
        25.5,
        12.24,
        6.0
      ],
      [
        20.8,
        17.46,
        10.0
      ],
      [
        5.8,
        7.64,
        4.0
      ],
      [
        15.9,
        10.69,
        2.0
      ],
      [
        13.52,
        13.27,
        8.0
      ],
      [
        22.5,
        13.22,
        6.0
      ],
      [
        15.3,
        10.5,
        6.0
      ],
      [
        17.7,
        11.34,
        6.0
      ],
      [
        10.2,
        19.61,
        12.0
      ],
      [
        20.4,
        38.59,
        24.0
      ],
      [
        17.7,
        11.54,
        6.0
      ],
      [
        2.9,
        3.51,
        2.0
      ],
      [
        11.8,
        8.95,
        4.0
      ],
      [
        2.5,
        3.47,
        2.0
      ],
      [
        2.5,
        4.05,
        2.0
      ],
      [
        15.0,
        10.05,
        4.0
      ],
      [
        4.92,
        3.88,
        2.0
      ],
      [
        10.2,
        18.26,
        12.0
      ],
      [
        20.8,
        17.46,
        10.0
      ],
      [
        5.04,
        17.19,
        12.0
      ],
      [
        61.2,
        21.0,
        8.0
      ],
      [
        17.0,
        11.01,
        4.0
      ],
      [
        3.75,
        5.69,
        1.0
      ],
      [
        1.25,
        1.7,
        1.0
      ],
      [
        1.63,
        2.71,
        1.0
      ],
      [
        2.9,
        4.67,
        2.0
      ],
      [
        15.79,
        17.62,
        1.0
      ],
      [
        12.5,
        16.32,
        10.0
      ],
      [
        10.2,
        19.8,
        12.0
      ],
      [
        2.52,
        9.44,
        6.0
      ],
      [
        0.83,
        2.19,
        1.0
      ],
      [
        4.95,
        6.28,
        3.0
      ],
      [
        6.25,
        8.41,
        5.0
      ],
      [
        0.85,
        0.28,
        1.0
      ],
      [
        5.95,
        8.0,
        1.0
      ],
      [
        1.63,
        3.1,
        1.0
      ],
      [
        12.6,
        10.57,
        6.0
      ],
      [
        8.29,
        9.11,
        1.0
      ],
      [
        165.0,
        159.91,
        100.0
      ],
      [
        16.6,
        10.51,
        4.0
      ],
      [
        16.3,
        16.56,
        10.0
      ],
      [
        5.9,
        6.18,
        2.0
      ],
      [
        1.1,
        1.91,
        2.0
      ],
      [
        12.5,
        14.97,
        10.0
      ],
      [
        8.25,
        9.64,
        5.0
      ],
      [
        51.0,
        17.25,
        6.0
      ],
      [
        10.2,
        17.87,
        12.0
      ],
      [
        2.9,
        4.28,
        2.0
      ],
      [
        29.7,
        28.27,
        18.0
      ],
      [
        20.8,
        17.07,
        10.0
      ],
      [
        17.7,
        11.73,
        6.0
      ],
      [
        4.25,
        4.33,
        1.0
      ],
      [
        15.9,
        11.08,
        2.0
      ],
      [
        14.75,
        10.92,
        5.0
      ],
      [
        14.75,
        9.76,
        5.0
      ],
      [
        8.7,
        10.22,
        6.0
      ],
      [
        2.5,
        3.47,
        2.0
      ],
      [
        4.95,
        6.86,
        1.0
      ],
      [
        15.0,
        19.87,
        12.0
      ],
      [
        5.95,
        7.8,
        1.0
      ],
      [
        9.92,
        8.26,
        2.0
      ],
      [
        10.44,
        56.36,
        36.0
      ],
      [
        3.75,
        4.67,
        3.0
      ],
      [
        1.65,
        2.35,
        1.0
      ],
      [
        0.42,
        -0.21,
        1.0
      ],
      [
        0.85,
        2.21,
        1.0
      ],
      [
        16.5,
        12.0,
        2.0
      ],
      [
        13.2,
        14.38,
        8.0
      ],
      [
        1.65,
        2.15,
        1.0
      ],
      [
        3.75,
        5.31,
        1.0
      ],
      [
        13.5,
        10.29,
        2.0
      ],
      [
        3.38,
        4.55,
        2.0
      ],
      [
        15.0,
        20.06,
        12.0
      ],
      [
        7.95,
        8.91,
        1.0
      ],
      [
        16.58,
        10.3,
        2.0
      ],
      [
        3.29,
        4.98,
        1.0
      ],
      [
        32.85,
        17.03,
        3.0
      ],
      [
        5.04,
        19.12,
        12.0
      ],
      [
        3.29,
        3.63,
        1.0
      ],
      [
        24.9,
        13.28,
        6.0
      ],
      [
        15.8,
        32.39,
        20.0
      ],
      [
        17.7,
        12.7,
        6.0
      ],
      [
        6.72,
        6.83,
        2.0
      ],
      [
        35.7,
        13.97,
        6.0
      ],
      [
        31.5,
        118.58,
        75.0
      ],
      [
        3.12,
        12.57,
        8.0
      ],
      [
        0.85,
        2.4,
        1.0
      ],
      [
        2.5,
        4.44,
        2.0
      ],
      [
        3.3,
        2.77,
        2.0
      ],
      [
        8.25,
        8.09,
        5.0
      ],
      [
        6.8,
        12.9,
        8.0
      ],
      [
        9.96,
        11.23,
        6.0
      ],
      [
        9.9,
        11.03,
        6.0
      ],
      [
        16.84,
        10.96,
        4.0
      ],
      [
        0.83,
        1.99,
        1.0
      ],
      [
        3.26,
        2.75,
        2.0
      ],
      [
        16.5,
        12.0,
        2.0
      ],
      [
        10.2,
        18.64,
        12.0
      ],
      [
        7.5,
        7.08,
        2.0
      ],
      [
        10.08,
        38.1,
        24.0
      ],
      [
        9.9,
        8.06,
        2.0
      ],
      [
        33.0,
        32.79,
        20.0
      ],
      [
        33.9,
        21.87,
        2.0
      ],
      [
        15.79,
        17.62,
        1.0
      ],
      [
        30.0,
        39.24,
        24.0
      ],
      [
        3.75,
        5.64,
        3.0
      ],
      [
        29.7,
        14.39,
        6.0
      ],
      [
        10.2,
        19.42,
        12.0
      ],
      [
        10.0,
        13.16,
        8.0
      ],
      [
        15.3,
        11.47,
        6.0
      ],
      [
        1.25,
        1.31,
        1.0
      ],
      [
        61.2,
        39.17,
        24.0
      ],
      [
        0.55,
        1.87,
        1.0
      ],
      [
        2.1,
        3.63,
        1.0
      ],
      [
        14.95,
        16.86,
        1.0
      ],
      [
        4.95,
        5.32,
        3.0
      ],
      [
        17.0,
        9.27,
        4.0
      ],
      [
        2.9,
        4.67,
        2.0
      ],
      [
        20.8,
        16.49,
        10.0
      ],
      [
        0.84,
        3.5,
        2.0
      ],
      [
        1.17,
        3.5,
        3.0
      ],
      [
        39.0,
        31.77,
        20.0
      ],
      [
        3.75,
        5.83,
        3.0
      ],
      [
        24.9,
        13.67,
        6.0
      ],
      [
        16.95,
        20.09,
        1.0
      ],
      [
        3.75,
        5.31,
        1.0
      ],
      [
        16.63,
        20.11,
        1.0
      ],
      [
        59.4,
        23.1,
        12.0
      ],
      [
        98.1,
        32.39,
        18.0
      ],
      [
        7.5,
        9.8,
        6.0
      ]
    ],
    "sample_prediction_lab": {
      "inputs": {
        "Quantity": 10,
        "UnitPrice": 5,
        "Month": 12
      },
      "predicted_sales": 21.35
    }
  },
  "lab5_decision_tree": {
    "target": "Sales_Category",
    "classes": [
      "Low",
      "Medium",
      "High"
    ],
    "criterion": "entropy",
    "max_depth": 5,
    "accuracy": 0.9434,
    "confusion_matrix": [
      [
        3201,
        95,
        0
      ],
      [
        110,
        3066,
        279
      ],
      [
        0,
        82,
        3167
      ]
    ],
    "feature_importance": {
      "Quantity": 0.52,
      "UnitPrice": 0.44,
      "Month": 0.04
    },
    "tree_structure": {
      "leaf": false,
      "feature": "Quantity",
      "threshold": 3.0,
      "left": {
        "leaf": false,
        "feature": "UnitPrice",
        "threshold": 4.95,
        "left": {
          "leaf": false,
          "feature": "Quantity",
          "threshold": 1.0,
          "left": {
            "leaf": true,
            "class": "Low",
            "probs": [
              1.0,
              0.0,
              0.0
            ]
          },
          "right": {
            "leaf": false,
            "feature": "UnitPrice",
            "threshold": 2.46,
            "left": {
              "leaf": false,
              "feature": "UnitPrice",
              "threshold": 1.65,
              "left": {
                "leaf": true,
                "class": "Low",
                "probs": [
                  1.0,
                  0.0,
                  0.0
                ]
              },
              "right": {
                "leaf": true,
                "class": "Low",
                "probs": [
                  0.6719,
                  0.3281,
                  0.0
                ]
              }
            },
            "right": {
              "leaf": false,
              "feature": "UnitPrice",
              "threshold": 2.55,
              "left": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0625,
                  0.9375,
                  0.0
                ]
              },
              "right": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0,
                  1.0,
                  0.0
                ]
              }
            }
          }
        },
        "right": {
          "leaf": false,
          "feature": "Quantity",
          "threshold": 1.0,
          "left": {
            "leaf": false,
            "feature": "UnitPrice",
            "threshold": 15.66,
            "left": {
              "leaf": false,
              "feature": "UnitPrice",
              "threshold": 4.96,
              "left": {
                "leaf": true,
                "class": "Low",
                "probs": [
                  1.0,
                  0.0,
                  0.0
                ]
              },
              "right": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0052,
                  0.9943,
                  0.0005
                ]
              }
            },
            "right": {
              "leaf": true,
              "class": "High",
              "probs": [
                0.0,
                0.0,
                1.0
              ]
            }
          },
          "right": {
            "leaf": false,
            "feature": "UnitPrice",
            "threshold": 7.46,
            "left": {
              "leaf": false,
              "feature": "Quantity",
              "threshold": 2.0,
              "left": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0,
                  1.0,
                  0.0
                ]
              },
              "right": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0,
                  0.0791,
                  0.9209
                ]
              }
            },
            "right": {
              "leaf": false,
              "feature": "UnitPrice",
              "threshold": 7.95,
              "left": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0,
                  0.0927,
                  0.9073
                ]
              },
              "right": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0,
                  0.0,
                  1.0
                ]
              }
            }
          }
        }
      },
      "right": {
        "leaf": false,
        "feature": "UnitPrice",
        "threshold": 1.25,
        "left": {
          "leaf": false,
          "feature": "Quantity",
          "threshold": 12.0,
          "left": {
            "leaf": false,
            "feature": "Quantity",
            "threshold": 5.0,
            "left": {
              "leaf": false,
              "feature": "UnitPrice",
              "threshold": 0.85,
              "left": {
                "leaf": true,
                "class": "Low",
                "probs": [
                  1.0,
                  0.0,
                  0.0
                ]
              },
              "right": {
                "leaf": true,
                "class": "Low",
                "probs": [
                  0.7635,
                  0.2365,
                  0.0
                ]
              }
            },
            "right": {
              "leaf": false,
              "feature": "UnitPrice",
              "threshold": 0.39,
              "left": {
                "leaf": true,
                "class": "Low",
                "probs": [
                  1.0,
                  0.0,
                  0.0
                ]
              },
              "right": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0676,
                  0.9324,
                  0.0
                ]
              }
            }
          },
          "right": {
            "leaf": false,
            "feature": "UnitPrice",
            "threshold": 0.55,
            "left": {
              "leaf": false,
              "feature": "Quantity",
              "threshold": 36.0,
              "left": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0536,
                  0.9257,
                  0.0207
                ]
              },
              "right": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0327,
                  0.1875,
                  0.7798
                ]
              }
            },
            "right": {
              "leaf": false,
              "feature": "Quantity",
              "threshold": 18.0,
              "left": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0,
                  0.5263,
                  0.4737
                ]
              },
              "right": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0,
                  0.0115,
                  0.9885
                ]
              }
            }
          }
        },
        "right": {
          "leaf": false,
          "feature": "Quantity",
          "threshold": 8.0,
          "left": {
            "leaf": false,
            "feature": "UnitPrice",
            "threshold": 2.46,
            "left": {
              "leaf": false,
              "feature": "Quantity",
              "threshold": 6.0,
              "left": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0,
                  1.0,
                  0.0
                ]
              },
              "right": {
                "leaf": true,
                "class": "Medium",
                "probs": [
                  0.0,
                  0.605,
                  0.395
                ]
              }
            },
            "right": {
              "leaf": false,
              "feature": "UnitPrice",
              "threshold": 3.75,
              "left": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0,
                  0.3526,
                  0.6474
                ]
              },
              "right": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0,
                  0.0,
                  1.0
                ]
              }
            }
          },
          "right": {
            "leaf": false,
            "feature": "Quantity",
            "threshold": 10.0,
            "left": {
              "leaf": false,
              "feature": "Quantity",
              "threshold": 9.0,
              "left": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0,
                  0.2317,
                  0.7683
                ]
              },
              "right": {
                "leaf": true,
                "class": "High",
                "probs": [
                  0.0,
                  0.0065,
                  0.9935
                ]
              }
            },
            "right": {
              "leaf": true,
              "class": "High",
              "probs": [
                0.0,
                0.0,
                1.0
              ]
            }
          }
        }
      }
    },
    "sample_prediction_lab": {
      "inputs": {
        "Quantity": 10,
        "UnitPrice": 5,
        "Month": 12
      },
      "predicted_category": "High"
    }
  },
  "lab6_naive_bayes": {
    "target": "Sales_Category",
    "classes": [
      "Low",
      "Medium",
      "High"
    ],
    "accuracy": 0.5621,
    "confusion_matrix": [
      [
        6198,
        468,
        5
      ],
      [
        2811,
        3909,
        77
      ],
      [
        918,
        4479,
        1135
      ]
    ],
    "model_parameters": {
      "classes": [
        "Low",
        "Medium",
        "High"
      ],
      "priors": [
        0.3346,
        0.3373,
        0.3281
      ],
      "means": [
        [
          2.059,
          1.933,
          7.736
        ],
        [
          7.45,
          3.331,
          7.471
        ],
        [
          22.799,
          6.48,
          7.481
        ]
      ],
      "vars": [
        [
          10.951,
          1.582,
          12.477
        ],
        [
          66.825,
          9.581,
          12.635
        ],
        [
          103206.417,
          3387.076,
          11.771
        ]
      ],
      "features": [
        "Quantity",
        "UnitPrice",
        "Month"
      ]
    },
    "sample_prediction_lab": {
      "inputs": {
        "Quantity": 10,
        "UnitPrice": 5,
        "Month": 12
      },
      "predicted_category": "Medium",
      "probabilities": {
        "Low": 0.0225,
        "Medium": 0.976,
        "High": 0.0015
      }
    }
  },
  "lab7_kmeans": {
    "features": [
      "TotalSpending",
      "TotalOrders",
      "TotalQuantity",
      "AverageOrderValue",
      "UniqueProducts"
    ],
    "optimal_k": 3,
    "wcss": [
      27985.31,
      11675.31,
      8784.17,
      7540.15,
      6578.19,
      6032.57,
      5405.71,
      5155.09,
      4844.49,
      4546.63
    ],
    "silhouette": 0.304,
    "cluster_sizes": [
      1170,
      1180,
      1988
    ],
    "profiles": [
      {
        "cluster": 1,
        "size": 1170,
        "avg_spending": 6044.79,
        "avg_orders": 10.34,
        "avg_quantity": 3503.16,
        "avg_order_value": 709.76,
        "avg_unique_products": 139.71
      },
      {
        "cluster": 2,
        "size": 1180,
        "avg_spending": 211.82,
        "avg_orders": 1.41,
        "avg_quantity": 113.92,
        "avg_order_value": 164.51,
        "avg_unique_products": 13.15
      },
      {
        "cluster": 3,
        "size": 1988,
        "avg_spending": 799.33,
        "avg_orders": 2.4,
        "avg_quantity": 470.17,
        "avg_order_value": 399.3,
        "avg_unique_products": 44.18
      }
    ],
    "scatter_sample": [
      {
        "id": 17785,
        "spending": 131.94,
        "orders": 1,
        "quantity": 67,
        "order_value": 131.94,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 14320,
        "spending": 477.79,
        "orders": 2,
        "quantity": 325,
        "order_value": 238.89,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 15977,
        "spending": 1054.73,
        "orders": 2,
        "quantity": 1016,
        "order_value": 527.37,
        "unique_prods": 48,
        "cluster": 2
      },
      {
        "id": 12364,
        "spending": 1313.1,
        "orders": 4,
        "quantity": 1506,
        "order_value": 328.28,
        "unique_prods": 70,
        "cluster": 0
      },
      {
        "id": 14566,
        "spending": 1432.0,
        "orders": 1,
        "quantity": 800,
        "order_value": 1432.0,
        "unique_prods": 4,
        "cluster": 2
      },
      {
        "id": 13521,
        "spending": 1093.65,
        "orders": 3,
        "quantity": 736,
        "order_value": 364.55,
        "unique_prods": 313,
        "cluster": 0
      },
      {
        "id": 12515,
        "spending": 383.7,
        "orders": 1,
        "quantity": 131,
        "order_value": 383.7,
        "unique_prods": 16,
        "cluster": 2
      },
      {
        "id": 15528,
        "spending": 229.33,
        "orders": 1,
        "quantity": 123,
        "order_value": 229.33,
        "unique_prods": 26,
        "cluster": 1
      },
      {
        "id": 15071,
        "spending": 982.07,
        "orders": 2,
        "quantity": 269,
        "order_value": 491.04,
        "unique_prods": 25,
        "cluster": 2
      },
      {
        "id": 16275,
        "spending": 559.87,
        "orders": 1,
        "quantity": 336,
        "order_value": 559.87,
        "unique_prods": 33,
        "cluster": 2
      },
      {
        "id": 15572,
        "spending": 2552.86,
        "orders": 7,
        "quantity": 1229,
        "order_value": 364.69,
        "unique_prods": 166,
        "cluster": 0
      },
      {
        "id": 16029,
        "spending": 81024.84,
        "orders": 63,
        "quantity": 40208,
        "order_value": 1286.11,
        "unique_prods": 44,
        "cluster": 0
      },
      {
        "id": 13772,
        "spending": 1132.13,
        "orders": 3,
        "quantity": 546,
        "order_value": 377.38,
        "unique_prods": 141,
        "cluster": 2
      },
      {
        "id": 18033,
        "spending": 97.97,
        "orders": 1,
        "quantity": 253,
        "order_value": 97.97,
        "unique_prods": 32,
        "cluster": 1
      },
      {
        "id": 14544,
        "spending": 2024.45,
        "orders": 2,
        "quantity": 1543,
        "order_value": 1012.23,
        "unique_prods": 97,
        "cluster": 0
      },
      {
        "id": 13495,
        "spending": 2044.87,
        "orders": 5,
        "quantity": 829,
        "order_value": 408.97,
        "unique_prods": 34,
        "cluster": 0
      },
      {
        "id": 17374,
        "spending": 495.77,
        "orders": 2,
        "quantity": 85,
        "order_value": 247.88,
        "unique_prods": 24,
        "cluster": 2
      },
      {
        "id": 16841,
        "spending": 1869.82,
        "orders": 6,
        "quantity": 2250,
        "order_value": 311.64,
        "unique_prods": 101,
        "cluster": 0
      },
      {
        "id": 12818,
        "spending": 1542.08,
        "orders": 1,
        "quantity": 929,
        "order_value": 1542.08,
        "unique_prods": 14,
        "cluster": 2
      },
      {
        "id": 17556,
        "spending": 157.9,
        "orders": 1,
        "quantity": 101,
        "order_value": 157.9,
        "unique_prods": 6,
        "cluster": 1
      },
      {
        "id": 17706,
        "spending": 10504.49,
        "orders": 17,
        "quantity": 3899,
        "order_value": 617.91,
        "unique_prods": 270,
        "cluster": 0
      },
      {
        "id": 13334,
        "spending": 3536.82,
        "orders": 3,
        "quantity": 1774,
        "order_value": 1178.94,
        "unique_prods": 207,
        "cluster": 0
      },
      {
        "id": 16555,
        "spending": 285.89,
        "orders": 2,
        "quantity": 175,
        "order_value": 142.94,
        "unique_prods": 15,
        "cluster": 1
      },
      {
        "id": 15750,
        "spending": 2465.48,
        "orders": 8,
        "quantity": 1786,
        "order_value": 308.19,
        "unique_prods": 214,
        "cluster": 0
      },
      {
        "id": 15245,
        "spending": 2515.84,
        "orders": 3,
        "quantity": 1784,
        "order_value": 838.61,
        "unique_prods": 55,
        "cluster": 0
      },
      {
        "id": 14850,
        "spending": 325.75,
        "orders": 1,
        "quantity": 293,
        "order_value": 325.75,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 12480,
        "spending": 3281.63,
        "orders": 4,
        "quantity": 1707,
        "order_value": 820.41,
        "unique_prods": 129,
        "cluster": 0
      },
      {
        "id": 16025,
        "spending": 439.66,
        "orders": 1,
        "quantity": 338,
        "order_value": 439.66,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 12721,
        "spending": 2656.13,
        "orders": 6,
        "quantity": 1959,
        "order_value": 442.69,
        "unique_prods": 133,
        "cluster": 0
      },
      {
        "id": 14333,
        "spending": 415.2,
        "orders": 1,
        "quantity": 58,
        "order_value": 415.2,
        "unique_prods": 15,
        "cluster": 1
      },
      {
        "id": 15976,
        "spending": 430.94,
        "orders": 2,
        "quantity": 277,
        "order_value": 215.47,
        "unique_prods": 83,
        "cluster": 2
      },
      {
        "id": 14346,
        "spending": 1021.58,
        "orders": 2,
        "quantity": 605,
        "order_value": 510.79,
        "unique_prods": 55,
        "cluster": 2
      },
      {
        "id": 17447,
        "spending": 541.53,
        "orders": 2,
        "quantity": 443,
        "order_value": 270.76,
        "unique_prods": 33,
        "cluster": 2
      },
      {
        "id": 16978,
        "spending": 344.33,
        "orders": 1,
        "quantity": 166,
        "order_value": 344.33,
        "unique_prods": 39,
        "cluster": 2
      },
      {
        "id": 13460,
        "spending": 183.44,
        "orders": 2,
        "quantity": 286,
        "order_value": 91.72,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 14462,
        "spending": 2004.02,
        "orders": 11,
        "quantity": 964,
        "order_value": 182.18,
        "unique_prods": 150,
        "cluster": 0
      },
      {
        "id": 15159,
        "spending": 18641.01,
        "orders": 30,
        "quantity": 11441,
        "order_value": 621.37,
        "unique_prods": 363,
        "cluster": 0
      },
      {
        "id": 15201,
        "spending": 1236.54,
        "orders": 5,
        "quantity": 1210,
        "order_value": 247.31,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 15088,
        "spending": 1160.07,
        "orders": 2,
        "quantity": 460,
        "order_value": 580.03,
        "unique_prods": 53,
        "cluster": 2
      },
      {
        "id": 12704,
        "spending": 2340.84,
        "orders": 8,
        "quantity": 1006,
        "order_value": 292.6,
        "unique_prods": 64,
        "cluster": 0
      },
      {
        "id": 12955,
        "spending": 4757.16,
        "orders": 11,
        "quantity": 3664,
        "order_value": 432.47,
        "unique_prods": 81,
        "cluster": 0
      },
      {
        "id": 17839,
        "spending": 338.8,
        "orders": 1,
        "quantity": 285,
        "order_value": 338.8,
        "unique_prods": 50,
        "cluster": 2
      },
      {
        "id": 17109,
        "spending": 885.04,
        "orders": 6,
        "quantity": 589,
        "order_value": 147.51,
        "unique_prods": 107,
        "cluster": 2
      },
      {
        "id": 14059,
        "spending": 183.6,
        "orders": 1,
        "quantity": 128,
        "order_value": 183.6,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 14019,
        "spending": 1421.61,
        "orders": 3,
        "quantity": 1037,
        "order_value": 473.87,
        "unique_prods": 37,
        "cluster": 2
      },
      {
        "id": 16858,
        "spending": 375.69,
        "orders": 1,
        "quantity": 91,
        "order_value": 375.69,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 15054,
        "spending": 302.1,
        "orders": 2,
        "quantity": 198,
        "order_value": 151.05,
        "unique_prods": 105,
        "cluster": 2
      },
      {
        "id": 15653,
        "spending": 877.44,
        "orders": 2,
        "quantity": 1200,
        "order_value": 438.72,
        "unique_prods": 4,
        "cluster": 2
      },
      {
        "id": 14104,
        "spending": 216.21,
        "orders": 2,
        "quantity": 72,
        "order_value": 108.1,
        "unique_prods": 21,
        "cluster": 1
      },
      {
        "id": 16150,
        "spending": 2053.02,
        "orders": 5,
        "quantity": 1047,
        "order_value": 410.6,
        "unique_prods": 91,
        "cluster": 0
      },
      {
        "id": 15381,
        "spending": 596.85,
        "orders": 2,
        "quantity": 171,
        "order_value": 298.43,
        "unique_prods": 8,
        "cluster": 2
      },
      {
        "id": 17158,
        "spending": 1266.97,
        "orders": 3,
        "quantity": 778,
        "order_value": 422.32,
        "unique_prods": 53,
        "cluster": 2
      },
      {
        "id": 13171,
        "spending": 468.41,
        "orders": 3,
        "quantity": 229,
        "order_value": 156.14,
        "unique_prods": 37,
        "cluster": 2
      },
      {
        "id": 14960,
        "spending": 221.27,
        "orders": 2,
        "quantity": 221,
        "order_value": 110.63,
        "unique_prods": 23,
        "cluster": 1
      },
      {
        "id": 13510,
        "spending": 1791.56,
        "orders": 4,
        "quantity": 1386,
        "order_value": 447.89,
        "unique_prods": 86,
        "cluster": 0
      },
      {
        "id": 15319,
        "spending": 204.5,
        "orders": 1,
        "quantity": 175,
        "order_value": 204.5,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 16160,
        "spending": 1025.44,
        "orders": 2,
        "quantity": 1162,
        "order_value": 512.72,
        "unique_prods": 20,
        "cluster": 2
      },
      {
        "id": 14367,
        "spending": 9261.52,
        "orders": 16,
        "quantity": 4438,
        "order_value": 578.85,
        "unique_prods": 270,
        "cluster": 0
      },
      {
        "id": 12526,
        "spending": 1316.66,
        "orders": 3,
        "quantity": 632,
        "order_value": 438.89,
        "unique_prods": 64,
        "cluster": 2
      },
      {
        "id": 16358,
        "spending": 2027.5,
        "orders": 4,
        "quantity": 1302,
        "order_value": 506.88,
        "unique_prods": 82,
        "cluster": 0
      },
      {
        "id": 14538,
        "spending": 388.25,
        "orders": 2,
        "quantity": 155,
        "order_value": 194.12,
        "unique_prods": 19,
        "cluster": 1
      },
      {
        "id": 14100,
        "spending": 194.9,
        "orders": 1,
        "quantity": 64,
        "order_value": 194.9,
        "unique_prods": 24,
        "cluster": 1
      },
      {
        "id": 13652,
        "spending": 1095.08,
        "orders": 3,
        "quantity": 578,
        "order_value": 365.03,
        "unique_prods": 48,
        "cluster": 2
      },
      {
        "id": 16898,
        "spending": 508.81,
        "orders": 3,
        "quantity": 419,
        "order_value": 169.6,
        "unique_prods": 150,
        "cluster": 2
      },
      {
        "id": 16293,
        "spending": 2248.99,
        "orders": 10,
        "quantity": 982,
        "order_value": 224.9,
        "unique_prods": 102,
        "cluster": 0
      },
      {
        "id": 16499,
        "spending": 365.45,
        "orders": 2,
        "quantity": 127,
        "order_value": 182.73,
        "unique_prods": 18,
        "cluster": 1
      },
      {
        "id": 16102,
        "spending": 1842.14,
        "orders": 3,
        "quantity": 942,
        "order_value": 614.05,
        "unique_prods": 41,
        "cluster": 2
      },
      {
        "id": 14527,
        "spending": 8508.82,
        "orders": 55,
        "quantity": 2089,
        "order_value": 154.71,
        "unique_prods": 330,
        "cluster": 0
      },
      {
        "id": 16131,
        "spending": 3506.54,
        "orders": 6,
        "quantity": 1802,
        "order_value": 584.42,
        "unique_prods": 55,
        "cluster": 0
      },
      {
        "id": 17761,
        "spending": 712.78,
        "orders": 1,
        "quantity": 398,
        "order_value": 712.78,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 15468,
        "spending": 467.51,
        "orders": 2,
        "quantity": 155,
        "order_value": 233.75,
        "unique_prods": 24,
        "cluster": 2
      },
      {
        "id": 12683,
        "spending": 8476.57,
        "orders": 15,
        "quantity": 4987,
        "order_value": 565.1,
        "unique_prods": 177,
        "cluster": 0
      },
      {
        "id": 12566,
        "spending": 351.65,
        "orders": 1,
        "quantity": 265,
        "order_value": 351.65,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 17574,
        "spending": 185.65,
        "orders": 1,
        "quantity": 77,
        "order_value": 185.65,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 13430,
        "spending": 679.45,
        "orders": 2,
        "quantity": 751,
        "order_value": 339.72,
        "unique_prods": 48,
        "cluster": 2
      },
      {
        "id": 18159,
        "spending": 530.15,
        "orders": 1,
        "quantity": 139,
        "order_value": 530.15,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 12432,
        "spending": 5059.32,
        "orders": 5,
        "quantity": 1801,
        "order_value": 1011.86,
        "unique_prods": 107,
        "cluster": 0
      },
      {
        "id": 16103,
        "spending": 1429.64,
        "orders": 6,
        "quantity": 558,
        "order_value": 238.27,
        "unique_prods": 30,
        "cluster": 2
      },
      {
        "id": 14356,
        "spending": 701.23,
        "orders": 2,
        "quantity": 277,
        "order_value": 350.62,
        "unique_prods": 33,
        "cluster": 2
      },
      {
        "id": 16715,
        "spending": 301.72,
        "orders": 1,
        "quantity": 642,
        "order_value": 301.72,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 17999,
        "spending": 382.06,
        "orders": 2,
        "quantity": 221,
        "order_value": 191.03,
        "unique_prods": 87,
        "cluster": 2
      },
      {
        "id": 17080,
        "spending": 287.62,
        "orders": 2,
        "quantity": 166,
        "order_value": 143.81,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 14002,
        "spending": 529.73,
        "orders": 2,
        "quantity": 877,
        "order_value": 264.86,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 12725,
        "spending": 427.8,
        "orders": 1,
        "quantity": 164,
        "order_value": 427.8,
        "unique_prods": 24,
        "cluster": 2
      },
      {
        "id": 12532,
        "spending": 349.83,
        "orders": 1,
        "quantity": 153,
        "order_value": 349.83,
        "unique_prods": 16,
        "cluster": 2
      },
      {
        "id": 16333,
        "spending": 26626.8,
        "orders": 22,
        "quantity": 32184,
        "order_value": 1210.31,
        "unique_prods": 9,
        "cluster": 0
      },
      {
        "id": 15917,
        "spending": 123.1,
        "orders": 1,
        "quantity": 42,
        "order_value": 123.1,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 15942,
        "spending": 337.44,
        "orders": 1,
        "quantity": 232,
        "order_value": 337.44,
        "unique_prods": 14,
        "cluster": 2
      },
      {
        "id": 16768,
        "spending": 478.09,
        "orders": 3,
        "quantity": 196,
        "order_value": 159.36,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 15117,
        "spending": 1551.78,
        "orders": 5,
        "quantity": 1948,
        "order_value": 310.36,
        "unique_prods": 63,
        "cluster": 0
      },
      {
        "id": 13532,
        "spending": 210.31,
        "orders": 1,
        "quantity": 129,
        "order_value": 210.31,
        "unique_prods": 66,
        "cluster": 2
      },
      {
        "id": 15797,
        "spending": 2207.4,
        "orders": 4,
        "quantity": 873,
        "order_value": 551.85,
        "unique_prods": 8,
        "cluster": 2
      },
      {
        "id": 15353,
        "spending": 777.02,
        "orders": 2,
        "quantity": 343,
        "order_value": 388.51,
        "unique_prods": 59,
        "cluster": 2
      },
      {
        "id": 13321,
        "spending": 567.36,
        "orders": 2,
        "quantity": 372,
        "order_value": 283.68,
        "unique_prods": 10,
        "cluster": 2
      },
      {
        "id": 12919,
        "spending": 1335.19,
        "orders": 6,
        "quantity": 673,
        "order_value": 222.53,
        "unique_prods": 34,
        "cluster": 2
      },
      {
        "id": 12875,
        "spending": 343.23,
        "orders": 2,
        "quantity": 2019,
        "order_value": 171.62,
        "unique_prods": 1,
        "cluster": 1
      },
      {
        "id": 17658,
        "spending": 595.42,
        "orders": 2,
        "quantity": 616,
        "order_value": 297.71,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 15005,
        "spending": 6316.57,
        "orders": 28,
        "quantity": 4247,
        "order_value": 225.59,
        "unique_prods": 360,
        "cluster": 0
      },
      {
        "id": 17849,
        "spending": 605.8,
        "orders": 4,
        "quantity": 114,
        "order_value": 151.45,
        "unique_prods": 14,
        "cluster": 1
      },
      {
        "id": 17768,
        "spending": 2273.18,
        "orders": 3,
        "quantity": 1186,
        "order_value": 757.73,
        "unique_prods": 77,
        "cluster": 0
      },
      {
        "id": 12712,
        "spending": 4396.13,
        "orders": 13,
        "quantity": 1062,
        "order_value": 338.16,
        "unique_prods": 58,
        "cluster": 0
      },
      {
        "id": 14856,
        "spending": 1311.38,
        "orders": 3,
        "quantity": 714,
        "order_value": 437.13,
        "unique_prods": 65,
        "cluster": 2
      },
      {
        "id": 14601,
        "spending": 213.96,
        "orders": 1,
        "quantity": 168,
        "order_value": 213.96,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 17863,
        "spending": 3160.0,
        "orders": 6,
        "quantity": 2638,
        "order_value": 526.67,
        "unique_prods": 110,
        "cluster": 0
      },
      {
        "id": 12890,
        "spending": 380.47,
        "orders": 1,
        "quantity": 259,
        "order_value": 380.47,
        "unique_prods": 78,
        "cluster": 2
      },
      {
        "id": 16698,
        "spending": 1998.0,
        "orders": 2,
        "quantity": 840,
        "order_value": 999.0,
        "unique_prods": 4,
        "cluster": 2
      },
      {
        "id": 15330,
        "spending": 714.96,
        "orders": 2,
        "quantity": 1312,
        "order_value": 357.48,
        "unique_prods": 10,
        "cluster": 2
      },
      {
        "id": 15147,
        "spending": 623.5,
        "orders": 1,
        "quantity": 366,
        "order_value": 623.5,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 17656,
        "spending": 1674.69,
        "orders": 5,
        "quantity": 1399,
        "order_value": 334.94,
        "unique_prods": 67,
        "cluster": 0
      },
      {
        "id": 14083,
        "spending": 1018.43,
        "orders": 9,
        "quantity": 732,
        "order_value": 113.16,
        "unique_prods": 162,
        "cluster": 0
      },
      {
        "id": 12544,
        "spending": 372.7,
        "orders": 1,
        "quantity": 136,
        "order_value": 372.7,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 13563,
        "spending": 777.53,
        "orders": 2,
        "quantity": 209,
        "order_value": 388.76,
        "unique_prods": 49,
        "cluster": 2
      },
      {
        "id": 13727,
        "spending": 333.48,
        "orders": 2,
        "quantity": 162,
        "order_value": 166.74,
        "unique_prods": 19,
        "cluster": 1
      },
      {
        "id": 15405,
        "spending": 349.1,
        "orders": 1,
        "quantity": 193,
        "order_value": 349.1,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 17585,
        "spending": 1133.07,
        "orders": 4,
        "quantity": 1671,
        "order_value": 283.27,
        "unique_prods": 176,
        "cluster": 0
      },
      {
        "id": 13859,
        "spending": 201.16,
        "orders": 1,
        "quantity": 129,
        "order_value": 201.16,
        "unique_prods": 27,
        "cluster": 1
      },
      {
        "id": 15584,
        "spending": 725.11,
        "orders": 4,
        "quantity": 314,
        "order_value": 181.28,
        "unique_prods": 89,
        "cluster": 2
      },
      {
        "id": 18055,
        "spending": 6784.19,
        "orders": 10,
        "quantity": 2455,
        "order_value": 678.42,
        "unique_prods": 223,
        "cluster": 0
      },
      {
        "id": 14257,
        "spending": 3099.72,
        "orders": 5,
        "quantity": 1682,
        "order_value": 619.94,
        "unique_prods": 88,
        "cluster": 0
      },
      {
        "id": 13354,
        "spending": 743.53,
        "orders": 1,
        "quantity": 604,
        "order_value": 743.53,
        "unique_prods": 51,
        "cluster": 2
      },
      {
        "id": 18095,
        "spending": 580.05,
        "orders": 2,
        "quantity": 419,
        "order_value": 290.02,
        "unique_prods": 20,
        "cluster": 2
      },
      {
        "id": 17345,
        "spending": 537.74,
        "orders": 4,
        "quantity": 346,
        "order_value": 134.44,
        "unique_prods": 70,
        "cluster": 2
      },
      {
        "id": 13014,
        "spending": 3466.28,
        "orders": 10,
        "quantity": 905,
        "order_value": 346.63,
        "unique_prods": 67,
        "cluster": 0
      },
      {
        "id": 14216,
        "spending": 1839.3,
        "orders": 4,
        "quantity": 594,
        "order_value": 459.83,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 13774,
        "spending": 345.0,
        "orders": 1,
        "quantity": 192,
        "order_value": 345.0,
        "unique_prods": 22,
        "cluster": 2
      },
      {
        "id": 12937,
        "spending": 1504.27,
        "orders": 4,
        "quantity": 1007,
        "order_value": 376.07,
        "unique_prods": 81,
        "cluster": 0
      },
      {
        "id": 14174,
        "spending": 134.46,
        "orders": 1,
        "quantity": 94,
        "order_value": 134.46,
        "unique_prods": 26,
        "cluster": 1
      },
      {
        "id": 12701,
        "spending": 797.71,
        "orders": 2,
        "quantity": 678,
        "order_value": 398.86,
        "unique_prods": 50,
        "cluster": 2
      },
      {
        "id": 13517,
        "spending": 2128.42,
        "orders": 3,
        "quantity": 1369,
        "order_value": 709.47,
        "unique_prods": 125,
        "cluster": 0
      },
      {
        "id": 14577,
        "spending": 859.71,
        "orders": 4,
        "quantity": 353,
        "order_value": 214.93,
        "unique_prods": 86,
        "cluster": 2
      },
      {
        "id": 13140,
        "spending": 423.72,
        "orders": 3,
        "quantity": 186,
        "order_value": 141.24,
        "unique_prods": 40,
        "cluster": 2
      },
      {
        "id": 14404,
        "spending": 1474.32,
        "orders": 6,
        "quantity": 839,
        "order_value": 245.72,
        "unique_prods": 70,
        "cluster": 0
      },
      {
        "id": 12902,
        "spending": 138.68,
        "orders": 1,
        "quantity": 66,
        "order_value": 138.68,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 14323,
        "spending": 605.06,
        "orders": 2,
        "quantity": 350,
        "order_value": 302.53,
        "unique_prods": 32,
        "cluster": 2
      },
      {
        "id": 14859,
        "spending": 1353.74,
        "orders": 4,
        "quantity": 671,
        "order_value": 338.44,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 12463,
        "spending": 1344.78,
        "orders": 4,
        "quantity": 776,
        "order_value": 336.2,
        "unique_prods": 65,
        "cluster": 2
      },
      {
        "id": 16215,
        "spending": 242.35,
        "orders": 1,
        "quantity": 104,
        "order_value": 242.35,
        "unique_prods": 14,
        "cluster": 1
      },
      {
        "id": 16157,
        "spending": 656.69,
        "orders": 3,
        "quantity": 347,
        "order_value": 218.9,
        "unique_prods": 12,
        "cluster": 2
      },
      {
        "id": 15712,
        "spending": 1072.36,
        "orders": 5,
        "quantity": 486,
        "order_value": 214.47,
        "unique_prods": 41,
        "cluster": 2
      },
      {
        "id": 13265,
        "spending": 2107.66,
        "orders": 5,
        "quantity": 1752,
        "order_value": 421.53,
        "unique_prods": 66,
        "cluster": 0
      },
      {
        "id": 13136,
        "spending": 2607.61,
        "orders": 5,
        "quantity": 1328,
        "order_value": 521.52,
        "unique_prods": 94,
        "cluster": 0
      },
      {
        "id": 16092,
        "spending": 817.86,
        "orders": 3,
        "quantity": 628,
        "order_value": 272.62,
        "unique_prods": 37,
        "cluster": 2
      },
      {
        "id": 15707,
        "spending": 945.58,
        "orders": 4,
        "quantity": 605,
        "order_value": 236.39,
        "unique_prods": 126,
        "cluster": 2
      },
      {
        "id": 16470,
        "spending": 762.39,
        "orders": 4,
        "quantity": 531,
        "order_value": 190.6,
        "unique_prods": 120,
        "cluster": 2
      },
      {
        "id": 13062,
        "spending": 346.98,
        "orders": 1,
        "quantity": 343,
        "order_value": 346.98,
        "unique_prods": 11,
        "cluster": 2
      },
      {
        "id": 12535,
        "spending": 716.35,
        "orders": 2,
        "quantity": 219,
        "order_value": 358.18,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 13531,
        "spending": 483.8,
        "orders": 2,
        "quantity": 174,
        "order_value": 241.9,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 16332,
        "spending": 1593.2,
        "orders": 7,
        "quantity": 801,
        "order_value": 227.6,
        "unique_prods": 125,
        "cluster": 0
      },
      {
        "id": 17940,
        "spending": 4106.44,
        "orders": 10,
        "quantity": 9755,
        "order_value": 410.64,
        "unique_prods": 6,
        "cluster": 0
      },
      {
        "id": 14415,
        "spending": 5900.28,
        "orders": 13,
        "quantity": 3011,
        "order_value": 453.87,
        "unique_prods": 283,
        "cluster": 0
      },
      {
        "id": 13743,
        "spending": 1341.6,
        "orders": 7,
        "quantity": 1776,
        "order_value": 191.66,
        "unique_prods": 8,
        "cluster": 2
      },
      {
        "id": 17827,
        "spending": 1995.46,
        "orders": 5,
        "quantity": 1247,
        "order_value": 399.09,
        "unique_prods": 190,
        "cluster": 0
      },
      {
        "id": 17254,
        "spending": 272.44,
        "orders": 2,
        "quantity": 252,
        "order_value": 136.22,
        "unique_prods": 100,
        "cluster": 2
      },
      {
        "id": 18212,
        "spending": 248.42,
        "orders": 1,
        "quantity": 101,
        "order_value": 248.42,
        "unique_prods": 30,
        "cluster": 1
      },
      {
        "id": 16618,
        "spending": 2647.59,
        "orders": 5,
        "quantity": 1363,
        "order_value": 529.52,
        "unique_prods": 79,
        "cluster": 0
      },
      {
        "id": 17775,
        "spending": 56.4,
        "orders": 1,
        "quantity": 72,
        "order_value": 56.4,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 17566,
        "spending": 901.21,
        "orders": 2,
        "quantity": 518,
        "order_value": 450.6,
        "unique_prods": 113,
        "cluster": 2
      },
      {
        "id": 16743,
        "spending": 2238.09,
        "orders": 7,
        "quantity": 2047,
        "order_value": 319.73,
        "unique_prods": 89,
        "cluster": 0
      },
      {
        "id": 17674,
        "spending": 551.04,
        "orders": 2,
        "quantity": 672,
        "order_value": 275.52,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 15301,
        "spending": 5070.35,
        "orders": 12,
        "quantity": 2775,
        "order_value": 422.53,
        "unique_prods": 167,
        "cluster": 0
      },
      {
        "id": 15885,
        "spending": 379.35,
        "orders": 3,
        "quantity": 111,
        "order_value": 126.45,
        "unique_prods": 18,
        "cluster": 1
      },
      {
        "id": 15571,
        "spending": 650.43,
        "orders": 4,
        "quantity": 264,
        "order_value": 162.61,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 17180,
        "spending": 796.03,
        "orders": 4,
        "quantity": 683,
        "order_value": 199.01,
        "unique_prods": 91,
        "cluster": 2
      },
      {
        "id": 18255,
        "spending": 103.3,
        "orders": 1,
        "quantity": 74,
        "order_value": 103.3,
        "unique_prods": 6,
        "cluster": 1
      },
      {
        "id": 12724,
        "spending": 1031.41,
        "orders": 4,
        "quantity": 445,
        "order_value": 257.85,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 18242,
        "spending": 2232.49,
        "orders": 4,
        "quantity": 1017,
        "order_value": 558.12,
        "unique_prods": 72,
        "cluster": 0
      },
      {
        "id": 17495,
        "spending": 497.56,
        "orders": 2,
        "quantity": 229,
        "order_value": 248.78,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 13005,
        "spending": 513.7,
        "orders": 2,
        "quantity": 172,
        "order_value": 256.85,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 17364,
        "spending": 4481.18,
        "orders": 11,
        "quantity": 2701,
        "order_value": 407.38,
        "unique_prods": 288,
        "cluster": 0
      },
      {
        "id": 15820,
        "spending": 206.98,
        "orders": 1,
        "quantity": 128,
        "order_value": 206.98,
        "unique_prods": 17,
        "cluster": 1
      },
      {
        "id": 15807,
        "spending": 903.9,
        "orders": 3,
        "quantity": 430,
        "order_value": 301.3,
        "unique_prods": 48,
        "cluster": 2
      },
      {
        "id": 16532,
        "spending": 6748.8,
        "orders": 3,
        "quantity": 2016,
        "order_value": 2249.6,
        "unique_prods": 2,
        "cluster": 2
      },
      {
        "id": 12497,
        "spending": 1043.1,
        "orders": 1,
        "quantity": 1236,
        "order_value": 1043.1,
        "unique_prods": 14,
        "cluster": 2
      },
      {
        "id": 13764,
        "spending": 1521.76,
        "orders": 3,
        "quantity": 932,
        "order_value": 507.25,
        "unique_prods": 183,
        "cluster": 0
      },
      {
        "id": 14693,
        "spending": 172.9,
        "orders": 1,
        "quantity": 34,
        "order_value": 172.9,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 15695,
        "spending": 409.98,
        "orders": 2,
        "quantity": 212,
        "order_value": 204.99,
        "unique_prods": 22,
        "cluster": 2
      },
      {
        "id": 14480,
        "spending": 279.05,
        "orders": 1,
        "quantity": 143,
        "order_value": 279.05,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 15814,
        "spending": 1945.33,
        "orders": 4,
        "quantity": 1271,
        "order_value": 486.33,
        "unique_prods": 63,
        "cluster": 0
      },
      {
        "id": 17767,
        "spending": 271.2,
        "orders": 1,
        "quantity": 128,
        "order_value": 271.2,
        "unique_prods": 21,
        "cluster": 1
      },
      {
        "id": 14423,
        "spending": 265.2,
        "orders": 1,
        "quantity": 120,
        "order_value": 265.2,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 14248,
        "spending": 302.58,
        "orders": 1,
        "quantity": 102,
        "order_value": 302.58,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 18045,
        "spending": 189.4,
        "orders": 1,
        "quantity": 142,
        "order_value": 189.4,
        "unique_prods": 43,
        "cluster": 1
      },
      {
        "id": 16727,
        "spending": 272.82,
        "orders": 1,
        "quantity": 177,
        "order_value": 272.82,
        "unique_prods": 41,
        "cluster": 2
      },
      {
        "id": 16997,
        "spending": 702.0,
        "orders": 3,
        "quantity": 360,
        "order_value": 234.0,
        "unique_prods": 7,
        "cluster": 2
      },
      {
        "id": 16902,
        "spending": 1706.88,
        "orders": 1,
        "quantity": 629,
        "order_value": 1706.88,
        "unique_prods": 43,
        "cluster": 2
      },
      {
        "id": 14286,
        "spending": 4628.75,
        "orders": 3,
        "quantity": 4338,
        "order_value": 1542.92,
        "unique_prods": 220,
        "cluster": 0
      },
      {
        "id": 13781,
        "spending": 127.84,
        "orders": 1,
        "quantity": 30,
        "order_value": 127.84,
        "unique_prods": 17,
        "cluster": 1
      },
      {
        "id": 12995,
        "spending": 211.32,
        "orders": 1,
        "quantity": 108,
        "order_value": 211.32,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 15374,
        "spending": 168.0,
        "orders": 1,
        "quantity": 126,
        "order_value": 168.0,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 13568,
        "spending": 192.85,
        "orders": 1,
        "quantity": 70,
        "order_value": 192.85,
        "unique_prods": 41,
        "cluster": 1
      },
      {
        "id": 15869,
        "spending": 149.64,
        "orders": 2,
        "quantity": 175,
        "order_value": 74.82,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 17698,
        "spending": 154.95,
        "orders": 1,
        "quantity": 93,
        "order_value": 154.95,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 13932,
        "spending": 307.4,
        "orders": 1,
        "quantity": 72,
        "order_value": 307.4,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 17972,
        "spending": 136.04,
        "orders": 1,
        "quantity": 37,
        "order_value": 136.04,
        "unique_prods": 30,
        "cluster": 1
      },
      {
        "id": 13194,
        "spending": 60.7,
        "orders": 1,
        "quantity": 26,
        "order_value": 60.7,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 17051,
        "spending": 247.14,
        "orders": 1,
        "quantity": 184,
        "order_value": 247.14,
        "unique_prods": 40,
        "cluster": 2
      },
      {
        "id": 16175,
        "spending": 1037.59,
        "orders": 4,
        "quantity": 533,
        "order_value": 259.4,
        "unique_prods": 45,
        "cluster": 2
      },
      {
        "id": 14867,
        "spending": 710.28,
        "orders": 3,
        "quantity": 328,
        "order_value": 236.76,
        "unique_prods": 31,
        "cluster": 2
      },
      {
        "id": 13305,
        "spending": 2000.86,
        "orders": 10,
        "quantity": 1232,
        "order_value": 200.09,
        "unique_prods": 50,
        "cluster": 0
      },
      {
        "id": 14451,
        "spending": 662.59,
        "orders": 2,
        "quantity": 389,
        "order_value": 331.3,
        "unique_prods": 86,
        "cluster": 2
      },
      {
        "id": 13730,
        "spending": 752.6,
        "orders": 2,
        "quantity": 488,
        "order_value": 376.3,
        "unique_prods": 38,
        "cluster": 2
      },
      {
        "id": 15861,
        "spending": 3165.36,
        "orders": 8,
        "quantity": 2544,
        "order_value": 395.67,
        "unique_prods": 339,
        "cluster": 0
      },
      {
        "id": 17609,
        "spending": 1112.22,
        "orders": 5,
        "quantity": 723,
        "order_value": 222.44,
        "unique_prods": 199,
        "cluster": 0
      },
      {
        "id": 18013,
        "spending": 187.29,
        "orders": 2,
        "quantity": 285,
        "order_value": 93.64,
        "unique_prods": 31,
        "cluster": 1
      },
      {
        "id": 16597,
        "spending": 90.04,
        "orders": 1,
        "quantity": 184,
        "order_value": 90.04,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 14505,
        "spending": 5905.64,
        "orders": 8,
        "quantity": 2759,
        "order_value": 738.21,
        "unique_prods": 540,
        "cluster": 0
      },
      {
        "id": 15537,
        "spending": 110.92,
        "orders": 1,
        "quantity": 29,
        "order_value": 110.92,
        "unique_prods": 24,
        "cluster": 1
      },
      {
        "id": 12410,
        "spending": 693.33,
        "orders": 2,
        "quantity": 211,
        "order_value": 346.66,
        "unique_prods": 26,
        "cluster": 2
      },
      {
        "id": 17926,
        "spending": 397.29,
        "orders": 2,
        "quantity": 306,
        "order_value": 198.65,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 12951,
        "spending": 1064.07,
        "orders": 6,
        "quantity": 503,
        "order_value": 177.34,
        "unique_prods": 53,
        "cluster": 2
      },
      {
        "id": 15311,
        "spending": 60767.9,
        "orders": 91,
        "quantity": 38194,
        "order_value": 667.78,
        "unique_prods": 567,
        "cluster": 0
      },
      {
        "id": 18006,
        "spending": 444.68,
        "orders": 1,
        "quantity": 220,
        "order_value": 444.68,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 13755,
        "spending": 2161.35,
        "orders": 9,
        "quantity": 1264,
        "order_value": 240.15,
        "unique_prods": 232,
        "cluster": 0
      },
      {
        "id": 15916,
        "spending": 1528.09,
        "orders": 8,
        "quantity": 757,
        "order_value": 191.01,
        "unique_prods": 124,
        "cluster": 0
      },
      {
        "id": 16372,
        "spending": 367.93,
        "orders": 2,
        "quantity": 166,
        "order_value": 183.96,
        "unique_prods": 86,
        "cluster": 2
      },
      {
        "id": 14598,
        "spending": 221.97,
        "orders": 1,
        "quantity": 189,
        "order_value": 221.97,
        "unique_prods": 49,
        "cluster": 2
      },
      {
        "id": 16624,
        "spending": 810.57,
        "orders": 2,
        "quantity": 488,
        "order_value": 405.28,
        "unique_prods": 44,
        "cluster": 2
      },
      {
        "id": 14581,
        "spending": 138.6,
        "orders": 1,
        "quantity": 217,
        "order_value": 138.6,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 13134,
        "spending": 1793.58,
        "orders": 4,
        "quantity": 1059,
        "order_value": 448.4,
        "unique_prods": 94,
        "cluster": 0
      },
      {
        "id": 14298,
        "spending": 51527.3,
        "orders": 44,
        "quantity": 58343,
        "order_value": 1171.07,
        "unique_prods": 884,
        "cluster": 0
      },
      {
        "id": 12534,
        "spending": 1089.18,
        "orders": 1,
        "quantity": 651,
        "order_value": 1089.18,
        "unique_prods": 63,
        "cluster": 2
      },
      {
        "id": 15106,
        "spending": 1422.52,
        "orders": 5,
        "quantity": 1181,
        "order_value": 284.5,
        "unique_prods": 90,
        "cluster": 0
      },
      {
        "id": 15364,
        "spending": 913.19,
        "orders": 2,
        "quantity": 493,
        "order_value": 456.6,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 13939,
        "spending": 568.55,
        "orders": 3,
        "quantity": 847,
        "order_value": 189.52,
        "unique_prods": 43,
        "cluster": 2
      },
      {
        "id": 12556,
        "spending": 603.71,
        "orders": 2,
        "quantity": 358,
        "order_value": 301.85,
        "unique_prods": 100,
        "cluster": 2
      },
      {
        "id": 18109,
        "spending": 8052.97,
        "orders": 26,
        "quantity": 4237,
        "order_value": 309.73,
        "unique_prods": 119,
        "cluster": 0
      },
      {
        "id": 16816,
        "spending": 417.06,
        "orders": 4,
        "quantity": 274,
        "order_value": 104.27,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 17806,
        "spending": 546.04,
        "orders": 1,
        "quantity": 727,
        "order_value": 546.04,
        "unique_prods": 43,
        "cluster": 2
      },
      {
        "id": 14719,
        "spending": 1602.13,
        "orders": 5,
        "quantity": 1032,
        "order_value": 320.43,
        "unique_prods": 177,
        "cluster": 0
      },
      {
        "id": 16748,
        "spending": 1515.9,
        "orders": 5,
        "quantity": 880,
        "order_value": 303.18,
        "unique_prods": 42,
        "cluster": 2
      },
      {
        "id": 18074,
        "spending": 489.6,
        "orders": 1,
        "quantity": 190,
        "order_value": 489.6,
        "unique_prods": 13,
        "cluster": 2
      },
      {
        "id": 15644,
        "spending": 813.0,
        "orders": 4,
        "quantity": 557,
        "order_value": 203.25,
        "unique_prods": 166,
        "cluster": 2
      },
      {
        "id": 13501,
        "spending": 1340.32,
        "orders": 1,
        "quantity": 560,
        "order_value": 1340.32,
        "unique_prods": 52,
        "cluster": 2
      },
      {
        "id": 17841,
        "spending": 40991.57,
        "orders": 124,
        "quantity": 23071,
        "order_value": 330.58,
        "unique_prods": 1323,
        "cluster": 0
      },
      {
        "id": 16849,
        "spending": 124.57,
        "orders": 1,
        "quantity": 33,
        "order_value": 124.57,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 14768,
        "spending": 192.6,
        "orders": 2,
        "quantity": 52,
        "order_value": 96.3,
        "unique_prods": 4,
        "cluster": 1
      },
      {
        "id": 13232,
        "spending": 1357.6,
        "orders": 7,
        "quantity": 778,
        "order_value": 193.94,
        "unique_prods": 147,
        "cluster": 0
      },
      {
        "id": 13950,
        "spending": 745.06,
        "orders": 4,
        "quantity": 323,
        "order_value": 186.27,
        "unique_prods": 33,
        "cluster": 2
      },
      {
        "id": 17582,
        "spending": 175.27,
        "orders": 1,
        "quantity": 123,
        "order_value": 175.27,
        "unique_prods": 28,
        "cluster": 1
      },
      {
        "id": 14409,
        "spending": 2059.45,
        "orders": 6,
        "quantity": 1230,
        "order_value": 343.24,
        "unique_prods": 40,
        "cluster": 0
      },
      {
        "id": 13984,
        "spending": 920.51,
        "orders": 5,
        "quantity": 679,
        "order_value": 184.1,
        "unique_prods": 14,
        "cluster": 2
      },
      {
        "id": 12536,
        "spending": 12601.83,
        "orders": 3,
        "quantity": 2803,
        "order_value": 4200.61,
        "unique_prods": 260,
        "cluster": 0
      },
      {
        "id": 15206,
        "spending": 420.3,
        "orders": 4,
        "quantity": 162,
        "order_value": 105.08,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 12572,
        "spending": 1020.42,
        "orders": 2,
        "quantity": 452,
        "order_value": 510.21,
        "unique_prods": 53,
        "cluster": 2
      },
      {
        "id": 17718,
        "spending": 139.35,
        "orders": 1,
        "quantity": 83,
        "order_value": 139.35,
        "unique_prods": 6,
        "cluster": 1
      },
      {
        "id": 14514,
        "spending": 1055.35,
        "orders": 3,
        "quantity": 589,
        "order_value": 351.78,
        "unique_prods": 65,
        "cluster": 2
      },
      {
        "id": 16718,
        "spending": 623.75,
        "orders": 1,
        "quantity": 413,
        "order_value": 623.75,
        "unique_prods": 41,
        "cluster": 2
      },
      {
        "id": 14034,
        "spending": 651.82,
        "orders": 3,
        "quantity": 423,
        "order_value": 217.27,
        "unique_prods": 82,
        "cluster": 2
      },
      {
        "id": 14023,
        "spending": 584.07,
        "orders": 2,
        "quantity": 345,
        "order_value": 292.03,
        "unique_prods": 30,
        "cluster": 2
      },
      {
        "id": 17454,
        "spending": 517.53,
        "orders": 4,
        "quantity": 243,
        "order_value": 129.38,
        "unique_prods": 57,
        "cluster": 2
      },
      {
        "id": 16208,
        "spending": 664.26,
        "orders": 2,
        "quantity": 333,
        "order_value": 332.13,
        "unique_prods": 61,
        "cluster": 2
      },
      {
        "id": 12942,
        "spending": 683.9,
        "orders": 3,
        "quantity": 203,
        "order_value": 227.97,
        "unique_prods": 68,
        "cluster": 2
      },
      {
        "id": 12355,
        "spending": 459.4,
        "orders": 1,
        "quantity": 240,
        "order_value": 459.4,
        "unique_prods": 13,
        "cluster": 2
      },
      {
        "id": 15938,
        "spending": 404.58,
        "orders": 5,
        "quantity": 240,
        "order_value": 80.92,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 13166,
        "spending": 417.2,
        "orders": 1,
        "quantity": 216,
        "order_value": 417.2,
        "unique_prods": 39,
        "cluster": 2
      },
      {
        "id": 13117,
        "spending": 984.91,
        "orders": 8,
        "quantity": 945,
        "order_value": 123.11,
        "unique_prods": 66,
        "cluster": 0
      },
      {
        "id": 14242,
        "spending": 280.55,
        "orders": 2,
        "quantity": 123,
        "order_value": 140.28,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 16536,
        "spending": 548.97,
        "orders": 1,
        "quantity": 251,
        "order_value": 548.97,
        "unique_prods": 49,
        "cluster": 2
      },
      {
        "id": 17165,
        "spending": 158.68,
        "orders": 1,
        "quantity": 100,
        "order_value": 158.68,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 12812,
        "spending": 229.64,
        "orders": 1,
        "quantity": 164,
        "order_value": 229.64,
        "unique_prods": 15,
        "cluster": 1
      },
      {
        "id": 16424,
        "spending": 133.56,
        "orders": 1,
        "quantity": 88,
        "order_value": 133.56,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 17651,
        "spending": 3945.0,
        "orders": 10,
        "quantity": 3112,
        "order_value": 394.5,
        "unique_prods": 149,
        "cluster": 0
      },
      {
        "id": 16085,
        "spending": 981.51,
        "orders": 5,
        "quantity": 636,
        "order_value": 196.3,
        "unique_prods": 123,
        "cluster": 2
      },
      {
        "id": 16139,
        "spending": 635.41,
        "orders": 3,
        "quantity": 330,
        "order_value": 211.8,
        "unique_prods": 25,
        "cluster": 2
      },
      {
        "id": 15175,
        "spending": 224.14,
        "orders": 1,
        "quantity": 454,
        "order_value": 224.14,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 14641,
        "spending": 110.46,
        "orders": 1,
        "quantity": 90,
        "order_value": 110.46,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 17601,
        "spending": 116.01,
        "orders": 1,
        "quantity": 103,
        "order_value": 116.01,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 12578,
        "spending": 2794.51,
        "orders": 2,
        "quantity": 1196,
        "order_value": 1397.25,
        "unique_prods": 111,
        "cluster": 0
      },
      {
        "id": 17571,
        "spending": 1498.51,
        "orders": 4,
        "quantity": 905,
        "order_value": 374.63,
        "unique_prods": 247,
        "cluster": 0
      },
      {
        "id": 17423,
        "spending": 698.41,
        "orders": 2,
        "quantity": 459,
        "order_value": 349.2,
        "unique_prods": 26,
        "cluster": 2
      },
      {
        "id": 13917,
        "spending": 272.04,
        "orders": 2,
        "quantity": 228,
        "order_value": 136.02,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 14125,
        "spending": 2740.43,
        "orders": 3,
        "quantity": 1640,
        "order_value": 913.48,
        "unique_prods": 159,
        "cluster": 0
      },
      {
        "id": 18287,
        "spending": 1837.28,
        "orders": 3,
        "quantity": 1586,
        "order_value": 612.43,
        "unique_prods": 59,
        "cluster": 0
      },
      {
        "id": 14461,
        "spending": 2103.06,
        "orders": 3,
        "quantity": 766,
        "order_value": 701.02,
        "unique_prods": 173,
        "cluster": 0
      },
      {
        "id": 12640,
        "spending": 1174.58,
        "orders": 3,
        "quantity": 311,
        "order_value": 391.53,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 18248,
        "spending": 804.02,
        "orders": 2,
        "quantity": 511,
        "order_value": 402.01,
        "unique_prods": 39,
        "cluster": 2
      },
      {
        "id": 17843,
        "spending": 205.48,
        "orders": 1,
        "quantity": 113,
        "order_value": 205.48,
        "unique_prods": 36,
        "cluster": 1
      },
      {
        "id": 17242,
        "spending": 1135.04,
        "orders": 2,
        "quantity": 611,
        "order_value": 567.52,
        "unique_prods": 30,
        "cluster": 2
      },
      {
        "id": 12609,
        "spending": 1126.85,
        "orders": 3,
        "quantity": 648,
        "order_value": 375.62,
        "unique_prods": 57,
        "cluster": 2
      },
      {
        "id": 12449,
        "spending": 4067.29,
        "orders": 4,
        "quantity": 1553,
        "order_value": 1016.82,
        "unique_prods": 118,
        "cluster": 0
      },
      {
        "id": 13085,
        "spending": 416.08,
        "orders": 2,
        "quantity": 216,
        "order_value": 208.04,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 18263,
        "spending": 1213.16,
        "orders": 3,
        "quantity": 1468,
        "order_value": 404.39,
        "unique_prods": 59,
        "cluster": 2
      },
      {
        "id": 14291,
        "spending": 3883.25,
        "orders": 11,
        "quantity": 2749,
        "order_value": 353.02,
        "unique_prods": 145,
        "cluster": 0
      },
      {
        "id": 12991,
        "spending": 503.76,
        "orders": 2,
        "quantity": 405,
        "order_value": 251.88,
        "unique_prods": 31,
        "cluster": 2
      },
      {
        "id": 14141,
        "spending": 915.13,
        "orders": 4,
        "quantity": 355,
        "order_value": 228.78,
        "unique_prods": 27,
        "cluster": 2
      },
      {
        "id": 17105,
        "spending": 665.78,
        "orders": 2,
        "quantity": 693,
        "order_value": 332.89,
        "unique_prods": 80,
        "cluster": 2
      },
      {
        "id": 17866,
        "spending": 329.65,
        "orders": 1,
        "quantity": 174,
        "order_value": 329.65,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 14463,
        "spending": 529.62,
        "orders": 3,
        "quantity": 179,
        "order_value": 176.54,
        "unique_prods": 6,
        "cluster": 1
      },
      {
        "id": 16619,
        "spending": 226.21,
        "orders": 1,
        "quantity": 133,
        "order_value": 226.21,
        "unique_prods": 14,
        "cluster": 1
      },
      {
        "id": 14243,
        "spending": 2588.77,
        "orders": 10,
        "quantity": 1221,
        "order_value": 258.88,
        "unique_prods": 99,
        "cluster": 0
      },
      {
        "id": 12732,
        "spending": 236.26,
        "orders": 1,
        "quantity": 111,
        "order_value": 236.26,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 14860,
        "spending": 170.32,
        "orders": 1,
        "quantity": 232,
        "order_value": 170.32,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 15883,
        "spending": 396.48,
        "orders": 2,
        "quantity": 223,
        "order_value": 198.24,
        "unique_prods": 42,
        "cluster": 2
      },
      {
        "id": 16185,
        "spending": 529.41,
        "orders": 2,
        "quantity": 260,
        "order_value": 264.71,
        "unique_prods": 31,
        "cluster": 2
      },
      {
        "id": 14524,
        "spending": 1867.68,
        "orders": 9,
        "quantity": 676,
        "order_value": 207.52,
        "unique_prods": 161,
        "cluster": 0
      },
      {
        "id": 17531,
        "spending": 296.7,
        "orders": 1,
        "quantity": 136,
        "order_value": 296.7,
        "unique_prods": 14,
        "cluster": 1
      },
      {
        "id": 12713,
        "spending": 848.55,
        "orders": 1,
        "quantity": 508,
        "order_value": 848.55,
        "unique_prods": 38,
        "cluster": 2
      },
      {
        "id": 12373,
        "spending": 364.6,
        "orders": 1,
        "quantity": 197,
        "order_value": 364.6,
        "unique_prods": 14,
        "cluster": 2
      },
      {
        "id": 13558,
        "spending": 605.06,
        "orders": 4,
        "quantity": 344,
        "order_value": 151.26,
        "unique_prods": 123,
        "cluster": 2
      },
      {
        "id": 12582,
        "spending": 511.36,
        "orders": 2,
        "quantity": 300,
        "order_value": 255.68,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 12735,
        "spending": 779.57,
        "orders": 2,
        "quantity": 368,
        "order_value": 389.79,
        "unique_prods": 38,
        "cluster": 2
      },
      {
        "id": 16134,
        "spending": 618.09,
        "orders": 2,
        "quantity": 371,
        "order_value": 309.05,
        "unique_prods": 34,
        "cluster": 2
      },
      {
        "id": 16342,
        "spending": 322.41,
        "orders": 4,
        "quantity": 157,
        "order_value": 80.6,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 13070,
        "spending": 228.8,
        "orders": 1,
        "quantity": 110,
        "order_value": 228.8,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 12679,
        "spending": 1113.02,
        "orders": 4,
        "quantity": 554,
        "order_value": 278.25,
        "unique_prods": 43,
        "cluster": 2
      },
      {
        "id": 15070,
        "spending": 106.2,
        "orders": 1,
        "quantity": 36,
        "order_value": 106.2,
        "unique_prods": 1,
        "cluster": 1
      },
      {
        "id": 17567,
        "spending": 4331.48,
        "orders": 8,
        "quantity": 2632,
        "order_value": 541.43,
        "unique_prods": 110,
        "cluster": 0
      },
      {
        "id": 17227,
        "spending": 939.32,
        "orders": 6,
        "quantity": 741,
        "order_value": 156.55,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 13473,
        "spending": 422.64,
        "orders": 2,
        "quantity": 266,
        "order_value": 211.32,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 13243,
        "spending": 600.07,
        "orders": 1,
        "quantity": 233,
        "order_value": 600.07,
        "unique_prods": 56,
        "cluster": 2
      },
      {
        "id": 13955,
        "spending": 322.96,
        "orders": 2,
        "quantity": 154,
        "order_value": 161.48,
        "unique_prods": 33,
        "cluster": 1
      },
      {
        "id": 13894,
        "spending": 564.62,
        "orders": 3,
        "quantity": 354,
        "order_value": 188.21,
        "unique_prods": 25,
        "cluster": 2
      },
      {
        "id": 17771,
        "spending": 245.81,
        "orders": 2,
        "quantity": 287,
        "order_value": 122.91,
        "unique_prods": 51,
        "cluster": 2
      },
      {
        "id": 17226,
        "spending": 393.49,
        "orders": 1,
        "quantity": 406,
        "order_value": 393.49,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 13282,
        "spending": 1132.14,
        "orders": 3,
        "quantity": 307,
        "order_value": 377.38,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 15465,
        "spending": 7354.62,
        "orders": 18,
        "quantity": 1257,
        "order_value": 408.59,
        "unique_prods": 43,
        "cluster": 0
      },
      {
        "id": 18004,
        "spending": 169.47,
        "orders": 1,
        "quantity": 78,
        "order_value": 169.47,
        "unique_prods": 32,
        "cluster": 1
      },
      {
        "id": 12513,
        "spending": 612.29,
        "orders": 1,
        "quantity": 462,
        "order_value": 612.29,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 18268,
        "spending": 25.5,
        "orders": 1,
        "quantity": 2,
        "order_value": 25.5,
        "unique_prods": 1,
        "cluster": 1
      },
      {
        "id": 13737,
        "spending": 339.6,
        "orders": 1,
        "quantity": 125,
        "order_value": 339.6,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 15758,
        "spending": 205.25,
        "orders": 1,
        "quantity": 47,
        "order_value": 205.25,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 13043,
        "spending": 516.42,
        "orders": 1,
        "quantity": 254,
        "order_value": 516.42,
        "unique_prods": 13,
        "cluster": 2
      },
      {
        "id": 14966,
        "spending": 191.32,
        "orders": 1,
        "quantity": 187,
        "order_value": 191.32,
        "unique_prods": 35,
        "cluster": 1
      },
      {
        "id": 14688,
        "spending": 5630.87,
        "orders": 21,
        "quantity": 3621,
        "order_value": 268.14,
        "unique_prods": 148,
        "cluster": 0
      },
      {
        "id": 16711,
        "spending": 1651.03,
        "orders": 5,
        "quantity": 833,
        "order_value": 330.21,
        "unique_prods": 18,
        "cluster": 2
      },
      {
        "id": 17228,
        "spending": 1906.09,
        "orders": 8,
        "quantity": 1532,
        "order_value": 238.26,
        "unique_prods": 140,
        "cluster": 0
      },
      {
        "id": 17245,
        "spending": 171.45,
        "orders": 1,
        "quantity": 75,
        "order_value": 171.45,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 16722,
        "spending": 4730.81,
        "orders": 13,
        "quantity": 5001,
        "order_value": 363.91,
        "unique_prods": 96,
        "cluster": 0
      },
      {
        "id": 15944,
        "spending": 325.1,
        "orders": 1,
        "quantity": 50,
        "order_value": 325.1,
        "unique_prods": 6,
        "cluster": 1
      },
      {
        "id": 17838,
        "spending": 2779.3,
        "orders": 5,
        "quantity": 1879,
        "order_value": 555.86,
        "unique_prods": 96,
        "cluster": 0
      },
      {
        "id": 15322,
        "spending": 679.68,
        "orders": 1,
        "quantity": 416,
        "order_value": 679.68,
        "unique_prods": 42,
        "cluster": 2
      },
      {
        "id": 12590,
        "spending": 9864.26,
        "orders": 2,
        "quantity": 4283,
        "order_value": 4932.13,
        "unique_prods": 68,
        "cluster": 0
      },
      {
        "id": 15673,
        "spending": 2881.02,
        "orders": 4,
        "quantity": 1514,
        "order_value": 720.25,
        "unique_prods": 107,
        "cluster": 0
      },
      {
        "id": 12618,
        "spending": 177.31,
        "orders": 1,
        "quantity": 96,
        "order_value": 177.31,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 15193,
        "spending": 499.32,
        "orders": 1,
        "quantity": 144,
        "order_value": 499.32,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 15706,
        "spending": 1060.56,
        "orders": 4,
        "quantity": 321,
        "order_value": 265.14,
        "unique_prods": 50,
        "cluster": 2
      },
      {
        "id": 12586,
        "spending": 196.94,
        "orders": 1,
        "quantity": 79,
        "order_value": 196.94,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 14051,
        "spending": 15610.39,
        "orders": 23,
        "quantity": 3756,
        "order_value": 678.71,
        "unique_prods": 52,
        "cluster": 0
      },
      {
        "id": 15277,
        "spending": 255.9,
        "orders": 1,
        "quantity": 205,
        "order_value": 255.9,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 15133,
        "spending": 982.42,
        "orders": 3,
        "quantity": 680,
        "order_value": 327.47,
        "unique_prods": 27,
        "cluster": 2
      },
      {
        "id": 12731,
        "spending": 18895.91,
        "orders": 12,
        "quantity": 8437,
        "order_value": 1574.66,
        "unique_prods": 109,
        "cluster": 0
      },
      {
        "id": 16837,
        "spending": 3170.98,
        "orders": 11,
        "quantity": 1563,
        "order_value": 288.27,
        "unique_prods": 123,
        "cluster": 0
      },
      {
        "id": 16659,
        "spending": 39.12,
        "orders": 1,
        "quantity": 72,
        "order_value": 39.12,
        "unique_prods": 2,
        "cluster": 1
      },
      {
        "id": 15743,
        "spending": 784.46,
        "orders": 4,
        "quantity": 216,
        "order_value": 196.12,
        "unique_prods": 59,
        "cluster": 2
      },
      {
        "id": 16324,
        "spending": 428.68,
        "orders": 3,
        "quantity": 282,
        "order_value": 142.89,
        "unique_prods": 100,
        "cluster": 2
      },
      {
        "id": 13389,
        "spending": 797.96,
        "orders": 3,
        "quantity": 429,
        "order_value": 265.99,
        "unique_prods": 50,
        "cluster": 2
      },
      {
        "id": 17398,
        "spending": 653.38,
        "orders": 3,
        "quantity": 310,
        "order_value": 217.79,
        "unique_prods": 30,
        "cluster": 2
      },
      {
        "id": 15339,
        "spending": 574.07,
        "orders": 2,
        "quantity": 416,
        "order_value": 287.03,
        "unique_prods": 77,
        "cluster": 2
      },
      {
        "id": 18202,
        "spending": 1396.99,
        "orders": 3,
        "quantity": 581,
        "order_value": 465.66,
        "unique_prods": 55,
        "cluster": 2
      },
      {
        "id": 13359,
        "spending": 439.56,
        "orders": 1,
        "quantity": 161,
        "order_value": 439.56,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 17948,
        "spending": 358.56,
        "orders": 1,
        "quantity": 144,
        "order_value": 358.56,
        "unique_prods": 1,
        "cluster": 1
      },
      {
        "id": 18170,
        "spending": 980.31,
        "orders": 3,
        "quantity": 409,
        "order_value": 326.77,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 13477,
        "spending": 1454.58,
        "orders": 6,
        "quantity": 1021,
        "order_value": 242.43,
        "unique_prods": 57,
        "cluster": 0
      },
      {
        "id": 17309,
        "spending": 82.75,
        "orders": 1,
        "quantity": 41,
        "order_value": 82.75,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 12912,
        "spending": 1662.3,
        "orders": 5,
        "quantity": 670,
        "order_value": 332.46,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 13124,
        "spending": 3866.33,
        "orders": 3,
        "quantity": 2147,
        "order_value": 1288.78,
        "unique_prods": 185,
        "cluster": 0
      },
      {
        "id": 12600,
        "spending": 2599.04,
        "orders": 10,
        "quantity": 774,
        "order_value": 259.9,
        "unique_prods": 32,
        "cluster": 0
      },
      {
        "id": 16617,
        "spending": 151.85,
        "orders": 1,
        "quantity": 91,
        "order_value": 151.85,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 16882,
        "spending": 705.12,
        "orders": 3,
        "quantity": 424,
        "order_value": 235.04,
        "unique_prods": 39,
        "cluster": 2
      },
      {
        "id": 17282,
        "spending": 1703.41,
        "orders": 3,
        "quantity": 1877,
        "order_value": 567.8,
        "unique_prods": 79,
        "cluster": 0
      },
      {
        "id": 13419,
        "spending": 221.06,
        "orders": 1,
        "quantity": 275,
        "order_value": 221.06,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 16855,
        "spending": 328.4,
        "orders": 2,
        "quantity": 164,
        "order_value": 164.2,
        "unique_prods": 19,
        "cluster": 1
      },
      {
        "id": 13426,
        "spending": 3641.32,
        "orders": 10,
        "quantity": 2245,
        "order_value": 364.13,
        "unique_prods": 103,
        "cluster": 0
      },
      {
        "id": 14607,
        "spending": 16569.5,
        "orders": 14,
        "quantity": 11766,
        "order_value": 1183.54,
        "unique_prods": 38,
        "cluster": 0
      },
      {
        "id": 17287,
        "spending": 1064.11,
        "orders": 7,
        "quantity": 559,
        "order_value": 152.02,
        "unique_prods": 88,
        "cluster": 0
      },
      {
        "id": 13975,
        "spending": 2526.28,
        "orders": 6,
        "quantity": 1732,
        "order_value": 421.05,
        "unique_prods": 240,
        "cluster": 0
      },
      {
        "id": 16710,
        "spending": 2483.04,
        "orders": 10,
        "quantity": 1836,
        "order_value": 248.3,
        "unique_prods": 268,
        "cluster": 0
      },
      {
        "id": 13417,
        "spending": 640.83,
        "orders": 2,
        "quantity": 162,
        "order_value": 320.42,
        "unique_prods": 26,
        "cluster": 2
      },
      {
        "id": 13860,
        "spending": 1245.9,
        "orders": 5,
        "quantity": 591,
        "order_value": 249.18,
        "unique_prods": 58,
        "cluster": 2
      },
      {
        "id": 13722,
        "spending": 2375.41,
        "orders": 3,
        "quantity": 1401,
        "order_value": 791.8,
        "unique_prods": 75,
        "cluster": 0
      },
      {
        "id": 13947,
        "spending": 90.6,
        "orders": 1,
        "quantity": 44,
        "order_value": 90.6,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 14589,
        "spending": 39.75,
        "orders": 1,
        "quantity": 5,
        "order_value": 39.75,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 12386,
        "spending": 401.9,
        "orders": 2,
        "quantity": 354,
        "order_value": 200.95,
        "unique_prods": 10,
        "cluster": 2
      },
      {
        "id": 16839,
        "spending": 16594.35,
        "orders": 34,
        "quantity": 8975,
        "order_value": 488.07,
        "unique_prods": 114,
        "cluster": 0
      },
      {
        "id": 13771,
        "spending": 2634.45,
        "orders": 4,
        "quantity": 1477,
        "order_value": 658.61,
        "unique_prods": 114,
        "cluster": 0
      },
      {
        "id": 16500,
        "spending": 400.86,
        "orders": 6,
        "quantity": 123,
        "order_value": 66.81,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 13376,
        "spending": 1019.76,
        "orders": 3,
        "quantity": 493,
        "order_value": 339.92,
        "unique_prods": 45,
        "cluster": 2
      },
      {
        "id": 13980,
        "spending": 200.14,
        "orders": 1,
        "quantity": 172,
        "order_value": 200.14,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 17181,
        "spending": 239.92,
        "orders": 2,
        "quantity": 241,
        "order_value": 119.96,
        "unique_prods": 23,
        "cluster": 1
      },
      {
        "id": 16906,
        "spending": 579.77,
        "orders": 4,
        "quantity": 281,
        "order_value": 144.94,
        "unique_prods": 74,
        "cluster": 2
      },
      {
        "id": 13548,
        "spending": 682.41,
        "orders": 2,
        "quantity": 441,
        "order_value": 341.21,
        "unique_prods": 114,
        "cluster": 2
      },
      {
        "id": 16569,
        "spending": 124.2,
        "orders": 1,
        "quantity": 93,
        "order_value": 124.2,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 16422,
        "spending": 34684.4,
        "orders": 51,
        "quantity": 33704,
        "order_value": 680.09,
        "unique_prods": 68,
        "cluster": 0
      },
      {
        "id": 12824,
        "spending": 397.12,
        "orders": 1,
        "quantity": 232,
        "order_value": 397.12,
        "unique_prods": 25,
        "cluster": 2
      },
      {
        "id": 13699,
        "spending": 308.58,
        "orders": 1,
        "quantity": 66,
        "order_value": 308.58,
        "unique_prods": 14,
        "cluster": 1
      },
      {
        "id": 14501,
        "spending": 251.21,
        "orders": 2,
        "quantity": 161,
        "order_value": 125.61,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 14093,
        "spending": 442.85,
        "orders": 1,
        "quantity": 406,
        "order_value": 442.85,
        "unique_prods": 95,
        "cluster": 2
      },
      {
        "id": 14499,
        "spending": 815.32,
        "orders": 3,
        "quantity": 501,
        "order_value": 271.77,
        "unique_prods": 146,
        "cluster": 2
      },
      {
        "id": 15795,
        "spending": 610.01,
        "orders": 1,
        "quantity": 581,
        "order_value": 610.01,
        "unique_prods": 42,
        "cluster": 2
      },
      {
        "id": 15396,
        "spending": 288.18,
        "orders": 1,
        "quantity": 122,
        "order_value": 288.18,
        "unique_prods": 14,
        "cluster": 1
      },
      {
        "id": 13095,
        "spending": 74.4,
        "orders": 1,
        "quantity": 144,
        "order_value": 74.4,
        "unique_prods": 6,
        "cluster": 1
      },
      {
        "id": 14585,
        "spending": 157.05,
        "orders": 1,
        "quantity": 91,
        "order_value": 157.05,
        "unique_prods": 29,
        "cluster": 1
      },
      {
        "id": 18118,
        "spending": 5653.82,
        "orders": 26,
        "quantity": 2882,
        "order_value": 217.45,
        "unique_prods": 424,
        "cluster": 0
      },
      {
        "id": 17749,
        "spending": 674.52,
        "orders": 2,
        "quantity": 320,
        "order_value": 337.26,
        "unique_prods": 33,
        "cluster": 2
      },
      {
        "id": 14295,
        "spending": 166.2,
        "orders": 1,
        "quantity": 84,
        "order_value": 166.2,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 12657,
        "spending": 1643.18,
        "orders": 4,
        "quantity": 1044,
        "order_value": 410.8,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 15668,
        "spending": 76.32,
        "orders": 1,
        "quantity": 72,
        "order_value": 76.32,
        "unique_prods": 1,
        "cluster": 1
      },
      {
        "id": 15689,
        "spending": 254.1,
        "orders": 2,
        "quantity": 84,
        "order_value": 127.05,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 16236,
        "spending": 432.2,
        "orders": 1,
        "quantity": 184,
        "order_value": 432.2,
        "unique_prods": 20,
        "cluster": 2
      },
      {
        "id": 17525,
        "spending": 422.7,
        "orders": 1,
        "quantity": 82,
        "order_value": 422.7,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 13748,
        "spending": 948.25,
        "orders": 5,
        "quantity": 439,
        "order_value": 189.65,
        "unique_prods": 24,
        "cluster": 2
      },
      {
        "id": 13137,
        "spending": 3650.41,
        "orders": 8,
        "quantity": 2226,
        "order_value": 456.3,
        "unique_prods": 345,
        "cluster": 0
      },
      {
        "id": 12967,
        "spending": 1660.9,
        "orders": 2,
        "quantity": 438,
        "order_value": 830.45,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 14173,
        "spending": 450.84,
        "orders": 4,
        "quantity": 150,
        "order_value": 112.71,
        "unique_prods": 28,
        "cluster": 1
      },
      {
        "id": 16987,
        "spending": 1625.05,
        "orders": 7,
        "quantity": 402,
        "order_value": 232.15,
        "unique_prods": 74,
        "cluster": 0
      },
      {
        "id": 13898,
        "spending": 155.93,
        "orders": 1,
        "quantity": 133,
        "order_value": 155.93,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 17034,
        "spending": 745.52,
        "orders": 3,
        "quantity": 410,
        "order_value": 248.51,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 14142,
        "spending": 311.81,
        "orders": 1,
        "quantity": 313,
        "order_value": 311.81,
        "unique_prods": 22,
        "cluster": 2
      },
      {
        "id": 15415,
        "spending": 572.81,
        "orders": 1,
        "quantity": 575,
        "order_value": 572.81,
        "unique_prods": 46,
        "cluster": 2
      },
      {
        "id": 12445,
        "spending": 133.4,
        "orders": 1,
        "quantity": 62,
        "order_value": 133.4,
        "unique_prods": 4,
        "cluster": 1
      },
      {
        "id": 17625,
        "spending": 2047.0,
        "orders": 4,
        "quantity": 1198,
        "order_value": 511.75,
        "unique_prods": 223,
        "cluster": 0
      },
      {
        "id": 16245,
        "spending": 1413.66,
        "orders": 3,
        "quantity": 1014,
        "order_value": 471.22,
        "unique_prods": 80,
        "cluster": 2
      },
      {
        "id": 12458,
        "spending": 947.4,
        "orders": 2,
        "quantity": 506,
        "order_value": 473.7,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 12785,
        "spending": 311.95,
        "orders": 1,
        "quantity": 131,
        "order_value": 311.95,
        "unique_prods": 14,
        "cluster": 1
      },
      {
        "id": 13759,
        "spending": 659.41,
        "orders": 2,
        "quantity": 287,
        "order_value": 329.7,
        "unique_prods": 24,
        "cluster": 2
      },
      {
        "id": 16764,
        "spending": 2799.25,
        "orders": 13,
        "quantity": 1259,
        "order_value": 215.33,
        "unique_prods": 209,
        "cluster": 0
      },
      {
        "id": 13244,
        "spending": 121.74,
        "orders": 1,
        "quantity": 38,
        "order_value": 121.74,
        "unique_prods": 27,
        "cluster": 1
      },
      {
        "id": 17526,
        "spending": 1195.9,
        "orders": 4,
        "quantity": 310,
        "order_value": 298.98,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 18121,
        "spending": 673.1,
        "orders": 2,
        "quantity": 450,
        "order_value": 336.55,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 18217,
        "spending": 621.75,
        "orders": 2,
        "quantity": 491,
        "order_value": 310.88,
        "unique_prods": 27,
        "cluster": 2
      },
      {
        "id": 16897,
        "spending": 289.78,
        "orders": 2,
        "quantity": 73,
        "order_value": 144.89,
        "unique_prods": 37,
        "cluster": 1
      },
      {
        "id": 18110,
        "spending": 236.3,
        "orders": 1,
        "quantity": 86,
        "order_value": 236.3,
        "unique_prods": 33,
        "cluster": 1
      },
      {
        "id": 12714,
        "spending": 4708.86,
        "orders": 5,
        "quantity": 3069,
        "order_value": 941.77,
        "unique_prods": 216,
        "cluster": 0
      },
      {
        "id": 16998,
        "spending": 295.0,
        "orders": 4,
        "quantity": 76,
        "order_value": 73.75,
        "unique_prods": 1,
        "cluster": 1
      },
      {
        "id": 14220,
        "spending": 632.4,
        "orders": 2,
        "quantity": 272,
        "order_value": 316.2,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 13267,
        "spending": 4521.49,
        "orders": 19,
        "quantity": 1969,
        "order_value": 237.97,
        "unique_prods": 88,
        "cluster": 0
      },
      {
        "id": 15690,
        "spending": 239.76,
        "orders": 2,
        "quantity": 408,
        "order_value": 119.88,
        "unique_prods": 19,
        "cluster": 1
      },
      {
        "id": 14397,
        "spending": 2612.96,
        "orders": 19,
        "quantity": 1890,
        "order_value": 137.52,
        "unique_prods": 18,
        "cluster": 0
      },
      {
        "id": 15838,
        "spending": 33643.08,
        "orders": 19,
        "quantity": 18368,
        "order_value": 1770.69,
        "unique_prods": 54,
        "cluster": 0
      },
      {
        "id": 14312,
        "spending": 1611.59,
        "orders": 6,
        "quantity": 1012,
        "order_value": 268.6,
        "unique_prods": 74,
        "cluster": 0
      },
      {
        "id": 12945,
        "spending": 462.95,
        "orders": 1,
        "quantity": 165,
        "order_value": 462.95,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 17289,
        "spending": 944.41,
        "orders": 3,
        "quantity": 520,
        "order_value": 314.8,
        "unique_prods": 86,
        "cluster": 2
      },
      {
        "id": 16377,
        "spending": 676.2,
        "orders": 1,
        "quantity": 1500,
        "order_value": 676.2,
        "unique_prods": 5,
        "cluster": 2
      },
      {
        "id": 17655,
        "spending": 2638.94,
        "orders": 7,
        "quantity": 1116,
        "order_value": 376.99,
        "unique_prods": 66,
        "cluster": 0
      },
      {
        "id": 14720,
        "spending": 663.81,
        "orders": 3,
        "quantity": 219,
        "order_value": 221.27,
        "unique_prods": 34,
        "cluster": 2
      },
      {
        "id": 17670,
        "spending": 205.7,
        "orders": 1,
        "quantity": 110,
        "order_value": 205.7,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 15154,
        "spending": 296.42,
        "orders": 1,
        "quantity": 104,
        "order_value": 296.42,
        "unique_prods": 66,
        "cluster": 2
      },
      {
        "id": 18139,
        "spending": 8438.34,
        "orders": 6,
        "quantity": 5557,
        "order_value": 1406.39,
        "unique_prods": 35,
        "cluster": 0
      },
      {
        "id": 14377,
        "spending": 617.05,
        "orders": 2,
        "quantity": 219,
        "order_value": 308.52,
        "unique_prods": 11,
        "cluster": 2
      },
      {
        "id": 16779,
        "spending": 10629.72,
        "orders": 22,
        "quantity": 5325,
        "order_value": 483.17,
        "unique_prods": 161,
        "cluster": 0
      },
      {
        "id": 17690,
        "spending": 4757.95,
        "orders": 15,
        "quantity": 1773,
        "order_value": 317.2,
        "unique_prods": 186,
        "cluster": 0
      },
      {
        "id": 17138,
        "spending": 380.5,
        "orders": 1,
        "quantity": 126,
        "order_value": 380.5,
        "unique_prods": 24,
        "cluster": 2
      },
      {
        "id": 13803,
        "spending": 277.07,
        "orders": 1,
        "quantity": 121,
        "order_value": 277.07,
        "unique_prods": 17,
        "cluster": 1
      },
      {
        "id": 15992,
        "spending": 41.99,
        "orders": 1,
        "quantity": 17,
        "order_value": 41.99,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 16270,
        "spending": 1141.24,
        "orders": 1,
        "quantity": 688,
        "order_value": 1141.24,
        "unique_prods": 54,
        "cluster": 2
      },
      {
        "id": 15307,
        "spending": 205.3,
        "orders": 1,
        "quantity": 37,
        "order_value": 205.3,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 13338,
        "spending": 487.02,
        "orders": 1,
        "quantity": 256,
        "order_value": 487.02,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 13753,
        "spending": 741.26,
        "orders": 1,
        "quantity": 512,
        "order_value": 741.26,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 17058,
        "spending": 1179.89,
        "orders": 3,
        "quantity": 592,
        "order_value": 393.3,
        "unique_prods": 51,
        "cluster": 2
      },
      {
        "id": 16665,
        "spending": 135.4,
        "orders": 1,
        "quantity": 59,
        "order_value": 135.4,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 17218,
        "spending": 1960.72,
        "orders": 10,
        "quantity": 958,
        "order_value": 196.07,
        "unique_prods": 146,
        "cluster": 0
      },
      {
        "id": 14057,
        "spending": 6217.96,
        "orders": 17,
        "quantity": 4876,
        "order_value": 365.76,
        "unique_prods": 179,
        "cluster": 0
      },
      {
        "id": 15790,
        "spending": 220.85,
        "orders": 1,
        "quantity": 114,
        "order_value": 220.85,
        "unique_prods": 34,
        "cluster": 1
      },
      {
        "id": 12431,
        "spending": 6487.45,
        "orders": 15,
        "quantity": 2906,
        "order_value": 432.5,
        "unique_prods": 163,
        "cluster": 0
      },
      {
        "id": 16014,
        "spending": 662.38,
        "orders": 3,
        "quantity": 265,
        "order_value": 220.79,
        "unique_prods": 123,
        "cluster": 2
      },
      {
        "id": 14714,
        "spending": 160.19,
        "orders": 1,
        "quantity": 229,
        "order_value": 160.19,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 16063,
        "spending": 335.32,
        "orders": 1,
        "quantity": 262,
        "order_value": 335.32,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 17362,
        "spending": 312.23,
        "orders": 2,
        "quantity": 191,
        "order_value": 156.11,
        "unique_prods": 30,
        "cluster": 1
      },
      {
        "id": 12755,
        "spending": 3811.95,
        "orders": 2,
        "quantity": 1491,
        "order_value": 1905.97,
        "unique_prods": 4,
        "cluster": 2
      },
      {
        "id": 17886,
        "spending": 899.61,
        "orders": 3,
        "quantity": 481,
        "order_value": 299.87,
        "unique_prods": 93,
        "cluster": 2
      },
      {
        "id": 12641,
        "spending": 185.9,
        "orders": 1,
        "quantity": 72,
        "order_value": 185.9,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 13253,
        "spending": 1030.4,
        "orders": 2,
        "quantity": 1572,
        "order_value": 515.2,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 17343,
        "spending": 193.64,
        "orders": 1,
        "quantity": 56,
        "order_value": 193.64,
        "unique_prods": 17,
        "cluster": 1
      },
      {
        "id": 16915,
        "spending": 621.68,
        "orders": 6,
        "quantity": 132,
        "order_value": 103.61,
        "unique_prods": 46,
        "cluster": 2
      },
      {
        "id": 15581,
        "spending": 3679.97,
        "orders": 13,
        "quantity": 286,
        "order_value": 283.07,
        "unique_prods": 134,
        "cluster": 0
      },
      {
        "id": 13235,
        "spending": 1031.07,
        "orders": 1,
        "quantity": 441,
        "order_value": 1031.07,
        "unique_prods": 53,
        "cluster": 2
      },
      {
        "id": 17027,
        "spending": 890.29,
        "orders": 6,
        "quantity": 421,
        "order_value": 148.38,
        "unique_prods": 110,
        "cluster": 2
      },
      {
        "id": 13874,
        "spending": 540.45,
        "orders": 1,
        "quantity": 180,
        "order_value": 540.45,
        "unique_prods": 18,
        "cluster": 2
      },
      {
        "id": 17735,
        "spending": 13110.02,
        "orders": 19,
        "quantity": 8439,
        "order_value": 690.0,
        "unique_prods": 319,
        "cluster": 0
      },
      {
        "id": 15990,
        "spending": 792.11,
        "orders": 2,
        "quantity": 443,
        "order_value": 396.06,
        "unique_prods": 52,
        "cluster": 2
      },
      {
        "id": 13954,
        "spending": 439.92,
        "orders": 2,
        "quantity": 150,
        "order_value": 219.96,
        "unique_prods": 24,
        "cluster": 2
      },
      {
        "id": 17861,
        "spending": 2100.8,
        "orders": 8,
        "quantity": 1988,
        "order_value": 262.6,
        "unique_prods": 172,
        "cluster": 0
      },
      {
        "id": 13218,
        "spending": 62.64,
        "orders": 1,
        "quantity": 88,
        "order_value": 62.64,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 16654,
        "spending": 601.27,
        "orders": 4,
        "quantity": 282,
        "order_value": 150.32,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 17958,
        "spending": 508.46,
        "orders": 1,
        "quantity": 84,
        "order_value": 508.46,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 14440,
        "spending": 2357.68,
        "orders": 5,
        "quantity": 588,
        "order_value": 471.54,
        "unique_prods": 33,
        "cluster": 2
      },
      {
        "id": 17931,
        "spending": 408.36,
        "orders": 2,
        "quantity": 249,
        "order_value": 204.18,
        "unique_prods": 63,
        "cluster": 2
      },
      {
        "id": 13301,
        "spending": 618.09,
        "orders": 4,
        "quantity": 345,
        "order_value": 154.52,
        "unique_prods": 75,
        "cluster": 2
      },
      {
        "id": 15436,
        "spending": 1122.53,
        "orders": 3,
        "quantity": 613,
        "order_value": 374.18,
        "unique_prods": 243,
        "cluster": 2
      },
      {
        "id": 12423,
        "spending": 1859.31,
        "orders": 8,
        "quantity": 1339,
        "order_value": 232.41,
        "unique_prods": 97,
        "cluster": 0
      },
      {
        "id": 17338,
        "spending": 6643.93,
        "orders": 8,
        "quantity": 3128,
        "order_value": 830.49,
        "unique_prods": 389,
        "cluster": 0
      },
      {
        "id": 17966,
        "spending": 1098.43,
        "orders": 5,
        "quantity": 2571,
        "order_value": 219.69,
        "unique_prods": 53,
        "cluster": 0
      },
      {
        "id": 17703,
        "spending": 798.74,
        "orders": 3,
        "quantity": 590,
        "order_value": 266.25,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 12403,
        "spending": 427.7,
        "orders": 1,
        "quantity": 96,
        "order_value": 427.7,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 13842,
        "spending": 3385.62,
        "orders": 9,
        "quantity": 1768,
        "order_value": 376.18,
        "unique_prods": 155,
        "cluster": 0
      },
      {
        "id": 15955,
        "spending": 4416.26,
        "orders": 14,
        "quantity": 2135,
        "order_value": 315.45,
        "unique_prods": 137,
        "cluster": 0
      },
      {
        "id": 16227,
        "spending": 314.22,
        "orders": 1,
        "quantity": 90,
        "order_value": 314.22,
        "unique_prods": 6,
        "cluster": 1
      },
      {
        "id": 17239,
        "spending": 382.5,
        "orders": 1,
        "quantity": 150,
        "order_value": 382.5,
        "unique_prods": 15,
        "cluster": 2
      },
      {
        "id": 12361,
        "spending": 189.9,
        "orders": 1,
        "quantity": 91,
        "order_value": 189.9,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 16168,
        "spending": 3787.6,
        "orders": 27,
        "quantity": 1892,
        "order_value": 140.28,
        "unique_prods": 57,
        "cluster": 0
      },
      {
        "id": 12868,
        "spending": 1607.06,
        "orders": 6,
        "quantity": 928,
        "order_value": 267.84,
        "unique_prods": 72,
        "cluster": 0
      },
      {
        "id": 14973,
        "spending": 1314.45,
        "orders": 3,
        "quantity": 369,
        "order_value": 438.15,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 13052,
        "spending": 348.15,
        "orders": 1,
        "quantity": 222,
        "order_value": 348.15,
        "unique_prods": 18,
        "cluster": 2
      },
      {
        "id": 16485,
        "spending": 363.65,
        "orders": 1,
        "quantity": 235,
        "order_value": 363.65,
        "unique_prods": 41,
        "cluster": 2
      },
      {
        "id": 14236,
        "spending": 490.86,
        "orders": 2,
        "quantity": 310,
        "order_value": 245.43,
        "unique_prods": 15,
        "cluster": 2
      },
      {
        "id": 17189,
        "spending": 384.4,
        "orders": 2,
        "quantity": 227,
        "order_value": 192.2,
        "unique_prods": 52,
        "cluster": 2
      },
      {
        "id": 17990,
        "spending": 630.84,
        "orders": 3,
        "quantity": 414,
        "order_value": 210.28,
        "unique_prods": 27,
        "cluster": 2
      },
      {
        "id": 12797,
        "spending": 254.03,
        "orders": 1,
        "quantity": 118,
        "order_value": 254.03,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 16846,
        "spending": 214.32,
        "orders": 1,
        "quantity": 135,
        "order_value": 214.32,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 17469,
        "spending": 1870.97,
        "orders": 5,
        "quantity": 787,
        "order_value": 374.19,
        "unique_prods": 61,
        "cluster": 0
      },
      {
        "id": 18014,
        "spending": 166.42,
        "orders": 1,
        "quantity": 68,
        "order_value": 166.42,
        "unique_prods": 29,
        "cluster": 1
      },
      {
        "id": 14401,
        "spending": 4051.48,
        "orders": 13,
        "quantity": 4507,
        "order_value": 311.65,
        "unique_prods": 113,
        "cluster": 0
      },
      {
        "id": 13725,
        "spending": 1980.56,
        "orders": 8,
        "quantity": 806,
        "order_value": 247.57,
        "unique_prods": 95,
        "cluster": 0
      },
      {
        "id": 15484,
        "spending": 3594.31,
        "orders": 4,
        "quantity": 3152,
        "order_value": 898.58,
        "unique_prods": 135,
        "cluster": 0
      },
      {
        "id": 16628,
        "spending": 2188.05,
        "orders": 5,
        "quantity": 1205,
        "order_value": 437.61,
        "unique_prods": 79,
        "cluster": 0
      },
      {
        "id": 14592,
        "spending": 570.46,
        "orders": 3,
        "quantity": 415,
        "order_value": 190.15,
        "unique_prods": 132,
        "cluster": 2
      },
      {
        "id": 16655,
        "spending": 3794.52,
        "orders": 6,
        "quantity": 2367,
        "order_value": 632.42,
        "unique_prods": 208,
        "cluster": 0
      },
      {
        "id": 15953,
        "spending": 1659.38,
        "orders": 8,
        "quantity": 892,
        "order_value": 207.42,
        "unique_prods": 63,
        "cluster": 0
      },
      {
        "id": 17206,
        "spending": 204.24,
        "orders": 1,
        "quantity": 76,
        "order_value": 204.24,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 13429,
        "spending": 1006.8,
        "orders": 4,
        "quantity": 1390,
        "order_value": 251.7,
        "unique_prods": 55,
        "cluster": 2
      },
      {
        "id": 14508,
        "spending": 276.42,
        "orders": 2,
        "quantity": 131,
        "order_value": 138.21,
        "unique_prods": 52,
        "cluster": 1
      },
      {
        "id": 14180,
        "spending": 4748.52,
        "orders": 25,
        "quantity": 719,
        "order_value": 189.94,
        "unique_prods": 112,
        "cluster": 0
      },
      {
        "id": 17859,
        "spending": 148.21,
        "orders": 1,
        "quantity": 127,
        "order_value": 148.21,
        "unique_prods": 23,
        "cluster": 1
      },
      {
        "id": 13132,
        "spending": 77.3,
        "orders": 1,
        "quantity": 20,
        "order_value": 77.3,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 14470,
        "spending": 461.19,
        "orders": 2,
        "quantity": 193,
        "order_value": 230.6,
        "unique_prods": 43,
        "cluster": 2
      },
      {
        "id": 12987,
        "spending": 558.7,
        "orders": 2,
        "quantity": 219,
        "order_value": 279.35,
        "unique_prods": 27,
        "cluster": 2
      },
      {
        "id": 14383,
        "spending": 1247.69,
        "orders": 3,
        "quantity": 817,
        "order_value": 415.9,
        "unique_prods": 49,
        "cluster": 2
      },
      {
        "id": 13639,
        "spending": 1033.34,
        "orders": 1,
        "quantity": 800,
        "order_value": 1033.34,
        "unique_prods": 39,
        "cluster": 2
      },
      {
        "id": 14800,
        "spending": 4339.74,
        "orders": 12,
        "quantity": 3655,
        "order_value": 361.64,
        "unique_prods": 246,
        "cluster": 0
      },
      {
        "id": 13078,
        "spending": 12627.94,
        "orders": 26,
        "quantity": 5630,
        "order_value": 485.69,
        "unique_prods": 95,
        "cluster": 0
      },
      {
        "id": 14624,
        "spending": 225.85,
        "orders": 2,
        "quantity": 162,
        "order_value": 112.92,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 17734,
        "spending": 700.63,
        "orders": 3,
        "quantity": 422,
        "order_value": 233.54,
        "unique_prods": 40,
        "cluster": 2
      },
      {
        "id": 17329,
        "spending": 523.11,
        "orders": 2,
        "quantity": 142,
        "order_value": 261.56,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 15525,
        "spending": 825.92,
        "orders": 3,
        "quantity": 416,
        "order_value": 275.31,
        "unique_prods": 133,
        "cluster": 2
      },
      {
        "id": 13006,
        "spending": 81.57,
        "orders": 1,
        "quantity": 55,
        "order_value": 81.57,
        "unique_prods": 4,
        "cluster": 1
      },
      {
        "id": 12843,
        "spending": 1702.26,
        "orders": 8,
        "quantity": 781,
        "order_value": 212.78,
        "unique_prods": 69,
        "cluster": 0
      },
      {
        "id": 13405,
        "spending": 572.45,
        "orders": 3,
        "quantity": 165,
        "order_value": 190.82,
        "unique_prods": 25,
        "cluster": 2
      },
      {
        "id": 16414,
        "spending": 126.25,
        "orders": 2,
        "quantity": 27,
        "order_value": 63.12,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 16497,
        "spending": 2965.69,
        "orders": 6,
        "quantity": 1396,
        "order_value": 494.28,
        "unique_prods": 128,
        "cluster": 0
      },
      {
        "id": 13876,
        "spending": 122.7,
        "orders": 1,
        "quantity": 36,
        "order_value": 122.7,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 14334,
        "spending": 2552.21,
        "orders": 8,
        "quantity": 1731,
        "order_value": 319.03,
        "unique_prods": 98,
        "cluster": 0
      },
      {
        "id": 14332,
        "spending": 866.31,
        "orders": 3,
        "quantity": 481,
        "order_value": 288.77,
        "unique_prods": 22,
        "cluster": 2
      },
      {
        "id": 18173,
        "spending": 2106.84,
        "orders": 4,
        "quantity": 1220,
        "order_value": 526.71,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 13519,
        "spending": 122.75,
        "orders": 1,
        "quantity": 23,
        "order_value": 122.75,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 13318,
        "spending": 640.76,
        "orders": 3,
        "quantity": 304,
        "order_value": 213.59,
        "unique_prods": 14,
        "cluster": 2
      },
      {
        "id": 14753,
        "spending": 563.15,
        "orders": 1,
        "quantity": 211,
        "order_value": 563.15,
        "unique_prods": 30,
        "cluster": 2
      },
      {
        "id": 14758,
        "spending": 1484.06,
        "orders": 4,
        "quantity": 419,
        "order_value": 371.01,
        "unique_prods": 54,
        "cluster": 2
      },
      {
        "id": 13538,
        "spending": 1280.85,
        "orders": 7,
        "quantity": 175,
        "order_value": 182.98,
        "unique_prods": 10,
        "cluster": 2
      },
      {
        "id": 15039,
        "spending": 19914.44,
        "orders": 47,
        "quantity": 9209,
        "order_value": 423.71,
        "unique_prods": 408,
        "cluster": 0
      },
      {
        "id": 15135,
        "spending": 139.05,
        "orders": 1,
        "quantity": 43,
        "order_value": 139.05,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 16016,
        "spending": 1508.76,
        "orders": 8,
        "quantity": 620,
        "order_value": 188.6,
        "unique_prods": 156,
        "cluster": 0
      },
      {
        "id": 16712,
        "spending": 3645.43,
        "orders": 11,
        "quantity": 1749,
        "order_value": 331.4,
        "unique_prods": 259,
        "cluster": 0
      },
      {
        "id": 15935,
        "spending": 416.86,
        "orders": 2,
        "quantity": 115,
        "order_value": 208.43,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 16620,
        "spending": 178.96,
        "orders": 2,
        "quantity": 88,
        "order_value": 89.48,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 16735,
        "spending": 2300.56,
        "orders": 5,
        "quantity": 1573,
        "order_value": 460.11,
        "unique_prods": 88,
        "cluster": 0
      },
      {
        "id": 15292,
        "spending": 180.94,
        "orders": 1,
        "quantity": 56,
        "order_value": 180.94,
        "unique_prods": 24,
        "cluster": 1
      },
      {
        "id": 13462,
        "spending": 151.5,
        "orders": 1,
        "quantity": 62,
        "order_value": 151.5,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 16257,
        "spending": 46.95,
        "orders": 1,
        "quantity": 2,
        "order_value": 46.95,
        "unique_prods": 2,
        "cluster": 1
      },
      {
        "id": 16048,
        "spending": 256.44,
        "orders": 2,
        "quantity": 144,
        "order_value": 128.22,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 14548,
        "spending": 652.8,
        "orders": 2,
        "quantity": 256,
        "order_value": 326.4,
        "unique_prods": 2,
        "cluster": 1
      },
      {
        "id": 16117,
        "spending": 232.21,
        "orders": 1,
        "quantity": 130,
        "order_value": 232.21,
        "unique_prods": 30,
        "cluster": 1
      },
      {
        "id": 14513,
        "spending": 455.59,
        "orders": 3,
        "quantity": 361,
        "order_value": 151.86,
        "unique_prods": 11,
        "cluster": 2
      },
      {
        "id": 14903,
        "spending": 2810.63,
        "orders": 5,
        "quantity": 1536,
        "order_value": 562.13,
        "unique_prods": 227,
        "cluster": 0
      },
      {
        "id": 13572,
        "spending": 1384.25,
        "orders": 1,
        "quantity": 534,
        "order_value": 1384.25,
        "unique_prods": 32,
        "cluster": 2
      },
      {
        "id": 15504,
        "spending": 52.83,
        "orders": 1,
        "quantity": 33,
        "order_value": 52.83,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 14066,
        "spending": 152.55,
        "orders": 1,
        "quantity": 45,
        "order_value": 152.55,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 14198,
        "spending": 701.4,
        "orders": 4,
        "quantity": 290,
        "order_value": 175.35,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 16813,
        "spending": 1692.98,
        "orders": 10,
        "quantity": 1525,
        "order_value": 169.3,
        "unique_prods": 248,
        "cluster": 0
      },
      {
        "id": 12753,
        "spending": 21429.39,
        "orders": 6,
        "quantity": 11421,
        "order_value": 3571.57,
        "unique_prods": 132,
        "cluster": 0
      },
      {
        "id": 18151,
        "spending": 653.35,
        "orders": 2,
        "quantity": 355,
        "order_value": 326.67,
        "unique_prods": 38,
        "cluster": 2
      },
      {
        "id": 14101,
        "spending": 5976.79,
        "orders": 6,
        "quantity": 6942,
        "order_value": 996.13,
        "unique_prods": 15,
        "cluster": 0
      },
      {
        "id": 16366,
        "spending": 327.3,
        "orders": 1,
        "quantity": 256,
        "order_value": 327.3,
        "unique_prods": 18,
        "cluster": 2
      },
      {
        "id": 13666,
        "spending": 84.65,
        "orders": 3,
        "quantity": 41,
        "order_value": 28.22,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 15660,
        "spending": 1600.86,
        "orders": 9,
        "quantity": 1050,
        "order_value": 177.87,
        "unique_prods": 55,
        "cluster": 0
      },
      {
        "id": 16810,
        "spending": 309.54,
        "orders": 1,
        "quantity": 114,
        "order_value": 309.54,
        "unique_prods": 15,
        "cluster": 1
      },
      {
        "id": 16766,
        "spending": 1145.6,
        "orders": 2,
        "quantity": 536,
        "order_value": 572.8,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 18092,
        "spending": 9068.26,
        "orders": 11,
        "quantity": 4252,
        "order_value": 824.39,
        "unique_prods": 28,
        "cluster": 0
      },
      {
        "id": 16110,
        "spending": 1337.48,
        "orders": 3,
        "quantity": 733,
        "order_value": 445.83,
        "unique_prods": 283,
        "cluster": 0
      },
      {
        "id": 16885,
        "spending": 471.51,
        "orders": 3,
        "quantity": 184,
        "order_value": 157.17,
        "unique_prods": 82,
        "cluster": 2
      },
      {
        "id": 17231,
        "spending": 3174.32,
        "orders": 10,
        "quantity": 1742,
        "order_value": 317.43,
        "unique_prods": 292,
        "cluster": 0
      },
      {
        "id": 12384,
        "spending": 585.27,
        "orders": 2,
        "quantity": 126,
        "order_value": 292.64,
        "unique_prods": 26,
        "cluster": 2
      },
      {
        "id": 16778,
        "spending": 245.94,
        "orders": 2,
        "quantity": 194,
        "order_value": 122.97,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 18034,
        "spending": 422.88,
        "orders": 2,
        "quantity": 561,
        "order_value": 211.44,
        "unique_prods": 99,
        "cluster": 2
      },
      {
        "id": 16233,
        "spending": 536.68,
        "orders": 3,
        "quantity": 174,
        "order_value": 178.89,
        "unique_prods": 22,
        "cluster": 2
      },
      {
        "id": 13994,
        "spending": 2313.14,
        "orders": 6,
        "quantity": 940,
        "order_value": 385.52,
        "unique_prods": 122,
        "cluster": 0
      },
      {
        "id": 14847,
        "spending": 309.4,
        "orders": 1,
        "quantity": 120,
        "order_value": 309.4,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 13196,
        "spending": 1797.78,
        "orders": 4,
        "quantity": 1224,
        "order_value": 449.44,
        "unique_prods": 97,
        "cluster": 0
      },
      {
        "id": 15255,
        "spending": 890.85,
        "orders": 1,
        "quantity": 489,
        "order_value": 890.85,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 13494,
        "spending": 316.26,
        "orders": 1,
        "quantity": 162,
        "order_value": 316.26,
        "unique_prods": 18,
        "cluster": 2
      },
      {
        "id": 14052,
        "spending": 225.36,
        "orders": 1,
        "quantity": 89,
        "order_value": 225.36,
        "unique_prods": 56,
        "cluster": 1
      },
      {
        "id": 17017,
        "spending": 8694.26,
        "orders": 20,
        "quantity": 6673,
        "order_value": 434.71,
        "unique_prods": 88,
        "cluster": 0
      },
      {
        "id": 12627,
        "spending": 4478.53,
        "orders": 7,
        "quantity": 2752,
        "order_value": 639.79,
        "unique_prods": 162,
        "cluster": 0
      },
      {
        "id": 13344,
        "spending": 2543.72,
        "orders": 3,
        "quantity": 971,
        "order_value": 847.91,
        "unique_prods": 115,
        "cluster": 0
      },
      {
        "id": 14946,
        "spending": 100.9,
        "orders": 1,
        "quantity": 22,
        "order_value": 100.9,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 12866,
        "spending": 559.12,
        "orders": 1,
        "quantity": 171,
        "order_value": 559.12,
        "unique_prods": 26,
        "cluster": 2
      },
      {
        "id": 12560,
        "spending": 2134.01,
        "orders": 3,
        "quantity": 1110,
        "order_value": 711.34,
        "unique_prods": 91,
        "cluster": 0
      },
      {
        "id": 18102,
        "spending": 259657.3,
        "orders": 60,
        "quantity": 64124,
        "order_value": 4327.62,
        "unique_prods": 150,
        "cluster": 0
      },
      {
        "id": 14725,
        "spending": 718.08,
        "orders": 1,
        "quantity": 593,
        "order_value": 718.08,
        "unique_prods": 45,
        "cluster": 2
      },
      {
        "id": 16407,
        "spending": 2126.93,
        "orders": 10,
        "quantity": 1124,
        "order_value": 212.69,
        "unique_prods": 99,
        "cluster": 0
      },
      {
        "id": 15626,
        "spending": 675.8,
        "orders": 2,
        "quantity": 766,
        "order_value": 337.9,
        "unique_prods": 49,
        "cluster": 2
      },
      {
        "id": 13349,
        "spending": 247.32,
        "orders": 1,
        "quantity": 225,
        "order_value": 247.32,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 18146,
        "spending": 160.35,
        "orders": 2,
        "quantity": 153,
        "order_value": 80.17,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 17692,
        "spending": 740.94,
        "orders": 4,
        "quantity": 672,
        "order_value": 185.23,
        "unique_prods": 34,
        "cluster": 2
      },
      {
        "id": 16526,
        "spending": 290.36,
        "orders": 1,
        "quantity": 106,
        "order_value": 290.36,
        "unique_prods": 15,
        "cluster": 1
      },
      {
        "id": 15507,
        "spending": 492.36,
        "orders": 1,
        "quantity": 162,
        "order_value": 492.36,
        "unique_prods": 41,
        "cluster": 2
      },
      {
        "id": 14851,
        "spending": 511.35,
        "orders": 2,
        "quantity": 325,
        "order_value": 255.67,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 15009,
        "spending": 1261.78,
        "orders": 3,
        "quantity": 642,
        "order_value": 420.59,
        "unique_prods": 148,
        "cluster": 2
      },
      {
        "id": 15877,
        "spending": 493.28,
        "orders": 2,
        "quantity": 371,
        "order_value": 246.64,
        "unique_prods": 122,
        "cluster": 2
      },
      {
        "id": 17278,
        "spending": 246.04,
        "orders": 1,
        "quantity": 179,
        "order_value": 246.04,
        "unique_prods": 15,
        "cluster": 1
      },
      {
        "id": 12401,
        "spending": 84.3,
        "orders": 1,
        "quantity": 11,
        "order_value": 84.3,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 14073,
        "spending": 151.04,
        "orders": 1,
        "quantity": 130,
        "order_value": 151.04,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 16036,
        "spending": 758.92,
        "orders": 2,
        "quantity": 716,
        "order_value": 379.46,
        "unique_prods": 55,
        "cluster": 2
      },
      {
        "id": 17464,
        "spending": 289.96,
        "orders": 1,
        "quantity": 220,
        "order_value": 289.96,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 13763,
        "spending": 1714.96,
        "orders": 1,
        "quantity": 728,
        "order_value": 1714.96,
        "unique_prods": 15,
        "cluster": 2
      },
      {
        "id": 16045,
        "spending": 1340.7,
        "orders": 4,
        "quantity": 897,
        "order_value": 335.18,
        "unique_prods": 71,
        "cluster": 2
      },
      {
        "id": 17880,
        "spending": 458.92,
        "orders": 1,
        "quantity": 314,
        "order_value": 458.92,
        "unique_prods": 26,
        "cluster": 2
      },
      {
        "id": 15930,
        "spending": 426.63,
        "orders": 1,
        "quantity": 139,
        "order_value": 426.63,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 13802,
        "spending": 4599.42,
        "orders": 3,
        "quantity": 2572,
        "order_value": 1533.14,
        "unique_prods": 55,
        "cluster": 0
      },
      {
        "id": 12653,
        "spending": 2209.85,
        "orders": 2,
        "quantity": 919,
        "order_value": 1104.92,
        "unique_prods": 37,
        "cluster": 2
      },
      {
        "id": 13414,
        "spending": 1390.5,
        "orders": 3,
        "quantity": 1574,
        "order_value": 463.5,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 16801,
        "spending": 1619.73,
        "orders": 4,
        "quantity": 499,
        "order_value": 404.93,
        "unique_prods": 72,
        "cluster": 2
      },
      {
        "id": 17483,
        "spending": 414.04,
        "orders": 3,
        "quantity": 191,
        "order_value": 138.01,
        "unique_prods": 18,
        "cluster": 1
      },
      {
        "id": 16757,
        "spending": 106.83,
        "orders": 1,
        "quantity": 81,
        "order_value": 106.83,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 17917,
        "spending": 341.28,
        "orders": 3,
        "quantity": 187,
        "order_value": 113.76,
        "unique_prods": 77,
        "cluster": 2
      },
      {
        "id": 17394,
        "spending": 203.87,
        "orders": 1,
        "quantity": 241,
        "order_value": 203.87,
        "unique_prods": 4,
        "cluster": 1
      },
      {
        "id": 15940,
        "spending": 35.8,
        "orders": 1,
        "quantity": 4,
        "order_value": 35.8,
        "unique_prods": 1,
        "cluster": 1
      },
      {
        "id": 12747,
        "spending": 4196.01,
        "orders": 11,
        "quantity": 1275,
        "order_value": 381.46,
        "unique_prods": 42,
        "cluster": 0
      },
      {
        "id": 14288,
        "spending": 426.6,
        "orders": 1,
        "quantity": 188,
        "order_value": 426.6,
        "unique_prods": 16,
        "cluster": 2
      },
      {
        "id": 18183,
        "spending": 632.07,
        "orders": 2,
        "quantity": 371,
        "order_value": 316.04,
        "unique_prods": 36,
        "cluster": 2
      },
      {
        "id": 16426,
        "spending": 1908.25,
        "orders": 10,
        "quantity": 1243,
        "order_value": 190.82,
        "unique_prods": 211,
        "cluster": 0
      },
      {
        "id": 15491,
        "spending": 3100.09,
        "orders": 6,
        "quantity": 1646,
        "order_value": 516.68,
        "unique_prods": 108,
        "cluster": 0
      },
      {
        "id": 16207,
        "spending": 394.38,
        "orders": 1,
        "quantity": 140,
        "order_value": 394.38,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 13988,
        "spending": 4147.96,
        "orders": 6,
        "quantity": 3044,
        "order_value": 691.33,
        "unique_prods": 188,
        "cluster": 0
      },
      {
        "id": 13165,
        "spending": 1021.48,
        "orders": 2,
        "quantity": 1376,
        "order_value": 510.74,
        "unique_prods": 40,
        "cluster": 2
      },
      {
        "id": 13431,
        "spending": 1269.1,
        "orders": 2,
        "quantity": 672,
        "order_value": 634.55,
        "unique_prods": 44,
        "cluster": 2
      },
      {
        "id": 17650,
        "spending": 166.08,
        "orders": 1,
        "quantity": 150,
        "order_value": 166.08,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 15724,
        "spending": 218.25,
        "orders": 2,
        "quantity": 73,
        "order_value": 109.12,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 17490,
        "spending": 2092.32,
        "orders": 7,
        "quantity": 1134,
        "order_value": 298.9,
        "unique_prods": 63,
        "cluster": 0
      },
      {
        "id": 15565,
        "spending": 173.16,
        "orders": 2,
        "quantity": 60,
        "order_value": 86.58,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 15857,
        "spending": 297.0,
        "orders": 1,
        "quantity": 308,
        "order_value": 297.0,
        "unique_prods": 14,
        "cluster": 2
      },
      {
        "id": 12468,
        "spending": 729.54,
        "orders": 2,
        "quantity": 366,
        "order_value": 364.77,
        "unique_prods": 36,
        "cluster": 2
      },
      {
        "id": 17018,
        "spending": 920.1,
        "orders": 2,
        "quantity": 176,
        "order_value": 460.05,
        "unique_prods": 15,
        "cluster": 2
      },
      {
        "id": 17914,
        "spending": 336.43,
        "orders": 1,
        "quantity": 473,
        "order_value": 336.43,
        "unique_prods": 72,
        "cluster": 2
      },
      {
        "id": 18071,
        "spending": 453.0,
        "orders": 2,
        "quantity": 260,
        "order_value": 226.5,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 16943,
        "spending": 816.73,
        "orders": 3,
        "quantity": 145,
        "order_value": 272.24,
        "unique_prods": 23,
        "cluster": 2
      },
      {
        "id": 14653,
        "spending": 1947.55,
        "orders": 7,
        "quantity": 950,
        "order_value": 278.22,
        "unique_prods": 154,
        "cluster": 0
      },
      {
        "id": 14362,
        "spending": 161.2,
        "orders": 1,
        "quantity": 100,
        "order_value": 161.2,
        "unique_prods": 37,
        "cluster": 1
      },
      {
        "id": 12993,
        "spending": 414.76,
        "orders": 4,
        "quantity": 240,
        "order_value": 103.69,
        "unique_prods": 26,
        "cluster": 1
      },
      {
        "id": 14390,
        "spending": 4652.82,
        "orders": 9,
        "quantity": 2136,
        "order_value": 516.98,
        "unique_prods": 135,
        "cluster": 0
      },
      {
        "id": 17253,
        "spending": 178.26,
        "orders": 1,
        "quantity": 43,
        "order_value": 178.26,
        "unique_prods": 18,
        "cluster": 1
      },
      {
        "id": 13845,
        "spending": 312.98,
        "orders": 1,
        "quantity": 182,
        "order_value": 312.98,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 17314,
        "spending": 2527.92,
        "orders": 8,
        "quantity": 1896,
        "order_value": 315.99,
        "unique_prods": 120,
        "cluster": 0
      },
      {
        "id": 16644,
        "spending": 833.78,
        "orders": 2,
        "quantity": 826,
        "order_value": 416.89,
        "unique_prods": 62,
        "cluster": 2
      },
      {
        "id": 13001,
        "spending": 9818.82,
        "orders": 13,
        "quantity": 5505,
        "order_value": 755.29,
        "unique_prods": 166,
        "cluster": 0
      },
      {
        "id": 13868,
        "spending": 3192.54,
        "orders": 2,
        "quantity": 1964,
        "order_value": 1596.27,
        "unique_prods": 32,
        "cluster": 0
      },
      {
        "id": 16091,
        "spending": 315.06,
        "orders": 2,
        "quantity": 154,
        "order_value": 157.53,
        "unique_prods": 16,
        "cluster": 1
      },
      {
        "id": 15720,
        "spending": 598.73,
        "orders": 1,
        "quantity": 281,
        "order_value": 598.73,
        "unique_prods": 128,
        "cluster": 2
      },
      {
        "id": 13144,
        "spending": 110.95,
        "orders": 1,
        "quantity": 21,
        "order_value": 110.95,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 15281,
        "spending": 2332.15,
        "orders": 9,
        "quantity": 1211,
        "order_value": 259.13,
        "unique_prods": 121,
        "cluster": 0
      },
      {
        "id": 16690,
        "spending": 225.58,
        "orders": 2,
        "quantity": 138,
        "order_value": 112.79,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 15221,
        "spending": 403.25,
        "orders": 1,
        "quantity": 43,
        "order_value": 403.25,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 14497,
        "spending": 475.37,
        "orders": 1,
        "quantity": 235,
        "order_value": 475.37,
        "unique_prods": 29,
        "cluster": 2
      },
      {
        "id": 14819,
        "spending": 272.07,
        "orders": 2,
        "quantity": 109,
        "order_value": 136.03,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 14348,
        "spending": 409.57,
        "orders": 1,
        "quantity": 183,
        "order_value": 409.57,
        "unique_prods": 18,
        "cluster": 2
      },
      {
        "id": 18142,
        "spending": 1019.52,
        "orders": 2,
        "quantity": 1276,
        "order_value": 509.76,
        "unique_prods": 9,
        "cluster": 2
      },
      {
        "id": 13304,
        "spending": 300.42,
        "orders": 1,
        "quantity": 238,
        "order_value": 300.42,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 12565,
        "spending": 145.92,
        "orders": 1,
        "quantity": 80,
        "order_value": 145.92,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 14472,
        "spending": 1936.84,
        "orders": 8,
        "quantity": 1160,
        "order_value": 242.1,
        "unique_prods": 153,
        "cluster": 0
      },
      {
        "id": 12615,
        "spending": 2291.19,
        "orders": 4,
        "quantity": 1376,
        "order_value": 572.8,
        "unique_prods": 82,
        "cluster": 0
      },
      {
        "id": 17540,
        "spending": 578.9,
        "orders": 2,
        "quantity": 194,
        "order_value": 289.45,
        "unique_prods": 20,
        "cluster": 2
      },
      {
        "id": 16513,
        "spending": 874.59,
        "orders": 4,
        "quantity": 407,
        "order_value": 218.65,
        "unique_prods": 33,
        "cluster": 2
      },
      {
        "id": 16365,
        "spending": 1540.42,
        "orders": 9,
        "quantity": 504,
        "order_value": 171.16,
        "unique_prods": 45,
        "cluster": 0
      },
      {
        "id": 13094,
        "spending": 1927.32,
        "orders": 12,
        "quantity": 1716,
        "order_value": 160.61,
        "unique_prods": 4,
        "cluster": 0
      },
      {
        "id": 14888,
        "spending": 369.2,
        "orders": 1,
        "quantity": 184,
        "order_value": 369.2,
        "unique_prods": 20,
        "cluster": 2
      },
      {
        "id": 14277,
        "spending": 4216.2,
        "orders": 3,
        "quantity": 1984,
        "order_value": 1405.4,
        "unique_prods": 195,
        "cluster": 0
      },
      {
        "id": 16893,
        "spending": 145.93,
        "orders": 1,
        "quantity": 62,
        "order_value": 145.93,
        "unique_prods": 44,
        "cluster": 1
      },
      {
        "id": 15458,
        "spending": 161.64,
        "orders": 1,
        "quantity": 156,
        "order_value": 161.64,
        "unique_prods": 7,
        "cluster": 1
      },
      {
        "id": 13398,
        "spending": 457.34,
        "orders": 1,
        "quantity": 281,
        "order_value": 457.34,
        "unique_prods": 26,
        "cluster": 2
      },
      {
        "id": 17702,
        "spending": 1824.37,
        "orders": 4,
        "quantity": 1353,
        "order_value": 456.09,
        "unique_prods": 58,
        "cluster": 0
      },
      {
        "id": 17790,
        "spending": 1965.55,
        "orders": 14,
        "quantity": 836,
        "order_value": 140.4,
        "unique_prods": 121,
        "cluster": 0
      },
      {
        "id": 16903,
        "spending": 373.24,
        "orders": 1,
        "quantity": 262,
        "order_value": 373.24,
        "unique_prods": 50,
        "cluster": 2
      },
      {
        "id": 17642,
        "spending": 712.29,
        "orders": 2,
        "quantity": 474,
        "order_value": 356.14,
        "unique_prods": 34,
        "cluster": 2
      },
      {
        "id": 15111,
        "spending": 1567.48,
        "orders": 3,
        "quantity": 710,
        "order_value": 522.49,
        "unique_prods": 70,
        "cluster": 2
      },
      {
        "id": 13161,
        "spending": 112.75,
        "orders": 1,
        "quantity": 29,
        "order_value": 112.75,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 13106,
        "spending": 76.5,
        "orders": 1,
        "quantity": 18,
        "order_value": 76.5,
        "unique_prods": 1,
        "cluster": 1
      },
      {
        "id": 17888,
        "spending": 726.05,
        "orders": 8,
        "quantity": 980,
        "order_value": 90.76,
        "unique_prods": 60,
        "cluster": 2
      },
      {
        "id": 13209,
        "spending": 5891.61,
        "orders": 8,
        "quantity": 4253,
        "order_value": 736.45,
        "unique_prods": 255,
        "cluster": 0
      },
      {
        "id": 17320,
        "spending": 1200.62,
        "orders": 3,
        "quantity": 634,
        "order_value": 400.21,
        "unique_prods": 57,
        "cluster": 2
      },
      {
        "id": 12541,
        "spending": 981.18,
        "orders": 3,
        "quantity": 680,
        "order_value": 327.06,
        "unique_prods": 46,
        "cluster": 2
      },
      {
        "id": 17119,
        "spending": 606.91,
        "orders": 2,
        "quantity": 334,
        "order_value": 303.45,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 17769,
        "spending": 3997.98,
        "orders": 10,
        "quantity": 1862,
        "order_value": 399.8,
        "unique_prods": 200,
        "cluster": 0
      },
      {
        "id": 14792,
        "spending": 6.2,
        "orders": 1,
        "quantity": 2,
        "order_value": 6.2,
        "unique_prods": 2,
        "cluster": 1
      },
      {
        "id": 13626,
        "spending": 257.23,
        "orders": 1,
        "quantity": 209,
        "order_value": 257.23,
        "unique_prods": 19,
        "cluster": 1
      },
      {
        "id": 16553,
        "spending": 5719.82,
        "orders": 12,
        "quantity": 4600,
        "order_value": 476.65,
        "unique_prods": 62,
        "cluster": 0
      },
      {
        "id": 12708,
        "spending": 2712.91,
        "orders": 10,
        "quantity": 1307,
        "order_value": 271.29,
        "unique_prods": 86,
        "cluster": 0
      },
      {
        "id": 12462,
        "spending": 1189.59,
        "orders": 2,
        "quantity": 536,
        "order_value": 594.8,
        "unique_prods": 51,
        "cluster": 2
      },
      {
        "id": 18101,
        "spending": 223.65,
        "orders": 2,
        "quantity": 88,
        "order_value": 111.82,
        "unique_prods": 37,
        "cluster": 1
      },
      {
        "id": 12642,
        "spending": 1013.26,
        "orders": 3,
        "quantity": 552,
        "order_value": 337.75,
        "unique_prods": 39,
        "cluster": 2
      },
      {
        "id": 17783,
        "spending": 283.47,
        "orders": 2,
        "quantity": 354,
        "order_value": 141.73,
        "unique_prods": 67,
        "cluster": 2
      },
      {
        "id": 15774,
        "spending": 270.8,
        "orders": 1,
        "quantity": 87,
        "order_value": 270.8,
        "unique_prods": 25,
        "cluster": 1
      },
      {
        "id": 15483,
        "spending": 233.81,
        "orders": 4,
        "quantity": 295,
        "order_value": 58.45,
        "unique_prods": 74,
        "cluster": 1
      },
      {
        "id": 15687,
        "spending": 2993.1,
        "orders": 9,
        "quantity": 1310,
        "order_value": 332.57,
        "unique_prods": 119,
        "cluster": 0
      },
      {
        "id": 14267,
        "spending": 1516.24,
        "orders": 3,
        "quantity": 530,
        "order_value": 505.41,
        "unique_prods": 25,
        "cluster": 2
      },
      {
        "id": 15358,
        "spending": 8347.2,
        "orders": 22,
        "quantity": 7050,
        "order_value": 379.42,
        "unique_prods": 292,
        "cluster": 0
      },
      {
        "id": 18145,
        "spending": 2861.55,
        "orders": 4,
        "quantity": 2625,
        "order_value": 715.39,
        "unique_prods": 174,
        "cluster": 0
      },
      {
        "id": 17707,
        "spending": 152.4,
        "orders": 2,
        "quantity": 144,
        "order_value": 76.2,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 16340,
        "spending": 549.07,
        "orders": 1,
        "quantity": 501,
        "order_value": 549.07,
        "unique_prods": 124,
        "cluster": 2
      },
      {
        "id": 12948,
        "spending": 2064.95,
        "orders": 7,
        "quantity": 1080,
        "order_value": 294.99,
        "unique_prods": 82,
        "cluster": 0
      },
      {
        "id": 16374,
        "spending": 473.03,
        "orders": 2,
        "quantity": 240,
        "order_value": 236.51,
        "unique_prods": 101,
        "cluster": 2
      },
      {
        "id": 16728,
        "spending": 1054.67,
        "orders": 4,
        "quantity": 677,
        "order_value": 263.67,
        "unique_prods": 218,
        "cluster": 0
      },
      {
        "id": 14354,
        "spending": 163.62,
        "orders": 2,
        "quantity": 210,
        "order_value": 81.81,
        "unique_prods": 9,
        "cluster": 1
      },
      {
        "id": 15655,
        "spending": 560.67,
        "orders": 1,
        "quantity": 324,
        "order_value": 560.67,
        "unique_prods": 34,
        "cluster": 2
      },
      {
        "id": 16746,
        "spending": 6697.66,
        "orders": 18,
        "quantity": 4665,
        "order_value": 372.09,
        "unique_prods": 234,
        "cluster": 0
      },
      {
        "id": 12380,
        "spending": 2724.81,
        "orders": 4,
        "quantity": 1127,
        "order_value": 681.2,
        "unique_prods": 77,
        "cluster": 0
      },
      {
        "id": 13684,
        "spending": 67.23,
        "orders": 1,
        "quantity": 39,
        "order_value": 67.23,
        "unique_prods": 29,
        "cluster": 1
      },
      {
        "id": 14804,
        "spending": 353.27,
        "orders": 1,
        "quantity": 121,
        "order_value": 353.27,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 17019,
        "spending": 1272.61,
        "orders": 4,
        "quantity": 827,
        "order_value": 318.15,
        "unique_prods": 166,
        "cluster": 0
      },
      {
        "id": 16866,
        "spending": 207.74,
        "orders": 3,
        "quantity": 60,
        "order_value": 69.25,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 12569,
        "spending": 4124.69,
        "orders": 32,
        "quantity": 1801,
        "order_value": 128.9,
        "unique_prods": 92,
        "cluster": 0
      },
      {
        "id": 16616,
        "spending": 500.42,
        "orders": 2,
        "quantity": 370,
        "order_value": 250.21,
        "unique_prods": 31,
        "cluster": 2
      },
      {
        "id": 14715,
        "spending": 867.38,
        "orders": 4,
        "quantity": 521,
        "order_value": 216.85,
        "unique_prods": 60,
        "cluster": 2
      },
      {
        "id": 14443,
        "spending": 1420.2,
        "orders": 4,
        "quantity": 938,
        "order_value": 355.05,
        "unique_prods": 84,
        "cluster": 0
      },
      {
        "id": 18154,
        "spending": 399.19,
        "orders": 2,
        "quantity": 255,
        "order_value": 199.59,
        "unique_prods": 15,
        "cluster": 2
      },
      {
        "id": 18048,
        "spending": 172.29,
        "orders": 2,
        "quantity": 127,
        "order_value": 86.15,
        "unique_prods": 6,
        "cluster": 1
      },
      {
        "id": 13826,
        "spending": 189.5,
        "orders": 1,
        "quantity": 82,
        "order_value": 189.5,
        "unique_prods": 10,
        "cluster": 1
      },
      {
        "id": 15858,
        "spending": 1438.85,
        "orders": 5,
        "quantity": 1167,
        "order_value": 287.77,
        "unique_prods": 145,
        "cluster": 0
      },
      {
        "id": 15287,
        "spending": 486.69,
        "orders": 2,
        "quantity": 433,
        "order_value": 243.34,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 12435,
        "spending": 7829.89,
        "orders": 2,
        "quantity": 2055,
        "order_value": 3914.95,
        "unique_prods": 31,
        "cluster": 0
      },
      {
        "id": 12921,
        "spending": 16587.09,
        "orders": 37,
        "quantity": 9526,
        "order_value": 448.3,
        "unique_prods": 233,
        "cluster": 0
      },
      {
        "id": 14191,
        "spending": 4684.76,
        "orders": 13,
        "quantity": 3662,
        "order_value": 360.37,
        "unique_prods": 145,
        "cluster": 0
      },
      {
        "id": 13752,
        "spending": 1186.28,
        "orders": 6,
        "quantity": 876,
        "order_value": 197.71,
        "unique_prods": 64,
        "cluster": 0
      },
      {
        "id": 15006,
        "spending": 502.09,
        "orders": 1,
        "quantity": 302,
        "order_value": 502.09,
        "unique_prods": 121,
        "cluster": 2
      },
      {
        "id": 14264,
        "spending": 333.97,
        "orders": 2,
        "quantity": 70,
        "order_value": 166.99,
        "unique_prods": 15,
        "cluster": 1
      },
      {
        "id": 14152,
        "spending": 621.29,
        "orders": 2,
        "quantity": 711,
        "order_value": 310.64,
        "unique_prods": 47,
        "cluster": 2
      },
      {
        "id": 14004,
        "spending": 4582.64,
        "orders": 7,
        "quantity": 2668,
        "order_value": 654.66,
        "unique_prods": 102,
        "cluster": 0
      },
      {
        "id": 18096,
        "spending": 911.15,
        "orders": 3,
        "quantity": 825,
        "order_value": 303.72,
        "unique_prods": 157,
        "cluster": 2
      },
      {
        "id": 12412,
        "spending": 1226.88,
        "orders": 3,
        "quantity": 829,
        "order_value": 408.96,
        "unique_prods": 43,
        "cluster": 2
      },
      {
        "id": 12855,
        "spending": 38.1,
        "orders": 1,
        "quantity": 30,
        "order_value": 38.1,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 17716,
        "spending": 5655.99,
        "orders": 11,
        "quantity": 3072,
        "order_value": 514.18,
        "unique_prods": 171,
        "cluster": 0
      },
      {
        "id": 12909,
        "spending": 2178.67,
        "orders": 5,
        "quantity": 1280,
        "order_value": 435.73,
        "unique_prods": 78,
        "cluster": 0
      },
      {
        "id": 15103,
        "spending": 703.36,
        "orders": 2,
        "quantity": 329,
        "order_value": 351.68,
        "unique_prods": 35,
        "cluster": 2
      },
      {
        "id": 13848,
        "spending": 1255.0,
        "orders": 3,
        "quantity": 3700,
        "order_value": 418.33,
        "unique_prods": 3,
        "cluster": 2
      },
      {
        "id": 17678,
        "spending": 298.11,
        "orders": 1,
        "quantity": 207,
        "order_value": 298.11,
        "unique_prods": 16,
        "cluster": 2
      },
      {
        "id": 13091,
        "spending": 345.82,
        "orders": 1,
        "quantity": 466,
        "order_value": 345.82,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 17881,
        "spending": 133.35,
        "orders": 1,
        "quantity": 32,
        "order_value": 133.35,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 17489,
        "spending": 376.64,
        "orders": 2,
        "quantity": 428,
        "order_value": 188.32,
        "unique_prods": 28,
        "cluster": 2
      },
      {
        "id": 15189,
        "spending": 16225.39,
        "orders": 41,
        "quantity": 6149,
        "order_value": 395.74,
        "unique_prods": 80,
        "cluster": 0
      },
      {
        "id": 12377,
        "spending": 1628.12,
        "orders": 2,
        "quantity": 944,
        "order_value": 814.06,
        "unique_prods": 72,
        "cluster": 2
      },
      {
        "id": 17262,
        "spending": 1253.36,
        "orders": 5,
        "quantity": 367,
        "order_value": 250.67,
        "unique_prods": 9,
        "cluster": 2
      },
      {
        "id": 18226,
        "spending": 5228.05,
        "orders": 11,
        "quantity": 3466,
        "order_value": 475.28,
        "unique_prods": 141,
        "cluster": 0
      },
      {
        "id": 12612,
        "spending": 704.04,
        "orders": 1,
        "quantity": 262,
        "order_value": 704.04,
        "unique_prods": 19,
        "cluster": 2
      },
      {
        "id": 12928,
        "spending": 2062.7,
        "orders": 5,
        "quantity": 1472,
        "order_value": 412.54,
        "unique_prods": 59,
        "cluster": 0
      },
      {
        "id": 15574,
        "spending": 702.25,
        "orders": 4,
        "quantity": 349,
        "order_value": 175.56,
        "unique_prods": 131,
        "cluster": 2
      },
      {
        "id": 14731,
        "spending": 380.02,
        "orders": 3,
        "quantity": 256,
        "order_value": 126.67,
        "unique_prods": 38,
        "cluster": 2
      },
      {
        "id": 17100,
        "spending": 971.74,
        "orders": 2,
        "quantity": 800,
        "order_value": 485.87,
        "unique_prods": 65,
        "cluster": 2
      },
      {
        "id": 15473,
        "spending": 1771.2,
        "orders": 7,
        "quantity": 672,
        "order_value": 253.03,
        "unique_prods": 4,
        "cluster": 2
      },
      {
        "id": 16473,
        "spending": 316.11,
        "orders": 3,
        "quantity": 196,
        "order_value": 105.37,
        "unique_prods": 18,
        "cluster": 1
      },
      {
        "id": 17857,
        "spending": 26879.04,
        "orders": 23,
        "quantity": 19256,
        "order_value": 1168.65,
        "unique_prods": 19,
        "cluster": 0
      },
      {
        "id": 15844,
        "spending": 130.74,
        "orders": 1,
        "quantity": 134,
        "order_value": 130.74,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 13792,
        "spending": 195.55,
        "orders": 2,
        "quantity": 92,
        "order_value": 97.77,
        "unique_prods": 13,
        "cluster": 1
      },
      {
        "id": 12739,
        "spending": 1013.04,
        "orders": 2,
        "quantity": 486,
        "order_value": 506.52,
        "unique_prods": 38,
        "cluster": 2
      },
      {
        "id": 16464,
        "spending": 1314.68,
        "orders": 3,
        "quantity": 963,
        "order_value": 438.23,
        "unique_prods": 152,
        "cluster": 0
      },
      {
        "id": 13508,
        "spending": 110.97,
        "orders": 1,
        "quantity": 24,
        "order_value": 110.97,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 13216,
        "spending": 333.74,
        "orders": 1,
        "quantity": 297,
        "order_value": 333.74,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 18192,
        "spending": 957.97,
        "orders": 1,
        "quantity": 339,
        "order_value": 957.97,
        "unique_prods": 45,
        "cluster": 2
      },
      {
        "id": 16769,
        "spending": 380.39,
        "orders": 1,
        "quantity": 83,
        "order_value": 380.39,
        "unique_prods": 33,
        "cluster": 2
      },
      {
        "id": 17321,
        "spending": 700.86,
        "orders": 2,
        "quantity": 373,
        "order_value": 350.43,
        "unique_prods": 94,
        "cluster": 2
      },
      {
        "id": 17976,
        "spending": 353.19,
        "orders": 1,
        "quantity": 106,
        "order_value": 353.19,
        "unique_prods": 56,
        "cluster": 2
      },
      {
        "id": 14357,
        "spending": 225.77,
        "orders": 1,
        "quantity": 148,
        "order_value": 225.77,
        "unique_prods": 39,
        "cluster": 2
      },
      {
        "id": 14770,
        "spending": 876.42,
        "orders": 2,
        "quantity": 490,
        "order_value": 438.21,
        "unique_prods": 49,
        "cluster": 2
      },
      {
        "id": 13037,
        "spending": 881.07,
        "orders": 3,
        "quantity": 431,
        "order_value": 293.69,
        "unique_prods": 44,
        "cluster": 2
      },
      {
        "id": 18189,
        "spending": 1090.24,
        "orders": 2,
        "quantity": 566,
        "order_value": 545.12,
        "unique_prods": 65,
        "cluster": 2
      },
      {
        "id": 12500,
        "spending": 4257.82,
        "orders": 11,
        "quantity": 2678,
        "order_value": 387.07,
        "unique_prods": 34,
        "cluster": 0
      },
      {
        "id": 16940,
        "spending": 3049.88,
        "orders": 3,
        "quantity": 2169,
        "order_value": 1016.63,
        "unique_prods": 226,
        "cluster": 0
      },
      {
        "id": 14785,
        "spending": 77.4,
        "orders": 2,
        "quantity": 84,
        "order_value": 38.7,
        "unique_prods": 2,
        "cluster": 1
      },
      {
        "id": 12402,
        "spending": 225.6,
        "orders": 1,
        "quantity": 94,
        "order_value": 225.6,
        "unique_prods": 11,
        "cluster": 1
      },
      {
        "id": 12703,
        "spending": 283.55,
        "orders": 1,
        "quantity": 164,
        "order_value": 283.55,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 14300,
        "spending": 43.2,
        "orders": 1,
        "quantity": 32,
        "order_value": 43.2,
        "unique_prods": 3,
        "cluster": 1
      },
      {
        "id": 13395,
        "spending": 307.72,
        "orders": 1,
        "quantity": 336,
        "order_value": 307.72,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 17350,
        "spending": 1286.07,
        "orders": 4,
        "quantity": 795,
        "order_value": 321.52,
        "unique_prods": 66,
        "cluster": 2
      },
      {
        "id": 12790,
        "spending": 324.92,
        "orders": 1,
        "quantity": 166,
        "order_value": 324.92,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 13705,
        "spending": 711.86,
        "orders": 3,
        "quantity": 363,
        "order_value": 237.29,
        "unique_prods": 25,
        "cluster": 2
      },
      {
        "id": 17324,
        "spending": 990.23,
        "orders": 4,
        "quantity": 844,
        "order_value": 247.56,
        "unique_prods": 43,
        "cluster": 2
      },
      {
        "id": 18250,
        "spending": 349.27,
        "orders": 1,
        "quantity": 199,
        "order_value": 349.27,
        "unique_prods": 21,
        "cluster": 2
      },
      {
        "id": 15630,
        "spending": 1186.35,
        "orders": 2,
        "quantity": 800,
        "order_value": 593.17,
        "unique_prods": 57,
        "cluster": 2
      },
      {
        "id": 15152,
        "spending": 4745.69,
        "orders": 13,
        "quantity": 2704,
        "order_value": 365.05,
        "unique_prods": 196,
        "cluster": 0
      },
      {
        "id": 14690,
        "spending": 371.7,
        "orders": 2,
        "quantity": 170,
        "order_value": 185.85,
        "unique_prods": 40,
        "cluster": 2
      },
      {
        "id": 13047,
        "spending": 3237.54,
        "orders": 10,
        "quantity": 1391,
        "order_value": 323.75,
        "unique_prods": 106,
        "cluster": 0
      },
      {
        "id": 14412,
        "spending": 770.03,
        "orders": 2,
        "quantity": 786,
        "order_value": 385.02,
        "unique_prods": 43,
        "cluster": 2
      },
      {
        "id": 14618,
        "spending": 553.44,
        "orders": 3,
        "quantity": 264,
        "order_value": 184.48,
        "unique_prods": 10,
        "cluster": 2
      },
      {
        "id": 16966,
        "spending": 2154.97,
        "orders": 7,
        "quantity": 1981,
        "order_value": 307.85,
        "unique_prods": 8,
        "cluster": 0
      },
      {
        "id": 14403,
        "spending": 1475.81,
        "orders": 4,
        "quantity": 519,
        "order_value": 368.95,
        "unique_prods": 17,
        "cluster": 2
      },
      {
        "id": 18167,
        "spending": 1384.86,
        "orders": 3,
        "quantity": 382,
        "order_value": 461.62,
        "unique_prods": 24,
        "cluster": 2
      },
      {
        "id": 12659,
        "spending": 91.68,
        "orders": 1,
        "quantity": 105,
        "order_value": 91.68,
        "unique_prods": 5,
        "cluster": 1
      },
      {
        "id": 15027,
        "spending": 1066.15,
        "orders": 4,
        "quantity": 565,
        "order_value": 266.54,
        "unique_prods": 30,
        "cluster": 2
      },
      {
        "id": 17912,
        "spending": 311.01,
        "orders": 5,
        "quantity": 185,
        "order_value": 62.2,
        "unique_prods": 35,
        "cluster": 1
      },
      {
        "id": 15107,
        "spending": 319.5,
        "orders": 6,
        "quantity": 169,
        "order_value": 53.25,
        "unique_prods": 12,
        "cluster": 1
      },
      {
        "id": 16909,
        "spending": 379.14,
        "orders": 1,
        "quantity": 436,
        "order_value": 379.14,
        "unique_prods": 18,
        "cluster": 2
      },
      {
        "id": 13203,
        "spending": 869.46,
        "orders": 4,
        "quantity": 800,
        "order_value": 217.36,
        "unique_prods": 56,
        "cluster": 2
      },
      {
        "id": 14931,
        "spending": 1257.68,
        "orders": 5,
        "quantity": 417,
        "order_value": 251.54,
        "unique_prods": 30,
        "cluster": 2
      },
      {
        "id": 15334,
        "spending": 351.67,
        "orders": 3,
        "quantity": 274,
        "order_value": 117.22,
        "unique_prods": 67,
        "cluster": 2
      },
      {
        "id": 13420,
        "spending": 159.85,
        "orders": 2,
        "quantity": 101,
        "order_value": 79.92,
        "unique_prods": 8,
        "cluster": 1
      },
      {
        "id": 14723,
        "spending": 1158.3,
        "orders": 6,
        "quantity": 695,
        "order_value": 193.05,
        "unique_prods": 193,
        "cluster": 0
      },
      {
        "id": 16011,
        "spending": 3362.71,
        "orders": 16,
        "quantity": 2042,
        "order_value": 210.17,
        "unique_prods": 99,
        "cluster": 0
      },
      {
        "id": 16222,
        "spending": 846.72,
        "orders": 1,
        "quantity": 365,
        "order_value": 846.72,
        "unique_prods": 120,
        "cluster": 2
      },
      {
        "id": 12705,
        "spending": 6868.29,
        "orders": 9,
        "quantity": 3997,
        "order_value": 763.14,
        "unique_prods": 228,
        "cluster": 0
      },
      {
        "id": 15860,
        "spending": 977.21,
        "orders": 8,
        "quantity": 440,
        "order_value": 122.15,
        "unique_prods": 105,
        "cluster": 0
      },
      {
        "id": 13941,
        "spending": 5112.96,
        "orders": 5,
        "quantity": 2364,
        "order_value": 1022.59,
        "unique_prods": 24,
        "cluster": 0
      },
      {
        "id": 18015,
        "spending": 120.03,
        "orders": 1,
        "quantity": 157,
        "order_value": 120.03,
        "unique_prods": 46,
        "cluster": 1
      },
      {
        "id": 18205,
        "spending": 517.36,
        "orders": 2,
        "quantity": 192,
        "order_value": 258.68,
        "unique_prods": 30,
        "cluster": 2
      }
    ],
    "scaler_mean": [
      6.5936,
      1.3456,
      5.9862,
      5.6511,
      3.5516
    ],
    "scaler_std": [
      1.2574,
      0.683,
      1.3699,
      0.7447,
      1.1314
    ]
  },
  "lab8_hierarchical": {
    "linkages_benchmark": [
      {
        "linkage": "Ward",
        "silhouette": 0.1971,
        "clusters": 4,
        "sizes": [
          64,
          21,
          92,
          123
        ],
        "merge_steps": [
          7.323,
          7.816,
          8.982,
          10.737,
          10.76,
          12.266,
          15.337,
          15.46,
          15.598,
          23.365,
          34.389,
          38.347,
          40.001,
          43.864,
          75.206
        ]
      },
      {
        "linkage": "Complete",
        "silhouette": 0.2345,
        "clusters": 4,
        "sizes": [
          60,
          201,
          18,
          21
        ],
        "merge_steps": [
          2.623,
          2.632,
          2.707,
          2.91,
          3.072,
          3.288,
          3.307,
          3.443,
          3.487,
          4.133,
          4.158,
          4.804,
          4.821,
          4.876,
          5.291
        ]
      },
      {
        "linkage": "Average",
        "silhouette": 0.283,
        "clusters": 4,
        "sizes": [
          1,
          2,
          288,
          9
        ],
        "merge_steps": [
          1.852,
          1.892,
          1.977,
          2.016,
          2.08,
          2.138,
          2.188,
          2.197,
          2.577,
          3.03,
          3.12,
          3.207,
          3.379,
          3.662,
          3.806
        ]
      },
      {
        "linkage": "Single",
        "silhouette": 0.5436,
        "clusters": 4,
        "sizes": [
          1,
          1,
          3,
          295
        ],
        "merge_steps": [
          0.983,
          0.984,
          1.005,
          1.055,
          1.084,
          1.172,
          1.212,
          1.23,
          1.236,
          1.372,
          1.389,
          1.601,
          1.706,
          1.712,
          1.908
        ]
      }
    ],
    "ward_profiles": [
      {
        "cluster": 1,
        "size": 64,
        "avg_spending": 604.35,
        "avg_orders": 2.75,
        "avg_quantity": 350.17,
        "avg_order_value": 226.86
      },
      {
        "cluster": 2,
        "size": 21,
        "avg_spending": 17837.75,
        "avg_orders": 29.76,
        "avg_quantity": 12052.76,
        "avg_order_value": 572.15
      },
      {
        "cluster": 3,
        "size": 92,
        "avg_spending": 254.97,
        "avg_orders": 1.27,
        "avg_quantity": 155.11,
        "avg_order_value": 224.57
      },
      {
        "cluster": 4,
        "size": 123,
        "avg_spending": 1793.94,
        "avg_orders": 4.09,
        "avg_quantity": 1110.89,
        "avg_order_value": 547.97
      }
    ],
    "sample_points": [
      {
        "spending": 131.94,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 477.79,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1054.73,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1313.1,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1432.0,
        "orders": 1,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1093.65,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 383.7,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 229.33,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 982.07,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 559.87,
        "orders": 1,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2552.86,
        "orders": 7,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 81024.84,
        "orders": 63,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 0
      },
      {
        "spending": 1132.13,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 97.97,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2024.45,
        "orders": 2,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2044.87,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 495.77,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1869.82,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1542.08,
        "orders": 1,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 157.9,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 10504.49,
        "orders": 17,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 3536.82,
        "orders": 3,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 285.89,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2465.48,
        "orders": 8,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2515.84,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 325.75,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 3281.63,
        "orders": 4,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 439.66,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2656.13,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 415.2,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 430.94,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1021.58,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 541.53,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 344.33,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 183.44,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2004.02,
        "orders": 11,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 18641.01,
        "orders": 30,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 3
      },
      {
        "spending": 1236.54,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1160.07,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2340.84,
        "orders": 8,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 4757.16,
        "orders": 11,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 338.8,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 885.04,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 183.6,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1421.61,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 375.69,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 302.1,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 877.44,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 216.21,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2053.02,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 596.85,
        "orders": 2,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1266.97,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 468.41,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 221.27,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1791.56,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 204.5,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1025.44,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 9261.52,
        "orders": 16,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1316.66,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2027.5,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 388.25,
        "orders": 2,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 194.9,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1095.08,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 508.81,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2248.99,
        "orders": 10,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 365.45,
        "orders": 2,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1842.14,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 8508.82,
        "orders": 55,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 3
      },
      {
        "spending": 3506.54,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 712.78,
        "orders": 1,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 467.51,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 8476.57,
        "orders": 15,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 351.65,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 185.65,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 679.45,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 530.15,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 5059.32,
        "orders": 5,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1429.64,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 701.23,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 301.72,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 382.06,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 287.62,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 529.73,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 427.8,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 349.83,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 26626.8,
        "orders": 22,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 1
      },
      {
        "spending": 123.1,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 337.44,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 478.09,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1551.78,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 210.31,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2207.4,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 777.02,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 567.36,
        "orders": 2,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1335.19,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 343.23,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 595.42,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 6316.57,
        "orders": 28,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 3
      },
      {
        "spending": 605.8,
        "orders": 4,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2273.18,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 4396.13,
        "orders": 13,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1311.38,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 213.96,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 3160.0,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 380.47,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1998.0,
        "orders": 2,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 714.96,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 623.5,
        "orders": 1,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1674.69,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1018.43,
        "orders": 9,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 372.7,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 777.53,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 333.48,
        "orders": 2,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 349.1,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1133.07,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 201.16,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 725.11,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 6784.19,
        "orders": 10,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 3099.72,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 743.53,
        "orders": 1,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 580.05,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 537.74,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 3466.28,
        "orders": 10,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1839.3,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 345.0,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1504.27,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 134.46,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 797.71,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2128.42,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 859.71,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 423.72,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1474.32,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 138.68,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 605.06,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1353.74,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1344.78,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 242.35,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 656.69,
        "orders": 3,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1072.36,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2107.66,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2607.61,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 817.86,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 945.58,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 762.39,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 346.98,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 716.35,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 483.8,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1593.2,
        "orders": 7,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 4106.44,
        "orders": 10,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 5900.28,
        "orders": 13,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1341.6,
        "orders": 7,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1995.46,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 272.44,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 248.42,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2647.59,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 56.4,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 1,
        "single": 3
      },
      {
        "spending": 901.21,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2238.09,
        "orders": 7,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 551.04,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 5070.35,
        "orders": 12,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 379.35,
        "orders": 3,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 650.43,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 796.03,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 103.3,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1031.41,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2232.49,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 497.56,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 513.7,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 4481.18,
        "orders": 11,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 206.98,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 903.9,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 6748.8,
        "orders": 3,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1043.1,
        "orders": 1,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1521.76,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 172.9,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 409.98,
        "orders": 2,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 279.05,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1945.33,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 271.2,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 265.2,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 302.58,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 189.4,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 272.82,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 702.0,
        "orders": 3,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1706.88,
        "orders": 1,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 4628.75,
        "orders": 3,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 127.84,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 211.32,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 168.0,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 192.85,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 149.64,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 154.95,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 307.4,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 136.04,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 60.7,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 1,
        "single": 3
      },
      {
        "spending": 247.14,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1037.59,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 710.28,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2000.86,
        "orders": 10,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 662.59,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 752.6,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 3165.36,
        "orders": 8,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1112.22,
        "orders": 5,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 187.29,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 90.04,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 5905.64,
        "orders": 8,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 110.92,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 693.33,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 397.29,
        "orders": 2,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1064.07,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 60767.9,
        "orders": 91,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 2
      },
      {
        "spending": 444.68,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2161.35,
        "orders": 9,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1528.09,
        "orders": 8,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 367.93,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 221.97,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 810.57,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 138.6,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1793.58,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 51527.3,
        "orders": 44,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 2
      },
      {
        "spending": 1089.18,
        "orders": 1,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1422.52,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 913.19,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 568.55,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 603.71,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 8052.97,
        "orders": 26,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 3
      },
      {
        "spending": 417.06,
        "orders": 4,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 546.04,
        "orders": 1,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1602.13,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1515.9,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 489.6,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 813.0,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1340.32,
        "orders": 1,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 40991.57,
        "orders": 124,
        "ward": 1,
        "complete": 3,
        "average": 3,
        "single": 2
      },
      {
        "spending": 124.57,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 192.6,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1357.6,
        "orders": 7,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 745.06,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 175.27,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2059.45,
        "orders": 6,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 920.51,
        "orders": 5,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 12601.83,
        "orders": 3,
        "ward": 3,
        "complete": 2,
        "average": 0,
        "single": 3
      },
      {
        "spending": 420.3,
        "orders": 4,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1020.42,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 139.35,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1055.35,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 623.75,
        "orders": 1,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 651.82,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 584.07,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 517.53,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 664.26,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 683.9,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 459.4,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 404.58,
        "orders": 5,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 417.2,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 984.91,
        "orders": 8,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 280.55,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 548.97,
        "orders": 1,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 158.68,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 229.64,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 133.56,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 3945.0,
        "orders": 10,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 981.51,
        "orders": 5,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 635.41,
        "orders": 3,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 224.14,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 110.46,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 116.01,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2794.51,
        "orders": 2,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1498.51,
        "orders": 4,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 698.41,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 272.04,
        "orders": 2,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2740.43,
        "orders": 3,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1837.28,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2103.06,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1174.58,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 804.02,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 205.48,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1135.04,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1126.85,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 4067.29,
        "orders": 4,
        "ward": 3,
        "complete": 2,
        "average": 2,
        "single": 3
      },
      {
        "spending": 416.08,
        "orders": 2,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1213.16,
        "orders": 3,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 3883.25,
        "orders": 11,
        "ward": 1,
        "complete": 3,
        "average": 2,
        "single": 3
      },
      {
        "spending": 503.76,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 915.13,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 665.78,
        "orders": 2,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 329.65,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 529.62,
        "orders": 3,
        "ward": 0,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 226.21,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 2588.77,
        "orders": 10,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 236.26,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 170.32,
        "orders": 1,
        "ward": 2,
        "complete": 0,
        "average": 2,
        "single": 3
      },
      {
        "spending": 396.48,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 529.41,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 1867.68,
        "orders": 9,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 296.7,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 848.55,
        "orders": 1,
        "ward": 3,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 364.6,
        "orders": 1,
        "ward": 2,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 605.06,
        "orders": 4,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      },
      {
        "spending": 511.36,
        "orders": 2,
        "ward": 0,
        "complete": 1,
        "average": 2,
        "single": 3
      }
    ]
  },
  "lab9_apriori": {
    "min_support": 0.02,
    "min_confidence": 0.3,
    "frequent_itemsets_counts": {
      "1-Itemsets": 50,
      "2-Itemsets": 1225
    },
    "top_rules": [
      {
        "ant": "ROSES REGENCY TEACUP AND SAUCER",
        "con": "GREEN REGENCY TEACUP AND SAUCER",
        "support": 0.0537,
        "confidence": 0.7202,
        "lift": 10.16
      },
      {
        "ant": "GREEN REGENCY TEACUP AND SAUCER",
        "con": "ROSES REGENCY TEACUP AND SAUCER",
        "support": 0.0537,
        "confidence": 0.7572,
        "lift": 10.16
      },
      {
        "ant": "ALARM CLOCK BAKELIKE RED",
        "con": "ALARM CLOCK BAKELIKE GREEN",
        "support": 0.0448,
        "confidence": 0.6089,
        "lift": 8.88
      },
      {
        "ant": "ALARM CLOCK BAKELIKE GREEN",
        "con": "ALARM CLOCK BAKELIKE RED",
        "support": 0.0448,
        "confidence": 0.6531,
        "lift": 8.88
      },
      {
        "ant": "RED RETROSPOT CHARLOTTE BAG",
        "con": "CHARLOTTE BAG SUKI DESIGN",
        "support": 0.0355,
        "confidence": 0.4913,
        "lift": 7.96
      },
      {
        "ant": "CHARLOTTE BAG SUKI DESIGN",
        "con": "RED RETROSPOT CHARLOTTE BAG",
        "support": 0.0355,
        "confidence": 0.5748,
        "lift": 7.96
      },
      {
        "ant": "WOODEN PICTURE FRAME WHITE FINISH",
        "con": "WOODEN FRAME ANTIQUE WHITE",
        "support": 0.0377,
        "confidence": 0.49,
        "lift": 7.21
      },
      {
        "ant": "WOODEN FRAME ANTIQUE WHITE",
        "con": "WOODEN PICTURE FRAME WHITE FINISH",
        "support": 0.0377,
        "confidence": 0.5551,
        "lift": 7.21
      },
      {
        "ant": "HEART OF WICKER SMALL",
        "con": "HEART OF WICKER LARGE",
        "support": 0.0345,
        "confidence": 0.4105,
        "lift": 6.34
      },
      {
        "ant": "HEART OF WICKER LARGE",
        "con": "HEART OF WICKER SMALL",
        "support": 0.0345,
        "confidence": 0.533,
        "lift": 6.34
      },
      {
        "ant": "JUMBO BAG APPLES",
        "con": "JUMBO BAG ALPHABET",
        "support": 0.0274,
        "confidence": 0.3998,
        "lift": 6.31
      },
      {
        "ant": "JUMBO BAG ALPHABET",
        "con": "JUMBO BAG APPLES",
        "support": 0.0274,
        "confidence": 0.4316,
        "lift": 6.31
      },
      {
        "ant": "JUMBO BAG APPLES",
        "con": "JUMBO BAG VINTAGE LEAF",
        "support": 0.0255,
        "confidence": 0.3722,
        "lift": 6.05
      },
      {
        "ant": "JUMBO BAG VINTAGE LEAF",
        "con": "JUMBO BAG APPLES",
        "support": 0.0255,
        "confidence": 0.4141,
        "lift": 6.05
      },
      {
        "ant": "LUNCH BAG SPACEBOY DESIGN",
        "con": "LUNCH BAG WOODLAND",
        "support": 0.0335,
        "confidence": 0.414,
        "lift": 5.82
      },
      {
        "ant": "LUNCH BAG WOODLAND",
        "con": "LUNCH BAG SPACEBOY DESIGN",
        "support": 0.0335,
        "confidence": 0.471,
        "lift": 5.82
      },
      {
        "ant": "LUNCH BAG CARS BLUE",
        "con": "LUNCH BAG PINK POLKADOT",
        "support": 0.0351,
        "confidence": 0.4365,
        "lift": 5.72
      },
      {
        "ant": "LUNCH BAG PINK POLKADOT",
        "con": "LUNCH BAG CARS BLUE",
        "support": 0.0351,
        "confidence": 0.4606,
        "lift": 5.72
      },
      {
        "ant": "LUNCH BAG SUKI DESIGN",
        "con": "LUNCH BAG APPLE DESIGN",
        "support": 0.0314,
        "confidence": 0.4142,
        "lift": 5.71
      },
      {
        "ant": "LUNCH BAG APPLE DESIGN",
        "con": "LUNCH BAG SUKI DESIGN",
        "support": 0.0314,
        "confidence": 0.4334,
        "lift": 5.71
      },
      {
        "ant": "JUMBO BAG ALPHABET",
        "con": "JUMBO BAG VINTAGE LEAF",
        "support": 0.0222,
        "confidence": 0.3499,
        "lift": 5.69
      },
      {
        "ant": "JUMBO BAG VINTAGE LEAF",
        "con": "JUMBO BAG ALPHABET",
        "support": 0.0222,
        "confidence": 0.3606,
        "lift": 5.69
      },
      {
        "ant": "LUNCH BAG  BLACK SKULL.",
        "con": "LUNCH BAG PINK POLKADOT",
        "support": 0.0381,
        "confidence": 0.4273,
        "lift": 5.6
      },
      {
        "ant": "LUNCH BAG PINK POLKADOT",
        "con": "LUNCH BAG  BLACK SKULL.",
        "support": 0.0381,
        "confidence": 0.4991,
        "lift": 5.6
      },
      {
        "ant": "JUMBO SHOPPER VINTAGE RED PAISLEY",
        "con": "JUMBO  BAG BAROQUE BLACK WHITE",
        "support": 0.0295,
        "confidence": 0.3583,
        "lift": 5.49
      }
    ],
    "total_rules": 125,
    "items_list": [
      "WHITE HANGING HEART T-LIGHT HOLDER",
      "JUMBO BAG RED RETROSPOT",
      "REGENCY CAKESTAND 3 TIER",
      "PARTY BUNTING",
      "LUNCH BAG RED RETROSPOT",
      "ASSORTED COLOUR BIRD ORNAMENT",
      "SET OF 3 CAKE TINS PANTRY DESIGN",
      "PACK OF 72 RETROSPOT CAKE CASES",
      "LUNCH BAG  BLACK SKULL.",
      "NATURAL SLATE HEART CHALKBOARD",
      "JUMBO BAG PINK POLKADOT",
      "HEART OF WICKER SMALL",
      "JUMBO STORAGE BAG SUKI",
      "JUMBO SHOPPER VINTAGE RED PAISLEY",
      "JAM MAKING SET PRINTED",
      "PAPER CHAIN KIT 50'S CHRISTMAS",
      "LUNCH BAG SPACEBOY DESIGN",
      "LUNCH BAG CARS BLUE",
      "SPOTTY BUNTING",
      "JAM MAKING SET WITH JARS",
      "POSTAGE",
      "RECIPE BOX PANTRY YELLOW DESIGN",
      "WOODEN PICTURE FRAME WHITE FINISH",
      "LUNCH BAG PINK POLKADOT",
      "LUNCH BAG SUKI DESIGN",
      "SET OF 4 PANTRY JELLY MOULDS",
      "ROSES REGENCY TEACUP AND SAUCER",
      "ALARM CLOCK BAKELIKE RED",
      "VICTORIAN GLASS HANGING T-LIGHT",
      "LUNCH BAG APPLE DESIGN",
      "RED RETROSPOT CHARLOTTE BAG",
      "LUNCH BAG WOODLAND",
      "GREEN REGENCY TEACUP AND SAUCER",
      "RABBIT NIGHT LIGHT",
      "SET/20 RED RETROSPOT PAPER NAPKINS",
      "ALARM CLOCK BAKELIKE GREEN",
      "JUMBO BAG APPLES",
      "WOODEN FRAME ANTIQUE WHITE",
      "RETROSPOT TEA SET CERAMIC 11 PC",
      "6 RIBBONS RUSTIC CHARM",
      "BAKING SET 9 PIECE RETROSPOT",
      "JUMBO  BAG BAROQUE BLACK WHITE",
      "VINTAGE SNAP CARDS",
      "HEART OF WICKER LARGE",
      "GARDENERS KNEELING PAD KEEP CALM",
      "JUMBO BAG ALPHABET",
      "SPACEBOY LUNCH BOX",
      "CHARLOTTE BAG SUKI DESIGN",
      "SET/5 RED RETROSPOT LID GLASS BOWLS",
      "JUMBO BAG VINTAGE LEAF"
    ],
    "baskets_sample": [
      [
        0
      ],
      [
        5
      ],
      [
        19
      ],
      [
        35,
        27,
        20,
        46
      ],
      [
        15
      ],
      [
        0,
        37,
        22
      ],
      [
        0,
        37,
        22
      ],
      [
        4,
        7,
        41,
        10,
        12
      ],
      [
        14
      ],
      [
        13,
        38,
        15
      ],
      [
        35,
        13
      ],
      [
        9,
        11,
        43
      ],
      [
        19,
        14
      ],
      [
        41,
        1
      ],
      [
        11
      ],
      [
        27,
        35
      ],
      [
        0,
        1,
        34,
        14,
        19
      ],
      [
        5
      ],
      [
        0
      ],
      [
        35,
        27,
        5,
        7
      ],
      [
        0,
        37,
        22
      ],
      [
        0,
        4,
        14,
        16,
        23,
        31
      ],
      [
        15
      ],
      [
        20
      ],
      [
        8,
        17,
        11,
        7
      ],
      [
        48
      ],
      [
        0,
        37,
        22
      ],
      [
        28,
        5,
        7
      ],
      [
        1,
        12
      ],
      [
        4,
        39,
        8,
        46,
        14,
        16,
        17,
        15
      ],
      [
        7,
        42,
        11,
        43,
        14,
        15
      ],
      [
        37
      ],
      [
        14
      ],
      [
        5
      ],
      [
        1,
        5,
        7,
        41,
        10,
        15,
        19
      ],
      [
        19,
        14
      ],
      [
        2,
        13
      ],
      [
        19,
        14
      ],
      [
        0,
        2,
        5
      ],
      [
        0,
        11,
        43
      ],
      [
        48,
        1,
        12
      ],
      [
        26
      ],
      [
        32
      ],
      [
        2
      ],
      [
        1,
        13
      ],
      [
        20
      ],
      [
        2,
        39,
        13,
        14,
        19
      ],
      [
        26,
        2,
        13
      ],
      [
        35,
        27,
        15
      ],
      [
        34,
        21,
        14,
        7
      ],
      [
        5
      ],
      [
        2
      ],
      [
        11,
        9,
        43,
        15
      ],
      [
        2
      ],
      [
        47
      ],
      [
        0,
        1,
        8,
        41,
        10,
        12,
        13,
        16
      ],
      [
        0,
        1,
        2,
        4,
        7,
        9,
        11,
        14,
        15,
        19,
        21,
        23,
        26,
        27,
        28,
        30,
        32,
        34,
        39,
        42,
        43,
        46,
        47,
        48
      ],
      [
        48,
        46
      ],
      [
        43,
        21
      ],
      [
        19
      ],
      [
        2
      ],
      [
        15
      ],
      [
        9
      ],
      [
        41,
        42
      ],
      [
        11
      ],
      [
        28
      ],
      [
        0,
        1
      ],
      [
        8,
        1,
        0
      ],
      [
        4
      ],
      [
        35
      ],
      [
        8
      ],
      [
        1
      ],
      [
        35
      ],
      [
        42,
        47
      ],
      [
        19,
        21,
        14
      ],
      [
        0,
        9
      ],
      [
        10
      ],
      [
        0,
        1,
        2,
        4,
        5,
        7,
        8,
        10,
        11,
        12,
        13,
        14,
        15,
        17,
        21,
        26,
        28,
        30,
        32,
        35,
        37,
        39,
        42,
        47,
        48
      ],
      [
        0
      ],
      [
        23,
        31,
        15
      ],
      [
        28
      ],
      [
        35,
        27
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        0,
        13
      ],
      [
        9,
        14
      ],
      [
        0,
        1,
        2,
        5,
        9,
        10
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        42
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        42
      ],
      [
        19,
        14
      ],
      [
        14,
        7
      ],
      [
        42
      ],
      [
        32,
        37
      ],
      [
        35,
        7,
        48,
        26,
        27
      ],
      [
        32,
        2,
        26,
        14
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        1,
        10,
        12,
        14
      ],
      [
        19,
        14,
        15
      ],
      [
        8,
        9,
        34,
        37
      ],
      [
        14
      ],
      [
        15
      ],
      [
        19,
        14,
        7
      ],
      [
        11
      ],
      [
        14
      ],
      [
        13
      ],
      [
        1
      ],
      [
        2,
        15
      ],
      [
        11
      ],
      [
        2,
        5
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        16,
        9,
        42
      ],
      [
        2
      ],
      [
        2,
        34,
        7,
        15
      ],
      [
        48,
        34
      ],
      [
        42
      ],
      [
        48
      ],
      [
        21
      ],
      [
        14
      ],
      [
        9,
        5,
        39
      ],
      [
        11,
        43,
        12,
        15,
        48,
        21
      ],
      [
        2
      ],
      [
        39
      ],
      [
        48,
        0,
        5,
        7
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        0,
        13,
        37,
        22
      ],
      [
        8,
        43,
        31,
        23
      ],
      [
        46
      ],
      [
        15
      ],
      [
        37
      ],
      [
        35,
        27,
        14
      ],
      [
        0
      ],
      [
        34,
        35,
        4,
        7,
        8,
        15,
        16,
        47,
        23,
        30
      ],
      [
        19,
        14
      ],
      [
        1
      ],
      [
        11,
        39
      ],
      [
        46,
        7
      ],
      [
        46,
        7
      ],
      [
        2,
        5
      ],
      [
        0,
        37,
        22
      ],
      [
        0,
        37,
        22
      ],
      [
        19,
        35,
        27
      ],
      [
        27,
        35
      ],
      [
        0,
        15
      ],
      [
        17,
        5,
        30,
        39
      ],
      [
        1,
        10,
        12
      ],
      [
        27,
        35,
        19,
        14
      ],
      [
        15
      ],
      [
        32,
        2,
        5
      ],
      [
        2
      ],
      [
        15
      ],
      [
        48
      ],
      [
        34,
        21
      ],
      [
        37
      ],
      [
        0
      ],
      [
        0
      ],
      [
        0,
        43,
        37,
        22
      ],
      [
        5
      ],
      [
        7,
        20,
        14,
        39
      ],
      [
        5,
        39,
        11,
        43,
        30
      ],
      [
        31
      ],
      [
        8,
        4,
        23
      ],
      [
        2,
        37,
        11,
        43,
        48,
        17,
        16,
        21
      ],
      [
        27
      ],
      [
        20
      ],
      [
        32,
        2,
        42,
        19,
        26
      ],
      [
        0
      ],
      [
        20
      ],
      [
        0,
        15
      ],
      [
        20,
        39
      ],
      [
        32,
        1,
        2,
        4,
        9,
        10,
        11,
        28
      ],
      [
        0,
        4,
        8,
        16,
        19,
        23
      ],
      [
        1,
        3,
        4
      ],
      [
        32,
        1,
        3,
        4,
        9,
        42,
        10,
        11,
        43,
        46,
        47,
        19,
        21,
        26,
        30
      ],
      [
        1,
        34,
        19,
        14
      ],
      [
        0,
        1,
        2,
        3,
        4,
        5,
        7,
        8,
        9,
        11,
        12,
        14,
        15,
        16,
        19,
        22,
        23,
        26,
        28,
        30,
        31,
        32,
        35,
        39,
        42,
        43,
        46,
        47
      ],
      [
        41,
        10,
        12,
        30
      ],
      [
        11,
        5,
        15
      ],
      [
        8,
        17,
        4,
        23
      ],
      [
        11,
        13
      ],
      [
        32,
        5,
        7,
        15,
        26
      ],
      [
        34,
        2,
        7
      ],
      [
        2,
        3
      ],
      [
        15
      ],
      [
        1,
        20
      ],
      [
        2
      ],
      [
        14
      ],
      [
        9,
        11
      ],
      [
        4,
        20,
        31
      ],
      [
        2,
        15
      ],
      [
        0,
        41,
        43,
        13
      ],
      [
        34
      ],
      [
        32,
        2,
        26
      ],
      [
        13
      ],
      [
        0,
        2,
        7,
        8,
        11,
        12,
        13,
        15,
        17,
        23,
        27,
        30,
        31,
        34,
        35,
        37,
        38,
        39,
        41,
        47
      ],
      [
        20
      ],
      [
        2
      ],
      [
        43
      ],
      [
        0,
        14
      ],
      [
        13,
        15
      ],
      [
        43,
        12
      ],
      [
        17,
        20,
        31
      ],
      [
        0,
        39,
        43,
        21,
        31
      ],
      [
        32,
        20
      ],
      [
        9,
        37,
        30
      ],
      [
        16,
        17
      ],
      [
        1,
        20,
        47,
        7
      ],
      [
        46
      ],
      [
        5,
        39
      ],
      [
        37
      ],
      [
        2,
        15
      ],
      [
        2
      ],
      [
        27,
        35,
        21,
        46
      ],
      [
        32,
        2,
        11,
        43,
        14,
        21,
        26
      ],
      [
        0
      ],
      [
        11
      ],
      [
        0,
        43,
        11,
        22
      ],
      [
        4,
        39,
        43,
        15,
        31
      ],
      [
        15
      ],
      [
        16,
        42,
        46,
        31
      ],
      [
        0,
        35,
        11,
        43,
        27
      ],
      [
        2,
        21
      ],
      [
        0,
        17,
        11
      ],
      [
        0,
        5,
        37,
        42,
        22
      ],
      [
        16,
        9,
        1,
        15
      ],
      [
        48
      ],
      [
        2,
        35,
        3,
        4,
        17,
        20,
        27,
        31
      ],
      [
        11
      ],
      [
        35,
        46,
        16,
        22,
        27
      ],
      [
        0,
        1,
        7,
        39,
        9,
        10,
        43,
        12,
        15,
        48,
        21,
        30
      ],
      [
        0
      ],
      [
        3,
        21,
        15
      ],
      [
        19,
        27
      ],
      [
        43,
        5,
        15
      ],
      [
        48,
        34
      ],
      [
        1,
        2,
        4,
        39,
        9,
        10,
        12,
        15,
        16,
        17,
        23,
        31
      ],
      [
        4,
        5,
        8,
        9,
        43,
        11,
        47,
        17,
        21,
        30
      ],
      [
        0,
        15
      ],
      [
        2
      ],
      [
        42
      ],
      [
        35,
        27,
        22,
        15
      ],
      [
        11,
        3
      ],
      [
        0,
        1,
        11,
        43,
        12,
        15
      ],
      [
        19
      ],
      [
        1,
        35,
        37,
        41,
        15,
        48,
        21,
        22,
        27
      ],
      [
        46
      ],
      [
        43,
        15
      ],
      [
        32,
        7
      ],
      [
        32,
        35,
        5,
        26,
        27
      ],
      [
        10,
        21,
        14
      ],
      [
        9,
        43
      ],
      [
        47,
        15
      ],
      [
        5
      ],
      [
        20,
        14
      ],
      [
        20
      ],
      [
        7
      ],
      [
        39
      ],
      [
        2,
        39,
        46,
        14,
        48,
        19,
        20,
        30
      ],
      [
        39
      ],
      [
        5
      ],
      [
        11,
        43,
        5
      ],
      [
        19
      ],
      [
        21,
        35,
        5
      ],
      [
        48
      ],
      [
        0,
        5,
        37,
        17,
        22,
        31
      ],
      [
        4,
        9,
        11,
        43,
        21
      ],
      [
        1,
        10,
        14,
        19,
        20
      ],
      [
        34
      ],
      [
        5
      ],
      [
        34
      ],
      [
        34
      ],
      [
        2,
        7,
        42,
        15,
        21
      ],
      [
        2,
        8,
        15,
        17,
        31
      ],
      [
        11
      ],
      [
        0,
        42,
        15
      ],
      [
        15,
        39
      ],
      [
        1,
        34,
        7
      ],
      [
        14
      ],
      [
        48
      ],
      [
        0,
        1,
        2,
        4,
        5,
        7,
        8,
        9,
        11,
        13,
        14,
        15,
        16,
        19,
        21,
        26,
        28,
        30,
        31,
        32,
        35,
        39,
        41,
        42,
        43,
        46,
        47,
        48
      ],
      [
        43,
        11,
        1
      ],
      [
        0,
        5
      ],
      [
        0,
        1,
        2,
        4,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        19,
        21,
        22,
        26,
        28,
        30,
        31,
        32,
        39,
        41,
        42,
        43,
        46,
        47,
        48
      ],
      [
        0,
        43
      ],
      [
        42
      ],
      [
        11
      ],
      [
        12,
        13,
        17,
        20,
        31
      ],
      [
        20
      ],
      [
        26
      ],
      [
        43,
        11,
        39
      ],
      [
        14,
        15
      ],
      [
        1,
        41,
        12,
        13,
        16
      ],
      [
        19
      ],
      [
        15
      ],
      [
        0,
        43
      ],
      [
        32,
        26,
        2
      ],
      [
        0,
        9,
        2,
        11
      ],
      [
        27,
        0,
        35,
        15
      ],
      [
        26,
        13,
        21,
        15
      ],
      [
        19,
        5,
        14
      ],
      [
        9
      ],
      [
        1,
        4,
        8,
        16,
        17,
        23,
        30,
        31
      ],
      [
        15
      ],
      [
        5
      ],
      [
        1,
        2,
        34,
        10,
        12,
        48
      ],
      [
        37
      ],
      [
        1,
        34,
        35,
        12,
        13
      ],
      [
        34,
        15,
        39
      ],
      [
        1,
        10,
        12
      ],
      [
        42,
        27
      ],
      [
        46,
        15
      ],
      [
        32,
        2,
        26
      ],
      [
        48
      ],
      [
        35,
        27,
        15
      ],
      [
        15
      ],
      [
        32,
        2,
        26
      ],
      [
        2
      ],
      [
        0,
        4,
        8,
        9,
        42,
        11,
        43,
        16,
        17,
        23,
        31
      ],
      [
        15
      ],
      [
        9,
        2,
        21,
        15
      ],
      [
        1,
        4,
        8,
        11,
        43,
        12,
        16,
        17,
        21,
        31
      ],
      [
        0,
        5,
        46,
        21,
        28
      ],
      [
        19,
        14
      ],
      [
        0,
        35,
        15
      ],
      [
        32,
        26,
        2,
        5
      ],
      [
        15
      ],
      [
        41,
        12
      ],
      [
        0,
        2,
        37,
        15,
        21
      ],
      [
        41
      ],
      [
        12,
        47
      ],
      [
        2
      ],
      [
        19
      ],
      [
        27,
        42,
        35,
        15
      ],
      [
        0
      ],
      [
        3,
        19,
        34,
        27
      ],
      [
        27,
        2,
        35,
        5
      ],
      [
        34,
        14
      ],
      [
        0,
        28
      ],
      [
        37,
        22
      ],
      [
        47
      ],
      [
        5,
        15
      ],
      [
        0,
        2,
        3,
        4,
        7,
        9,
        11,
        12,
        14,
        15,
        16,
        17,
        19,
        21,
        26,
        27,
        28,
        32,
        34,
        35,
        39,
        42,
        43,
        46,
        47
      ],
      [
        32,
        26
      ],
      [
        3,
        27
      ],
      [
        42,
        2,
        15
      ],
      [
        0,
        22
      ],
      [
        43,
        11
      ],
      [
        0,
        34,
        5
      ],
      [
        0
      ],
      [
        8,
        17,
        34,
        31
      ],
      [
        20,
        14,
        7
      ],
      [
        42,
        5
      ],
      [
        16,
        8,
        43
      ],
      [
        11,
        39
      ],
      [
        16,
        4,
        20
      ],
      [
        2,
        26
      ],
      [
        15
      ],
      [
        1
      ],
      [
        0,
        9,
        43,
        11,
        15,
        22
      ],
      [
        19,
        14
      ],
      [
        0
      ],
      [
        2,
        14
      ],
      [
        27
      ],
      [
        5
      ],
      [
        8,
        41,
        13
      ],
      [
        20
      ],
      [
        21
      ],
      [
        27
      ],
      [
        5
      ],
      [
        43,
        28,
        7
      ],
      [
        0,
        5,
        7
      ],
      [
        0,
        2
      ],
      [
        0,
        39,
        43,
        11,
        15
      ],
      [
        0,
        1,
        10
      ],
      [
        2,
        5,
        9,
        43,
        15,
        28
      ],
      [
        35
      ],
      [
        0,
        11,
        43
      ],
      [
        1,
        35,
        41,
        12,
        13,
        15,
        27
      ],
      [
        1
      ],
      [
        2,
        46,
        7
      ],
      [
        0
      ],
      [
        14
      ],
      [
        21,
        38
      ],
      [
        27,
        35
      ],
      [
        28,
        15
      ],
      [
        43,
        5,
        7
      ],
      [
        14
      ],
      [
        38
      ],
      [
        43,
        38
      ],
      [
        15
      ],
      [
        0,
        1,
        2,
        3,
        4,
        7,
        8,
        9,
        11,
        12,
        14,
        15,
        19,
        21,
        22,
        23,
        26,
        28,
        31,
        32,
        35,
        39,
        41,
        42,
        46,
        47,
        48
      ],
      [
        0,
        34,
        2,
        35,
        37,
        39,
        7,
        41,
        8,
        12,
        13,
        15,
        47,
        17,
        27,
        30,
        31
      ],
      [
        1,
        3,
        4,
        9,
        10,
        11,
        43
      ],
      [
        32,
        1,
        3,
        4,
        9,
        26
      ],
      [
        32,
        1,
        4,
        9,
        10,
        11,
        46,
        14,
        21,
        26,
        30
      ],
      [
        1,
        4,
        10,
        11,
        46,
        14,
        21,
        26
      ],
      [
        2,
        37,
        7,
        39,
        15,
        19,
        31
      ],
      [
        30,
        47
      ],
      [
        11
      ],
      [
        0,
        1,
        19,
        14
      ],
      [
        35,
        27
      ],
      [
        8,
        41,
        13,
        14
      ],
      [
        0
      ],
      [
        0,
        2,
        4,
        7,
        8,
        9,
        10,
        11,
        12,
        14,
        15,
        19,
        21,
        22,
        23,
        26,
        27,
        28,
        31,
        32,
        34,
        35,
        37,
        39,
        42,
        43,
        46,
        48
      ],
      [
        0
      ],
      [
        2,
        35,
        46
      ],
      [
        2,
        37
      ],
      [
        20
      ],
      [
        0,
        34,
        37,
        7,
        42,
        43,
        14,
        30
      ],
      [
        28,
        46
      ],
      [
        17,
        34,
        4,
        7
      ],
      [
        39
      ],
      [
        4,
        23
      ],
      [
        32,
        2,
        26
      ],
      [
        37
      ],
      [
        3,
        5,
        11,
        43,
        21
      ],
      [
        2,
        7
      ],
      [
        20,
        15
      ],
      [
        19,
        14
      ],
      [
        35
      ],
      [
        32,
        2,
        41,
        42,
        13
      ],
      [
        0,
        26,
        38
      ],
      [
        0,
        1
      ],
      [
        37,
        22
      ],
      [
        14
      ],
      [
        11
      ],
      [
        1,
        19,
        30,
        15
      ],
      [
        0,
        5,
        39,
        10,
        43,
        11,
        19
      ],
      [
        1
      ],
      [
        0,
        43,
        37,
        22
      ],
      [
        34,
        15,
        46,
        7
      ],
      [
        0,
        4,
        8,
        9,
        10,
        11,
        13,
        14,
        16,
        19,
        23,
        31
      ],
      [
        2
      ],
      [
        34
      ],
      [
        1,
        5,
        41,
        46,
        15
      ],
      [
        1,
        4,
        8,
        41,
        10,
        12,
        13,
        16,
        23,
        31
      ],
      [
        35,
        37,
        21,
        22,
        27
      ],
      [
        0,
        37,
        22
      ],
      [
        34
      ],
      [
        8
      ],
      [
        2,
        37,
        22
      ],
      [
        8
      ],
      [
        9,
        2
      ],
      [
        11
      ],
      [
        3
      ],
      [
        43
      ],
      [
        4,
        47
      ],
      [
        9,
        20
      ],
      [
        48,
        7
      ],
      [
        48,
        42,
        34
      ],
      [
        0,
        1,
        2,
        3,
        4,
        5,
        7,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        19,
        21,
        22,
        26,
        27,
        28,
        30,
        32,
        35,
        39,
        41,
        42,
        43,
        47
      ],
      [
        34,
        11,
        22,
        30
      ],
      [
        0,
        5,
        14
      ],
      [
        1,
        2,
        15,
        7
      ],
      [
        32,
        2,
        8,
        11,
        43,
        15
      ],
      [
        0,
        37,
        22
      ],
      [
        42
      ],
      [
        41,
        10,
        2,
        1
      ],
      [
        0,
        5
      ],
      [
        0
      ],
      [
        19,
        15
      ],
      [
        4,
        8,
        47,
        16,
        17,
        30,
        31
      ],
      [
        14
      ],
      [
        35,
        5,
        9,
        27,
        28
      ],
      [
        43
      ],
      [
        37
      ],
      [
        1,
        4,
        5,
        14,
        47,
        19
      ],
      [
        39
      ],
      [
        0
      ],
      [
        0
      ],
      [
        34,
        21,
        14,
        7
      ],
      [
        0,
        37
      ],
      [
        27
      ],
      [
        14
      ],
      [
        2
      ],
      [
        9
      ],
      [
        19,
        14
      ],
      [
        32,
        2,
        26
      ],
      [
        2
      ],
      [
        35,
        4,
        5,
        8,
        15,
        16,
        31
      ],
      [
        19,
        14
      ],
      [
        20
      ],
      [
        27,
        20
      ],
      [
        28
      ],
      [
        20
      ],
      [
        0,
        37,
        22
      ],
      [
        5,
        38
      ],
      [
        2,
        11
      ],
      [
        20
      ],
      [
        32,
        0,
        2,
        4,
        8,
        43,
        47,
        48,
        16,
        22,
        23,
        30
      ],
      [
        0
      ],
      [
        20
      ],
      [
        20,
        37
      ],
      [
        19,
        35,
        27,
        20
      ],
      [
        0
      ],
      [
        19
      ],
      [
        20
      ],
      [
        48,
        2,
        7
      ],
      [
        9,
        34,
        7
      ],
      [
        43,
        11
      ],
      [
        11
      ],
      [
        9,
        37,
        22
      ],
      [
        0,
        35,
        3,
        43,
        27
      ],
      [
        0,
        1,
        7,
        11,
        43,
        13,
        17,
        19
      ],
      [
        41,
        10,
        42,
        1
      ],
      [
        0,
        48,
        21,
        15
      ],
      [
        35,
        46
      ],
      [
        0,
        11
      ],
      [
        0,
        34,
        37,
        42,
        22,
        30
      ],
      [
        35
      ],
      [
        34
      ],
      [
        11,
        43,
        14,
        15
      ],
      [
        0,
        1,
        2,
        3,
        4,
        7,
        9,
        10,
        11,
        13,
        14,
        15,
        16,
        21,
        23,
        26,
        27,
        28,
        30,
        31,
        32,
        34,
        35,
        37,
        39,
        42,
        46,
        47,
        48
      ],
      [
        15,
        7
      ],
      [
        34
      ],
      [
        48,
        34,
        7
      ],
      [
        27,
        35,
        5,
        15
      ],
      [
        14
      ],
      [
        0,
        3,
        5,
        14,
        15,
        28
      ],
      [
        4,
        39,
        10,
        14,
        16,
        20,
        31
      ],
      [
        0,
        35,
        3,
        11
      ],
      [
        42
      ],
      [
        47,
        15
      ],
      [
        43
      ],
      [
        1,
        12,
        15
      ],
      [
        0,
        2,
        11,
        37
      ],
      [
        21,
        46
      ],
      [
        32,
        2,
        3,
        4,
        9,
        11,
        46,
        19,
        21,
        26
      ],
      [
        1,
        2,
        3,
        4,
        9,
        10,
        11,
        46,
        21,
        30
      ],
      [
        3,
        14
      ],
      [
        32,
        1,
        2,
        4,
        10,
        11,
        43,
        46,
        14,
        21,
        26
      ],
      [
        1,
        10,
        3
      ],
      [
        2,
        14,
        39
      ],
      [
        0
      ],
      [
        12,
        46
      ],
      [
        0
      ],
      [
        8,
        17,
        30,
        15
      ],
      [
        15,
        7
      ],
      [
        43,
        11
      ],
      [
        35,
        5,
        42,
        14,
        15
      ],
      [
        12,
        21
      ],
      [
        2,
        39,
        7
      ],
      [
        20
      ],
      [
        0,
        35
      ],
      [
        0,
        1,
        2,
        4,
        5,
        7,
        9,
        10,
        11,
        12,
        14,
        15,
        16,
        17,
        19,
        21,
        26,
        27,
        30,
        32,
        35,
        39,
        42,
        46,
        47,
        48
      ],
      [
        0,
        11
      ],
      [
        9,
        42
      ],
      [
        42
      ],
      [
        0
      ],
      [
        19,
        15
      ],
      [
        0,
        37,
        43,
        11,
        22
      ],
      [
        2,
        46,
        7
      ],
      [
        4,
        20,
        5
      ],
      [
        27
      ],
      [
        0,
        34,
        39,
        9,
        43,
        14
      ],
      [
        16,
        46
      ],
      [
        15
      ],
      [
        27,
        35,
        7
      ],
      [
        42
      ],
      [
        16,
        17
      ],
      [
        5
      ],
      [
        43,
        21
      ],
      [
        8
      ],
      [
        11,
        43,
        15
      ],
      [
        9,
        7
      ],
      [
        2,
        15
      ],
      [
        0,
        43,
        11
      ],
      [
        0
      ],
      [
        0,
        37,
        22
      ],
      [
        2,
        4,
        13
      ],
      [
        0
      ],
      [
        23
      ],
      [
        19,
        14
      ],
      [
        28
      ],
      [
        0,
        4,
        5,
        43,
        28
      ],
      [
        2,
        35,
        15
      ],
      [
        8,
        7
      ],
      [
        1,
        4,
        12,
        13,
        17,
        20
      ],
      [
        0,
        15,
        39
      ],
      [
        27,
        35,
        15
      ],
      [
        35,
        27,
        15
      ],
      [
        19,
        14,
        15
      ],
      [
        0,
        1,
        2,
        3,
        4,
        7,
        8,
        9,
        11,
        12,
        14,
        15,
        17,
        19,
        21,
        23,
        27,
        28,
        30,
        35,
        37,
        39,
        42,
        43,
        48
      ],
      [
        0,
        2,
        7,
        8,
        12,
        13,
        15,
        17,
        23,
        27,
        30,
        31,
        34,
        35,
        37,
        38,
        39,
        41,
        47
      ],
      [
        1,
        7,
        41,
        43,
        48
      ],
      [
        1,
        37,
        7,
        43,
        14,
        19,
        22,
        30
      ],
      [
        21,
        14,
        15
      ],
      [
        41,
        43,
        9,
        15
      ],
      [
        11
      ],
      [
        11
      ],
      [
        8,
        4,
        46
      ],
      [
        35,
        27
      ],
      [
        42
      ],
      [
        0,
        32,
        8,
        14,
        19,
        23,
        26,
        28
      ],
      [
        26,
        35,
        22,
        15
      ],
      [
        0,
        1,
        4,
        8,
        10,
        11,
        12,
        14,
        47,
        16,
        17,
        19,
        23,
        30
      ],
      [
        0,
        11,
        43,
        14,
        19,
        28
      ],
      [
        35,
        42,
        27
      ],
      [
        3,
        14
      ],
      [
        0,
        15
      ],
      [
        35,
        27,
        5
      ],
      [
        17,
        4
      ],
      [
        7,
        39,
        15
      ],
      [
        9,
        43,
        14,
        15
      ],
      [
        35,
        15
      ],
      [
        0,
        41,
        43,
        11
      ],
      [
        0,
        42,
        27
      ],
      [
        2
      ],
      [
        0
      ],
      [
        41,
        11,
        12,
        13
      ],
      [
        0,
        8,
        12,
        31
      ],
      [
        2
      ],
      [
        2
      ],
      [
        9,
        11
      ],
      [
        48,
        43,
        11,
        37
      ],
      [
        0,
        2,
        41,
        11,
        43,
        28
      ],
      [
        10,
        34,
        15
      ],
      [
        41,
        2,
        5,
        15
      ],
      [
        30
      ],
      [
        0,
        15
      ],
      [
        42,
        7
      ],
      [
        0,
        35,
        5,
        11,
        12,
        15,
        27
      ],
      [
        10,
        12
      ],
      [
        0,
        1,
        2,
        3,
        4,
        5,
        7,
        8,
        9,
        11,
        12,
        13,
        14,
        15,
        16,
        19,
        21,
        22,
        28,
        30,
        32,
        35,
        37,
        39,
        42,
        47,
        48
      ],
      [
        2,
        20
      ],
      [
        28
      ],
      [
        0,
        3,
        39,
        9,
        11,
        22
      ],
      [
        0,
        2,
        43,
        37
      ],
      [
        0
      ],
      [
        11,
        37,
        22
      ],
      [
        5,
        37,
        22
      ],
      [
        48,
        15
      ],
      [
        23
      ],
      [
        0,
        1,
        2,
        5,
        7,
        8,
        9,
        11,
        13,
        14,
        15,
        19,
        22,
        26,
        28,
        30,
        32,
        35,
        39,
        42,
        43,
        46,
        48
      ],
      [
        13,
        15
      ],
      [
        48,
        9,
        5
      ],
      [
        9,
        14
      ],
      [
        0
      ],
      [
        0
      ],
      [
        37,
        22
      ],
      [
        9,
        13,
        47,
        16,
        17
      ],
      [
        48,
        0,
        15
      ],
      [
        11
      ],
      [
        1,
        39,
        9,
        10,
        14
      ],
      [
        9,
        7
      ],
      [
        0,
        28
      ],
      [
        0,
        7,
        9,
        11,
        13
      ],
      [
        43,
        2,
        11,
        21
      ],
      [
        19,
        14,
        15
      ],
      [
        5
      ],
      [
        16,
        4,
        12
      ],
      [
        11
      ],
      [
        0,
        2,
        7,
        39,
        12,
        15,
        16,
        23,
        30
      ],
      [
        1,
        46
      ],
      [
        5
      ],
      [
        48
      ],
      [
        27,
        43,
        5
      ],
      [
        37,
        39,
        14,
        19,
        22,
        28
      ],
      [
        6
      ],
      [
        48
      ],
      [
        2,
        43,
        13,
        15
      ],
      [
        32,
        35,
        37,
        11,
        43,
        22,
        26,
        27
      ],
      [
        8,
        4,
        31
      ],
      [
        0,
        43,
        11,
        15
      ],
      [
        43
      ],
      [
        15
      ],
      [
        0
      ],
      [
        0,
        1,
        11
      ],
      [
        20
      ],
      [
        2,
        21,
        14
      ],
      [
        41,
        13,
        6
      ],
      [
        42,
        11,
        15
      ],
      [
        0,
        14,
        22
      ],
      [
        3
      ],
      [
        43,
        11
      ],
      [
        0,
        9,
        43,
        28
      ],
      [
        14,
        39
      ],
      [
        39
      ],
      [
        11
      ],
      [
        0,
        35,
        11,
        43,
        46,
        15,
        21,
        27
      ],
      [
        19,
        14
      ],
      [
        8,
        4,
        15,
        23
      ],
      [
        19,
        14,
        6
      ],
      [
        28,
        22
      ],
      [
        0,
        1,
        34,
        6,
        7,
        41,
        12,
        13
      ],
      [
        0,
        1,
        43,
        11
      ],
      [
        15
      ],
      [
        1,
        42
      ],
      [
        35,
        42,
        27
      ],
      [
        35,
        19
      ],
      [
        1,
        4,
        8,
        41,
        10,
        12,
        13,
        46,
        47,
        16,
        17,
        23,
        30,
        31
      ],
      [
        5
      ],
      [
        5
      ],
      [
        0,
        3,
        5
      ],
      [
        0
      ],
      [
        19,
        6
      ],
      [
        5
      ],
      [
        0,
        5
      ],
      [
        43,
        5
      ],
      [
        8,
        43,
        4,
        31
      ],
      [
        27,
        21
      ],
      [
        23,
        47
      ],
      [
        15
      ],
      [
        0,
        1,
        9,
        12,
        13,
        48
      ],
      [
        35,
        27
      ],
      [
        32,
        0,
        26,
        7
      ],
      [
        0,
        21,
        6
      ],
      [
        3
      ],
      [
        46
      ],
      [
        8,
        31
      ],
      [
        46
      ],
      [
        37
      ],
      [
        21
      ],
      [
        19,
        6
      ],
      [
        46
      ],
      [
        2,
        6,
        46,
        22,
        26
      ],
      [
        48,
        21
      ],
      [
        1,
        13,
        41
      ],
      [
        10,
        35,
        47
      ],
      [
        19,
        46,
        14
      ],
      [
        48
      ],
      [
        27,
        35
      ],
      [
        0,
        2,
        7,
        8,
        12,
        13,
        15,
        17,
        23,
        27,
        30,
        31,
        34,
        35,
        37,
        38,
        39,
        41,
        47
      ],
      [
        35,
        2,
        27
      ],
      [
        34,
        7
      ],
      [
        32,
        26
      ],
      [
        1,
        19
      ],
      [
        1,
        3,
        4,
        9,
        46,
        21,
        26
      ],
      [
        1,
        5,
        7,
        13,
        47,
        22,
        30
      ],
      [
        2,
        8,
        46,
        16,
        23
      ],
      [
        48,
        39
      ],
      [
        28
      ],
      [
        12,
        30
      ],
      [
        5
      ],
      [
        9,
        2,
        26,
        5
      ],
      [
        2
      ],
      [
        14
      ],
      [
        0,
        17,
        12
      ],
      [
        37,
        43,
        11,
        22,
        28
      ],
      [
        0
      ],
      [
        28
      ],
      [
        1,
        2,
        11,
        14,
        21
      ],
      [
        0,
        32,
        2,
        8,
        43,
        46,
        16,
        17,
        23,
        26,
        30,
        31
      ],
      [
        16,
        8,
        4
      ],
      [
        0,
        39,
        7,
        13,
        15,
        17
      ],
      [
        19,
        5,
        15
      ],
      [
        0,
        5,
        9,
        43,
        22
      ],
      [
        2
      ],
      [
        2
      ],
      [
        2,
        37,
        15
      ],
      [
        2,
        12
      ],
      [
        9,
        6
      ],
      [
        0,
        6
      ],
      [
        2,
        37
      ],
      [
        0,
        37,
        41,
        11,
        16,
        31
      ],
      [
        48
      ],
      [
        11,
        43,
        28
      ],
      [
        35,
        7
      ],
      [
        48,
        34
      ],
      [
        0,
        37,
        11,
        43,
        19,
        28
      ],
      [
        0,
        9,
        43,
        11,
        28
      ],
      [
        47
      ],
      [
        0,
        4,
        8,
        15,
        23
      ],
      [
        2,
        19
      ],
      [
        43,
        21,
        14
      ],
      [
        4,
        5,
        6,
        11,
        46,
        16,
        31
      ],
      [
        43,
        37,
        22
      ],
      [
        4
      ],
      [
        1,
        12,
        41
      ],
      [
        4,
        16,
        17,
        23,
        31
      ],
      [
        6,
        7,
        43,
        11,
        46,
        14
      ],
      [
        34
      ],
      [
        27,
        7,
        15
      ],
      [
        1,
        4,
        41,
        10,
        13,
        47,
        21,
        28,
        30
      ],
      [
        11,
        6
      ],
      [
        6
      ],
      [
        11,
        43,
        46
      ],
      [
        2
      ],
      [
        34
      ],
      [
        34,
        6,
        7
      ],
      [
        22
      ],
      [
        11
      ],
      [
        0
      ],
      [
        3
      ],
      [
        14,
        6
      ],
      [
        5
      ],
      [
        35,
        27,
        1,
        15
      ],
      [
        1,
        19
      ],
      [
        0,
        4,
        46,
        15,
        17,
        31
      ],
      [
        0,
        9,
        12
      ],
      [
        2
      ],
      [
        1
      ],
      [
        17,
        4
      ],
      [
        37
      ],
      [
        48
      ],
      [
        0,
        5,
        39
      ],
      [
        0,
        15
      ],
      [
        19
      ],
      [
        0
      ],
      [
        21,
        5,
        37
      ],
      [
        19,
        14
      ],
      [
        47
      ],
      [
        27,
        4
      ],
      [
        16,
        19,
        6,
        31
      ],
      [
        0,
        5,
        22
      ],
      [
        28
      ],
      [
        0,
        2,
        28,
        22
      ],
      [
        30,
        47
      ],
      [
        28
      ],
      [
        2,
        27,
        39
      ],
      [
        32,
        1,
        37,
        10,
        46,
        22,
        26
      ],
      [
        10,
        12,
        16,
        17,
        23,
        31
      ],
      [
        0,
        2,
        5,
        9,
        14,
        47,
        19
      ],
      [
        34
      ],
      [
        0,
        43,
        37,
        22
      ],
      [
        6
      ],
      [
        31
      ],
      [
        41,
        1
      ],
      [
        48,
        1,
        46
      ],
      [
        37
      ],
      [
        6
      ],
      [
        6,
        11,
        14,
        15,
        28
      ],
      [
        14
      ],
      [
        42
      ],
      [
        2
      ],
      [
        1,
        41,
        10,
        12,
        13
      ],
      [
        6
      ],
      [
        2
      ],
      [
        0
      ],
      [
        0,
        35,
        6,
        48,
        27
      ],
      [
        48
      ],
      [
        0,
        1,
        13,
        47,
        30
      ],
      [
        37,
        22
      ],
      [
        48,
        35,
        12,
        5
      ],
      [
        37,
        22
      ],
      [
        2
      ],
      [
        6
      ],
      [
        16,
        46,
        6
      ],
      [
        19
      ],
      [
        39
      ],
      [
        39
      ],
      [
        41,
        10,
        30,
        47
      ],
      [
        28
      ],
      [
        9,
        6
      ],
      [
        0,
        9
      ],
      [
        2,
        21
      ],
      [
        0,
        43,
        39
      ],
      [
        20
      ],
      [
        0
      ],
      [
        0,
        41,
        13
      ],
      [
        8,
        12,
        22
      ],
      [
        41,
        12,
        15
      ],
      [
        0,
        6
      ],
      [
        5,
        6
      ],
      [
        20
      ],
      [
        37
      ],
      [
        20
      ],
      [
        48,
        19,
        28,
        6
      ],
      [
        14
      ],
      [
        43,
        37,
        22
      ],
      [
        6,
        42,
        14,
        19,
        21,
        22
      ],
      [
        6,
        7
      ],
      [
        41,
        10,
        1
      ],
      [
        0,
        37,
        19,
        20,
        21
      ],
      [
        28,
        6,
        39
      ],
      [
        2,
        43
      ],
      [
        2,
        20,
        21
      ],
      [
        2,
        20,
        14
      ],
      [
        6
      ],
      [
        20
      ],
      [
        19,
        6,
        14
      ],
      [
        2,
        39,
        14,
        47,
        19,
        20
      ],
      [
        20
      ],
      [
        20,
        6,
        30
      ],
      [
        28,
        37,
        22
      ],
      [
        34
      ],
      [
        0,
        38
      ],
      [
        16
      ],
      [
        1,
        4
      ],
      [
        2,
        19,
        14,
        22
      ],
      [
        1,
        10,
        13,
        41
      ],
      [
        0,
        1,
        2,
        3,
        5,
        7,
        9,
        11,
        13,
        14,
        15,
        16,
        19,
        21,
        22,
        26,
        28,
        30,
        32,
        34,
        35,
        37,
        39,
        42,
        47,
        48
      ],
      [
        20
      ],
      [
        0,
        1,
        2,
        4,
        5,
        7,
        9,
        11,
        12,
        13,
        14,
        15,
        19,
        21,
        22,
        23,
        27,
        28,
        30,
        31,
        32,
        35,
        39,
        42,
        47
      ],
      [
        0,
        1,
        2,
        3,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        14,
        15,
        19,
        21,
        26,
        27,
        28,
        30,
        32,
        35,
        37,
        39,
        42,
        43,
        47
      ],
      [
        0,
        43,
        5
      ],
      [
        32,
        2,
        6,
        11,
        26
      ],
      [
        2
      ],
      [
        2,
        39
      ],
      [
        2
      ],
      [
        2,
        20
      ],
      [
        46,
        47,
        20,
        21,
        30
      ],
      [
        0,
        35,
        15,
        26,
        27
      ],
      [
        0,
        1,
        2,
        4,
        5,
        6,
        7,
        9,
        11,
        13,
        14,
        15,
        16,
        19,
        21,
        26,
        27,
        28,
        30,
        31,
        32,
        35,
        37,
        39,
        42,
        43,
        46,
        48
      ],
      [
        21
      ],
      [
        0,
        1,
        2,
        4,
        6,
        8,
        9,
        10,
        11,
        12,
        14,
        15,
        16,
        21,
        27,
        28,
        31,
        35,
        41,
        42,
        43,
        46,
        47
      ],
      [
        0
      ],
      [
        43
      ],
      [
        6
      ],
      [
        37
      ],
      [
        37
      ],
      [
        14
      ],
      [
        21,
        14
      ],
      [
        32,
        26,
        2,
        46
      ],
      [
        48,
        20
      ],
      [
        32,
        2,
        37,
        21,
        22
      ],
      [
        1,
        10,
        37
      ],
      [
        0,
        5
      ],
      [
        0
      ],
      [
        2,
        39
      ],
      [
        16,
        42,
        4
      ],
      [
        0,
        35,
        3
      ],
      [
        27,
        35
      ],
      [
        0,
        13,
        46,
        14
      ],
      [
        48,
        14,
        6
      ],
      [
        35,
        27,
        46
      ],
      [
        28,
        6,
        14
      ],
      [
        6,
        12,
        47,
        19,
        20
      ],
      [
        2,
        3,
        6,
        9,
        11,
        12,
        14,
        15,
        19,
        21,
        22,
        28,
        30,
        32,
        34,
        35,
        39,
        43,
        46,
        47,
        48
      ],
      [
        8,
        11,
        28
      ],
      [
        42,
        27
      ],
      [
        0
      ],
      [
        20,
        31
      ],
      [
        32,
        26,
        2
      ],
      [
        48,
        1,
        12,
        4
      ],
      [
        7
      ],
      [
        27,
        35,
        21,
        6
      ],
      [
        0,
        39
      ],
      [
        2,
        6
      ],
      [
        0,
        2,
        47,
        26,
        30
      ],
      [
        0,
        1
      ],
      [
        0,
        43,
        11,
        6
      ],
      [
        6
      ],
      [
        32,
        2,
        35,
        3,
        7,
        9,
        14,
        26,
        27,
        28
      ],
      [
        26,
        15
      ],
      [
        0,
        1,
        2,
        4,
        6,
        7,
        9,
        11,
        14,
        15,
        17,
        19,
        27,
        28,
        35,
        37,
        39,
        41,
        42,
        47
      ],
      [
        34,
        20,
        14
      ],
      [
        32,
        2,
        26,
        6
      ],
      [
        3
      ],
      [
        1,
        2,
        11
      ],
      [
        1,
        2,
        4,
        6,
        7,
        9,
        12,
        14,
        15,
        19,
        22,
        27,
        28,
        35,
        37,
        42,
        46,
        47,
        48
      ],
      [
        2,
        26
      ],
      [
        20,
        14
      ],
      [
        41,
        2,
        21
      ],
      [
        9,
        2
      ],
      [
        27,
        35,
        28
      ],
      [
        0
      ],
      [
        34,
        35,
        4,
        11,
        16,
        21
      ],
      [
        42
      ],
      [
        6
      ],
      [
        41,
        1
      ],
      [
        20,
        5
      ],
      [
        32,
        0,
        6,
        7,
        15,
        17,
        19,
        21,
        26,
        28
      ],
      [
        9,
        15
      ],
      [
        0,
        2,
        4,
        37,
        6,
        7,
        9,
        11,
        43
      ],
      [
        9,
        37,
        5
      ],
      [
        0,
        1,
        6,
        7,
        48,
        19,
        21
      ],
      [
        15
      ],
      [
        20
      ],
      [
        40,
        38
      ],
      [
        0,
        11,
        28,
        13
      ],
      [
        7,
        46,
        47,
        16,
        31
      ],
      [
        40
      ],
      [
        6
      ],
      [
        32,
        10,
        3,
        14
      ],
      [
        32,
        3,
        9,
        46,
        14,
        19,
        21,
        26
      ],
      [
        1,
        46,
        47,
        21,
        26,
        28
      ],
      [
        32,
        3,
        10,
        11,
        46,
        47,
        21,
        26
      ],
      [
        32,
        1,
        9,
        10,
        11,
        46,
        47,
        19,
        26
      ],
      [
        9,
        10,
        1,
        47
      ],
      [
        3,
        9,
        10,
        47,
        26
      ],
      [
        32,
        3,
        11
      ],
      [
        28,
        14
      ],
      [
        3,
        19,
        28,
        14
      ],
      [
        19,
        11
      ],
      [
        1
      ],
      [
        3
      ],
      [
        0,
        2,
        7,
        8,
        12,
        13,
        15,
        17,
        23,
        27,
        30,
        31,
        34,
        35,
        37,
        38,
        39,
        41,
        47
      ],
      [
        32,
        2,
        20,
        6
      ],
      [
        2,
        3
      ],
      [
        43,
        11
      ],
      [
        47
      ],
      [
        19,
        6
      ],
      [
        0,
        37,
        6,
        21,
        22
      ],
      [
        9,
        2
      ],
      [
        0,
        4,
        11,
        47,
        17,
        22,
        30
      ],
      [
        0,
        3,
        37,
        6,
        22
      ],
      [
        34,
        20,
        7
      ],
      [
        0
      ],
      [
        48,
        0,
        28
      ],
      [
        19,
        7
      ],
      [
        20
      ],
      [
        48,
        34
      ],
      [
        13
      ],
      [
        2,
        37,
        12,
        13,
        47,
        17,
        30,
        31
      ],
      [
        2,
        5,
        6,
        7,
        40,
        14,
        20
      ],
      [
        1,
        34,
        2,
        4,
        6,
        8,
        9,
        42,
        11,
        43,
        14,
        15,
        48,
        19,
        21
      ],
      [
        11
      ],
      [
        41,
        13,
        1
      ],
      [
        39,
        40,
        42,
        14,
        19
      ],
      [
        0,
        21
      ],
      [
        0,
        9
      ],
      [
        27
      ],
      [
        2
      ],
      [
        0,
        1,
        10,
        14
      ],
      [
        42
      ],
      [
        9,
        14,
        6
      ],
      [
        26,
        28
      ],
      [
        48,
        34,
        14
      ],
      [
        0,
        2
      ],
      [
        35,
        4,
        5,
        6,
        7,
        14,
        48,
        19,
        27,
        28,
        31
      ],
      [
        48,
        0,
        34
      ],
      [
        38
      ],
      [
        11
      ],
      [
        1,
        35,
        37,
        6,
        13,
        47
      ],
      [
        9,
        2,
        11,
        43
      ],
      [
        2,
        3,
        10,
        13,
        16,
        31
      ],
      [
        32,
        0,
        35,
        3,
        37,
        6,
        39,
        9,
        11,
        14,
        15,
        17,
        19
      ],
      [
        3
      ],
      [
        40,
        38
      ],
      [
        43,
        11,
        5
      ],
      [
        27,
        6
      ],
      [
        0
      ],
      [
        20,
        30
      ],
      [
        0,
        5,
        43,
        11,
        12
      ],
      [
        21,
        6,
        39
      ],
      [
        9,
        5,
        6
      ],
      [
        48
      ],
      [
        9,
        11,
        43
      ],
      [
        2
      ],
      [
        6
      ],
      [
        0,
        7,
        8,
        11,
        43,
        16,
        23
      ],
      [
        1,
        2,
        35,
        4,
        41,
        48,
        27,
        30,
        31
      ],
      [
        0,
        35,
        5,
        6,
        27
      ],
      [
        0
      ],
      [
        0,
        43,
        19,
        5
      ],
      [
        48,
        1,
        12,
        41
      ],
      [
        0,
        3
      ],
      [
        32,
        2,
        35,
        9,
        42,
        15
      ],
      [
        1,
        23
      ],
      [
        0,
        27
      ],
      [
        0,
        11,
        28
      ],
      [
        1,
        41
      ],
      [
        41,
        11,
        1,
        47
      ],
      [
        35,
        27
      ],
      [
        0,
        11
      ],
      [
        11
      ],
      [
        1,
        4,
        6,
        10,
        12,
        16
      ],
      [
        20,
        14,
        7
      ],
      [
        35,
        38,
        11,
        43,
        19,
        27
      ],
      [
        0
      ],
      [
        42,
        27
      ],
      [
        2,
        5
      ],
      [
        11,
        0,
        43
      ],
      [
        40,
        2,
        14
      ],
      [
        0
      ],
      [
        28
      ],
      [
        2,
        20,
        14
      ],
      [
        6
      ],
      [
        0,
        28,
        5,
        39
      ],
      [
        0,
        5,
        6,
        38,
        40,
        9,
        43,
        11,
        14,
        46,
        48,
        17,
        16,
        21
      ],
      [
        9
      ],
      [
        10
      ],
      [
        41,
        9,
        43,
        13,
        30
      ],
      [
        0,
        9
      ],
      [
        48
      ],
      [
        0,
        6,
        14,
        19,
        26
      ],
      [
        2
      ],
      [
        9,
        11,
        28
      ],
      [
        19,
        6
      ],
      [
        6,
        39
      ],
      [
        0,
        1,
        4,
        5,
        9,
        43,
        46,
        17,
        23,
        28,
        31
      ],
      [
        27,
        35
      ],
      [
        1,
        4,
        8,
        41,
        10,
        17,
        31
      ],
      [
        1,
        4,
        8,
        41,
        10,
        17,
        31
      ],
      [
        0,
        1,
        34,
        4,
        37,
        41,
        47,
        22
      ],
      [
        0,
        1,
        4,
        5,
        7,
        8,
        9,
        10,
        12,
        16,
        17,
        21,
        22,
        23,
        28,
        34,
        37,
        39,
        41,
        46,
        48
      ],
      [
        0,
        2,
        37,
        6,
        21,
        22
      ],
      [
        40,
        2,
        6
      ],
      [
        42,
        2
      ],
      [
        3
      ],
      [
        0,
        1,
        2,
        5,
        7,
        40,
        12
      ],
      [
        1,
        6,
        7,
        8,
        9,
        10,
        12,
        47,
        21,
        23,
        30,
        31
      ],
      [
        4,
        20,
        7
      ],
      [
        32,
        2,
        4,
        37,
        6,
        39,
        42,
        43,
        14,
        15,
        28
      ],
      [
        1,
        35,
        6,
        8,
        41,
        9,
        12,
        13,
        14,
        17,
        19,
        23,
        27
      ],
      [
        34,
        2,
        37,
        39,
        8,
        12,
        13,
        15,
        47,
        17,
        16,
        23,
        30,
        31
      ],
      [
        2,
        34,
        39,
        12,
        13,
        47,
        17,
        27,
        30,
        31
      ],
      [
        4,
        46,
        16,
        17,
        31
      ],
      [
        11
      ],
      [
        8,
        1,
        34
      ],
      [
        0
      ],
      [
        46,
        9,
        30,
        47
      ],
      [
        0,
        2,
        32,
        6
      ],
      [
        1,
        34,
        40,
        20,
        30
      ],
      [
        0,
        9,
        26,
        28
      ],
      [
        32,
        0,
        2,
        34,
        4,
        3,
        6,
        7,
        8,
        14,
        16,
        17,
        19,
        26,
        31
      ],
      [
        34,
        4,
        6,
        7,
        9
      ],
      [
        16,
        5,
        23
      ],
      [
        19,
        14
      ],
      [
        2
      ],
      [
        37,
        11,
        43,
        22,
        28
      ],
      [
        2
      ],
      [
        4,
        8,
        16,
        17,
        23,
        31
      ],
      [
        30,
        7
      ],
      [
        41,
        1
      ],
      [
        19,
        28,
        6
      ],
      [
        0
      ],
      [
        2
      ],
      [
        1,
        10,
        20
      ],
      [
        43,
        11,
        37,
        6
      ],
      [
        2,
        3,
        6,
        9,
        10,
        11,
        21
      ],
      [
        40,
        28,
        20
      ],
      [
        2,
        35,
        34,
        7,
        39,
        48,
        21,
        27,
        30
      ],
      [
        32,
        4,
        42,
        13,
        14,
        47,
        26,
        30
      ],
      [
        35,
        19,
        6
      ],
      [
        27,
        34,
        35,
        20
      ],
      [
        10,
        12
      ],
      [
        34,
        4,
        7,
        40,
        8,
        14,
        48,
        20,
        30
      ],
      [
        27
      ],
      [
        21
      ],
      [
        40,
        20,
        38
      ],
      [
        32,
        0,
        2,
        26
      ],
      [
        26
      ],
      [
        0,
        9,
        43,
        11,
        21,
        28
      ],
      [
        1,
        3,
        37,
        39,
        8,
        10,
        14,
        15,
        23
      ],
      [
        0,
        2,
        4,
        8,
        46,
        16,
        17,
        20,
        23
      ],
      [
        0,
        37
      ],
      [
        35,
        38,
        7,
        39,
        42,
        11,
        27
      ],
      [
        16,
        23
      ],
      [
        41,
        10,
        1
      ],
      [
        40,
        34
      ],
      [
        6,
        40,
        12,
        46,
        47,
        20,
        30
      ],
      [
        35,
        11,
        43,
        27,
        28
      ],
      [
        0,
        3,
        37,
        11,
        22
      ],
      [
        5
      ],
      [
        27,
        35
      ],
      [
        2,
        37
      ],
      [
        32,
        2,
        26,
        34
      ],
      [
        2
      ],
      [
        8,
        30,
        14
      ],
      [
        0,
        11,
        43
      ],
      [
        19,
        6
      ],
      [
        34,
        35,
        37,
        6,
        13,
        46,
        22,
        27
      ],
      [
        17
      ],
      [
        2,
        19
      ],
      [
        43,
        5,
        6
      ],
      [
        43,
        11,
        37,
        22
      ],
      [
        0
      ],
      [
        0,
        35,
        37,
        9,
        43,
        11,
        22,
        27
      ],
      [
        28
      ],
      [
        0,
        43
      ],
      [
        4,
        47,
        20,
        23,
        30,
        31
      ],
      [
        1,
        6,
        40,
        41,
        12,
        13,
        48
      ],
      [
        40,
        34
      ],
      [
        35,
        46
      ],
      [
        8,
        28,
        47
      ],
      [
        0,
        6,
        9,
        46,
        21
      ],
      [
        0,
        1,
        12,
        13
      ],
      [
        34
      ],
      [
        1,
        10,
        12,
        13
      ],
      [
        0,
        1,
        38,
        10,
        43,
        13
      ],
      [
        0,
        43,
        11,
        21
      ],
      [
        6
      ],
      [
        41,
        10,
        11,
        12
      ],
      [
        40
      ],
      [
        19
      ],
      [
        1,
        34,
        35,
        47,
        22
      ],
      [
        0,
        32,
        2,
        34,
        5,
        7,
        26
      ],
      [
        27,
        35
      ],
      [
        0
      ],
      [
        37,
        39,
        11,
        43,
        22
      ],
      [
        4,
        6,
        43,
        11,
        16
      ],
      [
        6,
        9,
        14,
        19,
        20,
        21
      ],
      [
        27,
        35
      ],
      [
        2,
        3,
        6,
        39,
        38,
        46,
        14,
        48,
        19
      ],
      [
        1,
        37,
        6,
        39,
        8,
        7,
        9,
        5,
        41,
        14,
        47,
        19,
        21,
        22,
        30
      ],
      [
        0,
        37,
        9,
        10,
        43,
        11
      ],
      [
        20
      ],
      [
        3
      ],
      [
        37,
        6,
        12,
        47,
        22,
        30
      ],
      [
        17,
        4,
        20,
        31
      ],
      [
        48,
        34
      ],
      [
        1,
        2,
        10,
        12,
        13,
        16
      ],
      [
        11,
        39
      ],
      [
        5
      ],
      [
        2,
        5
      ],
      [
        46
      ],
      [
        1,
        43,
        21
      ],
      [
        22
      ],
      [
        1,
        2,
        35,
        3,
        38,
        40,
        46,
        20,
        27
      ],
      [
        1,
        4,
        17,
        31
      ],
      [
        32,
        6,
        7,
        9,
        11,
        14,
        47,
        48,
        21,
        28
      ],
      [
        0,
        5,
        37,
        6,
        9,
        11,
        21
      ],
      [
        46
      ],
      [
        32,
        2,
        35,
        5,
        26,
        27
      ],
      [
        32,
        2,
        6,
        13,
        14,
        21
      ],
      [
        38
      ],
      [
        35,
        37,
        6,
        7,
        14,
        48,
        19,
        22
      ],
      [
        12,
        47
      ],
      [
        1,
        37,
        7,
        39,
        41,
        11,
        14,
        15,
        21,
        23,
        30
      ],
      [
        30
      ],
      [
        5
      ],
      [
        20,
        7
      ],
      [
        0,
        43,
        11
      ],
      [
        0
      ],
      [
        8,
        17,
        16,
        31
      ],
      [
        0,
        5,
        46,
        39
      ],
      [
        0,
        5
      ],
      [
        17,
        10,
        19,
        31
      ],
      [
        7
      ],
      [
        20,
        14,
        22
      ],
      [
        32,
        2,
        26
      ],
      [
        9,
        21,
        6
      ],
      [
        20
      ],
      [
        3
      ],
      [
        0
      ],
      [
        2,
        37,
        5,
        7,
        39,
        46,
        20
      ],
      [
        2,
        28
      ],
      [
        6,
        39,
        14,
        48,
        19
      ],
      [
        0,
        3,
        43,
        11,
        16
      ],
      [
        0
      ],
      [
        35,
        4,
        14,
        16,
        48,
        21,
        27
      ],
      [
        0,
        37,
        22
      ],
      [
        1,
        34,
        35,
        4,
        5,
        6,
        39,
        9,
        41,
        13,
        14,
        47,
        19,
        21,
        22,
        30
      ],
      [
        2,
        20
      ],
      [
        0,
        46
      ],
      [
        5,
        11,
        43,
        46,
        27
      ],
      [
        34,
        2,
        39,
        47,
        17,
        27
      ],
      [
        34,
        2,
        39,
        8,
        7,
        12,
        13,
        47,
        16,
        17,
        27,
        30,
        31
      ],
      [
        0,
        3,
        6,
        9,
        11,
        22
      ],
      [
        4,
        47,
        16,
        20,
        31
      ],
      [
        8,
        14,
        19,
        23,
        28
      ],
      [
        0,
        2,
        5,
        9,
        14,
        48,
        19,
        26
      ],
      [
        5,
        6
      ],
      [
        28
      ],
      [
        32,
        1,
        0,
        39,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        47,
        17,
        42,
        30
      ],
      [
        2,
        6,
        7,
        42,
        19,
        21
      ],
      [
        27,
        35
      ],
      [
        41
      ],
      [
        0,
        14
      ],
      [
        0
      ],
      [
        37,
        38,
        40,
        20,
        22
      ],
      [
        48,
        27,
        7
      ],
      [
        32,
        0,
        2,
        38,
        6,
        14,
        16,
        17,
        19,
        23,
        26
      ],
      [
        32,
        35,
        5,
        46,
        26
      ],
      [
        43,
        11
      ],
      [
        0,
        43
      ],
      [
        2,
        21,
        6
      ],
      [
        9
      ],
      [
        2,
        3,
        6
      ],
      [
        0,
        34,
        37,
        38,
        7,
        8,
        9,
        42,
        11,
        22
      ],
      [
        0,
        3
      ],
      [
        4,
        7,
        8,
        17,
        23,
        30
      ],
      [
        0,
        38
      ],
      [
        20,
        46
      ],
      [
        20
      ],
      [
        42,
        21,
        6,
        14
      ],
      [
        38,
        7,
        40,
        48,
        20,
        30
      ],
      [
        0,
        1,
        2,
        35,
        7,
        8,
        41,
        10,
        39,
        12,
        14,
        15,
        48,
        23
      ],
      [
        0,
        6,
        43,
        11,
        48
      ],
      [
        0,
        32,
        5,
        6,
        9,
        19,
        28
      ],
      [
        5
      ],
      [
        0,
        9,
        6
      ],
      [
        9,
        3,
        37
      ],
      [
        32,
        2,
        7,
        39,
        26
      ],
      [
        2,
        4,
        7,
        40,
        17
      ],
      [
        34,
        38,
        7
      ],
      [
        0,
        1,
        34,
        3,
        4,
        5,
        37,
        7,
        9,
        42,
        12,
        47,
        17,
        21,
        22,
        23,
        28,
        30
      ],
      [
        1,
        10
      ],
      [
        34
      ],
      [
        4
      ],
      [
        1
      ],
      [
        0,
        43
      ],
      [
        1,
        41,
        11,
        12,
        13,
        46,
        16
      ],
      [
        41,
        9
      ],
      [
        32,
        26
      ],
      [
        46
      ],
      [
        2,
        3,
        5,
        9,
        28
      ],
      [
        8,
        16,
        31
      ],
      [
        11,
        27
      ],
      [
        27,
        5
      ],
      [
        5
      ],
      [
        3
      ],
      [
        16,
        17,
        19,
        31
      ],
      [
        17,
        10,
        14,
        23
      ],
      [
        38
      ],
      [
        6
      ],
      [
        37,
        22
      ],
      [
        2,
        20
      ],
      [
        34,
        39,
        9,
        11,
        16,
        30
      ],
      [
        4,
        6,
        7,
        17,
        31
      ],
      [
        0,
        1,
        3,
        4,
        37,
        6,
        42,
        11,
        12,
        13,
        47,
        16,
        19,
        30,
        31
      ],
      [
        10
      ],
      [
        26
      ],
      [
        21,
        14
      ],
      [
        38
      ],
      [
        2
      ],
      [
        20,
        4,
        46
      ],
      [
        1,
        34,
        4,
        20,
        30
      ],
      [
        1
      ],
      [
        20,
        46
      ],
      [
        40,
        38
      ],
      [
        20
      ],
      [
        9
      ],
      [
        9
      ],
      [
        32,
        1,
        10,
        26
      ],
      [
        1,
        3,
        10,
        11,
        26,
        28
      ],
      [
        1,
        10,
        19
      ],
      [
        32,
        1,
        10
      ],
      [
        32,
        1,
        9,
        10,
        26
      ],
      [
        0,
        1,
        7,
        41,
        10,
        12,
        13,
        28
      ],
      [
        27
      ],
      [
        1,
        4,
        40,
        12,
        47,
        20
      ],
      [
        1,
        34,
        4,
        7,
        14,
        16
      ],
      [
        2,
        5
      ],
      [
        1,
        10,
        12,
        13
      ],
      [
        38
      ],
      [
        0,
        34,
        35,
        9,
        43,
        47,
        30
      ],
      [
        34,
        4,
        7,
        12,
        14,
        47,
        46,
        19,
        21,
        30
      ],
      [
        0
      ],
      [
        2,
        5,
        6,
        38,
        40,
        9,
        14,
        48
      ],
      [
        9
      ],
      [
        0,
        1,
        4,
        8,
        9,
        10,
        11,
        43,
        12,
        16,
        17,
        23,
        31
      ],
      [
        34,
        7,
        8,
        22,
        30
      ],
      [
        1,
        4,
        37,
        7,
        8,
        9,
        42,
        11,
        43,
        13,
        12,
        39,
        26,
        27,
        28,
        30
      ],
      [
        2,
        6,
        14,
        46,
        17,
        19,
        26
      ],
      [
        34,
        2,
        37,
        39,
        8,
        12,
        13,
        47,
        16,
        17,
        23,
        30,
        31
      ],
      [
        0,
        38
      ],
      [
        20,
        38
      ],
      [
        17,
        21,
        23
      ],
      [
        2
      ],
      [
        34,
        4
      ],
      [
        43,
        11
      ],
      [
        0,
        37,
        5,
        22
      ],
      [
        2
      ],
      [
        47
      ],
      [
        11
      ],
      [
        0
      ],
      [
        35,
        41,
        43,
        14,
        19
      ],
      [
        1,
        35,
        4,
        9,
        10,
        41,
        12,
        47,
        16,
        17,
        23,
        27,
        30
      ],
      [
        34,
        2,
        41,
        11,
        43,
        14
      ],
      [
        2,
        4,
        8,
        23,
        31
      ],
      [
        6,
        43,
        11,
        14,
        48,
        21
      ],
      [
        0,
        4,
        8,
        42,
        11,
        43,
        22,
        23
      ],
      [
        6,
        14,
        48,
        19,
        21
      ],
      [
        9,
        10,
        6
      ],
      [
        8,
        41,
        43,
        12,
        11,
        47,
        16,
        31
      ],
      [
        13,
        46,
        14
      ],
      [
        28,
        21,
        6,
        14
      ],
      [
        0,
        5,
        6,
        9,
        28
      ],
      [
        34,
        38,
        40,
        19,
        20
      ],
      [
        9
      ],
      [
        19,
        3,
        14,
        6
      ],
      [
        19,
        6
      ],
      [
        3,
        5
      ],
      [
        0
      ],
      [
        1,
        35,
        41,
        27,
        30
      ],
      [
        0,
        32,
        6,
        9,
        26
      ],
      [
        2,
        35,
        6,
        14,
        21,
        27
      ],
      [
        0
      ],
      [
        1,
        40,
        41,
        10,
        11,
        12,
        28
      ],
      [
        0,
        34,
        42,
        14,
        48
      ],
      [
        11,
        0,
        43
      ],
      [
        0
      ],
      [
        34,
        5
      ],
      [
        40,
        19,
        21,
        38
      ],
      [
        34,
        4,
        13
      ],
      [
        28
      ],
      [
        0,
        43,
        11
      ],
      [
        0,
        2,
        43
      ],
      [
        39
      ],
      [
        8,
        10
      ],
      [
        9,
        14,
        39
      ],
      [
        6
      ],
      [
        2,
        20,
        46
      ],
      [
        9,
        21
      ],
      [
        34
      ],
      [
        11,
        39
      ],
      [
        3,
        37,
        6,
        39,
        46,
        21
      ],
      [
        1
      ],
      [
        0,
        43
      ],
      [
        0,
        34,
        9,
        11,
        43
      ],
      [
        19,
        38,
        6
      ],
      [
        32,
        1,
        4,
        38,
        7,
        8,
        42,
        11,
        13,
        46,
        47,
        16,
        14,
        22,
        26,
        28
      ],
      [
        1,
        3,
        37,
        39,
        8,
        7,
        42,
        9,
        11,
        14,
        15,
        46,
        19,
        21,
        22,
        30
      ],
      [
        0,
        1,
        2,
        3,
        6,
        8,
        10,
        13,
        15,
        16,
        19,
        21,
        22,
        23,
        32,
        42,
        46,
        47,
        48
      ],
      [
        0,
        1,
        3,
        35,
        5,
        4,
        39,
        8,
        9,
        11,
        43,
        12,
        46,
        47,
        16,
        19,
        26
      ],
      [
        0,
        1,
        11
      ],
      [
        1,
        34
      ],
      [
        40,
        2,
        20
      ],
      [
        9
      ],
      [
        40
      ],
      [
        34
      ],
      [
        1
      ],
      [
        34
      ],
      [
        20,
        30
      ],
      [
        40,
        6
      ],
      [
        5
      ],
      [
        48,
        34,
        38
      ],
      [
        0,
        11
      ],
      [
        46,
        7
      ],
      [
        1,
        3,
        40,
        9,
        8,
        11,
        48,
        16,
        23
      ],
      [
        20,
        47
      ],
      [
        34,
        2,
        39,
        8,
        12,
        13,
        47,
        17,
        23,
        30,
        31
      ],
      [
        16
      ],
      [
        1,
        10,
        46,
        21,
        22,
        26
      ],
      [
        1,
        10,
        9
      ],
      [
        32,
        1,
        2,
        37,
        12,
        13,
        47,
        48,
        19,
        21,
        26,
        27,
        28,
        30
      ],
      [
        8
      ],
      [
        0,
        4,
        10,
        13,
        48
      ],
      [
        32,
        1,
        11,
        5
      ],
      [
        1
      ],
      [
        1,
        3,
        10,
        19,
        21
      ],
      [
        0,
        6,
        11,
        14,
        48,
        21
      ],
      [
        0,
        9,
        2
      ],
      [
        48,
        3,
        6,
        39
      ],
      [
        3,
        6,
        7,
        39,
        9,
        10,
        11,
        12,
        14,
        47,
        19,
        28
      ],
      [
        20
      ],
      [
        1,
        34,
        7,
        13,
        46,
        17,
        30,
        31
      ],
      [
        8,
        17,
        23,
        41
      ],
      [
        6
      ],
      [
        35,
        46
      ],
      [
        19,
        3,
        14
      ],
      [
        26,
        28,
        46
      ],
      [
        1,
        34,
        4,
        41,
        13
      ],
      [
        0
      ],
      [
        0,
        1,
        10
      ],
      [
        20,
        30
      ],
      [
        35
      ],
      [
        20
      ],
      [
        0,
        1,
        7,
        8,
        46
      ],
      [
        34,
        7
      ],
      [
        41,
        4
      ],
      [
        26,
        35,
        46
      ],
      [
        32,
        1,
        11,
        43,
        46,
        22,
        26
      ],
      [
        0,
        37,
        5,
        7,
        40,
        9
      ],
      [
        40
      ],
      [
        8,
        11,
        4
      ],
      [
        32,
        6,
        8,
        9,
        10,
        11,
        43,
        13,
        14,
        19,
        21,
        23,
        26,
        30
      ],
      [
        37,
        39,
        9,
        22,
        28
      ],
      [
        10
      ],
      [
        0,
        11,
        7
      ],
      [
        9
      ],
      [
        2,
        39
      ],
      [
        40,
        34
      ],
      [
        5
      ],
      [
        20
      ],
      [
        28
      ],
      [
        35,
        46,
        47,
        16,
        20,
        27,
        31
      ],
      [
        0,
        19
      ],
      [
        1,
        4,
        13,
        16,
        31
      ],
      [
        11,
        9,
        3,
        37
      ],
      [
        0,
        9,
        11,
        22
      ],
      [
        40
      ],
      [
        0
      ],
      [
        40,
        19,
        21,
        6
      ],
      [
        27,
        35,
        19,
        14
      ],
      [
        27,
        35
      ],
      [
        20
      ],
      [
        0,
        2,
        8,
        16,
        17
      ],
      [
        37,
        22
      ],
      [
        35
      ],
      [
        27
      ],
      [
        17,
        31
      ],
      [
        0,
        2,
        19,
        39
      ],
      [
        4,
        6,
        8,
        9,
        14,
        46,
        48,
        16,
        21
      ],
      [
        2
      ],
      [
        16,
        6
      ],
      [
        32,
        1,
        34,
        3,
        2,
        39,
        42,
        10,
        14,
        16,
        17,
        27,
        30
      ],
      [
        0,
        2,
        4,
        6,
        7,
        9,
        10,
        11,
        12,
        14,
        21,
        22,
        30,
        35,
        39,
        41,
        43,
        46,
        47
      ],
      [
        1,
        4,
        8,
        42,
        12,
        13,
        47,
        17,
        22,
        23,
        31
      ],
      [
        16
      ],
      [
        17,
        20,
        38,
        31
      ],
      [
        26,
        38,
        6
      ],
      [
        1,
        6,
        7,
        46,
        16,
        19,
        23
      ],
      [
        6
      ],
      [
        5
      ],
      [
        20
      ],
      [
        47
      ],
      [
        32,
        2,
        26,
        14
      ],
      [
        11,
        6,
        39
      ],
      [
        34,
        3
      ],
      [
        0,
        6,
        11,
        43,
        27
      ],
      [
        40
      ],
      [
        2,
        19,
        12,
        6
      ],
      [
        10,
        12,
        13,
        16,
        23,
        31
      ],
      [
        6,
        11,
        43,
        14,
        19
      ],
      [
        19,
        35,
        27,
        13
      ],
      [
        40,
        17
      ],
      [
        13
      ],
      [
        38
      ],
      [
        9
      ],
      [
        0,
        2,
        39,
        8,
        7,
        12,
        13,
        47,
        16,
        17,
        23,
        30,
        31
      ],
      [
        1,
        3,
        41,
        10,
        12,
        26
      ],
      [
        32,
        1,
        35,
        10,
        12,
        46,
        21,
        26
      ],
      [
        2,
        46
      ],
      [
        0,
        2,
        28
      ],
      [
        0,
        1,
        40,
        41,
        9,
        11,
        12
      ],
      [
        34,
        6,
        7,
        9,
        10,
        11,
        41,
        13,
        46,
        47,
        14,
        19,
        28,
        30
      ],
      [
        1,
        2,
        6,
        7,
        9,
        41,
        43,
        47,
        19,
        21,
        28,
        30
      ],
      [
        37
      ],
      [
        2
      ],
      [
        0,
        3,
        37,
        39,
        41,
        10,
        22
      ],
      [
        35,
        5,
        6,
        21,
        27
      ],
      [
        48,
        35,
        27,
        6
      ],
      [
        42,
        43,
        11,
        14,
        19
      ],
      [
        0,
        5,
        6,
        43,
        17
      ],
      [
        3,
        38,
        6
      ],
      [
        34,
        9,
        41,
        11,
        43,
        12,
        14,
        19
      ],
      [
        37,
        6,
        39,
        11,
        14,
        19
      ],
      [
        34,
        11,
        6,
        7
      ],
      [
        34,
        8,
        42,
        11,
        17
      ],
      [
        0,
        2,
        14,
        7
      ],
      [
        11,
        40,
        2,
        43
      ],
      [
        23
      ],
      [
        37
      ],
      [
        10,
        11,
        12,
        47,
        17,
        21
      ],
      [
        0,
        11,
        43,
        9
      ],
      [
        20
      ],
      [
        32,
        2,
        28
      ],
      [
        0,
        19,
        6
      ],
      [
        48,
        1,
        11
      ],
      [
        41
      ],
      [
        32,
        26,
        19
      ],
      [
        23
      ],
      [
        3,
        4,
        39,
        41,
        11,
        13,
        16,
        17,
        28
      ],
      [
        0,
        1,
        32,
        2,
        6,
        7,
        12,
        13,
        47,
        19,
        21
      ],
      [
        1,
        2,
        6,
        7,
        39,
        42,
        43,
        46,
        14,
        16,
        17,
        19,
        28,
        31
      ],
      [
        46,
        6
      ],
      [
        2,
        37,
        5,
        22
      ],
      [
        1,
        3,
        6,
        11,
        19
      ],
      [
        2,
        20
      ],
      [
        4,
        41,
        43,
        11,
        12
      ],
      [
        1,
        10,
        22,
        41
      ],
      [
        4,
        7,
        8,
        47,
        30,
        31
      ],
      [
        11,
        43
      ],
      [
        39,
        21,
        6,
        47
      ],
      [
        9
      ],
      [
        6,
        41,
        12,
        21,
        31
      ],
      [
        9,
        11,
        43
      ],
      [
        32,
        2,
        6,
        11,
        26
      ],
      [
        2,
        5,
        21,
        6
      ],
      [
        26,
        14,
        6
      ],
      [
        9
      ],
      [
        32,
        26
      ],
      [
        20
      ],
      [
        2,
        3,
        14,
        20,
        21
      ],
      [
        11,
        5
      ],
      [
        7
      ],
      [
        32,
        8,
        21,
        6
      ],
      [
        6
      ],
      [
        0,
        9,
        2,
        14
      ],
      [
        34,
        7,
        11,
        43,
        14,
        19
      ],
      [
        34
      ],
      [
        40,
        34
      ],
      [
        16,
        4,
        46,
        31
      ],
      [
        9
      ],
      [
        1,
        2,
        10,
        12,
        13
      ],
      [
        0,
        6
      ],
      [
        20
      ],
      [
        0,
        9
      ],
      [
        1
      ],
      [
        1,
        34,
        39,
        48,
        27,
        30
      ],
      [
        11,
        12,
        47
      ],
      [
        11,
        9,
        3,
        38
      ],
      [
        43
      ],
      [
        19,
        20,
        6
      ],
      [
        1
      ],
      [
        0,
        34,
        4,
        37,
        9,
        41,
        11,
        10,
        43,
        21,
        22
      ],
      [
        40,
        27
      ],
      [
        0,
        9,
        43,
        11,
        28
      ],
      [
        14
      ],
      [
        20
      ],
      [
        32,
        1,
        34,
        4,
        39,
        8,
        9,
        10,
        42,
        12,
        11,
        46,
        43,
        17,
        26,
        28
      ],
      [
        3,
        4,
        7,
        11,
        43,
        14,
        16,
        22,
        30,
        31
      ],
      [
        1,
        41,
        10,
        12,
        13,
        47
      ],
      [
        1
      ],
      [
        41,
        10,
        4,
        1
      ],
      [
        1,
        3,
        13,
        41
      ],
      [
        19,
        4,
        31
      ],
      [
        0
      ],
      [
        1,
        34,
        6,
        10,
        13,
        47,
        19,
        20,
        21
      ],
      [
        8,
        10,
        17,
        23,
        31
      ],
      [
        3,
        27,
        46
      ],
      [
        32,
        2,
        5,
        7,
        14,
        26
      ],
      [
        48,
        34,
        35,
        31
      ],
      [
        35,
        27,
        14,
        1
      ],
      [
        27
      ],
      [
        32,
        0,
        1,
        7,
        42,
        19,
        26
      ],
      [
        19,
        2,
        11
      ],
      [
        0,
        2,
        9,
        11,
        43,
        14
      ],
      [
        2
      ],
      [
        0,
        4,
        6,
        7,
        40,
        38,
        9,
        43,
        13,
        14,
        16,
        19,
        21,
        27,
        28
      ],
      [
        0
      ],
      [
        2,
        3,
        39,
        8,
        7,
        12,
        13,
        47,
        16,
        17,
        30,
        31
      ],
      [
        35,
        27,
        5,
        39
      ],
      [
        9,
        4,
        13,
        7
      ],
      [
        2,
        37,
        6,
        43,
        11,
        21,
        22
      ],
      [
        1
      ],
      [
        9
      ],
      [
        32,
        1,
        0,
        34,
        4,
        41,
        10,
        22
      ],
      [
        2
      ],
      [
        1,
        7,
        9,
        10,
        12,
        13
      ],
      [
        2,
        11
      ],
      [
        3,
        28
      ],
      [
        20,
        46
      ],
      [
        11
      ],
      [
        0
      ],
      [
        20
      ],
      [
        9
      ],
      [
        9,
        2
      ],
      [
        0
      ],
      [
        38,
        6,
        40,
        47,
        20,
        30
      ],
      [
        47
      ],
      [
        11
      ],
      [
        14
      ],
      [
        41,
        10
      ],
      [
        10
      ],
      [
        40,
        0,
        42
      ],
      [
        38,
        40,
        8,
        46,
        17,
        23
      ],
      [
        7
      ],
      [
        3
      ],
      [
        16,
        8,
        4
      ],
      [
        2,
        20,
        46,
        39
      ],
      [
        47,
        31
      ],
      [
        2,
        4,
        8,
        43,
        14,
        17,
        19,
        21,
        23
      ],
      [
        2
      ],
      [
        32,
        2,
        6,
        8,
        9,
        14,
        21,
        23
      ],
      [
        48,
        38,
        30
      ],
      [
        3,
        28
      ],
      [
        0
      ],
      [
        38,
        34,
        6,
        7
      ],
      [
        9,
        11
      ],
      [
        34,
        20
      ],
      [
        40
      ],
      [
        0,
        35,
        5,
        6,
        46,
        19,
        21,
        27
      ],
      [
        16,
        4,
        31
      ],
      [
        11
      ],
      [
        9,
        37,
        6,
        39
      ],
      [
        27,
        2,
        35
      ],
      [
        20,
        14
      ],
      [
        0,
        11
      ],
      [
        19
      ],
      [
        34,
        37,
        5,
        43,
        11,
        22
      ],
      [
        7
      ],
      [
        4,
        23
      ],
      [
        0,
        11,
        28
      ],
      [
        1,
        4,
        37,
        9,
        10,
        41,
        21
      ],
      [
        0,
        32,
        4,
        6,
        39,
        8,
        9,
        7,
        11,
        12,
        13,
        43,
        48,
        19,
        21,
        26,
        27
      ],
      [
        0,
        6
      ],
      [
        0,
        9,
        23
      ],
      [
        40,
        2,
        39
      ],
      [
        11,
        43
      ],
      [
        6,
        42,
        11,
        43,
        14,
        19,
        21
      ],
      [
        0,
        4,
        37,
        12,
        48
      ],
      [
        1,
        6,
        10,
        19,
        23,
        30
      ],
      [
        2,
        3,
        37,
        6,
        19,
        22
      ],
      [
        0,
        5,
        37,
        9,
        43,
        22
      ],
      [
        6
      ],
      [
        17,
        19
      ],
      [
        2,
        3,
        6,
        38,
        39,
        14,
        46,
        48,
        19
      ],
      [
        41,
        2,
        1
      ],
      [
        1,
        34,
        2,
        4,
        6,
        7,
        9,
        41,
        12,
        13,
        14,
        48,
        19,
        23,
        26,
        28
      ],
      [
        10
      ],
      [
        8,
        12,
        47,
        16,
        17
      ],
      [
        26
      ],
      [
        28
      ],
      [
        34
      ],
      [
        0,
        19,
        5,
        6
      ],
      [
        1,
        10,
        12,
        41
      ],
      [
        0,
        9,
        11,
        43
      ],
      [
        20
      ],
      [
        16,
        1,
        10,
        34
      ],
      [
        20
      ],
      [
        2,
        19,
        14
      ],
      [
        20,
        46
      ],
      [
        39
      ],
      [
        0
      ],
      [
        2,
        6
      ],
      [
        0,
        43
      ],
      [
        32,
        6,
        7,
        9,
        22
      ],
      [
        6
      ],
      [
        0,
        2,
        38
      ],
      [
        16,
        4
      ],
      [
        0,
        9,
        2
      ],
      [
        9,
        19,
        21
      ],
      [
        16,
        17,
        46
      ],
      [
        40
      ],
      [
        37
      ],
      [
        34,
        4,
        7,
        10,
        16,
        17,
        23,
        31
      ],
      [
        43
      ],
      [
        48
      ],
      [
        27
      ],
      [
        2,
        7
      ],
      [
        9
      ],
      [
        9,
        19,
        46
      ],
      [
        20,
        21,
        22
      ],
      [
        6
      ],
      [
        10,
        12,
        46,
        16,
        17
      ],
      [
        19,
        14
      ],
      [
        9,
        21
      ],
      [
        34,
        20
      ],
      [
        0
      ],
      [
        0,
        19,
        14
      ],
      [
        4,
        5,
        8,
        11,
        47,
        17,
        21,
        23,
        30,
        31
      ],
      [
        10,
        43,
        13,
        16,
        17,
        23
      ],
      [
        2,
        31
      ],
      [
        3
      ],
      [
        27,
        37,
        46,
        22
      ],
      [
        0,
        43
      ],
      [
        43,
        11
      ],
      [
        2,
        5,
        6,
        40,
        9,
        42,
        11,
        16,
        21
      ],
      [
        32
      ],
      [
        2,
        46
      ],
      [
        0,
        35,
        27,
        5
      ],
      [
        40,
        38
      ],
      [
        20,
        38,
        47
      ],
      [
        2,
        3,
        39,
        7,
        8,
        12,
        13,
        47,
        16,
        17,
        23,
        30
      ],
      [
        0,
        9,
        4,
        23
      ],
      [
        0,
        1,
        35,
        5,
        6,
        7,
        39,
        41,
        12,
        28,
        30
      ],
      [
        27,
        35
      ],
      [
        32,
        2,
        6,
        9,
        19,
        26
      ],
      [
        8,
        21,
        23
      ],
      [
        32,
        26
      ],
      [
        8,
        22
      ],
      [
        34,
        20
      ],
      [
        32,
        26,
        19
      ],
      [
        0,
        43,
        6
      ],
      [
        11,
        28
      ],
      [
        32,
        26,
        40
      ],
      [
        21,
        6
      ],
      [
        0
      ],
      [
        0,
        2,
        19,
        5
      ],
      [
        19,
        6
      ],
      [
        0
      ],
      [
        0,
        43,
        11
      ],
      [
        0,
        9,
        11,
        43
      ],
      [
        0,
        37,
        22
      ],
      [
        8,
        23
      ],
      [
        8,
        0,
        10,
        23
      ],
      [
        35,
        11,
        43,
        46,
        47
      ],
      [
        6,
        7,
        14,
        48,
        19
      ],
      [
        0,
        43,
        11
      ],
      [
        9,
        3
      ],
      [
        5,
        8,
        43,
        11,
        23
      ],
      [
        0,
        37,
        6,
        39,
        40,
        9,
        11,
        43,
        19,
        21
      ],
      [
        2,
        37,
        6,
        9,
        11,
        43,
        22,
        26,
        28
      ],
      [
        46,
        17,
        30
      ],
      [
        2,
        20,
        7
      ],
      [
        0,
        32,
        4,
        39,
        11,
        43,
        46,
        14,
        21,
        26,
        31
      ],
      [
        0
      ],
      [
        0,
        1,
        4,
        9,
        10,
        41
      ],
      [
        0,
        34,
        4,
        41,
        10,
        11
      ],
      [
        34,
        4,
        7,
        20,
        23,
        31
      ],
      [
        7
      ],
      [
        4,
        5,
        38,
        46,
        26
      ],
      [
        3
      ],
      [
        26,
        14
      ],
      [
        2,
        3,
        39,
        7,
        47,
        16,
        17,
        30
      ],
      [
        5,
        6
      ],
      [
        28
      ],
      [
        43,
        6
      ],
      [
        32,
        6,
        9,
        19,
        26
      ],
      [
        2,
        5,
        6,
        39,
        20
      ],
      [
        11,
        43
      ],
      [
        34,
        7
      ],
      [
        1,
        34,
        4,
        7,
        40,
        8,
        42,
        16,
        19,
        21,
        23,
        31
      ],
      [
        32,
        1,
        2,
        3,
        38,
        8,
        9,
        41,
        11,
        12,
        14,
        22,
        26
      ],
      [
        1,
        3,
        4,
        7,
        12,
        16,
        17,
        23,
        31
      ],
      [
        6
      ],
      [
        32,
        26,
        5
      ],
      [
        8,
        19,
        14,
        7
      ],
      [
        0,
        3,
        37,
        6,
        22
      ],
      [
        4,
        23
      ],
      [
        40,
        20,
        6
      ],
      [
        16,
        1,
        12,
        46
      ],
      [
        11,
        43,
        5,
        39
      ],
      [
        0,
        32,
        5,
        11,
        43,
        26
      ],
      [
        2,
        28
      ],
      [
        0,
        32,
        5,
        43,
        11,
        26
      ],
      [
        20
      ],
      [
        4
      ],
      [
        48,
        1,
        12,
        41
      ],
      [
        17,
        4,
        23
      ],
      [
        32,
        26,
        28
      ],
      [
        11,
        43,
        35
      ],
      [
        41
      ],
      [
        20
      ],
      [
        1,
        13,
        22,
        39
      ],
      [
        40
      ],
      [
        11,
        39
      ],
      [
        0,
        1,
        4,
        16
      ],
      [
        2,
        5,
        38
      ],
      [
        2,
        26,
        7
      ],
      [
        0,
        1,
        35,
        3,
        12,
        27
      ],
      [
        20,
        37
      ],
      [
        34
      ],
      [
        7
      ],
      [
        35,
        27,
        7
      ],
      [
        0,
        1,
        34,
        3,
        5
      ],
      [
        0,
        1,
        42,
        12,
        28
      ],
      [
        1,
        6,
        41,
        11,
        43,
        13,
        16
      ],
      [
        9,
        19,
        21,
        41
      ],
      [
        40,
        5,
        6
      ],
      [
        0,
        9,
        37
      ],
      [
        14,
        7
      ],
      [
        11,
        43
      ],
      [
        1,
        8,
        46,
        47,
        23,
        30
      ],
      [
        9
      ],
      [
        34,
        4,
        7,
        8,
        43,
        11
      ],
      [
        30
      ],
      [
        32,
        7,
        39,
        16,
        26
      ],
      [
        8
      ],
      [
        1,
        28,
        4
      ],
      [
        16,
        17,
        46
      ],
      [
        5
      ],
      [
        5,
        37
      ],
      [
        41,
        4,
        1
      ],
      [
        32,
        2,
        37,
        9,
        11,
        26
      ],
      [
        27,
        5,
        14
      ],
      [
        1,
        12,
        17,
        20,
        30,
        31
      ],
      [
        6,
        7,
        40,
        38,
        14,
        21
      ],
      [
        43
      ],
      [
        0,
        37,
        48,
        19,
        22,
        27,
        28
      ],
      [
        2,
        5,
        6,
        9,
        43,
        14,
        19
      ],
      [
        20
      ],
      [
        0,
        1,
        3,
        6,
        9,
        41,
        11,
        12,
        43
      ],
      [
        0
      ],
      [
        19,
        21,
        14,
        6
      ],
      [
        40
      ],
      [
        9
      ],
      [
        2,
        39,
        14,
        20,
        23
      ],
      [
        20,
        5
      ],
      [
        0,
        1,
        2,
        3,
        7,
        8,
        9,
        10,
        11,
        43,
        41,
        46,
        39,
        16,
        48,
        47
      ],
      [
        11
      ],
      [
        0,
        9,
        6
      ],
      [
        20
      ],
      [
        1,
        4,
        41,
        10,
        12,
        13,
        17,
        23
      ],
      [
        1
      ],
      [
        1
      ],
      [
        2,
        4,
        20,
        23
      ],
      [
        0,
        6,
        21,
        23,
        27
      ],
      [
        43,
        11,
        28,
        21
      ],
      [
        38,
        31
      ],
      [
        1,
        9,
        10,
        11,
        14
      ],
      [
        48,
        5
      ],
      [
        0,
        5,
        37,
        39,
        9,
        46,
        22,
        28
      ],
      [
        19,
        6
      ],
      [
        0,
        46
      ],
      [
        2
      ],
      [
        6
      ],
      [
        9,
        6,
        14
      ],
      [
        0,
        2
      ],
      [
        5
      ],
      [
        11,
        43,
        3,
        46
      ],
      [
        35,
        37,
        41,
        10,
        43,
        13,
        21,
        22
      ],
      [
        32,
        1,
        4,
        37,
        21,
        22
      ],
      [
        1,
        4,
        41,
        10,
        43,
        11,
        13,
        46,
        42,
        21
      ],
      [
        9,
        22
      ],
      [
        43,
        11,
        28,
        5
      ],
      [
        14
      ],
      [
        0,
        21,
        38
      ],
      [
        3,
        28
      ],
      [
        8
      ],
      [
        8,
        34
      ],
      [
        2,
        6,
        14,
        19,
        21
      ],
      [
        0,
        9,
        43,
        11
      ],
      [
        32,
        1,
        2,
        3,
        0,
        37,
        14,
        47,
        19,
        23,
        30
      ],
      [
        1,
        4
      ],
      [
        1
      ],
      [
        32,
        2
      ],
      [
        0,
        37,
        6,
        10,
        11,
        43,
        46
      ],
      [
        10,
        13
      ],
      [
        32,
        0,
        2,
        43,
        11,
        21,
        26
      ],
      [
        0,
        43,
        11,
        9
      ],
      [
        0,
        1
      ],
      [
        20
      ],
      [
        0,
        11
      ],
      [
        20
      ],
      [
        0,
        28
      ],
      [
        1
      ],
      [
        43,
        35,
        46,
        6
      ],
      [
        32,
        2,
        26,
        38
      ],
      [
        20
      ],
      [
        48
      ],
      [
        0,
        2,
        34,
        4,
        7,
        40,
        8,
        11,
        46,
        48,
        21
      ],
      [
        37
      ],
      [
        3,
        43,
        10,
        11
      ],
      [
        32,
        2
      ],
      [
        37
      ],
      [
        0
      ],
      [
        28,
        20,
        5
      ],
      [
        0
      ],
      [
        34,
        11
      ],
      [
        2,
        37,
        20,
        22,
        26
      ],
      [
        2,
        20,
        6,
        39
      ],
      [
        34,
        3,
        9,
        10,
        12,
        17
      ],
      [
        4,
        6,
        39,
        8,
        23
      ],
      [
        32,
        0,
        6,
        39,
        9,
        11,
        43,
        13,
        14,
        19,
        21,
        22,
        26,
        28
      ],
      [
        35,
        46
      ],
      [
        32,
        1,
        2,
        7,
        46,
        26,
        27
      ],
      [
        32,
        2,
        35,
        26,
        27
      ],
      [
        32,
        26
      ],
      [
        0,
        5,
        22
      ],
      [
        0,
        1,
        4,
        5,
        37,
        7,
        39,
        41,
        10,
        9,
        12,
        13,
        46,
        16,
        21,
        22,
        23,
        31
      ],
      [
        19,
        14,
        6
      ],
      [
        0,
        11,
        6
      ],
      [
        32,
        37,
        7,
        9,
        43,
        11,
        14,
        19,
        22,
        26
      ],
      [
        20
      ],
      [
        39
      ],
      [
        20
      ],
      [
        13,
        30,
        31
      ],
      [
        0,
        1,
        4,
        8,
        12,
        13,
        46,
        47,
        16,
        17
      ],
      [
        17
      ],
      [
        9,
        11
      ],
      [
        0
      ],
      [
        16,
        41,
        10
      ],
      [
        2
      ],
      [
        10
      ],
      [
        42
      ],
      [
        11
      ],
      [
        34,
        38,
        7,
        6,
        14,
        21
      ],
      [
        11,
        28
      ],
      [
        0,
        43,
        11
      ],
      [
        0,
        4
      ],
      [
        1,
        34,
        4,
        41,
        43,
        13
      ],
      [
        1,
        4,
        37,
        41,
        10,
        11,
        13,
        22
      ],
      [
        4,
        38,
        6,
        19,
        28
      ],
      [
        0,
        42,
        21,
        39
      ],
      [
        38
      ],
      [
        2,
        20
      ],
      [
        1,
        2,
        35,
        4,
        6,
        7,
        41,
        12,
        13,
        30
      ],
      [
        6
      ],
      [
        37,
        22
      ],
      [
        0,
        35,
        6,
        14,
        19,
        21,
        27
      ],
      [
        34,
        35,
        4,
        6,
        7,
        40,
        39,
        14,
        16,
        19,
        20,
        26,
        27,
        31
      ],
      [
        2
      ],
      [
        48,
        34,
        7
      ],
      [
        40,
        2,
        27,
        6
      ],
      [
        4,
        38,
        8,
        16,
        17
      ],
      [
        0,
        46
      ],
      [
        1,
        34,
        4,
        38,
        41,
        13
      ],
      [
        32,
        1,
        4,
        37,
        41,
        13,
        14,
        22
      ],
      [
        6,
        31
      ],
      [
        2,
        3
      ],
      [
        37,
        5
      ],
      [
        3,
        39,
        8,
        7,
        47,
        16,
        17,
        21,
        23,
        27,
        30
      ],
      [
        6
      ],
      [
        48,
        13
      ],
      [
        1
      ],
      [
        32,
        26,
        3
      ],
      [
        41,
        10
      ],
      [
        40
      ],
      [
        40,
        19,
        7
      ],
      [
        0,
        32,
        2,
        1,
        6,
        7,
        12,
        13,
        26
      ],
      [
        27
      ],
      [
        11
      ],
      [
        9,
        11
      ],
      [
        0,
        35,
        37,
        13,
        46,
        22,
        27
      ],
      [
        1,
        5,
        6,
        41,
        10,
        12,
        28
      ],
      [
        3,
        23
      ],
      [
        13
      ],
      [
        0,
        22
      ],
      [
        32,
        1,
        2,
        3,
        35,
        6,
        41,
        14,
        19,
        21,
        26,
        27
      ],
      [
        30,
        14
      ],
      [
        1,
        30
      ],
      [
        1,
        10,
        28,
        30
      ],
      [
        0,
        3,
        5,
        9,
        11,
        28
      ],
      [
        2
      ],
      [
        2,
        3,
        37,
        9,
        22
      ],
      [
        19,
        21,
        6,
        14
      ],
      [
        6
      ],
      [
        27,
        16,
        3,
        6
      ],
      [
        0,
        5,
        38,
        42,
        14
      ],
      [
        0,
        1,
        3,
        37,
        7,
        12,
        21,
        22
      ],
      [
        4,
        38,
        16,
        17,
        31
      ],
      [
        10,
        43
      ],
      [
        48
      ],
      [
        2,
        28
      ],
      [
        0,
        2,
        6,
        39,
        9,
        11,
        43,
        19,
        22,
        23,
        28
      ],
      [
        6
      ],
      [
        0,
        2,
        37
      ],
      [
        9,
        43
      ],
      [
        2,
        43,
        38
      ],
      [
        11,
        9,
        43,
        23
      ],
      [
        3,
        19,
        6
      ],
      [
        0,
        34,
        6,
        7,
        9,
        11,
        23,
        28,
        30
      ],
      [
        0,
        1,
        4,
        39,
        10,
        13
      ],
      [
        48,
        21,
        6
      ],
      [
        32,
        3,
        42,
        12,
        13,
        14,
        19,
        21,
        26
      ],
      [
        0,
        9,
        11
      ],
      [
        10,
        12
      ],
      [
        41,
        10,
        4,
        12
      ],
      [
        48,
        7
      ],
      [
        11,
        39
      ],
      [
        20,
        46
      ],
      [
        0,
        1,
        4,
        8,
        9,
        11,
        43
      ],
      [
        21
      ],
      [
        12,
        13,
        47
      ],
      [
        0
      ],
      [
        9
      ],
      [
        40,
        38
      ],
      [
        0,
        1,
        13,
        22,
        30
      ],
      [
        2,
        3,
        5,
        6,
        39,
        41,
        11,
        12,
        14,
        48,
        21,
        23,
        26,
        28,
        30
      ],
      [
        30,
        47
      ],
      [
        0,
        48
      ],
      [
        0,
        9
      ],
      [
        48,
        34
      ],
      [
        12,
        13,
        14,
        17,
        19,
        31
      ],
      [
        2,
        35,
        3,
        39,
        8,
        7,
        47,
        16,
        17,
        21,
        27,
        30
      ],
      [
        43
      ],
      [
        34,
        4,
        37,
        41,
        10,
        13
      ],
      [
        32,
        1,
        4,
        37,
        41,
        10,
        12,
        13,
        22,
        26
      ],
      [
        9,
        23
      ],
      [
        3
      ],
      [
        4,
        37,
        38,
        8,
        43,
        16,
        17,
        22,
        23,
        31
      ],
      [
        34,
        20,
        7
      ],
      [
        1,
        41,
        12,
        13,
        22
      ],
      [
        11
      ],
      [
        41,
        34
      ],
      [
        9
      ],
      [
        0,
        1,
        2,
        32,
        37,
        6,
        7,
        41,
        42,
        10,
        12,
        43,
        14,
        47,
        19,
        22,
        26,
        30
      ],
      [
        3,
        4,
        21,
        6
      ],
      [
        34,
        7
      ],
      [
        0,
        1,
        4,
        10,
        11,
        43,
        12,
        13,
        16,
        48,
        23,
        31
      ],
      [
        2,
        11,
        28,
        21
      ],
      [
        1
      ],
      [
        3
      ],
      [
        5
      ],
      [
        1,
        34,
        20,
        7
      ],
      [
        32,
        2,
        6
      ],
      [
        32,
        4,
        5,
        6,
        14,
        19,
        26,
        28
      ],
      [
        32,
        14,
        19,
        26,
        28
      ],
      [
        20
      ],
      [
        10,
        13,
        4,
        12
      ],
      [
        34,
        3,
        4,
        30
      ],
      [
        6
      ],
      [
        16,
        17,
        4
      ],
      [
        0,
        11,
        43,
        22
      ],
      [
        32,
        1,
        4,
        39,
        8,
        9,
        41,
        11,
        14,
        23,
        26,
        30,
        31
      ],
      [
        32,
        1,
        34,
        4,
        37,
        41,
        10,
        12,
        13,
        22,
        26
      ],
      [
        32,
        1,
        4,
        37,
        41,
        12,
        13,
        14,
        22,
        26
      ],
      [
        1,
        37,
        7,
        41,
        22
      ],
      [
        11
      ],
      [
        1,
        7,
        41,
        10,
        13
      ],
      [
        2,
        20
      ],
      [
        3,
        6,
        9,
        43,
        17,
        21
      ],
      [
        21
      ],
      [
        16,
        4,
        23
      ],
      [
        0,
        2,
        28,
        20
      ],
      [
        19
      ],
      [
        40
      ],
      [
        0,
        1,
        2,
        3,
        4,
        6,
        7,
        8,
        9,
        11,
        14,
        17,
        19,
        22,
        23,
        28,
        32,
        34,
        42
      ],
      [
        0,
        38
      ],
      [
        5
      ],
      [
        20,
        37
      ],
      [
        11,
        21,
        43,
        37
      ],
      [
        0,
        2,
        35,
        4,
        6,
        8,
        41,
        10,
        43,
        12,
        13,
        14,
        17,
        27,
        28
      ],
      [
        32,
        2,
        14,
        19,
        26
      ],
      [
        34
      ],
      [
        37,
        22
      ],
      [
        2,
        5
      ],
      [
        0,
        43
      ],
      [
        3
      ],
      [
        19
      ],
      [
        48,
        40,
        43,
        14
      ],
      [
        34
      ],
      [
        32,
        2,
        11
      ],
      [
        19
      ],
      [
        7
      ],
      [
        2,
        35,
        3,
        5,
        16,
        27
      ],
      [
        20
      ],
      [
        32,
        0,
        2,
        37,
        14,
        22,
        26
      ],
      [
        32,
        34,
        41,
        10,
        12,
        13,
        26
      ],
      [
        9,
        5
      ],
      [
        0,
        2,
        6,
        39,
        7,
        42,
        14,
        48
      ],
      [
        0
      ],
      [
        8,
        16
      ],
      [
        4,
        10,
        17,
        23,
        31
      ],
      [
        0,
        9,
        43
      ],
      [
        3
      ],
      [
        42
      ],
      [
        16,
        17,
        31
      ],
      [
        2,
        46,
        22
      ],
      [
        4,
        7,
        8,
        12,
        13
      ],
      [
        32,
        2,
        34,
        4,
        37,
        6,
        42,
        11,
        14,
        47,
        23,
        26,
        28
      ],
      [
        8,
        35,
        27
      ],
      [
        0,
        21
      ],
      [
        2
      ],
      [
        3
      ],
      [
        0
      ],
      [
        43,
        11
      ],
      [
        2,
        35,
        3,
        39,
        7,
        8,
        47,
        17,
        21,
        27,
        30
      ],
      [
        12
      ],
      [
        32,
        37,
        9,
        11,
        12,
        43,
        46,
        19
      ],
      [
        20
      ],
      [
        0,
        9,
        34
      ],
      [
        35,
        27,
        28,
        6
      ],
      [
        0,
        37,
        22
      ],
      [
        6
      ],
      [
        28,
        31
      ],
      [
        12
      ],
      [
        1,
        3,
        35,
        6,
        27
      ],
      [
        32,
        2,
        26
      ],
      [
        1,
        10,
        28,
        5
      ],
      [
        9
      ],
      [
        8,
        30,
        47
      ],
      [
        0
      ],
      [
        1,
        41,
        10,
        48,
        28
      ],
      [
        5
      ],
      [
        1,
        4,
        37,
        6,
        11,
        14,
        46,
        22
      ],
      [
        0,
        4,
        37,
        6,
        43,
        48,
        19,
        21,
        22
      ],
      [
        0,
        35,
        5,
        40,
        43,
        11,
        28
      ],
      [
        28,
        6
      ],
      [
        3,
        6
      ],
      [
        11,
        9,
        43
      ],
      [
        43
      ],
      [
        1,
        34,
        3,
        4,
        37,
        6,
        7,
        43,
        11,
        22,
        30
      ],
      [
        43,
        11,
        6,
        9
      ],
      [
        6,
        39,
        9,
        42,
        43,
        19,
        21
      ],
      [
        40,
        2
      ],
      [
        2,
        7
      ],
      [
        2
      ],
      [
        1,
        3,
        6,
        7,
        14,
        19,
        21
      ],
      [
        19,
        20,
        38
      ],
      [
        40,
        48
      ],
      [
        48,
        13
      ],
      [
        32,
        0,
        2,
        37,
        6,
        42,
        11,
        12,
        21,
        22,
        26
      ],
      [
        1,
        34,
        2,
        4,
        6,
        8,
        14,
        16,
        17,
        21,
        30,
        31
      ],
      [
        1,
        10,
        41
      ],
      [
        35,
        5,
        6,
        39,
        48,
        27
      ],
      [
        20,
        23
      ],
      [
        19,
        6,
        14
      ],
      [
        0,
        37,
        12,
        47,
        22
      ],
      [
        3,
        35,
        4,
        5,
        7,
        13
      ],
      [
        39,
        47,
        17,
        20,
        27,
        31
      ],
      [
        43,
        5
      ],
      [
        32,
        0,
        2,
        4,
        6,
        11,
        14,
        19,
        21,
        26,
        28
      ],
      [
        43,
        11
      ],
      [
        35,
        27
      ],
      [
        1,
        10,
        13,
        41
      ],
      [
        16,
        17,
        4,
        8
      ],
      [
        32,
        26
      ],
      [
        42
      ],
      [
        32,
        5,
        39,
        14,
        26
      ],
      [
        39
      ],
      [
        2,
        5
      ],
      [
        4,
        6,
        8,
        9,
        13,
        47,
        23,
        28
      ],
      [
        4,
        5,
        38,
        7,
        8,
        13,
        14,
        47,
        16,
        19,
        22,
        30,
        31
      ],
      [
        16,
        12
      ],
      [
        19
      ],
      [
        2,
        11,
        28
      ],
      [
        32,
        1,
        34,
        35,
        4,
        39,
        40,
        41,
        12,
        13,
        14,
        48,
        22,
        26,
        30
      ],
      [
        2,
        19,
        14
      ],
      [
        32,
        2,
        34,
        38,
        7,
        46,
        16,
        19,
        21,
        26,
        31
      ],
      [
        1,
        9,
        19,
        22,
        23
      ],
      [
        1,
        4,
        8,
        10,
        12,
        13,
        14,
        19,
        23
      ],
      [
        35,
        19
      ],
      [
        3,
        39
      ],
      [
        34,
        38,
        47
      ],
      [
        2
      ],
      [
        34,
        6,
        7,
        11,
        14,
        48,
        19,
        21
      ],
      [
        21,
        6,
        14
      ],
      [
        48,
        39
      ],
      [
        3
      ],
      [
        2,
        22,
        6
      ],
      [
        1,
        4,
        6,
        41,
        42,
        12,
        17
      ],
      [
        0,
        32,
        5
      ],
      [
        42,
        22
      ],
      [
        37
      ],
      [
        27
      ],
      [
        41
      ],
      [
        41,
        12
      ],
      [
        9,
        37,
        22
      ],
      [
        17,
        31,
        23
      ],
      [
        32,
        41,
        5
      ],
      [
        5
      ],
      [
        20
      ],
      [
        10
      ],
      [
        38,
        2,
        19,
        6
      ],
      [
        19,
        6
      ],
      [
        1,
        6,
        39,
        12,
        13,
        46
      ],
      [
        32,
        26,
        27,
        46
      ],
      [
        5
      ],
      [
        41
      ],
      [
        32,
        2,
        26
      ],
      [
        35,
        27,
        6
      ],
      [
        11
      ],
      [
        43,
        28,
        37,
        22
      ],
      [
        32,
        34,
        39,
        9,
        11,
        14,
        26
      ],
      [
        6,
        40,
        11,
        43,
        14,
        19
      ],
      [
        34,
        4,
        7,
        47,
        16,
        17,
        30,
        31
      ],
      [
        32,
        2,
        3,
        6,
        19,
        26
      ],
      [
        9,
        14
      ],
      [
        0
      ],
      [
        2,
        5
      ],
      [
        0,
        4,
        5,
        43,
        23
      ],
      [
        17
      ],
      [
        1,
        6,
        9,
        10,
        11
      ],
      [
        0,
        9,
        11,
        43,
        22,
        28
      ],
      [
        9
      ],
      [
        2,
        46,
        30
      ],
      [
        19
      ],
      [
        3,
        39
      ],
      [
        11,
        43
      ],
      [
        34,
        20
      ],
      [
        9,
        28,
        5
      ],
      [
        0,
        35,
        3,
        8,
        43,
        11,
        47,
        16,
        27
      ],
      [
        2
      ],
      [
        20,
        46
      ],
      [
        0,
        34
      ],
      [
        9,
        43,
        5
      ],
      [
        0,
        9,
        5
      ],
      [
        1,
        4,
        38,
        17,
        23,
        30
      ],
      [
        11,
        9,
        43,
        5
      ],
      [
        0,
        37,
        6
      ],
      [
        0,
        2,
        35,
        5,
        27
      ],
      [
        0
      ],
      [
        0,
        5
      ],
      [
        0,
        34,
        3,
        4,
        5,
        6,
        38,
        37,
        11,
        12,
        23
      ],
      [
        28
      ],
      [
        11,
        9,
        3
      ],
      [
        1,
        6,
        14,
        48,
        19,
        25
      ],
      [
        32,
        34,
        3,
        6,
        7,
        8,
        39,
        10,
        11,
        12,
        14,
        21,
        30
      ],
      [
        48,
        38,
        4,
        14
      ],
      [
        34,
        3,
        4,
        5,
        43,
        14,
        19,
        22
      ],
      [
        34,
        46,
        16,
        20,
        30
      ],
      [
        1,
        19,
        14,
        6
      ],
      [
        1,
        12
      ],
      [
        0,
        1
      ],
      [
        4,
        12,
        47,
        20,
        30
      ],
      [
        1,
        37,
        6,
        9,
        10,
        11,
        41,
        13,
        46,
        12,
        22,
        26
      ],
      [
        1,
        37,
        41,
        10,
        12
      ],
      [
        4,
        46,
        17,
        20,
        31
      ],
      [
        1,
        9,
        10,
        11,
        41,
        14,
        19
      ],
      [
        32,
        1,
        34,
        4,
        37,
        41,
        10,
        12,
        15
      ],
      [
        32,
        1,
        4,
        38,
        41,
        11,
        12,
        13,
        26
      ],
      [
        1,
        34,
        4,
        37,
        10,
        12,
        13,
        26
      ],
      [
        4,
        6,
        41,
        10,
        12,
        13,
        46,
        26
      ],
      [
        21
      ],
      [
        0,
        43,
        11,
        9
      ],
      [
        40,
        19,
        21
      ],
      [
        2,
        35,
        3,
        39,
        8,
        7,
        47,
        17,
        21,
        27,
        30
      ],
      [
        2
      ],
      [
        8,
        48,
        46,
        7
      ],
      [
        42,
        5
      ],
      [
        20
      ],
      [
        2
      ],
      [
        0,
        2,
        9,
        43,
        21,
        28
      ],
      [
        6,
        7,
        40,
        14,
        47,
        48
      ],
      [
        1,
        34,
        4,
        8,
        41,
        10,
        12,
        47,
        16,
        21,
        30
      ],
      [
        0,
        37
      ],
      [
        43,
        11,
        25,
        6
      ],
      [
        4,
        8,
        16,
        17,
        23,
        31
      ],
      [
        32,
        26,
        28
      ],
      [
        20,
        46
      ],
      [
        0,
        37,
        38,
        22,
        25
      ],
      [
        25,
        37,
        22,
        47
      ],
      [
        32,
        2,
        37,
        6,
        22,
        26
      ],
      [
        40,
        42
      ],
      [
        6
      ],
      [
        34,
        2,
        4
      ],
      [
        25,
        35,
        30,
        47
      ],
      [
        32,
        35,
        5,
        26,
        27
      ],
      [
        34
      ],
      [
        42,
        3,
        28,
        6
      ],
      [
        2,
        3,
        28
      ],
      [
        0,
        35,
        13,
        14,
        27
      ],
      [
        0
      ],
      [
        1,
        34,
        4,
        37,
        6,
        41,
        10,
        11,
        46,
        14,
        19,
        27,
        30,
        31
      ],
      [
        48,
        21
      ],
      [
        20
      ],
      [
        13
      ],
      [
        19,
        39,
        6,
        14
      ],
      [
        2
      ],
      [
        0,
        34,
        5,
        7,
        8,
        47,
        16,
        17,
        23
      ],
      [
        32,
        2,
        6,
        40,
        48,
        26
      ],
      [
        32,
        2,
        6,
        7,
        14,
        19,
        21,
        25,
        26
      ],
      [
        1,
        12,
        13
      ],
      [
        27
      ],
      [
        34,
        20
      ],
      [
        34,
        14,
        7
      ],
      [
        1
      ],
      [
        1,
        7,
        14,
        6
      ],
      [
        1,
        10,
        12,
        47,
        30
      ],
      [
        1,
        4,
        41,
        10,
        12,
        13,
        46,
        16,
        17,
        23,
        25,
        31
      ],
      [
        27,
        26,
        2,
        35
      ],
      [
        25,
        21,
        6
      ],
      [
        4,
        13
      ],
      [
        20
      ],
      [
        5
      ],
      [
        8,
        31
      ],
      [
        9
      ],
      [
        43
      ],
      [
        35,
        3,
        25
      ],
      [
        23
      ],
      [
        32,
        2,
        5,
        26,
        28
      ],
      [
        25
      ],
      [
        2,
        3,
        4,
        6,
        7,
        11,
        14,
        26,
        30,
        31,
        32,
        34,
        38,
        39,
        40,
        41,
        43,
        47,
        48
      ],
      [
        2,
        21
      ],
      [
        27,
        30,
        31
      ],
      [
        2,
        6,
        46,
        17,
        25,
        27,
        31
      ],
      [
        0
      ],
      [
        40,
        38
      ],
      [
        4,
        21,
        6,
        7
      ],
      [
        48,
        25,
        6,
        9
      ],
      [
        43
      ],
      [
        11
      ],
      [
        11,
        39
      ],
      [
        2,
        3,
        35,
        6,
        27
      ],
      [
        32,
        26
      ],
      [
        1,
        10,
        12
      ],
      [
        25,
        21,
        6
      ],
      [
        34,
        10,
        43,
        11,
        12
      ],
      [
        6,
        39,
        14,
        19,
        21,
        25
      ],
      [
        2,
        37,
        5,
        40,
        43
      ],
      [
        47
      ],
      [
        0,
        6,
        39
      ],
      [
        8,
        34,
        31
      ],
      [
        6,
        7,
        39,
        48,
        25,
        28
      ],
      [
        0,
        2,
        35,
        37,
        40,
        42,
        14,
        19,
        21,
        22
      ],
      [
        38
      ],
      [
        9,
        6
      ],
      [
        5
      ],
      [
        20,
        30,
        6
      ],
      [
        46,
        25,
        6,
        7
      ],
      [
        4,
        39,
        46,
        14,
        47,
        21,
        23
      ],
      [
        1,
        2,
        34,
        13,
        25,
        30
      ],
      [
        11
      ],
      [
        42,
        35
      ],
      [
        25,
        20
      ],
      [
        4,
        21,
        23
      ],
      [
        19
      ],
      [
        34,
        38,
        40,
        9,
        20,
        21
      ],
      [
        32,
        2,
        37
      ],
      [
        2,
        34,
        38,
        7,
        40,
        6,
        42,
        14,
        46,
        16
      ],
      [
        32,
        34,
        7,
        43,
        14,
        19,
        26
      ],
      [
        14,
        39
      ],
      [
        19,
        5,
        6
      ],
      [
        2,
        12,
        14,
        47,
        19,
        20
      ],
      [
        32,
        2,
        26
      ],
      [
        46
      ],
      [
        20
      ],
      [
        0,
        37,
        38,
        7,
        46,
        48,
        22
      ],
      [
        38
      ],
      [
        26,
        38
      ],
      [
        0,
        42,
        14,
        19,
        21,
        25
      ],
      [
        1,
        35,
        37,
        6,
        41,
        42,
        11,
        12,
        46,
        47,
        14,
        21,
        24,
        25
      ],
      [
        0,
        1,
        35,
        4,
        37,
        7,
        39,
        9,
        11,
        14,
        19,
        22,
        27,
        28
      ],
      [
        2,
        35,
        5
      ],
      [
        1
      ],
      [
        40,
        25,
        14,
        7
      ],
      [
        4,
        16,
        17,
        23,
        24
      ],
      [
        6
      ],
      [
        7
      ],
      [
        19,
        21,
        6,
        14
      ],
      [
        16,
        46,
        38,
        31
      ],
      [
        41,
        13,
        1
      ],
      [
        43,
        37,
        22
      ],
      [
        25,
        7
      ],
      [
        27,
        35,
        6,
        7
      ],
      [
        32,
        0,
        3,
        4,
        35,
        38,
        7,
        6,
        19,
        22,
        25,
        26,
        27,
        28
      ],
      [
        9
      ],
      [
        2,
        14,
        16,
        25,
        26
      ],
      [
        0,
        16,
        2,
        48
      ],
      [
        48,
        7
      ],
      [
        3
      ],
      [
        43,
        2,
        26,
        6
      ],
      [
        0
      ],
      [
        0,
        1,
        8,
        10,
        12,
        25
      ],
      [
        0,
        2,
        6,
        43,
        11,
        21,
        26
      ],
      [
        1,
        34,
        7,
        10,
        14,
        46,
        19
      ],
      [
        1,
        34,
        12,
        13,
        15,
        25
      ],
      [
        39
      ],
      [
        9
      ],
      [
        0,
        32,
        2,
        35,
        5,
        11,
        43,
        26,
        27
      ],
      [
        21,
        38
      ],
      [
        42
      ],
      [
        0,
        1,
        32,
        7,
        39,
        11,
        43,
        14,
        19,
        26
      ],
      [
        0,
        3,
        6,
        7,
        8,
        9,
        11,
        14,
        19,
        21,
        24,
        25,
        26,
        28,
        32,
        34,
        37,
        38,
        43
      ],
      [
        2,
        35,
        4,
        47,
        16,
        17,
        23,
        27,
        30
      ],
      [
        41
      ],
      [
        25,
        43
      ],
      [
        0,
        2
      ],
      [
        6,
        7,
        40,
        19,
        21
      ],
      [
        16
      ],
      [
        6
      ],
      [
        17,
        2,
        27,
        5
      ],
      [
        17,
        19,
        6
      ],
      [
        11,
        22
      ],
      [
        40
      ],
      [
        25,
        14
      ],
      [
        40
      ],
      [
        26,
        27
      ],
      [
        1,
        4,
        41,
        10,
        11,
        12,
        13,
        22
      ],
      [
        32,
        9,
        11,
        12,
        13
      ],
      [
        1,
        37,
        11,
        13,
        26
      ],
      [
        41,
        4,
        46
      ],
      [
        1,
        4,
        37,
        41,
        10,
        43,
        11,
        12
      ],
      [
        1,
        34,
        4,
        38,
        9,
        10,
        11,
        12,
        41,
        22,
        24
      ],
      [
        40,
        38
      ],
      [
        2,
        35,
        3,
        39,
        7,
        8,
        47,
        17,
        21,
        23,
        27,
        30
      ],
      [
        31,
        47
      ],
      [
        32,
        26,
        21,
        6
      ],
      [
        32,
        2,
        28,
        39
      ],
      [
        1,
        9
      ],
      [
        9,
        19,
        14
      ],
      [
        0,
        1,
        3,
        39,
        8,
        12,
        13,
        17,
        21,
        24,
        30,
        31
      ],
      [
        9
      ],
      [
        0,
        35,
        5,
        25,
        27
      ],
      [
        3
      ],
      [
        12
      ],
      [
        0,
        39,
        9,
        43,
        11
      ],
      [
        10
      ],
      [
        8,
        1,
        4
      ],
      [
        40,
        38,
        7
      ],
      [
        6,
        7,
        8,
        39,
        48
      ],
      [
        8,
        2,
        13
      ],
      [
        11,
        9,
        43
      ],
      [
        3,
        11
      ],
      [
        21
      ],
      [
        0,
        3,
        5,
        6,
        13
      ],
      [
        25,
        20,
        6
      ],
      [
        0,
        4,
        6,
        7,
        8,
        10,
        11,
        14,
        19,
        22,
        25,
        26,
        27,
        28,
        30,
        32,
        34,
        35,
        37,
        38,
        40,
        41,
        48
      ],
      [
        0
      ],
      [
        11,
        39
      ],
      [
        40
      ],
      [
        20
      ],
      [
        25,
        42,
        27,
        35
      ],
      [
        0,
        32,
        2,
        1,
        4,
        5,
        6,
        38,
        8,
        10,
        46,
        48,
        19,
        21,
        23,
        25,
        26,
        30
      ],
      [
        39
      ],
      [
        32,
        2,
        38,
        43,
        11,
        26
      ],
      [
        9
      ],
      [
        0,
        5
      ],
      [
        32,
        14,
        48,
        19,
        26
      ],
      [
        1,
        2,
        6,
        41,
        10,
        11,
        13,
        19
      ],
      [
        1
      ],
      [
        11,
        37,
        38
      ],
      [
        20,
        7
      ],
      [
        32,
        25,
        26,
        39
      ],
      [
        32,
        1,
        2
      ],
      [
        32,
        26,
        7
      ],
      [
        3,
        7,
        8,
        41,
        21,
        27,
        30
      ],
      [
        35
      ],
      [
        25,
        19
      ],
      [
        3,
        6,
        40,
        19,
        21
      ],
      [
        0,
        39
      ],
      [
        30,
        6,
        14
      ],
      [
        11
      ],
      [
        25
      ],
      [
        0,
        2,
        9,
        41,
        11,
        43,
        13,
        10,
        17
      ],
      [
        28
      ],
      [
        6
      ],
      [
        5
      ],
      [
        28
      ],
      [
        32,
        26
      ],
      [
        4,
        8,
        16,
        17,
        23,
        31
      ],
      [
        0
      ],
      [
        1
      ],
      [
        25,
        21
      ],
      [
        4,
        16,
        17,
        23,
        31
      ],
      [
        32,
        26,
        19
      ],
      [
        47
      ],
      [
        3,
        22
      ],
      [
        1
      ],
      [
        0,
        25
      ],
      [
        32,
        1,
        34,
        3,
        4,
        0,
        6,
        37,
        9,
        41,
        43,
        12,
        14,
        48,
        21,
        25,
        26,
        30
      ],
      [
        2,
        3
      ],
      [
        7,
        9,
        43,
        48,
        21,
        25
      ],
      [
        0,
        11,
        38
      ],
      [
        38
      ],
      [
        1,
        20,
        38,
        7
      ],
      [
        16,
        12,
        46
      ],
      [
        2,
        35,
        5,
        39,
        21,
        27
      ],
      [
        41,
        12,
        47,
        22,
        30
      ],
      [
        0
      ],
      [
        28
      ],
      [
        4,
        7,
        48,
        19,
        26
      ],
      [
        3
      ],
      [
        8,
        24,
        4,
        23
      ],
      [
        43,
        11,
        1
      ],
      [
        9
      ],
      [
        8,
        43,
        11,
        16,
        23,
        25,
        31
      ],
      [
        0,
        43,
        5
      ],
      [
        38,
        40,
        11,
        43,
        28
      ],
      [
        9,
        11,
        43
      ],
      [
        20
      ],
      [
        10,
        13,
        6,
        39
      ],
      [
        6,
        9,
        11,
        48,
        21,
        28
      ],
      [
        25,
        21
      ],
      [
        28,
        6
      ],
      [
        3,
        11,
        14
      ],
      [
        3
      ],
      [
        24,
        16,
        48,
        4
      ],
      [
        32,
        2,
        35,
        6,
        41,
        48,
        19,
        21,
        26,
        27,
        30
      ],
      [
        0,
        37,
        22
      ],
      [
        9
      ],
      [
        4,
        46,
        16,
        20,
        31
      ],
      [
        9
      ],
      [
        32
      ],
      [
        0
      ],
      [
        32,
        27,
        2,
        26
      ],
      [
        1,
        34,
        4,
        7,
        9,
        17,
        28
      ],
      [
        4,
        6,
        41,
        12,
        13,
        14,
        22,
        24
      ],
      [
        1,
        34,
        4,
        37,
        6,
        41,
        43,
        12,
        13,
        24
      ],
      [
        2,
        3,
        7,
        47,
        17,
        23,
        30
      ],
      [
        13,
        14
      ],
      [
        40
      ],
      [
        1,
        4
      ],
      [
        2
      ],
      [
        32,
        26,
        2
      ],
      [
        20
      ],
      [
        1,
        2,
        4,
        12,
        48
      ],
      [
        4,
        6,
        11,
        19,
        21,
        26
      ],
      [
        0
      ],
      [
        37
      ],
      [
        37,
        7,
        43,
        11,
        28
      ],
      [
        3
      ],
      [
        0,
        37,
        39,
        11,
        22
      ],
      [
        7
      ],
      [
        0,
        35,
        37,
        9,
        43,
        11,
        22,
        27
      ],
      [
        0,
        34,
        35,
        37,
        6,
        46,
        16,
        21,
        22,
        27
      ],
      [
        5
      ],
      [
        3,
        9,
        11,
        43,
        13
      ],
      [
        20
      ],
      [
        17,
        14,
        9,
        23
      ],
      [
        1,
        2,
        4,
        37,
        8,
        41,
        42,
        43,
        11,
        48,
        22
      ],
      [
        0,
        43,
        5,
        14
      ],
      [
        34,
        6,
        7,
        40,
        47,
        48,
        30
      ],
      [
        28,
        5
      ],
      [
        32,
        2,
        35,
        5,
        26,
        27
      ],
      [
        11,
        14
      ],
      [
        40,
        48,
        7
      ],
      [
        35,
        42,
        27
      ],
      [
        32,
        26,
        13
      ],
      [
        25,
        3
      ],
      [
        0,
        11
      ],
      [
        23
      ],
      [
        42,
        11,
        7
      ],
      [
        2
      ],
      [
        11
      ],
      [
        1,
        2,
        35,
        10,
        23,
        30
      ],
      [
        0
      ],
      [
        32,
        2,
        6,
        7,
        39,
        9,
        40,
        12,
        21,
        25,
        26,
        28
      ],
      [
        0,
        38,
        10,
        12,
        47,
        23,
        24,
        31
      ],
      [
        25,
        7
      ],
      [
        6,
        14,
        19,
        21,
        23
      ],
      [
        6,
        7
      ],
      [
        17,
        20,
        31
      ],
      [
        0,
        1,
        6,
        41,
        10,
        43,
        12,
        13,
        23,
        25
      ],
      [
        40,
        20,
        7
      ],
      [
        34
      ],
      [
        16,
        20,
        46,
        30
      ],
      [
        20
      ],
      [
        0,
        3
      ],
      [
        19
      ],
      [
        1,
        9,
        41,
        10,
        14,
        19,
        23
      ],
      [
        42
      ],
      [
        40,
        30
      ],
      [
        32,
        2,
        26,
        27
      ],
      [
        0,
        7
      ],
      [
        16
      ],
      [
        2
      ],
      [
        9,
        3
      ],
      [
        24,
        16,
        23
      ],
      [
        0,
        1,
        37,
        10,
        22,
        30
      ],
      [
        5,
        6,
        39,
        22,
        25
      ],
      [
        20,
        14
      ],
      [
        3,
        20,
        47
      ],
      [
        19,
        28
      ],
      [
        2,
        28,
        39
      ],
      [
        35,
        11,
        43,
        47,
        30
      ],
      [
        35,
        6,
        7,
        42,
        46,
        48,
        25,
        27
      ],
      [
        9,
        2,
        37,
        6
      ],
      [
        1,
        20,
        4,
        13
      ],
      [
        26,
        28
      ],
      [
        32,
        1,
        34,
        35,
        0,
        37,
        38,
        7,
        6,
        2,
        42,
        11,
        3,
        14,
        47,
        19,
        26
      ],
      [
        32,
        34,
        3,
        37,
        6,
        14,
        19,
        21,
        22,
        23,
        24,
        25,
        27,
        28
      ],
      [
        2,
        3,
        4,
        5,
        6,
        7,
        10,
        14,
        15,
        19,
        21,
        25,
        28,
        30,
        31,
        35,
        37,
        39,
        47
      ],
      [
        1,
        6,
        10,
        17,
        19,
        23
      ],
      [
        19,
        38
      ],
      [
        25,
        19,
        14
      ],
      [
        9,
        6
      ],
      [
        8,
        24,
        10,
        31
      ],
      [
        0,
        1,
        3,
        38,
        10,
        14,
        19
      ],
      [
        34,
        6,
        7
      ],
      [
        3
      ],
      [
        9,
        14,
        21,
        25,
        28
      ],
      [
        0,
        9,
        23
      ],
      [
        0,
        43,
        11,
        6
      ],
      [
        20,
        39,
        7
      ],
      [
        3
      ],
      [
        7
      ],
      [
        1
      ],
      [
        1,
        4,
        8,
        13,
        15,
        30
      ],
      [
        25,
        10,
        14,
        39
      ],
      [
        10
      ],
      [
        34,
        7
      ],
      [
        3,
        28
      ],
      [
        20,
        46
      ],
      [
        9,
        39
      ],
      [
        8,
        19,
        3,
        24
      ],
      [
        34,
        2
      ],
      [
        0,
        25,
        19
      ],
      [
        0,
        22
      ],
      [
        24,
        17,
        42
      ],
      [
        28
      ],
      [
        0,
        2,
        11,
        5
      ],
      [
        9,
        20
      ],
      [
        1,
        38,
        10,
        43,
        13,
        22
      ],
      [
        4
      ],
      [
        1,
        41,
        11,
        12,
        13,
        24
      ],
      [
        1
      ],
      [
        26
      ],
      [
        10,
        5,
        13
      ],
      [
        1,
        10,
        11,
        13
      ],
      [
        40,
        20
      ],
      [
        0,
        17,
        37,
        22
      ],
      [
        6
      ],
      [
        28,
        6
      ],
      [
        0,
        1,
        2,
        3,
        4,
        8,
        9,
        11,
        12,
        14,
        21,
        22,
        24,
        26,
        27,
        28,
        32,
        34,
        35,
        37,
        41,
        43,
        47
      ],
      [
        11,
        38
      ],
      [
        43,
        28,
        37,
        22
      ],
      [
        2,
        6,
        7,
        14,
        19
      ],
      [
        32,
        2,
        38,
        7,
        39,
        9,
        40,
        11,
        43,
        14,
        19,
        26
      ],
      [
        2
      ],
      [
        9,
        3
      ],
      [
        32,
        26,
        11
      ],
      [
        19
      ],
      [
        3
      ],
      [
        1,
        7,
        8,
        41,
        48,
        23,
        24,
        25
      ],
      [
        32,
        8,
        13,
        48,
        17
      ],
      [
        2,
        35,
        3,
        7,
        27
      ],
      [
        2,
        4,
        7,
        39,
        27,
        31
      ],
      [
        19,
        21
      ],
      [
        9,
        19,
        14,
        6
      ],
      [
        32,
        1,
        34,
        3,
        0,
        6,
        13,
        28
      ],
      [
        32,
        2,
        38,
        14,
        48,
        19,
        25,
        26
      ],
      [
        6,
        47,
        16,
        21,
        30
      ],
      [
        27,
        41,
        35
      ],
      [
        43,
        11
      ],
      [
        2,
        6
      ],
      [
        0,
        43
      ],
      [
        26,
        32,
        42,
        2
      ],
      [
        32,
        2,
        6,
        40,
        26
      ],
      [
        32,
        2,
        5,
        21,
        26
      ],
      [
        0,
        37,
        22
      ],
      [
        15
      ],
      [
        3
      ],
      [
        6,
        14
      ],
      [
        0,
        2,
        6,
        14,
        19,
        26,
        28
      ],
      [
        2,
        35,
        6,
        7,
        42,
        13,
        14,
        19,
        25,
        27
      ],
      [
        48,
        21
      ],
      [
        32,
        1,
        2,
        41,
        10,
        13,
        46,
        48,
        26
      ],
      [
        1,
        2,
        4,
        7,
        41,
        12,
        13,
        14,
        16,
        19,
        24
      ],
      [
        11,
        6
      ],
      [
        2
      ],
      [
        0,
        2,
        3,
        4,
        5,
        11,
        14,
        17,
        22,
        25,
        28,
        31,
        32,
        34,
        35,
        37,
        39,
        43,
        46
      ],
      [
        3
      ],
      [
        32,
        2
      ],
      [
        19,
        28,
        6,
        39
      ],
      [
        25,
        6
      ],
      [
        32,
        2,
        37,
        5,
        6,
        48,
        26
      ],
      [
        2,
        34,
        14,
        46,
        16,
        19,
        21,
        25,
        26
      ],
      [
        37,
        19,
        21,
        6
      ],
      [
        0,
        4,
        8,
        46,
        16,
        17,
        23,
        24,
        28,
        31
      ],
      [
        40
      ],
      [
        8,
        31
      ],
      [
        34,
        20,
        6
      ],
      [
        20
      ],
      [
        8,
        24
      ],
      [
        25
      ],
      [
        4
      ],
      [
        32,
        2,
        26
      ],
      [
        1,
        2,
        41,
        10,
        12,
        13,
        47,
        30
      ],
      [
        20
      ],
      [
        0,
        1,
        3,
        4,
        48
      ],
      [
        25,
        20
      ],
      [
        0,
        2,
        40,
        19,
        26
      ],
      [
        25
      ],
      [
        34,
        35,
        4,
        7,
        8,
        16,
        17,
        31
      ],
      [
        34
      ],
      [
        40,
        25
      ],
      [
        20
      ],
      [
        0,
        37,
        38,
        40,
        41,
        10,
        42,
        8,
        11,
        46,
        47,
        48,
        22,
        25,
        30
      ],
      [
        0,
        2,
        3,
        6,
        9,
        11,
        12,
        13,
        14,
        19,
        22,
        25,
        27,
        28,
        31,
        32,
        34,
        35,
        38,
        39,
        40,
        42,
        47,
        48
      ],
      [
        20,
        5,
        38
      ],
      [
        0,
        2,
        3,
        5,
        6
      ],
      [
        47
      ],
      [
        2,
        39
      ],
      [
        2
      ],
      [
        19,
        6,
        39
      ],
      [
        0,
        17,
        8
      ],
      [
        41,
        13
      ],
      [
        1,
        41,
        16,
        24,
        25,
        30
      ],
      [
        48,
        23,
        7
      ],
      [
        1,
        38,
        40,
        12,
        20
      ],
      [
        40,
        10,
        20,
        7
      ],
      [
        0,
        5
      ],
      [
        1,
        27
      ],
      [
        42
      ],
      [
        1,
        4,
        13,
        24,
        30
      ],
      [
        25,
        6
      ],
      [
        27
      ],
      [
        28
      ],
      [
        17
      ],
      [
        48,
        26,
        21,
        6
      ],
      [
        1,
        41,
        10,
        9,
        13
      ],
      [
        2,
        21
      ],
      [
        42,
        35,
        28
      ],
      [
        9,
        5
      ],
      [
        27,
        35
      ],
      [
        9
      ],
      [
        20
      ],
      [
        4,
        23
      ],
      [
        0,
        37,
        41,
        12,
        13,
        22
      ],
      [
        1,
        12,
        13,
        22
      ],
      [
        14
      ],
      [
        0,
        7,
        14,
        16,
        23
      ],
      [
        0,
        35,
        5,
        6,
        42,
        11,
        14,
        46,
        16,
        19,
        21
      ],
      [
        0,
        34,
        7,
        39
      ],
      [
        0,
        2,
        3,
        14
      ],
      [
        2,
        39,
        7
      ],
      [
        25
      ],
      [
        20,
        6
      ],
      [
        2,
        3,
        6,
        7,
        9,
        11,
        19,
        22,
        25,
        26,
        28,
        30,
        32,
        35,
        37,
        40,
        42,
        43,
        47
      ],
      [
        5
      ],
      [
        2,
        21
      ],
      [
        25
      ],
      [
        0,
        32,
        37,
        40,
        47,
        23,
        24,
        26,
        28,
        30
      ],
      [
        19
      ],
      [
        0,
        35,
        37,
        11,
        43,
        22,
        27
      ],
      [
        19
      ],
      [
        0,
        9,
        43,
        17,
        25,
        30
      ],
      [
        28,
        22
      ],
      [
        1,
        5,
        6,
        8,
        40,
        16,
        17,
        23,
        25,
        30,
        31
      ],
      [
        35,
        37,
        6,
        5,
        11,
        43,
        19,
        21,
        22,
        25,
        27
      ],
      [
        0,
        32,
        3,
        6,
        39,
        9,
        48,
        19,
        21,
        26,
        28
      ],
      [
        0
      ],
      [
        2,
        46
      ],
      [
        7
      ],
      [
        34,
        3,
        6,
        40,
        14,
        48,
        19,
        25
      ],
      [
        0,
        32,
        34,
        37,
        5,
        26,
        28
      ],
      [
        0,
        37,
        5,
        6,
        22
      ],
      [
        0,
        1,
        32,
        3,
        4,
        35,
        8,
        41,
        12,
        24,
        26
      ],
      [
        0,
        2,
        27,
        6
      ],
      [
        27,
        35
      ],
      [
        20,
        37,
        22
      ],
      [
        5
      ],
      [
        5
      ],
      [
        20
      ],
      [
        9,
        5
      ],
      [
        27
      ],
      [
        2,
        35,
        3,
        39,
        7,
        47,
        16,
        17,
        21,
        23,
        27,
        30
      ],
      [
        34,
        37,
        41,
        10,
        11,
        12,
        13,
        46,
        22,
        24
      ],
      [
        1,
        10,
        11,
        12,
        13,
        46,
        14,
        22,
        24
      ],
      [
        1,
        38,
        41,
        10,
        43,
        11,
        13,
        12,
        22
      ],
      [
        1,
        34,
        6,
        41,
        10,
        11,
        13,
        46
      ],
      [
        32,
        2,
        3,
        6,
        7,
        14,
        19,
        21,
        25,
        26
      ],
      [
        32,
        1,
        41,
        10,
        12,
        13,
        24,
        26
      ],
      [
        2
      ],
      [
        40,
        19
      ],
      [
        32,
        3,
        6,
        19,
        25
      ],
      [
        0,
        21
      ],
      [
        1,
        3,
        37,
        6,
        39,
        9,
        10,
        11,
        22,
        28
      ],
      [
        32,
        2,
        6,
        39,
        42,
        26
      ],
      [
        3
      ],
      [
        9
      ],
      [
        1,
        37,
        6,
        10,
        13,
        28
      ],
      [
        37,
        22
      ],
      [
        2
      ],
      [
        48,
        11
      ],
      [
        8,
        17
      ],
      [
        1,
        2,
        6,
        46,
        17,
        23,
        25
      ],
      [
        0,
        37,
        22
      ],
      [
        0,
        9,
        10,
        12,
        25,
        30
      ],
      [
        39
      ],
      [
        40
      ],
      [
        9
      ],
      [
        1,
        10,
        41
      ],
      [
        8,
        43,
        12,
        47,
        25
      ],
      [
        6
      ],
      [
        1,
        8,
        41,
        10,
        11,
        17,
        23
      ],
      [
        25
      ],
      [
        39
      ],
      [
        1
      ],
      [
        5,
        11,
        21,
        6
      ],
      [
        0,
        1,
        2,
        3,
        5,
        7,
        8,
        11,
        12,
        14,
        17,
        19,
        21,
        25,
        28,
        30,
        32,
        37,
        42,
        43
      ],
      [
        1,
        6,
        7,
        8,
        41,
        42,
        43,
        11,
        13,
        48,
        17,
        19,
        21,
        22,
        25,
        28
      ],
      [
        28
      ],
      [
        35,
        4,
        6,
        46,
        16,
        27,
        31
      ],
      [
        0,
        1,
        28,
        9
      ],
      [
        35,
        6,
        38,
        12,
        14,
        46,
        16,
        19,
        25,
        31
      ],
      [
        40,
        42,
        38
      ],
      [
        1,
        41,
        10,
        12,
        13
      ],
      [
        38,
        40,
        10,
        42,
        14
      ],
      [
        7
      ],
      [
        32,
        26,
        2
      ],
      [
        1,
        7
      ],
      [
        0,
        4,
        6,
        7,
        10,
        14,
        16,
        17,
        48,
        19,
        23
      ],
      [
        9,
        5
      ],
      [
        2,
        20,
        6
      ],
      [
        1,
        6,
        25
      ],
      [
        34,
        28,
        5,
        6
      ],
      [
        1,
        4,
        5,
        41,
        10,
        12,
        13,
        47,
        17,
        23,
        24,
        30
      ],
      [
        32,
        35,
        39,
        26,
        27
      ],
      [
        1,
        3,
        6,
        7,
        8,
        10,
        12,
        13,
        14,
        16,
        17,
        19,
        23,
        24,
        25,
        27,
        30,
        31,
        34,
        35
      ],
      [
        1,
        8,
        10,
        16,
        17,
        23,
        30,
        31
      ],
      [
        6,
        22
      ],
      [
        20,
        13,
        31
      ],
      [
        3
      ],
      [
        0,
        4
      ],
      [
        1,
        20,
        30
      ],
      [
        1,
        5,
        8,
        11,
        43,
        48,
        23
      ],
      [
        34,
        3,
        6,
        40,
        8,
        16,
        17,
        19,
        23,
        25
      ],
      [
        1,
        6
      ],
      [
        1,
        8,
        14,
        46,
        16,
        21,
        22,
        28,
        30,
        31
      ],
      [
        2,
        5
      ],
      [
        3,
        4,
        8,
        14,
        48
      ],
      [
        38,
        40,
        6
      ],
      [
        32,
        2,
        37,
        6,
        7,
        10,
        14,
        19,
        21,
        25,
        30
      ],
      [
        32,
        0,
        3,
        4,
        39,
        42,
        11,
        13,
        14,
        19,
        21,
        22,
        25,
        26,
        28
      ],
      [
        34,
        15
      ],
      [
        0,
        7,
        9,
        11,
        19,
        22
      ],
      [
        0,
        2,
        13
      ],
      [
        10
      ],
      [
        0,
        40,
        46,
        16,
        20
      ],
      [
        0,
        1,
        6,
        7,
        25
      ],
      [
        14
      ],
      [
        35,
        28,
        22
      ],
      [
        5
      ],
      [
        34,
        4,
        8,
        23,
        30
      ],
      [
        28
      ],
      [
        0
      ],
      [
        11
      ],
      [
        25,
        11,
        43
      ],
      [
        1,
        34,
        7,
        10,
        47,
        30
      ],
      [
        28
      ],
      [
        34,
        2,
        4,
        7,
        8,
        14,
        48,
        23
      ],
      [
        19,
        2,
        3,
        37
      ],
      [
        0,
        26,
        2
      ],
      [
        0,
        6,
        19,
        21,
        25
      ],
      [
        2
      ],
      [
        2
      ],
      [
        43
      ],
      [
        1,
        10,
        31
      ],
      [
        34,
        38,
        16,
        17,
        23,
        31
      ],
      [
        0,
        48,
        37
      ],
      [
        0,
        32,
        2,
        37,
        43,
        26
      ],
      [
        0,
        5,
        47
      ],
      [
        21,
        6,
        7
      ],
      [
        0,
        2,
        34,
        6,
        11,
        14
      ],
      [
        41,
        10,
        13
      ],
      [
        37,
        5,
        22,
        6
      ],
      [
        3,
        5,
        6
      ],
      [
        2,
        3
      ],
      [
        48
      ],
      [
        25
      ],
      [
        38,
        42,
        46,
        16,
        31
      ],
      [
        20
      ],
      [
        3,
        6
      ],
      [
        1,
        3,
        4,
        6,
        7,
        11,
        14,
        19,
        21,
        24,
        25,
        26,
        27,
        30,
        31,
        32,
        39,
        43,
        47,
        48
      ],
      [
        17,
        4,
        6
      ],
      [
        27,
        16,
        35,
        46
      ],
      [
        37
      ],
      [
        32,
        2,
        42,
        19,
        26
      ],
      [
        9
      ],
      [
        10
      ],
      [
        0,
        37,
        22
      ],
      [
        9
      ],
      [
        9,
        6
      ],
      [
        5
      ],
      [
        5
      ],
      [
        17,
        19,
        14,
        31
      ],
      [
        9,
        39
      ],
      [
        46
      ],
      [
        25
      ],
      [
        7,
        42,
        46,
        26,
        27
      ],
      [
        1,
        4,
        8,
        12,
        13,
        47,
        16,
        17,
        22,
        23,
        24,
        31
      ],
      [
        9,
        3
      ],
      [
        34
      ],
      [
        1,
        7,
        8,
        13,
        17,
        21,
        23,
        30
      ],
      [
        3,
        14
      ],
      [
        1,
        2,
        37,
        6,
        39
      ],
      [
        0,
        1,
        6,
        9,
        47,
        30
      ],
      [
        0,
        28
      ],
      [
        7
      ],
      [
        37,
        6,
        39,
        21,
        22
      ],
      [
        2,
        19,
        14,
        6
      ],
      [
        8
      ],
      [
        0,
        3,
        4,
        43,
        16,
        17,
        23,
        31
      ],
      [
        1,
        10
      ],
      [
        0
      ],
      [
        14
      ],
      [
        0,
        1,
        4,
        5,
        38,
        11,
        43,
        46,
        16,
        17,
        23
      ],
      [
        6,
        14
      ],
      [
        9,
        11
      ],
      [
        0
      ],
      [
        0,
        1,
        41,
        12,
        13,
        47,
        25,
        30,
        31
      ],
      [
        37,
        22
      ],
      [
        25
      ],
      [
        20
      ],
      [
        16,
        27,
        35,
        4
      ],
      [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        9,
        11,
        12,
        19,
        22,
        24,
        25,
        26,
        27,
        28,
        30,
        31,
        32,
        47
      ],
      [
        32,
        26,
        2
      ],
      [
        32,
        2,
        3,
        6,
        26,
        30
      ],
      [
        0
      ],
      [
        0,
        3,
        28
      ],
      [
        25,
        28,
        5,
        6
      ],
      [
        8
      ],
      [
        2,
        3,
        34,
        7,
        40,
        46,
        48,
        20
      ],
      [
        32,
        2,
        3,
        5,
        21,
        26,
        27
      ],
      [
        40
      ],
      [
        17,
        4,
        31
      ],
      [
        34,
        20
      ],
      [
        5,
        37
      ],
      [
        34
      ],
      [
        10
      ],
      [
        10
      ],
      [
        0,
        3,
        5
      ],
      [
        27,
        9,
        2,
        35
      ],
      [
        9,
        28
      ],
      [
        19,
        21,
        6,
        14
      ],
      [
        2,
        35,
        3,
        39,
        7,
        47,
        17,
        21,
        23,
        27,
        30
      ],
      [
        9,
        19,
        6
      ],
      [
        0,
        34,
        4,
        37,
        38,
        43,
        16,
        22
      ],
      [
        6,
        7,
        38,
        39,
        14,
        19,
        21,
        25
      ],
      [
        19,
        21,
        14
      ],
      [
        0
      ],
      [
        31
      ],
      [
        19,
        21,
        14,
        6
      ],
      [
        1,
        2,
        3,
        6,
        9,
        41,
        11,
        12,
        42,
        14,
        47,
        25,
        28,
        30
      ],
      [
        1
      ],
      [
        48,
        34,
        19
      ],
      [
        5
      ],
      [
        16,
        46
      ],
      [
        41,
        13
      ],
      [
        5,
        6
      ],
      [
        6,
        8,
        13,
        16,
        21
      ],
      [
        47
      ],
      [
        9,
        37,
        22
      ],
      [
        0,
        37,
        5,
        22,
        28
      ],
      [
        19,
        5
      ],
      [
        0,
        8,
        17,
        23
      ],
      [
        34,
        31
      ],
      [
        20
      ],
      [
        42,
        7
      ],
      [
        3,
        30,
        39
      ],
      [
        40,
        3,
        7
      ],
      [
        21
      ],
      [
        20
      ],
      [
        20
      ],
      [
        34,
        7
      ],
      [
        17,
        4,
        46,
        31
      ],
      [
        5,
        6,
        14,
        19,
        21,
        25
      ],
      [
        0,
        37,
        16,
        17,
        22,
        23
      ],
      [
        22
      ],
      [
        32,
        26
      ],
      [
        42
      ],
      [
        1
      ],
      [
        34,
        3
      ],
      [
        0,
        1,
        3,
        38,
        40,
        9,
        41,
        8,
        12,
        48,
        16,
        21,
        25,
        30
      ],
      [
        25,
        3,
        20,
        31
      ],
      [
        1,
        2,
        34,
        7,
        41,
        10,
        12,
        13,
        21
      ],
      [
        32,
        2,
        34,
        48,
        22,
        26
      ],
      [
        48,
        25,
        34
      ],
      [
        1
      ],
      [
        21,
        38
      ],
      [
        25,
        6
      ],
      [
        42,
        39
      ],
      [
        2,
        3
      ],
      [
        35,
        3,
        4,
        5,
        7,
        6,
        48,
        27
      ],
      [
        25
      ],
      [
        14
      ],
      [
        9,
        3,
        6
      ],
      [
        34,
        4,
        12,
        47,
        31
      ],
      [
        6,
        38,
        7
      ],
      [
        5
      ],
      [
        4,
        37,
        6,
        5,
        21,
        22
      ],
      [
        2,
        3,
        4,
        6,
        16,
        23
      ],
      [
        4,
        38,
        8,
        9,
        23,
        31
      ],
      [
        19,
        39
      ],
      [
        6,
        39,
        21,
        25,
        28
      ],
      [
        3,
        8,
        9,
        47,
        16,
        19,
        24,
        30
      ],
      [
        5
      ],
      [
        32,
        26,
        37
      ],
      [
        0,
        2,
        48,
        16,
        24,
        25
      ],
      [
        9,
        37
      ],
      [
        0,
        25,
        31
      ],
      [
        0,
        35,
        3,
        6,
        7
      ],
      [
        13,
        6
      ],
      [
        34,
        5
      ],
      [
        32,
        0,
        2
      ],
      [
        9,
        42
      ],
      [
        14
      ],
      [
        0,
        13,
        37
      ],
      [
        1,
        4,
        8,
        10,
        12,
        13,
        47,
        16,
        17,
        30
      ]
    ]
  }
};

    // Curated Matte Color System
    const COLORS = {
      violet: '#8B5CF6',
      teal: '#14B8A6',
      amber: '#F59E0B',
      coral: '#F97373',
      cyan: '#22D3EE',
      indigo: '#6366F1',
      emerald: '#10B981',
      slate: '#71717A'
    };

    // Coordinated Categorical Palette for Multi-Series Bars and Donut
    const PALETTE_SEQ = [
      '#8B5CF6', '#14B8A6', '#F59E0B', '#22D3EE', '#F97373',
      '#6366F1', '#10B981', '#EC4899', '#38BDF8', '#A78BFA'
    ];

    // Consistent Model Class Palette across DT, NB, Confusion Matrices
    const CLASS_PALETTE = {
      Low: '#F97373',     // Coral
      Medium: '#F59E0B',  // Amber
      High: '#14B8A6'     // Teal
    };

    // Consistent Customer Cluster Palette across K-Means & Hierarchical
    const CLUSTER_PALETTE = [
      '#8B5CF6', // Cluster 1: Violet
      '#14B8A6', // Cluster 2: Teal
      '#F59E0B', // Cluster 3: Amber
      '#22D3EE'  // Cluster 4: Cyan
    ];

    let CURRENT_TAB = 'overview';
    const CHARTS = {};

    const $ = id => document.getElementById(id);
    const fmt = n => Math.abs(n) >= 1e6 ? (n/1e6).toFixed(2) + 'M' : Math.abs(n) >= 1e3 ? (n/1e3).toFixed(1) + 'K' : Number(n).toLocaleString();
    const fmtGbp = n => '£' + fmt(n);

    function createChart(id, config) {
      if (CHARTS[id]) { CHARTS[id].destroy(); }
      const ctx = $(id);
      if (!ctx) return;
      const isDark = document.documentElement.getAttribute('data-theme') !== 'light';
      const textColor = isDark ? '#A1A1AA' : '#52525B';
      const gridColor = isDark ? 'rgba(255, 255, 255, 0.05)' : 'rgba(0, 0, 0, 0.05)';

      config.options = Object.assign({
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
            labels: {
              color: textColor,
              font: { family: 'Inter', size: 11 },
              boxWidth: 12,
              padding: 14
            }
          },
          tooltip: {
            backgroundColor: isDark ? '#1C1C27' : '#FFFFFF',
            titleColor: isDark ? '#F4F4F5' : '#09090B',
            bodyColor: isDark ? '#A1A1AA' : '#52525B',
            borderColor: isDark ? '#2B2B38' : '#E2E8F0',
            borderWidth: 1,
            padding: 10,
            cornerRadius: 6,
            titleFont: { family: 'Outfit', size: 12.5, weight: '600' },
            bodyFont: { family: 'Inter', size: 11.5 }
          }
        },
        scales: config.options && config.options.scales ? config.options.scales : undefined
      }, config.options || {});

      // Apply consistent grid & tick styling if scales exist
      if (config.options.scales) {
        ['x', 'y'].forEach(axis => {
          if (config.options.scales[axis]) {
            config.options.scales[axis].grid = Object.assign({ color: gridColor }, config.options.scales[axis].grid || {});
            config.options.scales[axis].ticks = Object.assign({ color: textColor, font: { family: 'Inter', size: 10.5 } }, config.options.scales[axis].ticks || {});
            if (config.options.scales[axis].title) {
              config.options.scales[axis].title.color = textColor;
              config.options.scales[axis].title.font = { family: 'Inter', size: 11, weight: '500' };
            }
          }
        });
      }

      CHARTS[id] = new Chart(ctx, config);
    }

    // Theme Switcher
    $('themeBtn').onclick = () => {
      const current = document.documentElement.getAttribute('data-theme');
      const next = current === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      $('themeLabel').textContent = next.charAt(0).toUpperCase() + next.slice(1);
      renderTab(CURRENT_TAB);
    };

    // Navigation Wiring
    document.querySelectorAll('aside nav button').forEach(btn => {
      btn.onclick = () => {
        document.querySelectorAll('aside nav button').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        CURRENT_TAB = btn.dataset.tab;
        renderTab(CURRENT_TAB);
      };
    });

    function renderTab(tab) {
      const mainElem = document.querySelector('main');
      if (mainElem) mainElem.scrollTop = 0;
      $('toolbar').style.display = 'flex';
      $('cardsGrid').innerHTML = '';
      $('kpiGrid').innerHTML = '';

      switch(tab) {
        case 'overview': renderOverview(); break;
        case 'eda': renderEDA(); break;
        case 'regression': renderRegression(); break;
        case 'decision_tree': renderDecisionTree(); break;
        case 'naive_bayes': renderNaiveBayes(); break;
        case 'kmeans': renderKMeans(); break;
        case 'hierarchical': renderHierarchical(); break;
        case 'apriori': renderApriori(); break;
      }
    }

    // =============================================================
    // VIEW 1: EXECUTIVE OVERVIEW
    // =============================================================
    function renderOverview() {
      $('pageTitle').textContent = "Executive Overview";
      $('pageDesc').textContent = "High-level transactional volume, market concentrations, and verified dataset profile.";
      $('sectionBadge').textContent = "Enterprise Overview";

      $('toolbar').innerHTML = `
        <div class="control-item">
          <label>Breakdown Slices</label>
          <select id="ovDimension">
            <option value="countries">Country Markets</option>
            <option value="products">Top Products</option>
            <option value="day_of_week">Day of Week Pattern</option>
            <option value="monthly">Monthly Seasonality</option>
          </select>
        </div>
        <div class="control-item">
          <label>Metric</label>
          <select id="ovMetric">
            <option value="1">Revenue (£)</option>
            <option value="2">Units Sold</option>
            <option value="3">Invoices</option>
          </select>
        </div>
        <div class="status-badge" style="margin-left:auto">
          <span>ETL: Zero Cancellations ('C') & Positive Quantities/Prices</span>
        </div>
      `;

      $('kpiGrid').innerHTML = `
        <div class="kpi-card">
          <span class="kpi-label">Cleaned Revenue</span>
          <span class="kpi-val" style="color:var(--teal)">${fmtGbp(D.meta.total_revenue)}</span>
          <span class="kpi-sub">530,104 Valid Invoices</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Active Customers</span>
          <span class="kpi-val">${D.meta.customers.toLocaleString()}</span>
          <span class="kpi-sub">Avg Spend: £${(D.meta.total_revenue / D.meta.customers).toFixed(0)}</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Unique Products</span>
          <span class="kpi-val">${D.meta.products.toLocaleString()}</span>
          <span class="kpi-sub">Catalog StockCodes</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Global Markets</span>
          <span class="kpi-val">${D.meta.countries}</span>
          <span class="kpi-sub">UK Dominant (>85%)</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Median Tertiles</span>
          <span class="kpi-val">£5 – £15</span>
          <span class="kpi-sub">q1 = £5.00 · q2 = £15.00</span>
        </div>
      `;

      $('cardsGrid').innerHTML = `
        <div class="card">
          <div class="card-header">
            <div>
              <h3>Performance Ranking</h3>
              <p>Top items ranked across selected dimension</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cOv1"></canvas></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Market Share Distribution</h3>
              <p>Top markets vs remaining aggregate</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cOv2"></canvas></div>
        </div>

        <div class="card wide">
          <div class="card-header">
            <div>
              <h3>Cleaning & Preprocessing Verification Audit</h3>
              <p>Raw vs Cleaned data verification across analytic models</p>
            </div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Validation Step</th>
                  <th>Raw Dataset</th>
                  <th>Cleaning Filter</th>
                  <th>Verified Cleaned</th>
                  <th>Methodology Status</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><b>Total Transaction Rows</b></td>
                  <td>541,909</td>
                  <td>Strip cancelled 'C' invoices (9,288) & Qty/Price &le; 0</td>
                  <td><b>530,104</b></td>
                  <td><span style="color:var(--teal)">Verified Clean Baseline</span></td>
                </tr>
                <tr>
                  <td><b>Customer Segmentation</b></td>
                  <td>135,080 missing CustomerID</td>
                  <td>Drop records missing CustomerID</td>
                  <td><b>4,338 Unique Customers</b></td>
                  <td><span style="color:var(--teal)">Complete Customer Profile</span></td>
                </tr>
                <tr>
                  <td><b>Transaction Tertiles</b></td>
                  <td>530,104 line items</td>
                  <td>q1 = 33.3%, q2 = 66.7% percentiles</td>
                  <td><b>Low &le; £5, Med &le; £15, High &gt; £15</b></td>
                  <td><span style="color:var(--teal)">Discretized Target</span></td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      `;

      function updateOvCharts() {
        const dim = $('ovDimension').value;
        const metIdx = parseInt($('ovMetric').value);
        const dataArr = D.lab3_eda[dim] || D.lab3_eda.countries;
        const metName = $('ovMetric').selectedOptions[0].text;

        const topSlice = dataArr.slice(0, 8);
        createChart('cOv1', {
          type: 'bar',
          data: {
            labels: topSlice.map(x => x[0].length > 20 ? x[0].slice(0, 20) + '...' : x[0]),
            datasets: [{
              label: metName,
              data: topSlice.map(x => x[metIdx]),
              backgroundColor: PALETTE_SEQ.slice(0, topSlice.length),
              borderRadius: 4
            }]
          },
          options: {
            indexAxis: 'y',
            plugins: { legend: { display: false } }
          }
        });

        // Market share donut
        const ctry = D.lab3_eda.countries;
        const ctop = ctry.slice(0, 5);
        const crest = ctry.slice(5).reduce((acc, c) => acc + c[metIdx], 0);
        createChart('cOv2', {
          type: 'doughnut',
          data: {
            labels: [...ctop.map(x => x[0]), 'Others'],
            datasets: [{
              data: [...ctop.map(x => x[metIdx]), crest],
              backgroundColor: ['#8B5CF6', '#14B8A6', '#F59E0B', '#22D3EE', '#F97373', '#3F3F46'],
              borderWidth: 0
            }]
          },
          options: { cutout: '65%', plugins: { legend: { position: 'right' } } }
        });
      }

      $('ovDimension').onchange = updateOvCharts;
      $('ovMetric').onchange = updateOvCharts;
      updateOvCharts();
    }

    // =============================================================
    // VIEW 2: EXPLORATORY ANALYSIS
    // =============================================================
    function renderEDA() {
      $('pageTitle').textContent = "Exploratory Analysis";
      $('pageDesc').textContent = "Sales revenue, transaction volume, product trends, geographic performance, and seasonal distributions.";
      $('sectionBadge').textContent = "Exploratory Analytics";

      $('toolbar').innerHTML = `
        <div class="control-item">
          <label>Dimension</label>
          <select id="edaDim">
            <option value="products">Top Products</option>
            <option value="countries">Top Countries</option>
            <option value="customers">Top Customers</option>
            <option value="hours">Hour of Day</option>
          </select>
        </div>
        <div class="control-item">
          <label>Metric</label>
          <select id="edaMet">
            <option value="1">Sales Revenue (£)</option>
            <option value="2">Quantity Sold</option>
            <option value="3">Orders Count</option>
          </select>
        </div>
        <div class="control-item">
          <label>Top N Items</label>
          <input type="number" id="edaN" value="10" min="5" max="30">
        </div>
      `;

      $('kpiGrid').innerHTML = `
        <div class="kpi-card">
          <span class="kpi-label">Top Selling Item</span>
          <span class="kpi-val" style="font-size:16px">${D.lab3_eda.products[0][0].slice(0, 22)}</span>
          <span class="kpi-sub">Revenue: £${fmt(D.lab3_eda.products[0][1])}</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Peak Sales Month</span>
          <span class="kpi-val" style="color:var(--teal)">Nov 2011</span>
          <span class="kpi-sub">Holiday Season Surge</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Peak Shopping Hour</span>
          <span class="kpi-val">12:00 PM</span>
          <span class="kpi-sub">Midday E-Commerce Spike</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Top Customer Revenue</span>
          <span class="kpi-val">£${fmt(D.lab3_eda.customers[0][1])}</span>
          <span class="kpi-sub">Customer ID: ${D.lab3_eda.customers[0][0]}</span>
        </div>
      `;

      $('cardsGrid').innerHTML = `
        <div class="card">
          <div class="card-header">
            <div>
              <h3>Ranked Dimensional Analysis</h3>
              <p>Top items ranked by selected measure</p>
            </div>
          </div>
          <div class="chart-container tall"><canvas id="cEda1"></canvas></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Monthly Sales Trend (Dec 2010 – Dec 2011)</h3>
              <p>Revenue and seasonality curve over 13 month timeline</p>
            </div>
          </div>
          <div class="chart-container tall"><canvas id="cEda2"></canvas></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Day-of-Week Shopping Patterns</h3>
              <p>Trading volumes across weekdays and Sunday</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cEda3"></canvas></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Transaction Value Distribution (Log10 £)</h3>
              <p>Frequency of line items across low, medium, and high price tiers</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cEda4"></canvas></div>
        </div>
      `;

      function updateEda() {
        const dim = $('edaDim').value;
        const met = parseInt($('edaMet').value);
        const topN = parseInt($('edaN').value) || 10;
        const metName = $('edaMet').selectedOptions[0].text;

        const sliceData = D.lab3_eda[dim].slice(0, topN);
        createChart('cEda1', {
          type: 'bar',
          data: {
            labels: sliceData.map(x => x[0].length > 22 ? x[0].slice(0, 22) + '...' : x[0]),
            datasets: [{
              label: metName,
              data: sliceData.map(x => x[met]),
              backgroundColor: sliceData.map((_, i) => PALETTE_SEQ[i % PALETTE_SEQ.length]),
              borderRadius: 4
            }]
          },
          options: { indexAxis: 'y', plugins: { legend: { display: false } } }
        });

        // Monthly Trend
        const m = D.lab3_eda.monthly;
        createChart('cEda2', {
          type: 'line',
          data: {
            labels: m.map(x => x[0]),
            datasets: [{
              label: 'Monthly Revenue (£)',
              data: m.map(x => x[1]),
              borderColor: COLORS.teal,
              backgroundColor: 'rgba(20, 184, 166, 0.08)',
              fill: true,
              tension: 0.3,
              pointBackgroundColor: COLORS.teal,
              pointRadius: 4
            }]
          },
          options: { plugins: { legend: { display: false } } }
        });

        // Day of week
        const d = D.lab3_eda.day_of_week;
        createChart('cEda3', {
          type: 'bar',
          data: {
            labels: d.map(x => x[0]),
            datasets: [{
              label: 'Sales Revenue (£)',
              data: d.map(x => x[1]),
              backgroundColor: ['#8B5CF6', '#8B5CF6', '#8B5CF6', '#22D3EE', '#22D3EE', '#F59E0B'],
              borderRadius: 4
            }]
          },
          options: { plugins: { legend: { display: false } } }
        });

        // Value Histogram with tertile coloring
        const histBins = ['£0.1', '£0.5', '£1.5', '£4', '£10', '£25', '£65', '£160', '£400', '£1K', '£2.5K', '£10K+'];
        const binColors = histBins.map((_, i) => i < 4 ? COLORS.coral : i < 7 ? COLORS.amber : COLORS.teal);
        createChart('cEda4', {
          type: 'bar',
          data: {
            labels: histBins,
            datasets: [{
              label: 'Transactions',
              data: D.lab3_eda.value_histogram,
              backgroundColor: binColors,
              borderRadius: 4
            }]
          },
          options: { plugins: { legend: { display: false } } }
        });
      }

      $('edaDim').onchange = updateEda;
      $('edaMet').onchange = updateEda;
      $('edaN').oninput = updateEda;
      updateEda();
    }

    // =============================================================
    // VIEW 3: LINEAR REGRESSION
    // =============================================================
    function renderRegression() {
      $('pageTitle').textContent = "Linear Regression";
      $('pageDesc').textContent = "Modeling transaction SalesAmount using Quantity, UnitPrice, and Month with train/test validation.";
      $('sectionBadge').textContent = "Predictive Regression";

      const r = D.lab4_regression;

      $('toolbar').innerHTML = `
        <div class="status-badge">
          <span>Split: 80% Train / 20% Test · Random State: 42</span>
        </div>
      `;

      $('kpiGrid').innerHTML = `
        <div class="kpi-card">
          <span class="kpi-label">SLR R² Score</span>
          <span class="kpi-val">${r.slr.r2.toFixed(4)}</span>
          <span class="kpi-sub">Feature: Quantity Only</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">MLR R² Score</span>
          <span class="kpi-val" style="color:var(--teal)">${r.mlr.r2.toFixed(4)}</span>
          <span class="kpi-sub">+${((r.mlr.r2 - r.slr.r2)*100).toFixed(1)}% variance explained</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">SLR Test MSE</span>
          <span class="kpi-val">${r.slr.mse.toLocaleString()}</span>
          <span class="kpi-sub">Mean Squared Error</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">MLR Test MSE</span>
          <span class="kpi-val">${r.mlr.mse.toLocaleString()}</span>
          <span class="kpi-sub">Lower Error = Better Fit</span>
        </div>
      `;

      $('cardsGrid').innerHTML = `
        <div class="card wide">
          <div class="card-header">
            <div>
              <h3>Interactive Transaction Sales Predictor</h3>
              <p>Input new transaction parameters to compute regression predictions in real time</p>
            </div>
          </div>
          <div class="predictor-box">
            <div class="predictor-inputs">
              <div class="pred-field">
                <label>Quantity</label>
                <input type="number" id="regInQ" value="10" min="1" max="1000">
              </div>
              <div class="pred-field">
                <label>Unit Price (£)</label>
                <input type="number" id="regInP" value="5" step="0.5" min="0.1">
              </div>
              <div class="pred-field">
                <label>Month (1–12)</label>
                <input type="number" id="regInM" value="12" min="1" max="12">
              </div>
              <div class="pred-result-card" style="margin-left:auto">
                <div>
                  <div style="font-size:10.5px;color:var(--tx-muted);font-weight:600;text-transform:uppercase">Predicted Sales Amount</div>
                  <div class="pred-badge" id="regPredOut" style="color:var(--teal)">£21.35</div>
                </div>
              </div>
            </div>
            <div class="callout teal" id="regEqCallout">
              <b>MLR Model Formula:</b> SalesAmount ≈ -2.4599 + 1.5818 &times; Quantity + 1.1346 &times; UnitPrice + 0.1931 &times; Month.
              <br>Model Benchmark: Input (10, 5, 12) yields <b>£21.31</b>.
            </div>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Actual vs Predicted Sales</h3>
              <p>Test observations vs predicted values with diagonal reference line</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cReg1"></canvas></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Model Performance Comparison</h3>
              <p>Simple Linear Regression vs Multiple Linear Regression</p>
            </div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Model</th>
                  <th>Features Used</th>
                  <th>R² Score</th>
                  <th>Mean Squared Error</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td><b>Simple Linear Regression</b></td>
                  <td>Quantity</td>
                  <td>${r.slr.r2.toFixed(4)}</td>
                  <td>${r.slr.mse.toLocaleString()}</td>
                </tr>
                <tr>
                  <td><b>Multiple Linear Regression</b></td>
                  <td>Quantity, UnitPrice, Month</td>
                  <td><b style="color:var(--teal)">${r.mlr.r2.toFixed(4)}</b></td>
                  <td><b>${r.mlr.mse.toLocaleString()}</b></td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="callout amber">
            <b>Evaluation Conclusion:</b> Adding <code>UnitPrice</code> and <code>Month</code> substantially reduces MSE and increases variance explained ($R^2$), establishing multivariate regression as the superior estimator.
          </div>
        </div>
      `;

      function updateRegCalc() {
        const q = parseFloat($('regInQ').value) || 0;
        const p = parseFloat($('regInP').value) || 0;
        const m = parseFloat($('regInM').value) || 0;
        const predVal = r.mlr.intercept + r.mlr.coefs.Quantity * q + r.mlr.coefs.UnitPrice * p + r.mlr.coefs.Month * m;
        $('regPredOut').textContent = '£' + predVal.toFixed(2);
      }

      $('regInQ').oninput = updateRegCalc;
      $('regInP').oninput = updateRegCalc;
      $('regInM').oninput = updateRegCalc;

      const pts = r.actual_vs_pred;
      createChart('cReg1', {
        type: 'scatter',
        data: {
          datasets: [
            {
              label: 'Actual vs Predicted',
              data: pts.map(p => ({ x: p[0], y: p[1] })),
              backgroundColor: 'rgba(139, 92, 246, 0.4)',
              pointRadius: 3
            },
            {
              type: 'line',
              label: 'Ideal Reference (y = x)',
              data: [{ x: 0, y: 0 }, { x: 450, y: 450 }],
              borderColor: COLORS.teal,
              borderDash: [5, 5],
              pointRadius: 0,
              borderWidth: 1.5
            }
          ]
        },
        options: {
          scales: {
            x: { title: { display: true, text: 'Actual Sales (£)' }, max: 500 },
            y: { title: { display: true, text: 'Predicted Sales (£)' }, max: 500 }
          },
          plugins: { legend: { position: 'top' } }
        }
      });
    }

    // =============================================================
    // VIEW 4: DECISION TREE
    // =============================================================
    function renderDecisionTree() {
      $('pageTitle').textContent = "Decision Tree Classifier";
      $('pageDesc').textContent = "Predicting transaction value tiers (Low / Medium / High) using entropy-based decision splits.";
      $('sectionBadge').textContent = "Supervised Tree Model";

      const dt = D.lab5_decision_tree;

      $('toolbar').innerHTML = `
        <div class="status-badge">
          <span>Criterion: Entropy · Max Depth: 5 · Stratified 80/20 Split</span>
        </div>
      `;

      $('kpiGrid').innerHTML = `
        <div class="kpi-card">
          <span class="kpi-label">Tree Accuracy</span>
          <span class="kpi-val" style="color:var(--teal)">${(dt.accuracy * 100).toFixed(1)}%</span>
          <span class="kpi-sub">High Discretization Precision</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Criterion</span>
          <span class="kpi-val" style="font-size:17px">Information Gain</span>
          <span class="kpi-sub">Entropy Minimization</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Tree Max Depth</span>
          <span class="kpi-val">5 Levels</span>
          <span class="kpi-sub">Controlled Overfitting</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Target Tertiles</span>
          <span class="kpi-val">Low, Med, High</span>
          <span class="kpi-sub">q1 = £5 · q2 = £15 cutoffs</span>
        </div>
      `;

      $('cardsGrid').innerHTML = `
        <div class="card wide">
          <div class="card-header">
            <div>
              <h3>Interactive Decision Tree Inference</h3>
              <p>Test new transaction inputs against the decision tree rules</p>
            </div>
          </div>
          <div class="predictor-box">
            <div class="predictor-inputs">
              <div class="pred-field">
                <label>Quantity</label>
                <input type="number" id="dtInQ" value="10" min="1">
              </div>
              <div class="pred-field">
                <label>UnitPrice (£)</label>
                <input type="number" id="dtInP" value="5" min="0.1" step="0.5">
              </div>
              <div class="pred-field">
                <label>Month (1–12)</label>
                <input type="number" id="dtInM" value="12" min="1" max="12">
              </div>
              <div class="pred-result-card" style="margin-left:auto">
                <div>
                  <div style="font-size:10.5px;color:var(--tx-muted);font-weight:600;text-transform:uppercase">Predicted Category</div>
                  <div class="pred-badge" id="dtPredOut" style="color:var(--teal)">High</div>
                </div>
              </div>
            </div>
            <div class="callout teal" id="dtPathCallout">
              <b>Model Verification:</b> Transaction with Quantity=10, UnitPrice=5 (SalesAmount = £50 > £15) is classified as <b>High</b> value tier.
            </div>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Confusion Matrix Heatmap</h3>
              <p>Actual vs. Predicted class counts on stratified test partition</p>
            </div>
          </div>
          <div class="cm-grid">
            <div class="cm-cell header"></div>
            <div class="cm-cell header" style="color:var(--coral)">Pred Low</div>
            <div class="cm-cell header" style="color:var(--amber)">Pred Med</div>
            <div class="cm-cell header" style="color:var(--teal)">Pred High</div>

            <div class="cm-cell header" style="color:var(--coral)">Act Low</div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.4)">
              <span class="cm-val">${dt.confusion_matrix[0][0].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.08)">
              <span class="cm-val">${dt.confusion_matrix[0][1].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.02)">
              <span class="cm-val">${dt.confusion_matrix[0][2].toLocaleString()}</span>
            </div>

            <div class="cm-cell header" style="color:var(--amber)">Act Med</div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.06)">
              <span class="cm-val">${dt.confusion_matrix[1][0].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.4)">
              <span class="cm-val">${dt.confusion_matrix[1][1].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.05)">
              <span class="cm-val">${dt.confusion_matrix[1][2].toLocaleString()}</span>
            </div>

            <div class="cm-cell header" style="color:var(--teal)">Act High</div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.02)">
              <span class="cm-val">${dt.confusion_matrix[2][0].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.04)">
              <span class="cm-val">${dt.confusion_matrix[2][1].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.4)">
              <span class="cm-val">${dt.confusion_matrix[2][2].toLocaleString()}</span>
            </div>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Feature Importance & Decision Split Hierarchy</h3>
              <p>Split thresholds driving entropy reduction</p>
            </div>
          </div>
          <div class="chart-container short"><canvas id="cDtFeat"></canvas></div>
          <div class="tree-diagram">
            <div class="tree-node-line"><span class="tree-branch">Root Node:</span> If <b>Quantity &le; 2.50</b></div>
            <div class="tree-node-line" style="padding-left:14px"><span class="tree-branch">&#9500;&#9472;</span> If <b>UnitPrice &le; 2.55</b> &rarr; <span class="tree-leaf-low">Class Low</span></div>
            <div class="tree-node-line" style="padding-left:14px"><span class="tree-branch">&#9492;&#9472;</span> If <b>UnitPrice &gt; 2.55</b> &rarr; Check Month seasonality</div>
            <div class="tree-node-line"><span class="tree-branch">Branch Node:</span> If <b>Quantity &gt; 2.50</b></div>
            <div class="tree-node-line" style="padding-left:14px"><span class="tree-branch">&#9500;&#9472;</span> If <b>UnitPrice &le; 1.65</b> &rarr; <span class="tree-leaf-med">Class Medium</span></div>
            <div class="tree-node-line" style="padding-left:14px"><span class="tree-branch">&#9492;&#9472;</span> If <b>UnitPrice &gt; 1.65</b> &rarr; <span class="tree-leaf-high">Class High</span></div>
          </div>
        </div>
      `;

      function evaluateTree(node, q, p, m) {
        if (node.leaf) return node.class;
        const val = node.feature === 'Quantity' ? q : node.feature === 'UnitPrice' ? p : m;
        return val <= node.threshold ? evaluateTree(node.left, q, p, m) : evaluateTree(node.right, q, p, m);
      }

      function updateDtPredict() {
        const q = parseFloat($('dtInQ').value) || 0;
        const p = parseFloat($('dtInP').value) || 0;
        const m = parseFloat($('dtInM').value) || 0;
        const res = evaluateTree(dt.tree_structure, q, p, m);
        $('dtPredOut').textContent = res;
        $('dtPredOut').style.color = CLASS_PALETTE[res] || 'var(--tx)';
      }

      $('dtInQ').oninput = updateDtPredict;
      $('dtInP').oninput = updateDtPredict;
      $('dtInM').oninput = updateDtPredict;

      createChart('cDtFeat', {
        type: 'bar',
        data: {
          labels: Object.keys(dt.feature_importance),
          datasets: [{
            label: 'Importance',
            data: Object.values(dt.feature_importance),
            backgroundColor: [COLORS.teal, COLORS.violet, COLORS.slate],
            borderRadius: 4
          }]
        },
        options: { indexAxis: 'y', plugins: { legend: { display: false } } }
      });
    }

    // =============================================================
    // VIEW 5: NAIVE BAYES
    // =============================================================
    function renderNaiveBayes() {
      $('pageTitle').textContent = "Naive Bayes Classification";
      $('pageDesc').textContent = "Probabilistic classification into sales tiers using Bayes' rule and Gaussian feature distributions.";
      $('sectionBadge').textContent = "Probabilistic Classifier";

      const nb = D.lab6_naive_bayes;

      $('toolbar').innerHTML = `
        <div class="status-badge">
          <span>Split: 70% Train / 30% Test · Stratified on Sales Category</span>
        </div>
      `;

      $('kpiGrid').innerHTML = `
        <div class="kpi-card">
          <span class="kpi-label">Model Accuracy</span>
          <span class="kpi-val">${(nb.accuracy * 100).toFixed(1)}%</span>
          <span class="kpi-sub">Overall Test Performance</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Prior Distribution</span>
          <span class="kpi-val">33.3% Each</span>
          <span class="kpi-sub">Balanced Tertile Classes</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Assumed Likelihood</span>
          <span class="kpi-val" style="font-size:17px">Gaussian P(X|C)</span>
          <span class="kpi-sub">Continuous Bell Curves</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Target Classes</span>
          <span class="kpi-val">Low, Med, High</span>
          <span class="kpi-sub">q1 = £5 · q2 = £15 cutoffs</span>
        </div>
      `;

      $('cardsGrid').innerHTML = `
        <div class="card wide">
          <div class="card-header">
            <div>
              <h3>Interactive Naive Bayes Inference</h3>
              <p>Computes log-likelihoods and exact posterior probabilities in real time</p>
            </div>
          </div>
          <div class="predictor-box">
            <div class="predictor-inputs">
              <div class="pred-field">
                <label>Quantity</label>
                <input type="number" id="nbInQ" value="10" min="1">
              </div>
              <div class="pred-field">
                <label>UnitPrice (£)</label>
                <input type="number" id="nbInP" value="5" min="0.1" step="0.5">
              </div>
              <div class="pred-field">
                <label>Month (1–12)</label>
                <input type="number" id="nbInM" value="12" min="1" max="12">
              </div>
              <div class="pred-result-card" style="margin-left:auto">
                <div>
                  <div style="font-size:10.5px;color:var(--tx-muted);font-weight:600;text-transform:uppercase">Predicted Category</div>
                  <div class="pred-badge" id="nbPredOut" style="color:var(--amber)">Medium</div>
                </div>
              </div>
            </div>
            <div class="callout teal" id="nbProbCallout">
              <b>Model Verification:</b> Test input (Q=10, P=5, M=12) posterior:
              <b>Low: 2.2%</b> · <b style="color:var(--amber)">Medium: 97.6%</b> · <b>High: 0.2%</b>.
            </div>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Confusion Matrix Heatmap</h3>
              <p>Evaluation on 30% stratified test partition</p>
            </div>
          </div>
          <div class="cm-grid">
            <div class="cm-cell header"></div>
            <div class="cm-cell header" style="color:var(--coral)">Pred Low</div>
            <div class="cm-cell header" style="color:var(--amber)">Pred Med</div>
            <div class="cm-cell header" style="color:var(--teal)">Pred High</div>

            <div class="cm-cell header" style="color:var(--coral)">Act Low</div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.4)">
              <span class="cm-val">${nb.confusion_matrix[0][0].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.15)">
              <span class="cm-val">${nb.confusion_matrix[0][1].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.05)">
              <span class="cm-val">${nb.confusion_matrix[0][2].toLocaleString()}</span>
            </div>

            <div class="cm-cell header" style="color:var(--amber)">Act Med</div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.15)">
              <span class="cm-val">${nb.confusion_matrix[1][0].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.35)">
              <span class="cm-val">${nb.confusion_matrix[1][1].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.08)">
              <span class="cm-val">${nb.confusion_matrix[1][2].toLocaleString()}</span>
            </div>

            <div class="cm-cell header" style="color:var(--teal)">Act High</div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.05)">
              <span class="cm-val">${nb.confusion_matrix[2][0].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.12)">
              <span class="cm-val">${nb.confusion_matrix[2][1].toLocaleString()}</span>
            </div>
            <div class="cm-cell" style="background:rgba(20, 184, 166, 0.4)">
              <span class="cm-val">${nb.confusion_matrix[2][2].toLocaleString()}</span>
            </div>
          </div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Class Feature Gaussian Means (&mu;)</h3>
              <p>Mean values across Low, Medium, and High classes</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cNbMeans"></canvas></div>
        </div>
      `;

      function calcNbProbs(q, p, m) {
        const x = [q, p, m];
        const params = nb.model_parameters;
        const logProbs = [];
        for (let c = 0; c < 3; c++) {
          let lp = Math.log(params.priors[c]);
          for (let f = 0; f < 3; f++) {
            const mu = params.means[c][f];
            const v = params.vars[c][f];
            lp += -0.5 * Math.log(2 * Math.PI * v) - Math.pow(x[f] - mu, 2) / (2 * v);
          }
          logProbs.push(lp);
        }
        const maxLp = Math.max(...logProbs);
        const exps = logProbs.map(lp => Math.exp(lp - maxLp));
        const sumExp = exps.reduce((a, b) => a + b, 0);
        return exps.map(e => e / sumExp);
      }

      function updateNbPredict() {
        const q = parseFloat($('nbInQ').value) || 0;
        const p = parseFloat($('nbInP').value) || 0;
        const m = parseFloat($('nbInM').value) || 0;
        const probs = calcNbProbs(q, p, m);
        const maxIdx = probs.indexOf(Math.max(...probs));
        const resClass = nb.classes[maxIdx];

        $('nbPredOut').textContent = resClass;
        $('nbPredOut').style.color = CLASS_PALETTE[resClass] || 'var(--tx)';
        $('nbProbCallout').innerHTML = `<b>Posterior Probabilities:</b> Low: ${(probs[0]*100).toFixed(1)}% · Medium: ${(probs[1]*100).toFixed(1)}% · High: ${(probs[2]*100).toFixed(1)}%`;
      }

      $('nbInQ').oninput = updateNbPredict;
      $('nbInP').oninput = updateNbPredict;
      $('nbInM').oninput = updateNbPredict;

      createChart('cNbMeans', {
        type: 'bar',
        data: {
          labels: ['Quantity', 'UnitPrice', 'Month'],
          datasets: [
            { label: 'Low Class Mean', data: nb.model_parameters.means[0], backgroundColor: CLASS_PALETTE.Low, borderRadius: 4 },
            { label: 'Medium Class Mean', data: nb.model_parameters.means[1], backgroundColor: CLASS_PALETTE.Medium, borderRadius: 4 },
            { label: 'High Class Mean', data: nb.model_parameters.means[2], backgroundColor: CLASS_PALETTE.High, borderRadius: 4 }
          ]
        },
        options: { plugins: { legend: { position: 'top' } } }
      });
    }

    // =============================================================
    // VIEW 6: K-MEANS CLUSTERING
    // =============================================================
    function renderKMeans() {
      $('pageTitle').textContent = "K-Means Clustering";
      $('pageDesc').textContent = "Customer behavioral segmentation using TotalSpending, TotalOrders, TotalQuantity, AverageOrderValue, and UniqueProducts.";
      $('sectionBadge').textContent = "Customer Segmentation";

      const km = D.lab7_kmeans;

      $('toolbar').innerHTML = `
        <div class="control-item">
          <label>Number of Clusters (K)</label>
          <input type="number" id="kmK" value="3" min="2" max="8" style="width:70px">
        </div>
        <div class="control-item">
          <label>X Axis Feature</label>
          <select id="kmAxisX">
            <option value="orders">Total Orders</option>
            <option value="quantity">Total Quantity</option>
            <option value="unique_prods">Unique Products</option>
          </select>
        </div>
        <div class="control-item">
          <label>Y Axis Feature</label>
          <select id="kmAxisY">
            <option value="spending">Total Spending (£)</option>
            <option value="order_value">Average Order Value (£)</option>
          </select>
        </div>
      `;

      $('kpiGrid').innerHTML = `
        <div class="kpi-card">
          <span class="kpi-label">Optimal Clusters (K)</span>
          <span class="kpi-val" style="color:var(--teal)">K = 3</span>
          <span class="kpi-sub">Verified via Elbow Method</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Silhouette Score</span>
          <span class="kpi-val">${km.silhouette.toFixed(3)}</span>
          <span class="kpi-sub">Cluster Separation Index</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Customers Segmented</span>
          <span class="kpi-val">4,338</span>
          <span class="kpi-sub">Complete Customer Base</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Feature Engineering</span>
          <span class="kpi-val" style="font-size:17px">log1p + Scaling</span>
          <span class="kpi-sub">StandardScaler Normalization</span>
        </div>
      `;

      $('cardsGrid').innerHTML = `
        <div class="card">
          <div class="card-header">
            <div>
              <h3>Elbow Method (WCSS vs K)</h3>
              <p>Inertia curve identifying optimal cluster count bend at K=3</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cKmElbow"></canvas></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Customer Segmentation Map (800 Sampled Clients)</h3>
              <p>2D projection of customer behavioral positions</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cKmScatter"></canvas></div>
        </div>

        <div class="card wide">
          <div class="card-header">
            <div>
              <h3>Optimal Cluster Characteristics (K=3 Summary)</h3>
              <p>Average behavioral metrics across customer segments</p>
            </div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Segment</th>
                  <th>Customers</th>
                  <th>Avg Spending (£)</th>
                  <th>Avg Orders</th>
                  <th>Avg Quantity</th>
                  <th>Avg Order Value (£)</th>
                  <th>Unique Products</th>
                </tr>
              </thead>
              <tbody>
                ${km.profiles.map(p => `
                  <tr>
                    <td><b style="color:${CLUSTER_PALETTE[p.cluster-1]}">Cluster ${p.cluster}</b></td>
                    <td>${p.size.toLocaleString()}</td>
                    <td>£${p.avg_spending.toLocaleString()}</td>
                    <td>${p.avg_orders}</td>
                    <td>${p.avg_quantity.toLocaleString()}</td>
                    <td>£${p.avg_order_value}</td>
                    <td>${p.avg_unique_products}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;

      // Elbow line chart
      createChart('cKmElbow', {
        type: 'line',
        data: {
          labels: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
          datasets: [{
            label: 'WCSS / Inertia',
            data: km.wcss,
            borderColor: COLORS.amber,
            backgroundColor: 'rgba(245, 158, 11, 0.08)',
            fill: true,
            tension: 0.2,
            pointBackgroundColor: COLORS.amber,
            pointRadius: [3, 3, 6, 3, 3, 3, 3, 3, 3, 3]
          }]
        },
        options: {
          plugins: { legend: { display: false } },
          scales: {
            x: { title: { display: true, text: 'Number of Clusters (K)' } },
            y: { title: { display: true, text: 'Within-Cluster Sum of Squares' } }
          }
        }
      });

      function updateKmScatter() {
        const ax = $('kmAxisX').value;
        const ay = $('kmAxisY').value;
        const pts = km.scatter_sample;

        const datasets = [0, 1, 2].map(c => ({
          label: 'Cluster ' + (c + 1),
          data: pts.filter(p => p.cluster === c).map(p => ({
            x: Math.log1p(p[ax]),
            y: Math.log1p(p[ay])
          })),
          backgroundColor: CLUSTER_PALETTE[c],
          pointRadius: 3
        }));

        createChart('cKmScatter', {
          type: 'scatter',
          data: { datasets },
          options: {
            scales: {
              x: { title: { display: true, text: 'log1p(' + ax + ')' } },
              y: { title: { display: true, text: 'log1p(' + ay + ')' } }
            }
          }
        });
      }

      $('kmAxisX').onchange = updateKmScatter;
      $('kmAxisY').onchange = updateKmScatter;
      updateKmScatter();
    }

    // =============================================================
    // VIEW 7: HIERARCHICAL CLUSTERING
    // =============================================================
    function renderHierarchical() {
      $('pageTitle').textContent = "Hierarchical Clustering";
      $('pageDesc').textContent = "Comparative evaluation of linkage methods: Ward, Complete, Average, and Single on customer profiles.";
      $('sectionBadge').textContent = "Linkage Benchmark";

      const h = D.lab8_hierarchical;

      $('toolbar').innerHTML = `
        <div class="control-item">
          <label>Active Linkage Method</label>
          <select id="hLink">
            <option value="ward">Ward (Variance Minimization)</option>
            <option value="complete">Complete Linkage</option>
            <option value="average">Average Linkage</option>
            <option value="single">Single Linkage</option>
          </select>
        </div>
        <div class="status-badge" style="margin-left:auto">
          <span>Clusters: K = 4 · Subspace Sample (Disclosed)</span>
        </div>
      `;

      $('kpiGrid').innerHTML = `
        <div class="kpi-card">
          <span class="kpi-label">Recommended Linkage</span>
          <span class="kpi-val" style="color:var(--teal)">Ward</span>
          <span class="kpi-sub">Balanced Segmentation</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Linkages Compared</span>
          <span class="kpi-val">4 Methods</span>
          <span class="kpi-sub">Ward, Complete, Avg, Single</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Target Clusters</span>
          <span class="kpi-val">K = 4</span>
          <span class="kpi-sub">Dendrogram Cut Point</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Comparative Metric</span>
          <span class="kpi-val" style="font-size:17px">Silhouette Score</span>
          <span class="kpi-sub">Cluster Quality Benchmark</span>
        </div>
      `;

      $('cardsGrid').innerHTML = `
        <div class="card">
          <div class="card-header">
            <div>
              <h3>Silhouette Comparison Across Linkage Methods</h3>
              <p>Comparative cluster quality benchmark across all 4 linkages</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cHSil"></canvas></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Hierarchical Merge Distance Step Progression</h3>
              <p>Height at which clusters merge in agglomerative tree</p>
            </div>
          </div>
          <div class="chart-container"><canvas id="cHDist"></canvas></div>
        </div>

        <div class="card wide">
          <div class="card-header">
            <div>
              <h3>Comparative Linkage Benchmark Summary Table</h3>
              <p>Cluster counts, silhouette scores, and cluster balance across methods</p>
            </div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>Linkage Method</th>
                  <th>Silhouette Score</th>
                  <th>Number of Clusters</th>
                  <th>Cluster Distribution (Cluster 1 / 2 / 3 / 4)</th>
                  <th>Practical Assessment</th>
                </tr>
              </thead>
              <tbody>
                ${h.linkages_benchmark.map(b => `
                  <tr>
                    <td><b>${b.linkage}</b></td>
                    <td><b style="color:${b.linkage==='Ward'?'var(--teal)':'var(--tx)'}">${b.silhouette}</b></td>
                    <td>${b.clusters}</td>
                    <td>${b.sizes.join(' · ')}</td>
                    <td>${b.linkage==='Ward' ? '<span style="color:var(--teal)">Balanced, informative customer segments (Recommended)</span>' : b.linkage==='Single' ? '<span style="color:var(--coral)">High chaining effect; single-outlier clusters</span>' : 'Intermediate grouping performance'}</td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          </div>
        </div>
      `;

      // Silhouette bar chart with distinct colors per linkage
      createChart('cHSil', {
        type: 'bar',
        data: {
          labels: h.linkages_benchmark.map(b => b.linkage),
          datasets: [{
            label: 'Silhouette Score',
            data: h.linkages_benchmark.map(b => b.silhouette),
            backgroundColor: [COLORS.teal, COLORS.violet, COLORS.amber, COLORS.cyan],
            borderRadius: 4
          }]
        },
        options: { plugins: { legend: { display: false } }, scales: { y: { min: 0, max: 0.6 } } }
      });

      function updateHDist() {
        const link = $('hLink').value;
        const targetB = h.linkages_benchmark.find(b => b.linkage.toLowerCase() === link);
        if (!targetB || !targetB.merge_steps) return;

        createChart('cHDist', {
          type: 'line',
          data: {
            labels: targetB.merge_steps.map((_, i) => 'Merge ' + (i + 1)),
            datasets: [{
              label: 'Merge Distance',
              data: targetB.merge_steps,
              borderColor: COLORS.cyan,
              backgroundColor: 'rgba(34, 211, 238, 0.08)',
              fill: true,
              tension: 0.2,
              pointBackgroundColor: COLORS.cyan
            }]
          },
          options: { plugins: { legend: { display: false } } }
        });
      }

      $('hLink').onchange = updateHDist;
      updateHDist();
    }

    // =============================================================
    // VIEW 8: MARKET BASKET ANALYSIS
    // =============================================================
    function renderApriori() {
      $('pageTitle').textContent = "Market Basket Analysis";
      $('pageDesc').textContent = "Association rule mining extracting frequent itemsets and co-purchasing affinity from invoice baskets.";
      $('sectionBadge').textContent = "Association Mining";

      const ap = D.lab9_apriori;

      $('toolbar').innerHTML = `
        <div class="control-item">
          <label>Min Lift Filter</label>
          <input type="number" id="apMinLift" value="1.5" min="1.0" max="10.0" step="0.5" style="width:80px">
        </div>
        <div class="control-item">
          <label>Search Product</label>
          <input type="text" id="apSearch" placeholder="Filter rule text..." style="width:160px">
        </div>
        <div class="status-badge" style="margin-left:auto">
          <span>Min Support &ge; 2% · Min Confidence &ge; 30% · Top 50 Items</span>
        </div>
      `;

      $('kpiGrid').innerHTML = `
        <div class="kpi-card">
          <span class="kpi-label">Rules Extracted</span>
          <span class="kpi-val">${ap.total_rules} Rules</span>
          <span class="kpi-sub">Support &ge; 2% & Conf &ge; 30%</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Top Rule Lift</span>
          <span class="kpi-val" style="color:var(--teal)">${ap.top_rules[0].lift}&times;</span>
          <span class="kpi-sub">Strongest Product Association</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Baskets Analyzed</span>
          <span class="kpi-val">14,291</span>
          <span class="kpi-sub">Multi-Item Transactions</span>
        </div>
        <div class="kpi-card">
          <span class="kpi-label">Item Universe</span>
          <span class="kpi-val">Top 50 Items</span>
          <span class="kpi-sub">Dimensionality Reduction</span>
        </div>
      `;

      $('cardsGrid').innerHTML = `
        <div class="card">
          <div class="card-header">
            <div>
              <h3>Top 10 Association Rules by Lift</h3>
              <p>Color-coded by affinity strength (teal &ge; 10&times;, cyan &ge; 6&times;, violet &ge; 3&times;)</p>
            </div>
          </div>
          <div class="chart-container tall"><canvas id="cApLift"></canvas></div>
        </div>

        <div class="card">
          <div class="card-header">
            <div>
              <h3>Support vs Confidence Distribution</h3>
              <p>Rule density and strength distribution</p>
            </div>
          </div>
          <div class="chart-container tall"><canvas id="cApScatter"></canvas></div>
        </div>

        <div class="card wide">
          <div class="card-header">
            <div>
              <h3>Interpretable Association Rules Table</h3>
              <p>If Customer Buys (Antecedent) &rarr; They Also Buy (Consequent)</p>
            </div>
          </div>
          <div class="table-container">
            <table>
              <thead>
                <tr>
                  <th>If Customer Buys (Antecedent)</th>
                  <th>They Also Buy (Consequent)</th>
                  <th>Support</th>
                  <th>Confidence</th>
                  <th>Lift</th>
                  <th>Strength Interpretation</th>
                </tr>
              </thead>
              <tbody id="apTableBody"></tbody>
            </table>
          </div>
        </div>
      `;

      function renderRulesTable() {
        const minL = parseFloat($('apMinLift').value) || 1.0;
        const query = ($('apSearch').value || '').toLowerCase();

        const filtered = ap.top_rules.filter(r => r.lift >= minL && (r.ant.toLowerCase().includes(query) || r.con.toLowerCase().includes(query)));
        $('apTableBody').innerHTML = filtered.map(r => `
          <tr>
            <td><b>${r.ant}</b></td>
            <td><b style="color:var(--ac)">${r.con}</b></td>
            <td>${(r.support * 100).toFixed(2)}%</td>
            <td>${(r.confidence * 100).toFixed(1)}%</td>
            <td><b style="color:var(--teal)">${r.lift.toFixed(2)}&times;</b></td>
            <td>${r.lift >= 10 ? '<span style="color:var(--teal)">Very High Affinity</span>' : r.lift >= 5 ? '<span style="color:var(--cyan)">Strong Affinity</span>' : '<span style="color:var(--amber)">Moderate Affinity</span>'}</td>
          </tr>
        `).join('') || `<tr><td colspan="6" style="text-align:center;padding:20px;color:var(--tx-muted)">No rules match the current filter.</td></tr>`;
      }

      $('apMinLift').oninput = renderRulesTable;
      $('apSearch').oninput = renderRulesTable;
      renderRulesTable();

      // Top 10 rules bar chart with strength-scaled colors
      const top10 = ap.top_rules.slice(0, 10);
      const liftBarColors = top10.map(r => r.lift >= 10 ? COLORS.teal : r.lift >= 6 ? COLORS.cyan : COLORS.violet);

      createChart('cApLift', {
        type: 'bar',
        data: {
          labels: top10.map(r => r.ant.slice(0, 16) + '... → ' + r.con.slice(0, 16) + '...'),
          datasets: [{
            label: 'Lift Factor',
            data: top10.map(r => r.lift),
            backgroundColor: liftBarColors,
            borderRadius: 4
          }]
        },
        options: {
          indexAxis: 'y',
          plugins: { legend: { display: false } },
          scales: { x: { title: { display: true, text: 'Lift Factor (×)' } } }
        }
      });

      // Support vs Confidence scatter
      createChart('cApScatter', {
        type: 'scatter',
        data: {
          datasets: [{
            label: 'Association Rules',
            data: ap.top_rules.map(r => ({ x: r.support, y: r.confidence })),
            backgroundColor: 'rgba(245, 158, 11, 0.6)',
            pointRadius: 4
          }]
        },
        options: {
          scales: {
            x: { title: { display: true, text: 'Support' } },
            y: { title: { display: true, text: 'Confidence' } }
          },
          plugins: { legend: { display: false } }
        }
      });
    }

    // Initialize Default View
    renderTab('overview');
  </script>
</body>
</html>
"""

with open('Retail Analytics Dashboard.html', 'w', encoding='utf-8') as out_f:
    out_f.write(html_template)

with open('index.html', 'w', encoding='utf-8') as idx_f:
    idx_f.write(html_template)

print("Generated refined Retail Analytics Dashboard.html and index.html successfully!")
