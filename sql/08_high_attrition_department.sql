with department_attrition as (
SELECT Department, COUNT(*) AS Total_Employees,
SUM(
CASE
WHEN Attrition="Yes" THEN 1
ELSE 0
END) AS Employees_Left,
ROUND(SUM(CASE WHEN Attrition="Yes" THEN 1 ELSE 0 END)*100/COUNT(*),2) AS Attrition_Rate
FROM employees
GROUP BY Department
)
SELECT * FROM department_attrition
WHERE Attrition_Rate>15