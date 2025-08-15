from airflow import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_operator", # 화면 이름 , python 파일명과 관련없음. -> 근데 일치 시키는게 좋음 몇백개 이상임.
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 8, 15, tz="Asia/Seoul"),
    catchup=False, # 누락 구간을 돌릴지 결정 -> bulk 성 데이터를 한꺼번에 돌림.. 
    tags=["example1", "example2", "example3"], # categories 가능. 
) as dag:
    bash_t1 = BashOperator (
          task_id = "bash_t1",
          bash_command = "echo who am i",
     )

    bash_t2 = BashOperator (
          task_id = "bash_t2",
          bash_command = "echo $HOSTNAME",
    )

    bash_t1 >> bash_t2