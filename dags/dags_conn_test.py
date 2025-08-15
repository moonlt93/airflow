from airflow import DAG
import datetime
import pendulum
from airflow.providers.standard.operators.empty import EmptyOperator

with DAG(
    dag_id="dags_bash_operator", # 화면 이름 , python 파일명과 관련없음. -> 근데 일치 시키는게 좋음 몇백개 이상임.
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2025, 8, 15, tz="Asia/Seoul"),
    catchup=False, # 누락 구간을 돌릴지 결정 -> bulk 성 데이터를 한꺼번에 돌림.. 
    tags=["example1", "example2", "example3"], # categories 가능. 
) as dag:
    t1 = EmptyOperator(
        task_id = "t1"
    )

    t2 = EmptyOperator(
        task_id = "t2"
    )

    t3 = EmptyOperator(
        task_id = "t3"
    )

    t4 = EmptyOperator(
        task_id = "t4"
    )

    t5 = EmptyOperator(
        task_id = "t5"
    )

    t6 = EmptyOperator(
        task_id = "t6"
    )

    t7 = EmptyOperator(
        task_id = "t7"
    )

    t8 = EmptyOperator(
        task_id = "t8"
    )

    t1 >> [t2,t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8
    