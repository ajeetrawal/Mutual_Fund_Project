CREATE TABLE fund_master (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT
);

CREATE TABLE nav_history (
    amfi_code INTEGER,
    date DATE,
    nav REAL
);

CREATE TABLE aum_by_fund_house (
    date DATE,
    fund_house TEXT,
    aum_lakh_crore REAL,
    aum_crore REAL,
    num_schemes INTEGER
);

CREATE TABLE monthly_sip_inflows (
    month TEXT,
    sip_inflow_crore REAL,
    active_sip_accounts_crore REAL,
    new_sip_accounts_lakh REAL,
    sip_aum_lakh_crore REAL,
    yoy_growth_pct REAL
);

CREATE TABLE category_inflows (
    month TEXT,
    category TEXT,
    net_inflow_crore REAL
);

CREATE TABLE industry_folio_count (
    month TEXT,
    total_folios_crore REAL,
    equity_folios_crore REAL,
    debt_folios_crore REAL,
    hybrid_folios_crore REAL,
    others_folios_crore REAL
);

CREATE TABLE scheme_performance (
    amfi_code INTEGER,
    scheme_name TEXT,
    expense_ratio_pct REAL,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL
);

CREATE TABLE investor_transactions (
    investor_id INTEGER,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL
);

CREATE TABLE portfolio_holdings (
    amfi_code INTEGER,
    stock_symbol TEXT,
    stock_name TEXT,
    sector TEXT,
    weight_pct REAL
);

CREATE TABLE benchmark_indices (
    date DATE,
    index_name TEXT,
    close_value REAL
);