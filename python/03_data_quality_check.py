import pandas as pd

df=pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

print("Duplicate Rows : ")
print(df.duplicated().sum())

print("\n Minimum Age : ")
print(df["Age"].min())

print("\n Maximum Age : ")
print(df["Age"].max())

print("\n Minimum monthly Income : ")
print(df["MonthlyIncome"].min())

print("\n Maximum monthly Income : ")
print(df["MonthlyIncome"].max())


