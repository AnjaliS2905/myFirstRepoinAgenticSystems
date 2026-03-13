import pandas as pd
import numpy as np


df= pd.read_csv("sample_data.csv")

print(df.head())
print(df.tail())
print(df.info())
print(df.describe())

score_column = df["Score"]
subset_df = df[["Name", "Age"]]
age_filter = df[df["Age"] > 30]

print(score_column)
print(subset_df)
print(age_filter)