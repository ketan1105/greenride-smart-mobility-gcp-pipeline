# GreenRide: Smart Mobility Analytics on GCP

GreenRide is a full-scale data engineering project built to simulate and analyze smart electric vehicle (EV) ride data using Google Cloud Platform (GCP). The goal is to offer cities and mobility startups actionable insights into electric ride patterns, charging behavior, and route efficiency to support green urban transport planning.

> ✅ This project demonstrates my ability to design scalable pipelines using GCP services like Cloud Run, Pub/Sub, Dataflow, BigQuery, Looker Studio, and Cloud Composer — backed by realistic simulated data for near real-time analytics.

---

## 🚀 Project Architecture

![GreenRide Architecture](architecture_diagram.png)

---

## 🎯 Objective

To simulate and analyze EV ride-sharing data to:
- Monitor ride and charging trends across urban zones.
- Detect route inefficiencies and charging station bottlenecks.
- Enable real-time decision-making via Looker dashboards.

---

## 🛠️ Services Used

| GCP Service      | Purpose |
|------------------|---------|
| Cloud Storage    | Store raw ride JSON files |
| Cloud Pub/Sub    | Stream ride data to Dataflow |
| Cloud Run  | Trigger simulation and publish events |
| Dataflow (Apache Beam) | Transform and enrich streaming data |
| BigQuery         | Store and analyze processed data |
| Looker Studio    | Build real-time interactive dashboards |
| Cloud Composer   | Schedule pipeline orchestration |

---

## 📦 Project Structure

```
greenride-smart-mobility-gcp-pipeline/
│
├── README.md
├── architecture/
│   └── greenride_architecture_diagram.png
│
├── data_simulation/
│   └── generate_greenride_data.py
│
├── cloud_run/
│   └── push_to_gcs.py
│
├── dataflow_pipeline/
│   └── greenride_dataflow_job.py
│
├── airflow_dag/
│   └── greenride_data_ingestion_dag.py
│
├── bigquery/
│   └── schema/
│       ├── trips_schema.json
│       └── stations_schema.json
│
├── looker_dashboard/
│   ├── dashboard_screenshot_1.png
│   ├── dashboard_screenshot_2.png
│   └── dashboard_explanation.md
│
└── docs/
    ├── greenride_summary.md
    └── deployment_steps.md

```
---

## 📊 Looker Dashboard Preview

![Dashboard Screenshot](dashboard/dashboard_mockup.png)

### Dashboard KPIs:
- ⚡ Total Rides | 🔋 Avg Battery Consumption | ⏱️ Avg Trip Duration
- 📍 Zone-wise EV traffic | 🔌 Charging Station Load | 📈 Hourly Trends

---

## 🧪 Data Simulation

The ride and charge data is **simulated using Python** to reflect realistic patterns:
- EV ID, location (lat/lon), battery %, start/end time
- Charging station usage and energy consumed
- Randomized across 5 zones and 24-hour period

Why simulate?  
→ Real ride data is not public. Simulation lets us test streaming pipelines and analytics design effectively, ensuring architectural skill demonstration.

---

## ⚙️ Deployment Steps

> These steps assume the project is fully implemented and deployed.

### 1. Create GCS Buckets
- `greenride-raw-bucket` – for raw JSON ride data
- `greenride-processed-bucket` – for backups, logs

### 2. Deploy Cloud Function
Trigger the `publisher_function.py` daily to send data to Pub/Sub.

### 3. Set up Pub/Sub
Topic: `greenride-stream`  
Subscription: `dataflow-sub`

### 4. Launch Dataflow Job
Dataflow pipeline (`main.py`) reads from Pub/Sub, transforms data, and writes to BigQuery.

### 5. Create BigQuery Dataset
Dataset: `greenride_dataset`  
Table: `ride_summary`

### 6. Orchestrate via Cloud Composer
The DAG (`greenride_dag.py`) schedules Cloud Function + Dataflow daily.

### 7. Connect BigQuery to Looker Studio
Build dashboard using connected BQ views to present EV trends and zone insights.

---

## 🧠 Key Learnings

- Designed streaming + batch hybrid pipelines
- Simulated realistic EV mobility data
- Used Pub/Sub → Dataflow → BigQuery for real-time analysis
- Dashboarded data in Looker Studio for storytelling
- Scheduled workflows via Cloud Composer

---

## 👨‍💻 Skills Demonstrated

- Data Engineering | GCP | Python | Apache Beam
- Pub/Sub | Dataflow | BigQuery | Looker | Cloud Run | DAG orchestration

---

## 📢 Real-World Impact (Simulated)

This project showcases how mobility platforms or city governments can:
- Optimize EV routes based on ride demand
- Predict high-traffic zones for EV deployment
- Prevent charging station overload via usage analytics

---

## 📬 Contact

*Author:* Ketan Jain  
📧 Email: ketanjain1105@gmail.com
🔗 LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/ketan-jain-/)  
