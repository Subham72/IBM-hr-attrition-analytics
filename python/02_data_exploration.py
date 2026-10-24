import pandas as pd

df=pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== Column Names =====")
print(df.columns)

print("\n===== Dataset INFO =====")
print(df.info())

print("\n===== Numeric Summary =====")
print(df.describe())