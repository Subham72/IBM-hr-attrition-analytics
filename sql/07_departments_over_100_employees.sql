SELECT Department, COUNT(*) AS Total_Employees
FROM employees
GROUP BY Department
HAVING COUNT(*)>100
ORDER BY Total_Employees;