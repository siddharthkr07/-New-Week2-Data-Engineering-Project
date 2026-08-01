
# Week 2: Relational Schema Merging & Multi-Source ETL Rules

## Project Title

# E-Commerce Multi-Table Data Integration Engine

---

## Project Objective

The objective of this project is to build a Python-based ETL pipeline that integrates multiple e-commerce datasets including Customers, Orders, Payments, and Shipping. The pipeline performs SQL-style joins, validates relational keys, removes duplicate records, standardizes schema, computes business KPIs, and generates analytical visualizations.

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- Git
- GitHub
- VS Code
- Google Colab

---

# Project Structure

```
Week2_Data_Engineering_Project
│
├── data
│   ├── customers.csv
│   ├── orders.csv
│   ├── payments.csv
│   ├── shipping.csv
│   ├── final_merged_data.csv
│   ├── customer_ltv.csv
│   └── shipping_report.csv
│
├── screenshots
│   ├── customer_ltv.png
│   ├── payment_status.png
│   ├── shipping_status.png
│   └── order_status.png
│
├── week2_project.py
└── README.md
```

---

# Input Datasets

- customers.csv
- orders.csv
- payments.csv
- shipping.csv

---

# ETL Pipeline

## Step 1

Load all CSV datasets using Pandas.

## Step 2

Validate relational keys.

## Step 3

Perform SQL-style joins using

- Inner Join
- Left Join

## Step 4

Standardize schema and data types.

## Step 5

Remove duplicate keys.

## Step 6

Generate business KPIs.

---

# Merge Flow Diagram

```
Customers
     │
     ▼
Orders
     │
     ▼
Payments
     │
     ▼
Shipping
     │
     ▼
Final Merged Dataset
```

---

# Business KPIs

The following KPIs are generated.

- Customer Lifetime Value (LTV)
- Order Completion Rate
- Payment Success Rate
- Shipping Status Summary

---

# Output Files

- final_merged_data.csv
- customer_ltv.csv
- shipping_report.csv

---

# Visualizations

The project generates

- Customer Lifetime Value Bar Chart
- Payment Status Pie Chart
- Shipping Status Bar Chart
- Order Status Pie Chart

---

# Screenshots

## Customer Lifetime Value

![Customer LTV](screenshots/customer_ltv.png)

---

## Payment Status

![Payment Status](screenshots/payment_status.png)

---

## Shipping Status

![Shipping Status](screenshots/shipping_status.png)

---

## Order Status

![Order Status](screenshots/order_status.png)

---

# Skills Demonstrated

- Data Engineering
- ETL Pipeline
- Pandas
- SQL Style Merge
- Data Cleaning
- Duplicate Validation
- Schema Standardization
- KPI Extraction
- Data Visualization
- Git & GitHub

---

# Author

**Siddharth Kumar**

B.Tech CSE