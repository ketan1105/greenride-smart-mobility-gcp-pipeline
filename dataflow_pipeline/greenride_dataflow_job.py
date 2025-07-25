import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, GoogleCloudOptions, StandardOptions
import json

# Set your project and BigQuery dataset/table info
PROJECT_ID = "your-gcp-project-id"
BQ_DATASET = "greenride_dataset"
TRIPS_TABLE = f"{PROJECT_ID}:{BQ_DATASET}.trips"
STATIONS_TABLE = f"{PROJECT_ID}:{BQ_DATASET}.stations"

class ParseJson(beam.DoFn):
    def process(self, element):
        yield json.loads(element)

def run():
    options = PipelineOptions()
    google_cloud_options = options.view_as(GoogleCloudOptions)
    google_cloud_options.project = PROJECT_ID
    google_cloud_options.region = "us-central1"
    google_cloud_options.job_name = "greenride-dataflow-job"
    google_cloud_options.staging_location = "gs://greenride-raw-bucket/staging"
    google_cloud_options.temp_location = "gs://greenride-raw-bucket/temp"
    options.view_as(StandardOptions).runner = "DataflowRunner"

    with beam.Pipeline(options=options) as pipeline:

        # Process trips data
        trips = (
            pipeline
            | "Read Trips" >> beam.io.ReadFromText("gs://greenride-raw-bucket/raw/trips.json")
            | "Parse Trips JSON" >> beam.ParDo(ParseJson())
            | "Write Trips to BQ" >> beam.io.WriteToBigQuery(
                TRIPS_TABLE,
                schema="SCHEMA_AUTODETECT",
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

        # Process stations data
        stations = (
            pipeline
            | "Read Stations" >> beam.io.ReadFromText("gs://greenride-raw-bucket/raw/stations.json")
            | "Parse Stations JSON" >> beam.ParDo(ParseJson())
            | "Write Stations to BQ" >> beam.io.WriteToBigQuery(
                STATIONS_TABLE,
                schema="SCHEMA_AUTODETECT",
                write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
        )

if __name__ == "__main__":
    run()
