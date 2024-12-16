FROM ubuntu:latest

USER root

ENV HADOOP_VERSION 3.3.6
ENV BASE_DIR /opt/bd
ENV LOG_TAG "[BASE Hadoop_${HADOOP_VERSION}]"
ENV REPOSITORY https://dlcdn.apache.org/hadoop/common

RUN echo "$LOG_TAG Actualizando e instalando paquetes básicos" && \
    apt-get update && \
    apt-get install -y --no-install-recommends openjdk-8-jre python3 curl locales iputils-ping nano python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN echo "$LOG_TAG Creando locales" && \
    locale-gen es_ES.UTF-8 && update-locale LANG=es_ES.UTF-8

RUN mkdir -p ${BASE_DIR}

WORKDIR ${BASE_DIR}

RUN echo "$LOG_TAG Descargando Hadoop" && \
    curl -fLO "${REPOSITORY}/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz"  && \
    tar xzvf hadoop-${HADOOP_VERSION}.tar.gz && \
    ln -s hadoop-${HADOOP_VERSION} hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Crear un entorno virtual y instalar mrjob
RUN python3 -m venv ${BASE_DIR}/venv && \
    ${BASE_DIR}/venv/bin/pip install --upgrade pip && \
    ${BASE_DIR}/venv/bin/pip install mrjob

RUN groupadd -r hadoop && \
    useradd -r -g hadoop -d ${BASE_DIR} -s /bin/bash hdadmin

RUN chown -R hdadmin:hadoop ${BASE_DIR}
