import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("===================DAY 7:SALES DATA ANALYSIS================")
#Load dataset
df=pd.read_csv("Day7_sales.csv")
#1.First five records
print("\n======================FIRST FIVE RECORDS======================")
print(df.head())
#2.Dataset shape
print("\n================DATASET SHAPE=================")
print(df.shape)
#3.Dataset information
print("\n===================DATASET INFORMATION================")
df.info()
#4.Missing values
print("\n================MISSSING VALUES==================")
print(df.isnull().sum())
#5.Duplicate records
print("\n================DUPLICATES========================")
print(df.duplicated().sum())
#6.Data types
print("\n=============DATA TYPES=====================")
print(df.dtypes)
#7.Descriptive statistics
print("\n=====================DESCRIPTIVE STATISTICS=====================")
print(df.describe())
#8.Product count
print("\n==================PRODUCT COUNT================")
print(df["Product"].value_counts())
#9.Region-wise sales
region_sales=df.groupby("Region")["Sales"].sum()
print("\n===============REGION-WISE SALES==================")
print(region_sales)
#10.Product-wise sales
product_sales=df.groupby("Product")["Sales"].sum()
print("\n===============PRODUCT-WISE SALES=============")
#11.Total sales
print("\n================TOTAL SALES====================")
print(df["Sales"].sum())
#12.Total profit
print("\n=============TOTAL PROFIT ================")
print(df["Profit"].sum())
#13.Highest sales region
print("\n=========HIGHEST SALES REGION================")
print(region_sales.idxmax())
#14.Highest selling product
print("\n=======================HIGHEST SELLING PRODUCT============")
print(product_sales.idxmax())
#15.Pivot table
print("\n================PIVOT TABLE=================")
pivot=pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    fill_value=0
    )
print(pivot)
#16. Region-wise sales chart
plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Day7_region_sales.png")
plt.show()
#17. Product-wise sales chart
plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Day7_product_sales.png")
plt.show()
#18.Sales distribution
plt.figure(figsize=(8,5))
sns.histplot(data=df,x="Sales")
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Day7_sales_distribution.png")
plt.show()

print("\n===================SALES ANALYSIS COMPLETED SUCCESSFULLY=========================")
