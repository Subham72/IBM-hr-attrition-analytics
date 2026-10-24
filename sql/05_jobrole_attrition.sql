SELECT JobRole, COUNT(*) AS Total_Employees,
SUM(CASE
WHEN Attrition="Yes" THEN 1
ELSE 0
END) AS Employees_Left,
ROUND(SUM(CASE
WHEN Attrition = "Yes" THEN 1
ELSE 0
END)*100/COUNT(*),2) AS Attrition_Rate
From employees
GROUP BY JobRole
ORDER BY Attrition_Rate DESC;