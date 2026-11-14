# Power BI Guide

Page 1 - Executive Dashboard
Cards:
- Total Revenue
- Total Bookings
- Total Customers
- Average Rating

Charts:
- Revenue by Month (Line)
- Revenue by City (Bar)
- Booking Status (Donut)
- Top Routes (Column)

Page 2 - Operations
- Bus Type Utilization
- Revenue by Bus Type
- Average Fare
- Route Performance Matrix

Page 3 - Customer Insights
- Customer Growth
- Gender Split
- Age Group Analysis
- City-wise Customers
- Rating Distribution

Recommended DAX:
Total Revenue = SUM(bookings[NetFare])
Total Bookings = COUNT(bookings[BookingID])
Average Rating = AVERAGE(bookings[Rating])
