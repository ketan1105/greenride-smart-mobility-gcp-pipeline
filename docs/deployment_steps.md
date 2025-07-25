# 🚀 Deployment Steps for GreenRide Smart Mobility GCP Pipeline

This document outlines the step-by-step guide to deploy the **GreenRide Smart Mobility Data Pipeline** using Google Cloud Platform services. The pipeline processes simulated smart mobility data and builds a real-time analytics dashboard.

---

## 1. Create Required GCP Resources

- **GCS Buckets**:
  - `greenride-raw-bucket`: For storing raw incoming data.
  - `greenride-processed-bucket`: For transformed outputs.
  - `greenride-archive-bucket`: For archiving processed data.

- **BigQuery Datasets & Tables**:
  - Dataset: `greenride_dataset`
  - Tables:
    - `trips_data` – Load using `trips_schema.json`
    - `stations_data` – Load using `stations_schema.json`

---

## 2. Simulate and Push Data to GCS

- **Run `generate_greenride_data.py`**:
  - Simulates smart mobility data (trips, stations, fares, etc.)
  - Generates CSV or JSON files locally.

- **Deploy `push_to_gcs.py` as Cloud Run Service**:
  - This service uploads the generated data to `greenride-raw-bucket`.
  - Triggered manually or on a schedule.

---

## 3. Orchestrate Pipeline with Cloud Composer (Airflow)

- **Deploy `greenride_data_ingestion_dag.py`**:
  - Scheduled DAG to trigger Cloud Run → Dataflow pipeline.
  - Monitors GCS bucket and triggers ingestion jobs.
  - Logs job run in Airflow UI.

---

## 4. Data Transformation using Dataflow

- **Deploy `greenride_dataflow_job.py`**:
  - Reads raw data from GCS.
  - Cleans, transforms, and loads into BigQuery.
  - Handles error records and logs metrics.

---

## 5. Create Looker Studio Dashboard

- Connect to BigQuery `greenride_dataset`.
- Visualize:
  - Trip trends over time
  - Busiest stations
  - Route-wise traffic
  - Revenue distribution
- Take screenshots and save them in `looker_dashboard/`.

---

## 6. Monitor and Logging

- Enable **Cloud Logging** and **Cloud Monitoring**.
- View logs for:
  - Cloud Run data push
  - Dataflow jobs
  - Airflow task runs

---

## 7. Security and IAM (Optional)

- Service account roles:
  - Cloud Run → GCS Writer
  - Dataflow → GCS & BigQuery Editor
  - Airflow → Cloud Run & Dataflow Triggerer

---

## ✅ Summary

| Component     | GCP Service       |
|---------------|------------------|
| Ingestion     | Cloud Run        |
| Orchestration | Cloud Composer   |
| Processing    | Dataflow         |
| Storage       | Cloud Storage    |
| Warehousing   | BigQuery         |
| Visualization | Looker Studio    |
| Monitoring    | Cloud Logging    |
