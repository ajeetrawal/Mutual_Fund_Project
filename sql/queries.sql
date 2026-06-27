-- 1 Top 5 Funds by AUM
SELECT scheme_name,aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2 Average NAV
SELECT AVG(nav) FROM nav_history;

-- 3 Monthly Average NAV
SELECT strftime('%Y-%m',date),AVG(nav)
FROM nav_history
GROUP BY strftime('%Y-%m',date);

-- 4 Transactions by State
SELECT state,COUNT(*)
FROM investor_transactions
GROUP BY state;

-- 5 Expense Ratio below 1%
SELECT scheme_name
FROM scheme_performance
WHERE expense_ratio_pct<1;

-- 6 Total Investment
SELECT SUM(amount_inr)
FROM investor_transactions;

-- 7 Fund Count by Category
SELECT category,COUNT(*)
FROM fund_master
GROUP BY category;

-- 8 Highest NAV
SELECT MAX(nav)
FROM nav_history;

-- 9 Lowest NAV
SELECT MIN(nav)
FROM nav_history;

--10 Average 3 Year Return
SELECT AVG(return_3yr_pct)
FROM scheme_performance;