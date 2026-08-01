

import pandas as pd

print("======================================")
print(" Week 2 Data Engineering Project ")
print("======================================")

# Load Datasets

customers = pd.read_csv("data/customers.csv")
orders = pd.read_csv("data/orders.csv")
payments = pd.read_csv("data/payments.csv")
shipping = pd.read_csv("data/shipping.csv")

print("\nDatasets Loaded Successfully!\n")

print("===== CUSTOMERS =====")
print(customers.head())

print("\n===== ORDERS =====")
print(orders.head())

print("\n===== PAYMENTS =====")
print(payments.head())

print("\n===== SHIPPING =====")
print(shipping.head())

print("\n========== DATASET INFORMATION ==========\n")

print("Customers")
customers.info()

print("\nOrders")
orders.info()

print("\nPayments")
payments.info()

print("\nShipping")
shipping.info()

print("\n========== DATASET SHAPES ==========\n")

print("Customers :", customers.shape)
print("Orders :", orders.shape)
print("Payments :", payments.shape)
print("Shipping :", shipping.shape)

print("\n========== INNER JOIN ==========\n")

merged_data = pd.merge(
    orders,
    customers,
    on="Customer_ID",
    how="inner"
)

print(merged_data)

print("\n========== MERGE PAYMENTS ==========\n")

merged_data = pd.merge(
    merged_data,
    payments,
    on="Order_ID",
    how="left"
)

print(merged_data)
print("\n========== MERGE SHIPPING ==========\n")

merged_data = pd.merge(
    merged_data,
    shipping,
    on="Order_ID",
    how="left"
)

print(merged_data)
merged_data.to_csv("data/final_merged_data.csv", index=False)

print("\nFinal Merged Dataset Saved Successfully!")

print("\n========== CUSTOMER LIFETIME VALUE ==========\n")

customer_ltv = merged_data.groupby("Customer_Name")["Order_Amount"].sum()

print(customer_ltv)

print("\n========== ORDER COMPLETION RATE ==========\n")

total_orders = len(merged_data)

completed_orders = len(
    merged_data[merged_data["Order_Status"] == "Completed"]
)

completion_rate = (completed_orders / total_orders) * 100

print(f"Total Orders : {total_orders}")
print(f"Completed Orders : {completed_orders}")
print(f"Completion Rate : {completion_rate:.2f}%")

print("\n========== PAYMENT SUCCESS RATE ==========\n")

paid_orders = len(
    merged_data[merged_data["Payment_Status"] == "Paid"]
)

payment_rate = (paid_orders / total_orders) * 100

print(f"Paid Orders : {paid_orders}")
print(f"Payment Success Rate : {payment_rate:.2f}%")

print("\n========== SHIPPING STATUS ==========\n")

shipping_report = merged_data["Shipping_Status"].value_counts()

print(shipping_report)

print("\n========== DUPLICATE VALIDATION ==========\n")

print("Duplicate Customer IDs :", customers["Customer_ID"].duplicated().sum())

print("Duplicate Order IDs :", orders["Order_ID"].duplicated().sum())

print("\n========== DATA TYPES ==========\n")

merged_data["Customer_ID"] = merged_data["Customer_ID"].astype(str)
merged_data["Order_ID"] = merged_data["Order_ID"].astype(str)

print(merged_data.dtypes)

customer_ltv.to_csv("data/customer_ltv.csv")

shipping_report.to_csv("data/shipping_report.csv")

print("\nKPI Reports Saved Successfully!")

import matplotlib.pyplot as plt

plt.figure(figsize=(8,5))

customer_ltv.sort_values().plot(kind="bar")

plt.title("Customer Lifetime Value (LTV)")
plt.xlabel("Customer")
plt.ylabel("Total Purchase Amount")

plt.tight_layout()

plt.show()

payment_status = merged_data["Payment_Status"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    payment_status.values,
    labels=payment_status.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Payment Status Distribution")

plt.show()

shipping_report.plot(kind="bar", figsize=(8,5))

plt.title("Shipping Status")

plt.xlabel("Shipping Status")
plt.ylabel("Orders")

plt.tight_layout()

plt.show()

order_status = merged_data["Order_Status"].value_counts()

plt.figure(figsize=(6,6))

plt.pie(
    order_status.values,
    labels=order_status.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Order Status")

plt.show()