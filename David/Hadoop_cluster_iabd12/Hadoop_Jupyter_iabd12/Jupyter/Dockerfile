FROM hadoop-base-image-iabd12:latest

ENV LOG_TAG="[Jupyter Notebook]:"
ENV BASE_DIR=/opt/bd
ENV VENV_DIR=${BASE_DIR}/venv
ENV HADOOP_HOME=${BASE_DIR}/hadoop
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
ENV PATH=${PATH}:${HADOOP_HOME}/bin

USER root
RUN echo "$LOG_TAG Instalando Python, pip y dependencias adicionales" && \
    apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-venv python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN python3 -m venv ${VENV_DIR} && \
    ${VENV_DIR}/bin/pip install --upgrade pip && \
    ${VENV_DIR}/bin/pip install jupyter pyspark numpy pandas matplotlib seaborn hdfs

COPY ./Config-files/core-site.xml ${HADOOP_CONF_DIR}/core-site.xml
COPY ./Config-files/hdfs-site.xml ${HADOOP_CONF_DIR}/hdfs-site.xml

EXPOSE 8888

USER hdadmin

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
ENV PATH=${PATH}:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin/

WORKDIR ${HADOOP_HOME}

CMD ["/bin/bash", "-c", "${VENV_DIR}/bin/jupyter-notebook --ip=0.0.0.0 --port=8888 --no-browser"]
