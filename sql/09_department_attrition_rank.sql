with department_attrition as (
SELECT Department, Count(*) AS Total_Employees,
SUM(CASE WHEN Attrition="Yes" THEN 1 ELSE 0 END) AS Employees_Left,
ROUND(SUM(CASE WHEN Attrition="Yes" THEN 1 ELSE 0 END)*100/Count(*),2) AS Attrition_Rate
FROM employees
GROUP BY Department
)
SELECT Department,Total_Employees, Employees_Left, Attrition_Rate,
Rank() Over(ORDER BY Attrition_Rate DESC) AS Attrition_Rank
FROM department_attrition;

