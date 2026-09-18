import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("===================DAY 6:DATA VISUALISATION=======================")
#Load dataset
df=pd.read_csv(r"C:\Users\Dell\Documents\Week4\Day6_sales.csv")
print("\n---------------DATASET---------------")
print(df)
#1.Bar Chart-Region-wise Sales
region_sales=df.groupby("Region")["Sales"].sum()
plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Day6_region_sales.png")
plt.show()
#2.Bar Chart-Product-wise Sales
product_sales=df.groupby("Product")["Sales"].sum()
plt.figure(figsize=(8,5))
product_sales.plot(kind="bar")
plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.savefig("Day6_product_sales.png")
plt.show()
#3.Histogram-Sales Distribution
plt.figure(figsize=(8,5))
sns.histplot(data=df,x="Sales")
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("Day6_sales_distribution.png")
plt.show()
#4.Boxplot - Sales by Region
plt.figure(figsize=(8,5))
sns.boxplot(data=df,x="Region",y="Sales")
plt.title("Sales Distribution by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Day6_sales_boxplot.png")
plt.show()

print("\nAll visualizations created successfully.")
