# 🌿 GreenRide – Smart Mobility GCP Pipeline

GreenRide is a scalable data engineering solution built on Google Cloud Platform (GCP) to process and analyze smart mobility data (e.g., bike/scooter trips, station data). The project mimics real-time ingestion, transformation, and visualization using modern cloud-native tools.

---

## 🎯 Objective

- Simulate ride and station data using a custom Python script
- Store raw data in Cloud Storage
- Ingest and process data via Apache Beam on Dataflow
- Orchestrate workflows using Cloud Composer (Airflow)
- Load clean data into BigQuery for analysis
- Build insightful dashboards in Looker Studio

---

## 🏗️ Key Components

| Component         | Purpose                                                                 |
|------------------|-------------------------------------------------------------------------|
| Data Simulation   | Simulates trip and station data mimicking API-like structure            |
| Cloud Run         | Hosts API logic and pushes data to GCS                                  |
| Cloud Storage     | Acts as raw and staging storage layers                                  |
| Dataflow          | Transforms and cleans data in a scalable pipeline                       |
| Cloud Composer    | Automates end-to-end orchestration (DAG for ingestion)                  |
| BigQuery          | Stores clean data in analytics-ready tables                             |
| Looker Studio     | Visualizes metrics, KPIs, and usage trends for stakeholders             |

---

## 🧱 Data Flow

1. **Simulation** → `generate_greenride_data.py`
2. **Ingestion** → `Cloud Run` triggers data to `GCS`
3. **Transformation** → `Dataflow` job loads clean data to `BigQuery`
4. **Orchestration** → `Airflow DAG` handles daily ETL
5. **Visualization** → `Looker Studio` dashboard from `BigQuery` tables

---

## 📌 Tables in BigQuery

- `greenride.trips`
- `greenride.stations`

---

## 🚀 Why This Project?

✅ End-to-end GCP experience  
✅ Real-time & batch processing simulation  
✅ Production-like orchestration and schema handling  
✅ Dashboard with meaningful KPIs for business and ops

---

