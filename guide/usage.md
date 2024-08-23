***
# **Usage Guide**
This Docker container creates a comprehensive data engineering pipeline with components for streaming data, workflow management, and distributed processing. The services include Kafka, Spark, Schema Registry, Control Center, ZooKeeper Airflow, PostgreSQL, and Cassandra as shown in figure below.

![System Architecture Figure](https://github.com/brmil07/RT_Data_Streaming_Project/blob/main/System_Architecture.png)

# **Getting Started**
## **1. Navigate to the Directory**
navigate to the correct folder where the docker compose file is located
```bash
cd RT_Data_Streaming_Project
```
## **1. Start the Services**
```bash
docker compose up -d
```

### **1.1. Check the Status**
```bash
docker ps
```
### **1.2. Stopping the Services**
```bash
docker compose down
```
### **1.3. Viewing Logs**
```bash
docker-compose logs <service-name>
```

## **2. Trigger Airflow DAG**
Navigate to the browser and type:
```bash
localhost:8080
```
Enter the username and password, and then trigger the DAG

![airflow](https://github.com/brmil07/RT_Data_Streaming_Project/blob/main/guide/airflow_data_stream.png)

## **3. Monitor Streamed Data**
After DAG file is triggered, the streamed data can be monitored in the control center.
Navigate to the browser and type:
```bash
localhost:9021
```
![control center topic](https://github.com/brmil07/RT_Data_Streaming_Project/blob/main/guide/control_center.png)

The data streamed from the random user api can be seen here:

![control center monitor](https://github.com/brmil07/RT_Data_Streaming_Project/blob/main/guide/control_center_data_stream.png)

## **4. Activate Spark Streaming**
Navigate to the directory where the "spark_stream.py" is located.
```bash
cd stream
```
Execute the Python command to enable the streaming session utilizing Kafka and Apache Spark
```bash
python spark_stream.py
```
If the setup is done properly, it will shows this:

![spark stream](https://github.com/brmil07/RT_Data_Streaming_Project/blob/main/guide/spark_stream.png)

This process will keep continue until the code is terminated or an error occurs.

## **5. Cassandra**
To access Cassandra interactive terminal:
```bash
docker exec -it cassandra cqlsh -u cassandra -p cassandra localhost 9042
```
![cassandra cqlsh](https://github.com/brmil07/RT_Data_Streaming_Project/blob/main/guide/access_cassandra.png)

If the Airflow DAG is already executed and the data streaming process has been executed as well as the spark_streams.py,
the data will be populated in Cassandra DB, and this is the example query:
```bash
SELECT username, first_name, gender, dob FROM spark_streams.created_users;
```
![cassandra cqlsh](https://github.com/brmil07/RT_Data_Streaming_Project/blob/main/guide/cassandra_query.png)

To exit the interactive terminal:
```bash
exit
```

# **Additional Information**
Refer to the official documentation for each service for more in-depth configuration and usage details:

* [Kafka Documentation](https://kafka.apache.org/documentation/)
* [ZooKeeper Documentation](https://zookeeper.apache.org/documentation.html)
* [Schema Registry Documentation](https://docs.confluent.io/platform/current/schema-registry/index.html)
* [Control Center Documentation](https://docs.confluent.io/platform/current/control-center/index.html)
* [Airflow Documentation](https://airflow.apache.org/docs/)
* [Cassandra Documentation](https://cassandra.apache.org/doc/latest/)
* [Apache Spark](https://spark.apache.org/docs/latest/)