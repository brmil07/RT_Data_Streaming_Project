from kafka import KafkaProducer
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def stream_data():
    try:
        producer = KafkaProducer(
            bootstrap_servers=['localhost:9092'],
            max_block_ms=5000
        )
        logger.info("Kafka Producer connected successfully.")
        # Your data streaming code here
    except Exception as e:
        logger.error(f"Error connecting Kafka Producer: {e}")

if __name__ == "__main__":
    stream_data()