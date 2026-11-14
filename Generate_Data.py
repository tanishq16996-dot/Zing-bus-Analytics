import pandas as pd
import numpy as np

np.random.seed(42)

# -------------------------
# Customers
# -------------------------
n_customers = 1000
customers = pd.DataFrame({
    "CustomerID": np.arange(1, n_customers+1),
    "CustomerName": [f"Customer_{i}" for i in range(1, n_customers+1)],
    "Age": np.random.randint(18,60,n_customers),
    "Gender": np.random.choice(["Male","Female"],n_customers),
    "City": np.random.choice(["Delhi","Jaipur","Lucknow","Chandigarh","Mumbai"],n_customers),
    "SignupDate": pd.to_datetime("2024-01-01")+pd.to_timedelta(np.random.randint(0,365,n_customers),unit="D")
})

# Missing values & duplicates for practice
customers.loc[np.random.choice(customers.index,20),"Age"]=np.nan
customers = pd.concat([customers,customers.iloc[:10]],ignore_index=True)

# -------------------------
# Routes
# -------------------------
routes = pd.DataFrame({
    "RouteID":[1,2,3,4,5],
    "Source":["Delhi","Delhi","Mumbai","Lucknow","Jaipur"],
    "Destination":["Jaipur","Chandigarh","Pune","Delhi","Delhi"],
    "DistanceKM":[280,250,150,500,280]
})

# -------------------------
# Buses
# -------------------------
buses = pd.DataFrame({
    "BusID":np.arange(1,51),
    "BusType":np.random.choice(["AC Sleeper","Volvo","Seater"],50),
    "Capacity":np.random.choice([35,40,45],50)
})

# -------------------------
# Bookings
# -------------------------
n_bookings=10000
bookings=pd.DataFrame({
    "BookingID":np.arange(1,n_bookings+1),
    "CustomerID":np.random.choice(customers.CustomerID.unique(),n_bookings),
    "BusID":np.random.choice(buses.BusID,n_bookings),
    "RouteID":np.random.choice(routes.RouteID,n_bookings),
    "JourneyDate":pd.to_datetime("2025-01-01")+pd.to_timedelta(np.random.randint(0,180,n_bookings),unit="D"),
    "Fare":np.round(np.random.normal(900,250,n_bookings),2),
    "Discount":np.random.randint(0,300,n_bookings),
    "Rating":np.random.randint(1,6,n_bookings),
    "Status":np.random.choice(["Completed","Cancelled"],n_bookings,p=[0.9,0.1])
})

bookings["NetFare"]=bookings["Fare"]-bookings["Discount"]

# -------------------------
# Cleaning Examples
# -------------------------
customers["Age"]=customers["Age"].fillna(customers["Age"].median())
customers=customers.drop_duplicates()

merged=bookings.merge(customers,on="CustomerID",how="left")
merged=merged.merge(routes,on="RouteID",how="left")
merged=merged.merge(buses,on="BusID",how="left")

summary=merged.groupby("City").agg(
    TotalRevenue=("NetFare","sum"),
    TotalBookings=("BookingID","count"),
    AvgRating=("Rating","mean")
).reset_index()

customers.to_csv("customers.csv",index=False)
routes.to_csv("routes.csv",index=False)
buses.to_csv("buses.csv",index=False)
bookings.to_csv("bookings.csv",index=False)
summary.to_csv("city_summary.csv",index=False)

print("Files generated successfully.")
