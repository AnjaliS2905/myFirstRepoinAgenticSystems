import pandas as pd 
import plotly.express as px 

df =pd.read_csv("iris.csv")

print(df.head())
print(df.shape)
print(df.columns)
#-----------------info------------------
print(df.info())
print(df.describe())
print(df.isnull().sum())

#---------------Petal Length Distribution--------
if "petal_length" in df.columns:
    fig = px.histogram(df, x="petal_length", nbins=30,
                       title="Distribution of Petal Length")
    fig.show()

#-------------box plot for outlier detection------------------------
if "petal_length" in df.columns:
    # Box plot
    fig2 = px.box(df, y="petal_length", title="Box Plot for Petal Length")
    fig2.show()

# -----------------Relationship Between Variables-----------------


fig3 = px.scatter(df,
                    x="petal_length",
                    y="petal_width",
                    color="species" if "species" in df.columns else None,
                    title="Petal Length vs Petal Width")
fig3.show()

#------------------------Correlation Heatmap----------------------------
corr = df.corr(numeric_only=True)

fig4= px.imshow(corr,
                text_auto=True,
                title="Correlation Heatmap")
fig4.show()

# ===============================
# 8. Species-wise Analysis
# ===============================
if "species" in df.columns:
    print(df.groupby("species").mean())

    if "petal_length" in df.columns:
        fig5 = px.box(df,
                     x="species",
                     y="petal_length",
                     color="species",
                     title="Petal Length Across Species")
        fig5.show()

# -----------------------Key Insights (Printed)----------------------

print("\n--- Key Insights ---")
print("""
      1.There are no missing values.
      2.Most Flowers have petal-length between 1.6-5.1 with an average length if 4.35
      3.Virgincia has more Petal-length to petal-width Ratio and setosa has least
      4.Setosa is smallest species
      5.Sepal Width to sepal_length low correlation sepal-length to petal-length high correlation
      6.sepal-length and petal width have high correlation.
""")