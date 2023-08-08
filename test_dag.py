from airflow import DAG
from airflow.operators import PythonOperator #Функция которая позволяет описывать task внутри DAGa
from datatime import datatime # Позволяет прописывать время задач
import pathlib

# 2. Прописываем дефолтные аргументы в словаре
default_args = {
'owner': 'osilyutina',
'depends_on_past': False,
'start_date': datetime(2019, 2, 20),
'retries': 0
}
# 3. Описываем основные метаданные DAGа - расписание, название
dag = DAG('hello_world',
default_args=default_args,
schedule_interval='00 12 * * 1')

# 4. Если используем PythonOperator, можем прямо здесь описать функцию,
которая будет исполняться по расписанию

def hello():
print('Hello, world!')

def sum_int():
return print('2+3')

5. Описываем таску, которая будет исполнять нашу функцию hello()
t1 = PythonOperator(task_id='task1', python_callable=hello,
dag=dag)
t2 = PythonOperator(task_id='task1', python_callable=sum_int,
dag=dag)
t1 >> t2

