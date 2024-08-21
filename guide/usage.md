***
# **Usage Guide**
This Docker container creates a comprehensive data engineering pipeline with components for streaming data, workflow management, and distributed processing. The services include Kafka, Schema Registry, Control Center, ZooKeeper Airflow, PostgreSQL, and Cassandra as shown in figure below.

![System Architecture Figure](https://github.com/brmil07/RT_Data_Streaming_Project/blob/main/guide/System_Architecture_2.png)

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

## **2. Check the Status**
```bash
docker ps
```
## **3. Stopping the Services**
```bash
docker compose down
```
## **4. Viewing Logs**
```bash
docker-compose logs <service-name>
```

# **Additional Information**
Refer to the official documentation for each service for more in-depth configuration and usage details:

* [Kafka Documentation](https://kafka.apache.org/documentation/)
* [ZooKeeper Documentation](https://zookeeper.apache.org/documentation.html)
* [Schema Registry Documentation](https://docs.confluent.io/platform/current/schema-registry/index.html)
* [Control Center Documentation](https://docs.confluent.io/platform/current/control-center/index.html)
* [Airflow Documentation](https://airflow.apache.org/docs/)
* [Cassandra Documentation](https://cassandra.apache.org/doc/latest/)