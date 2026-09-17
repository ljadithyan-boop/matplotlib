import pandas as pd
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel(r"C:\Users\Adithyan\Downloads\Sales_Data.xlsx")
print("Shape (rows, columns):", df.shape)
print("\nColumn names:", list(df.columns))
print("\nFirst 5 records:")
print(df.head())
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
daily_sales = df.groupby("Order_Date")["Total_Sale"].sum().reset_index()
plt.figure(figsize=(12, 6))
plt.plot(daily_sales["Order_Date"], daily_sales["Total_Sale"], marker="o", linewidth=1)
plt.figure(1)
plt.title("Total Sales Over Time")
plt.xlabel("Order Date")
plt.ylabel("Total Sale")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
# barchart creation for city
city_sales = df.groupby("City")["Total_Sale"].sum().sort_values(ascending=False)
plt.figure(2,figsize=(10,6))
plt.bar(city_sales.index, city_sales.values, color="steelblue",linewidth=2)
plt.title("CITY WISED SALES")
plt.xlabel("CITY")
plt.ylabel("TOTAL SALES")
plt.grid(True)
plt.tight_layout()
plt.show()
# category distribution
category_count=df["Category"].value_counts()
plt.figure(figsize=(8, 8))
plt.pie(
    category_count.values,
    labels=category_count.index,
    autopct="%1.1f%%",
    startangle=90
)
plt.title("CATEGORY DISTIBUTION")
plt.grid(True)
plt.tight_layout()
plt.show()
# monthly sales trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Month"] = df["Order_Date"].dt.to_period("M")
monthly_sales = df.groupby("Month")["Total_Sale"].sum().sort_index()
month_labels = monthly_sales.index.strftime("%b %Y")
plt.figure(figsize=(10, 6))
plt.plot(month_labels, monthly_sales.values, marker="o", linewidth=2, color="darkred")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
# top 10 products
city_sales = df.groupby("Product")["Total_Sale"].sum().sort_values(ascending=False)
plt.figure(2,figsize=(10,6))
plt.bar(city_sales.index, city_sales.values, color="violet",linewidth=10)
plt.title("CITY WISED SALES")
plt.xlabel("PRODUCT")
plt.ylabel("TOTAL SALES")
plt.xticks(rotation=45, ha='center', fontsize=9)
plt.grid(True)
plt.tight_layout()
plt.show()
# PRICE VS QUANTITY
plt.figure(3, figsize=(10, 6))
plt.scatter(df["Unit_Price"], df["Quantity"], color="green", alpha=0.6, edgecolor="ORANGE")
plt.title("PRICE VS QUANTITY")
plt.xlabel("UNIT PRICE")
plt.ylabel("QUANTITY")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
# HIGHLIGHTING HIGHEST SALES PRODUCT
product_sales = df.groupby("Product")["Total_Sale"].sum().sort_values(ascending=False)
top_product = product_sales.idxmax()
top_value = product_sales.max()
plt.figure(4, figsize=(14, 6))
bars = plt.bar(product_sales.index, product_sales.values, color="RED")
top_index = list(product_sales.index).index(top_product)
bars[top_index].set_color("BLUE")
plt.annotate(
    f"Highest: {top_product}\n({top_value:,.0f})",
    xy=(top_index, top_value),
    xytext=(top_index, top_value + top_value * 0.1),
    ha="center",
    fontsize=10,
    fontweight="bold",
    color="orange",
    arrowprops=dict(arrowstyle="->", color="BLUE")
)
plt.title("TOTAL SALES BY PRODUCT (HIGHEST HIGHLIGHTED)")
plt.xlabel("PRODUCT")
plt.ylabel("TOTAL SALES")
plt.xticks(rotation=45, ha="right", fontsize=9)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()