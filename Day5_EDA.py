import pandas as pd
print("==========================DAY 5:EXPLORATORY DATA ANALYSIS====================")
#Load dataset
df=pd.read_csv("Day5_sales.csv")
print("\n------------DATASET-----------")
print(df)
#Descriptive statistics
print("\n-------------------DESCRIPTIVE STATISTICS----------")
print(df.describe())
#Count products
print("\n--------------PRODUCT COUNT-------------------")
print(df["Product"].value_counts())
#Region-wise sales
print("\n----------REGION-WISE SALES-----------------------")
region_sales=df.groupby("Region")["Sales"].sum()
print(region_sales)
#Product-wise sales
print("\n------------PRODUCT-WISE SALES-------------------")
product_sales=df.groupby("Product")["Sales"].sum()
print(product_sales)
#Region-wise profit
print("\n--------------REGION-WISE PROFIT-------------")
print(df.groupby("Region")["Profit"].sum())
pivot=pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
    )
print(pivot)
print("\nEDA completed successfully.")
