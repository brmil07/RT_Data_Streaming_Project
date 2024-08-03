import uuid
import requests
import json
import time
import logging

from datetime import datetime, timedelta
from kafka import KafkaProducer
from kafka.errors import KafkaError
from airflow import DAG
from airflow.operators.python import PythonOperator

# Configure logging
logging.basicConfig(level=logging.INFO)
now = datetime.now()
default_args = {'owner': 'brmil07',
                'start_date': now,
                'retries': 1,
                'retry_delay': timedelta(minutes=5)
                }


def on_send_success(record_metadata):
    logging.info(f'Message successfully sent to topic {record_metadata.topic} '
                 f'partition {record_metadata.partition} '
                 'offset {record_metadata.offset}')


def on_send_error(excp):
    logging.error(f'Failed to send message: {excp}')


def get_data():
    try:
        response = requests.get("https://randomuser.me/api/")
        response.raise_for_status()
        data = response.json()
        return data['results'][0]
    except requests.RequestException as e:
        logging.error(f'Error fetching data: {e}')
        return None
    

def format_data(res):
    data = {}
    location = res['location']
    data['id'] = str(uuid.uuid4())
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data


def stream_data():
    try:
        producer = KafkaProducer(
            bootstrap_servers=['broker:29092'], #broker:29092 localhost:9092
            max_block_ms=5000,
            acks='all',  # Ensure all brokers acknowledge
            retries=3    # Retry on failure
        )

        # Check if connected
        if producer.bootstrap_connected():
            logging.info('Successfully connected to Kafka broker.')
        else:
            logging.warning('Failed to connect to Kafka broker.')

        curr_time = time.time()

        while True:
            if time.time() > curr_time + 60:  # Sending data for 1 minute
                break

            try:
                res = get_data()
                res = format_data(res)

                # Send message and add callbacks for success and error
                producer.send('users_created', json.dumps(res).encode('utf-8')) \
                    .add_callback(on_send_success) \
                    .add_errback(on_send_error)
                
                time.sleep(1)

            except Exception as e:
                logging.error(f'An error occurred: {e}')
                continue

    except KafkaError as e:
        logging.error(f'KafkaError occurred: {e}')
    except Exception as e:
        logging.error(f'An unexpected error occurred: {e}')
    finally:
        producer.close()


with DAG('user_automation',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )

if __name__ == "__main__":
    stream_data()