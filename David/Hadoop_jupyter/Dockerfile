# Usamos una imagen base de OpenJDK 11 con Python 3.8
FROM openjdk:11-slim

# Instalamos dependencias del sistema
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    wget \
    curl \
    git \
    vim \
    ssh \
    sshpass \
    procps \
    lsof \
    && apt-get clean

# Establecemos las versiones de Hadoop y Spark
ENV HADOOP_VERSION 3.3.6
ENV SPARK_VERSION 3.5.3

# Descargamos e instalamos Hadoop 3.3.6
RUN wget https://downloads.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz -P /tmp && \
    tar -xvzf /tmp/hadoop-$HADOOP_VERSION.tar.gz -C /opt && \
    rm /tmp/hadoop-$HADOOP_VERSION.tar.gz && \
    mv /opt/hadoop-$HADOOP_VERSION /opt/hadoop

# Descargamos e instalamos Spark 3.5.3 (archivo válido)
RUN wget https://dlcdn.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz -P /tmp && \
    tar -xvzf /tmp/spark-3.5.3-bin-hadoop3.tgz -C /opt && \
    rm /tmp/spark-3.5.3-bin-hadoop3.tgz && \
    mv /opt/spark-3.5.3-bin-hadoop3 /opt/spark

# Instalamos Python y dependencias necesarias
RUN pip install pyspark jupyter

# Configuramos las variables de entorno de Hadoop y Spark
ENV HADOOP_HOME=/opt/hadoop
ENV SPARK_HOME=/opt/spark
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$HADOOP_HOME/bin:$SPARK_HOME/bin:$PATH
ENV PYSPARK_PYTHON=python3
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook"

# Exponemos el puerto para Jupyter Notebook
EXPOSE 8888

# Comando por defecto
CMD ["/bin/bash"]
