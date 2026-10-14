# ============================================================
# BLACK FRIDAY SALES DATA ANALYSIS
# ============================================================

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("BlackFriday   .csv")

print("BLACK FRIDAY SALES DATA ANALYSIS")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Records:")
print(df.head())


# ============================================================
# 2. CHECK DATA TYPES
# ============================================================

print("\nData Types:")
print(df.dtypes)


# ============================================================
# 3. CHECK MISSING VALUES
# ============================================================

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())


# ============================================================
# 4. HANDLE MISSING VALUES
# ============================================================

# Product category 2 and 3 contain missing values
df["Product_Category_2"] = df["Product_Category_2"].fillna(0)
df["Product_Category_3"] = df["Product_Category_3"].fillna(0)

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())


# ============================================================
# 5. CHECK DUPLICATES
# ============================================================

print("\nDuplicate Records:")
print(df.duplicated().sum())

# Remove duplicate records
df = df.drop_duplicates()

print("Shape After Removing Duplicates:")
print(df.shape)


# ============================================================
# 6. OUTLIER DETECTION
# ============================================================

# Find Q1 and Q3
Q1 = df["Purchase"].quantile(0.25)
Q3 = df["Purchase"].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Find outliers
outliers = df[
    (df["Purchase"] < lower_limit) |
    (df["Purchase"] > upper_limit)
]

print("\nOUTLIER ANALYSIS")
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Number of Outliers:", len(outliers))


# ============================================================
# 7. BASIC STATISTICS
# ============================================================

print("\nBasic Statistics:")
print(df["Purchase"].describe())


# ============================================================
# 8. VISUALIZATION 1 - GENDER-WISE SALES
# ============================================================

gender_sales = df.groupby("Gender")["Purchase"].sum()

plt.figure(figsize=(6, 4))
gender_sales.plot(kind="bar")

plt.title("Gender-wise Sales")
plt.xlabel("Gender")
plt.ylabel("Total Purchase")

plt.show()


# ============================================================
# 9. VISUALIZATION 2 - AGE-WISE SALES
# ============================================================

age_sales = df.groupby("Age")["Purchase"].sum()

plt.figure(figsize=(7, 4))
age_sales.plot(kind="bar")

plt.title("Age-wise Sales")
plt.xlabel("Age Group")
plt.ylabel("Total Purchase")

plt.xticks(rotation=45)
plt.show()


# ============================================================
# 10. VISUALIZATION 3 - CITY-WISE SALES
# ============================================================

city_sales = df.groupby("City_Category")["Purchase"].sum()

plt.figure(figsize=(6, 4))
city_sales.plot(kind="bar")

plt.title("City Category-wise Sales")
plt.xlabel("City Category")
plt.ylabel("Total Purchase")

plt.show()


# ============================================================
# 11. VISUALIZATION 4 - TOP 10 PRODUCT CATEGORIES
# ============================================================

product_sales = df.groupby("Product_Category_1")["Purchase"].sum()

top_products = product_sales.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(8, 5))
top_products.plot(kind="bar")

plt.title("Top 10 Product Categories")
plt.xlabel("Product Category")
plt.ylabel("Total Purchase")

plt.show()


# ============================================================
# 12. VISUALIZATION 5 - PURCHASE DISTRIBUTION
# ============================================================

plt.figure(figsize=(7, 4))

plt.hist(df["Purchase"], bins=30)

plt.title("Purchase Distribution")
plt.xlabel("Purchase Amount")
plt.ylabel("Number of Customers")

plt.show()


# ============================================================
# 13. VISUALIZATION 6 - TOP 10 OCCUPATIONS
# ============================================================

occupation_sales = df.groupby("Occupation")["Purchase"].sum()

top_occupations = occupation_sales.sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(8, 5))
top_occupations.plot(kind="bar")

plt.title("Top 10 Occupations by Sales")
plt.xlabel("Occupation")
plt.ylabel("Total Purchase")

plt.show()


# ============================================================
# 14. SHORT PROJECT INSIGHTS
# ============================================================

highest_gender = gender_sales.idxmax()
highest_age = age_sales.idxmax()
highest_city = city_sales.idxmax()
highest_product = product_sales.idxmax()

average_purchase = df["Purchase"].mean()
maximum_purchase = df["Purchase"].max()


print("\n")
print("=" * 50)
print("PROJECT INSIGHTS")
print("=" * 50)

print("\n1. Highest Spending Gender:", highest_gender)
print("2. Highest Spending Age Group:", highest_age)
print("3. Highest Sales City Category:", highest_city)
print("4. Highest Sales Product Category:", highest_product)
print("5. Average Purchase Amount: ₹", round(average_purchase, 2))
print("6. Maximum Purchase Amount: ₹", maximum_purchase)
print("7. Number of Outliers:", len(outliers))

print("\nAnalysis Completed Successfully!")