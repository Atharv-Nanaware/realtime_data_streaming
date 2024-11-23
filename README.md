# StreamFlow: Real-Time Data Pipeline and Analytics


## Table of Contents
- [Introduction](#introduction)
- [System Architecture](#system-architecture)
- [Learnings from Project](#Learnings-From-Project)
- [Technologies](#technologies)
- [Documents reffered](#Documents-reffered)
- [Getting Started](#getting-started)


## Introduction

This project serves as a comprehensive guide to building an end-to-end data engineering pipeline. It covers each stage from data ingestion to processing and finally to storage, utilizing a robust tech stack that includes Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. Everything is containerized using Docker for ease of deployment and scalability.

## System Architecture

![System Architecture]()

The project is designed with the following components:

- **Data Source**: We use `randomuser.me` API to generate random user data for our pipeline.
- **Apache Airflow**: Responsible for orchestrating the pipeline and storing fetched data in a PostgreSQL database.
- **Apache Kafka and Zookeeper**: Used for streaming data from PostgreSQL to the processing engine.
- **Control Center and Schema Registry**: Helps in monitoring and schema management of our Kafka streams.
- **Apache Spark**: For data processing with its master and worker nodes.
- **Cassandra**: Where the processed data will be stored.

## Learnings From Project

- Building and orchestrating a data pipeline with Apache Airflow.
- Implementing real-time data streaming with Apache Kafka.
- Managing distributed synchronization with Apache Zookeeper.
- Performing large-scale data processing using Apache Spark.
- Using PostgreSQL and Cassandra for reliable data storage.
- Containerizing and orchestrating the entire setup with Docker for streamlined deployment


## Technologies

- Apache Airflow
- Python
- Apache Kafka
- Apache Zookeeper
- Apache Spark
- Cassandra
- PostgreSQL
- Docker

## Documents reffered

- https://mvnrepository.com/
- https://airflow.apache.org/docs/
- https://cassandra.apache.org/doc/latest/



## Getting Started

1. Clone the repository:
    ```bash
    git clone 
    ```

2. Navigate to the project directory:
    ```bash
    cd 
    ```

3. Run Docker Compose to spin up the services:
    ```bash
    docker-compose up
    ```