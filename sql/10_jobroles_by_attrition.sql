WITH jobrole_attrition AS (
SELECT JobRole, COUNT(*) AS Total_Employees,
SUM(CASE WHEN Attrition="Yes" THEN 1 ELSE 0 END) AS Employees_Left,
ROUND(SUM(CASE WHEN Attrition="Yes" THEN 1 ELSE 0 END)*100/COUNT(*),2) AS Attrition_Rate
FROM employees
GROUP BY JobRole),

ranked_jobrole AS (
SELECT *,
RANK() OVER(ORDER BY Attrition_Rate DESC) AS JobRole_Attrition_Ranking
FROM jobrole_attrition
)

SELECT *
FROM ranked_jobrole
WHERE JobRole_Attrition_Ranking<=3;
