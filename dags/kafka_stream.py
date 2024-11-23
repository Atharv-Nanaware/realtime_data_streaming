from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
import requests
import json
import time
from kafka import KafkaProducer

# Default args for the DAG
default_args = {
    'owner': 'Atharv',
    'start_date': datetime(2024, 10, 10, 12, 0)  # Corrected start_date to datetime
}

# Function to fetch user data from randomuser.me
def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    res = res['results'][0]  # To get Only one user data
    return res

# Function to format the data as required
def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']
    return data

# Function to stream data to Kafka
def stream_data():
    import json
    from kafka import KafkaProducer
    import time
    import logging

    producer = KafkaProducer(bootstrap_servers=['broker:29092'], max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 60: #1 minute
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('users_created', json.dumps(res).encode('utf-8'))
        except Exception as e:
            logging.error(f'An error occured: {e}')
            continue
# DAG definition
with DAG('user_automation',  # Corrected the typo in the DAG name
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:
    
    # Task to stream data
    streaming_task = PythonOperator(
        task_id='streaming_task',
        python_callable=stream_data,
        dag=dag
    )
