import pandas as pd

df = pd.read_csv(
    r"C:\Users\jesus\Documents\proyecto de dattos\data\Sample - Superstore.csv",
    encoding="latin1"
)


print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df["Sales"].sum())
print(df["Product Name"].value_counts().head(10))
print(df.groupby("Category")["Sales"].sum())
print(df.groupby("City")["Sales"].sum().sort_values(ascending=False).head(10))