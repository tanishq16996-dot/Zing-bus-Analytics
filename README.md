# Zing-bus-Analytics


An end-to-end analytics project built with **Python, SQL, Power BI and DAX**. It covers generating a dataset, designing a database schema, cleaning the data, building a star-schema model and creating a 3-page interactive dashboard on bus bookings.

> **Note:** The dataset is **synthetic**. I generated it in Python to practise the full workflow, including data cleaning, so it does not represent a real company.

---

## Project Overview

| Item | Detail |
|---|---|
| Bookings | 10K+ |
| Customers | 1,000 |
| Routes | 5 |
| Bus types | 3 |
| Cities | 5 |
| Total revenue | ₹7.4M |

---

## Workflow

1. **Data generation (Python):** Created a reproducible synthetic dataset with pandas and NumPy. Missing values and duplicates were included deliberately to practise cleaning.
2. **Database design (SQL):** Designed a relational schema with customers, routes, buses and bookings tables, using primary keys and typed fields.
3. **Data cleaning (Jupyter Notebook):** Handled missing values and duplicates and prepared the data for loading.
4. **Data modeling (Power BI):** Built a star schema with a bookings fact table, bus, customer and route dimensions, and a date table for time-based analysis.
5. **Dashboard (Power BI + DAX):** Built a 3-page interactive dashboard.

---

## Dashboard Pages

### 1. Executive Dashboard
- KPI cards: Total Revenue, Total Bookings, Total Customers, Average Rating
- Revenue by City and Revenue by Route
- Monthly Revenue Trend
- Booking Status (confirmed vs cancelled)

![Executive Dashboard](images/executive_dashboard.png)

### 2. Operations
- KPI cards: Total Revenue, Total Bookings, Average Fare, Total Customers, Average Rating
- Revenue and Average Fare by Bus Type
- Route Performance Matrix (revenue, bookings and average fare by route)

![Operations](images/operations.png)

### 3. Customer Insights
- Customer Growth over time
- Age Group Analysis and Gender Split
- City-wise Customers
- Rating Distribution

![Customer Insights](images/customer_insights.png)

**Interactivity:** slicers, drill-downs and page navigation let users filter by city, month and bus type.

---

## DAX Measures

Measures were written for:
- Total Revenue
- Total Bookings
- Total Customers
- Average Fare
- Average Rating
- Cancellation Rate

Calculated columns were used for age groups and route labels.

---

## Key Findings

- About **10% of bookings were cancelled**.
- Revenue and fares were compared across routes, cities and bus types to see where performance differs.

---

## Tools Used

- **Python:** pandas, NumPy, Jupyter Notebook
- **SQL:** relational schema design
- **Power BI:** data modeling, dashboards
- **DAX:** measures and calculated columns

---

## Repository Structure

```
bus-booking-analytics/
├── data/          # generated and cleaned datasets
├── sql/           # database schema script
├── notebooks/     # Jupyter notebook for data generation and cleaning
├── powerbi/       # Power BI file (.pbix)
├── images/        # dashboard screenshots
└── README.md
```

---

## How to Use

1. Open the Jupyter notebook in `notebooks/` to generate and clean the dataset.
2. Run the schema script in `sql/` to create the tables.
3. Open the `.pbix` file in `powerbi/` using Power BI Desktop (free).
4. If prompted, refresh the data source to point to the files in `data/`.

---

## Author

**Tanishq Jain**
[LinkedIn](https://www.linkedin.com/in/tanishq-jain-38461520b)
