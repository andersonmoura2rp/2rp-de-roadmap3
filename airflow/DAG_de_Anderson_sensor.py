from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from custom_operators.tworp_spark_submit_operator import TwoRPSparkSubmitOperator
from airflow.operators.trigger_dagrun.TriggerDagRunLink import TriggerDagRunOperator

user = "2rp-anderson"

default_args = {
    "owner":user,
    "start_date": datetime(2021,12,22),
    "depend_on_past": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=1),
    "run_as_user": user,
    "proxy_user": user
}

with DAG(dag_id='DAG_de_Anderson_sensor', schedule_interval=None, default_args=default_args, catchup=False) as dag:
    t_dummy = DummyOperator(
        task_id="t_dummy"
    )

    trigger_target = TriggerDagOperator(
        task_id = "trigger_target",
        trigger_dag_id = "DAG_de_Anderson_dev"

    )

t_dummy >> trigger_target