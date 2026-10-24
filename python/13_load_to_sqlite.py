import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("../data/IBM_HR_Attrition_Enhanced.csv")

engine = create_engine("sqlite:///../hr_attrition.db")

df.to_sql("employees", engine, if_exists="replace", index=False)

print("Data Loaded Successfully")