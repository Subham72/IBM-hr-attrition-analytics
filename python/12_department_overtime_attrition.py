import pandas as pd

df=pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

result = (df.groupby(["Department","OverTime"]).agg(Total_Employees = ("Attrition","count"),
                                                   Employees_Left = ("Attrition",lambda x:(x=="Yes").sum())).reset_index())

result["Attrition_Rate"]=((result["Employees_Left"]/result["Total_Employees"])*100).round(2)

result=result.sort_values(by="Attrition_Rate", ascending=False)

print(result[["Department", "OverTime", "Total_Employees", "Employees_Left", "Attrition_Rate"]])

