from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from custom_operators.tworp_spark_submit_operator import TwoRPSparkSubmitOperator
default_args = {
    "owner":"2rp-anderson",
    "start_date": datetime(2021,12,22),
    "depend_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "run_as_user": "2rp-anderson",
    "proxy_user": "2rp-anderson"
}

with DAG(dag_id='DAG_de_Anderson_dev', schedule_interval=None, default_args=default_args, catchup=False) as dag:
    task_1 = DummyOperator(
        task_id="task_1"
    )
    t_kinit = BashOperator(
        task_id="t_kinit",
        bash_command=f'kinit -kt /home/2rp-anderson/2rp-anderson.keytab 2rp-anderson'
    )
    t_executar = BashOperator(
        task_id="t_executar",
        bash_command=f'/home/2rp-anderson/executar.sh'
    )
    t_pokemon = TwoRPSparkSubmitOperator(
        task_id="t_pokemon",
        name="t_pokemon",
        conn_id="spark_conn",
        application=f'/home/2rp-anderson/pokemons_oldschool.py',
        keytab=f'/home/2rp-anderson/2rp-anderson.keytab',
        proxy_user=None,
        verbose=True
    )

    task_1 >> t_kinit >> t_executar >> t_pokemon 