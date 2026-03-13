import pandas as pd 
import numpy as np
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)
null_values=df.isnull().sum()
print("missingValues:",null_values)
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print("\nMean Replaced Salary:",df["Salary"])
df=df.drop(columns=["Temporary_Notes"])
df=df.rename(columns={"Salary":"Annual_Salary"})
Summary=df.groupby("Department").agg({
    "Annual_Salary":"mean",
    "Employee": "count"
})
print(df)
print("\n Summary Table: \n",Summary)