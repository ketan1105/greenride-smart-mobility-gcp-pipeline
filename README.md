# GreenRide: Smart Mobility Analytics GCP Pipeline 🚴‍♂️🌍

GreenRide is a simulated real-time data engineering project that showcases a scalable end-to-end pipeline to analyze smart urban mobility data using **Google Cloud Platform**. It highlights how ride data from electric vehicles (e-scooters, e-bikes, taxis) can be processed and analyzed to optimize routes, detect anomalies, and support city planning using GCP services.

---

## 🎯 Problem Statement

Urban cities are shifting toward sustainable transport. But without real-time analytics, it's hard to:

- Identify high-traffic or under-utilized zones
- Detect anomalies like sudden trip drops
- Monitor EV usage trends across zones

---

## ✅ Key Objectives

- Simulate real-world mobility ride data
- Build a real-time data ingestion and processing pipeline using **Cloud Functions**, **Pub/Sub**, **Dataflow**, **BigQuery**
- Visualize insights in **Looker Studio**
- Showcase anomaly detection and zone-wise analytics

---

## 🧰 Tech Stack & GCP Services Used

| Component       | Service Used                          |
|----------------|----------------------------------------|
| Data Generation | Cloud Function + Pub/Sub              |
| Ingestion       | Pub/Sub + Cloud Storage               |
| Processing      | Dataflow (Apache Beam Python SDK)     |
| Storage         | BigQuery                              |
| Orchestration   | Cloud Composer (Airflow)              |
| Visualization   | Looker Studio                         |

---

## 🛠️ Architecture Diagram

![Architecture](architecture/greenride_architecture.png)

---

## 🧪 Sample Simulated Data

```json
{
  "ride_id": "RIDE10098",
  "vehicle_type": "e-scooter",
  "start_time": "2025-07-24T08:35:00Z",
  "end_time": "2025-07-24T08:55:00Z",
  "start_zone": "Zone A",
  "end_zone": "Zone C",
  "distance_km": 2.5,
  "avg_speed_kmph": 12.1,
  "battery_usage_pct": 4.7
}
