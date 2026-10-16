# Most recently: 
    # Neil was here June 1, 2026, ensuring that this also works in Prod
    # Ref: https://monitor.library.ualberta.ca/unixDoc/Change/2026/Q2/CR1330.html
#Earlier:
    # Neil was here Apr 17, 2026
    # Ref: https://monitor.library.ualberta.ca/unixDoc/Projects/2025/Q3/PDP/HashiCorp_Vault.html
    # This culminates weeks of effort to get Airflow to connect to Vault & read a credential from it
from airflow import DAG
from airflow.sdk.bases.hook import BaseHook
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime, timedelta

def test_vault_connection():
    #conn = BaseHook.get_connection("my_db") # please don't use this!
    conn = BaseHook.get_connection("archives/my_db")
    print(f"✅ host: {conn.host}, login: {conn.login}, schema: {conn.schema}")

with DAG(
    dag_id="vault_smoke_test",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    tags=["infra", "test"],
) as dag:
    PythonOperator(
        task_id="read_vault_secret",
        python_callable=test_vault_connection,
    )

