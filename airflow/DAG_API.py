from airflow import DAG
from datetime import datetime
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators import SimpleHttpOperator
from airflow.models import Variable
from airflow.operators.python_operator import PythonOperator
import json
import pandas as pd 

dag_id = Varible.get("Dag Id")
execution_date = Variable.get("Execution Date")
state = Variable.get("State")

default_args = {
    'owner' : '2rp-anderson',
    'depends_on_past' : 'False',
    'retries' : 3
}

def processing_user(dag_id, execution_date, state):
    