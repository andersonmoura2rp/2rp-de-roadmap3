from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.bash_operator import BashOperator
from custom_operators.tworp_spark_submit_operator import TwoRPSparkSubmitOperator

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

with DAG(dag_id='DAG_de_Anderson_dev', schedule_interval=None, default_args=default_args, catchup=False) as dag:
    t_dummy = DummyOperator(
        task_id="t_dummy"
    )
    t_kinit = BashOperator(
        task_id="t_kinit",
        bash_command=f'kinit -kt /home/{user}/{user}.keytab {user}'
    )
    t_executar = BashOperator(
        task_id="t_executar",
        bash_command=f'bash /home/{user}/shell-script/executar.sh /home/{user}/teste arquivo'
    )
    t_pokemon = TwoRPSparkSubmitOperator(
        task_id="t_pokemon",
        name="pokemon",
        conn_id="spark_conn",
        application=f'/home/{user}/pokemons_oldschool.py',
	    conf={'spark.yarn.queue':'root.users.2rp-anderson','spark.driver.memory':'20g'},
        keytab=f'/home/{user}/{user}.keytab',
        principal=user,
        proxy_user=None,
        verbose=True
    )

    t_dummy >> t_kinit >> t_executar >> t_pokemon