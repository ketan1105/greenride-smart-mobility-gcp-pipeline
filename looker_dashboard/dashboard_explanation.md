# 🚲 GreenRide Looker Dashboard Overview

This Looker Studio dashboard provides a visual and interactive way to monitor, analyze, and derive insights from GreenRide’s smart mobility data. It helps stakeholders make data-driven decisions by tracking trends, anomalies, and performance metrics.

---

## 📊 Dashboard Components

### 1. **Total Rides and Fare Trend**
- **Chart Type:** Time Series Line Chart
- **Data:** Total trips and total fare over time (daily/weekly)
- **Insight:** Identifies peak usage days and correlates revenue trends.

---

### 2. **Top Performing Stations**
- **Chart Type:** Bar Chart
- **Data:** Stations with the highest number of trip starts and ends
- **Insight:** Highlights popular locations for better fleet management and placement.

---

### 3. **Trip Duration Distribution**
- **Chart Type:** Histogram
- **Data:** Distribution of trip durations in minutes
- **Insight:** Helps understand user behavior (e.g., average usage time).

---

### 4. **Map View: Active Station Locations**
- **Chart Type:** Geo Map
- **Data:** Latitude and longitude of stations
- **Insight:** Visualizes operational area and potential coverage gaps.

---

### 5. **Bike Type Usage Breakdown**
- **Chart Type:** Pie Chart
- **Data:** Share of trip count by bike type (e.g., Electric, Regular)
- **Insight:** Evaluates user preference and inventory allocation.

---

### 6. **Revenue by Station**
- **Chart Type:** Table with conditional formatting
- **Data:** Total fare collected per station
- **Insight:** Pinpoints revenue hotspots.

---

### 7. **Failed or Cancelled Trips**
- **Chart Type:** KPI & Time Series
- **Data:** Count of trips with “Cancelled” or “Failed” status
- **Insight:** Tracks operational issues or anomalies.

---

## ✅ Key Use Cases

- **Ops Teams**: Optimize station placement and bike distribution.
- **Business Teams**: Monitor revenue trends and usage patterns.
- **Product Teams**: Identify areas to improve ride experience or app features.

---

## 📍 Data Source

All visualizations are powered by **BigQuery tables** populated via:
- `Dataflow` (real-time ingestion)
- `Cloud Composer` (daily orchestration)
- `Cloud Run` (API simulation + GCS push)

---

