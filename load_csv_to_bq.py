from datetime import datetime
from google.operators.empty import EmptyOperator
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

default_args = {
    "owner": "airflow",
    "retries": 1,
    
}

with DAG(
    dag_id="gcs_to_bigquery_load",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
   
) as dag:

    start =EmptyOperator(task_id="start")


    load_csv_to_bq = GCSToBigQueryOperator(
        task_id="load_csv_to_bq",
        bucket=bkt-demo-33,
        source_objects=["customer.csv"],
        destination_project_dataset_table="`project-b7277fe2-8bfe-4e91-8a2.composer.customer`",
        source_format="CSV",
        skip_leading_rows=1,
        write_disposition="WRITE_TRUNCATE",
        
        
    )

    end=EmptyOperator(task_id="end")

    start >> load_csv_to_bq >> end
