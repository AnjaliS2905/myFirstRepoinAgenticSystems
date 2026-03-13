import pandas as pd
df=pd.read_csv("student_scores.csv")
score=df["Score"]
print(score)
df_new=df[["Name","Score"]]
print(df_new)
x=df.iloc[0:3]
print(x)
df.index = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"]
print(df.loc["j"])
df_2=df[df["Score"]>85]
df_3=df[(df["Score"]>85)&(df["Passed"]==True)]
df_4=df.sort_values("Score",ascending=False)
df_5=df[(df["Score"]>85)&(df["Passed"]==True)].sort_values("Score",ascending=False)
print(df_2)
print(df_3)
print(df_4)
print("High-performing students:\n",df_5)