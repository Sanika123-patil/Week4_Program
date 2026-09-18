import pandas as pd
print("============================ DAY 4: DATA CLEANING==================")
#Load dataset
df=pd.read_csv("Day4_data.csv")
print("\n-----ORIGINAL DATA-------")
print(df)
#Check missing values
print("\n===============MISSING VALUES=================")
print(df.isnull().sum())
#Check duplicate records
print("\n-------DUPPLICATE RECORDS------")
print("Duplicates:",
      df.duplicated().sum())
#Remove duplicate records
df=df.drop_duplicates()
# Handle missing values
df["Product"]=df["Product"].fillna("Unknown")
df["Quantity"]=df["Quantity"].fillna(df["Quantity"].mean())
df["Sales"]=df["Sales"].fillna(df["Sales"].mean())
#Correct data types
df["Quantity"]=pd.to_numeric(df["Quantity"])
df["Sales"]=pd.to_numeric(df["Sales"])
print("\n--------- DATA TYPES------")
print(df.dtypes)
print("\n--------CLEANED DATA --------------")
print(df)
# Save cleaned dataset
df.to_csv("day4_cleaned_data.csv",index=False)
print("\nData cleaning completed successfully.")
               
