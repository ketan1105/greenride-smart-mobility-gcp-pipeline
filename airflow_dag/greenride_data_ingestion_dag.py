from airflow import models
from airflow.providers.google.cloud.operators.cloud_run import CloudRunExecuteJobOperator
from airflow.providers.google.cloud.operators.dataflow import DataflowStartPythonJobOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"
GCS_SCRIPT_PATH = "gs://greenride-raw-bucket/scripts/greenride_dataflow_job.py"

with models.DAG(
    dag_id="greenride_data_ingestion_dag",
    schedule_interval="@daily",
    start_date=days_ago(1),
    catchup=False,
    default_args={
        "owner": "data-engineering",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["greenride", "data-pipeline"],
) as dag:

    trigger_cloud_run = CloudRunExecuteJobOperator(
        task_id="trigger_cloud_run_push",
        project_id=PROJECT_ID,
        region=REGION,
        job_name="greenride-cloud-run-job",  # Assuming a job has been created via Cloud Run Job
    )

    start_dataflow_job = DataflowStartPythonJobOperator(
        task_id="start_dataflow_job",
        py_file=GCS_SCRIPT_PATH,
        project_id=PROJECT_ID,
        location=REGION,
        job_name="greenride-dataflow",
        options={
            "tempLocation": "gs://greenride-raw-bucket/temp",
            "stagingLocation": "gs://greenride-raw-bucket/staging",
            "runner": "DataflowRunner",
        },
    )

    trigger_cloud_run >> start_dataflow_job
