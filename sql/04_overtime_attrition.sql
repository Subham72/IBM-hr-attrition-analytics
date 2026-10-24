SELECT overtime, Count(*) AS Total_Employees,
SUM(CASE WHEN Attrition="Yes" THEN 1
ELSE 0
END) AS Employees_Left,
ROUND(SUM(CASE WHEN Attrition="Yes" THEN 1 ELSE 0 END)*100/COUNT(*),2) AS Attrition_Rate
FROM employees
GROUP BY overtime
Order BY Attrition_Rate DESC;

