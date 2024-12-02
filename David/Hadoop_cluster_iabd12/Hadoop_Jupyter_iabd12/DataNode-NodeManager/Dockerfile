FROM hadoop-base-image-iabd12:latest

USER root

ENV HADOOP_VERSION=3.3.6
ENV LOG_TAG="[DNNM Hadoop_${HADOOP_VERSION}]"
ENV BASE_DIR=/opt/bd
ENV HADOOP_HOME=${BASE_DIR}/hadoop/
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop/
ENV DATA_DIR=/var/data/hadoop/hdfs

RUN echo "$LOG_TAG Crea directorios para los datos de HDFS del DataNode" && \
    mkdir -p ${DATA_DIR}/dn && chown -R hdadmin:hadoop ${DATA_DIR}

RUN echo "$LOG_TAG Crea directorio para los ficheros de log" && \
    mkdir ${HADOOP_HOME}/logs

RUN echo "$LOG_TAG Copia los ficheros de configuracion y el script de inicio"
COPY Config-files/core-site.xml ${HADOOP_CONF_DIR}/core-site.xml
COPY Config-files/hdfs-site-datanode.xml ${HADOOP_CONF_DIR}/hdfs-site.xml
COPY Config-files/yarn-site-nodemanager.xml ${HADOOP_CONF_DIR}/yarn-site.xml
COPY Config-files/mapred-site-nodemanager.xml ${HADOOP_CONF_DIR}/mapred-site.xml

COPY Config-files/start-daemons-dnnm.sh ${BASE_DIR}/start-daemons.sh

RUN chmod +x ${BASE_DIR}/start-daemons.sh && \
    chown -R hdadmin:hadoop ${BASE_DIR}

EXPOSE 9864 9865 9866 9867
EXPOSE 8040 8042 8044 8048
EXPOSE 50000-50050 50100-50200

USER hdadmin

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
ENV HADOOP_HOME=${BASE_DIR}/hadoop/
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop/
ENV PATH=${PATH}:${HADOOP_HOME}/bin/:${HADOOP_HOME}/sbin/

WORKDIR ${HADOOP_HOME}

RUN echo "$LOG_TAG Iniciando demonios"
CMD ["/opt/bd/start-daemons.sh"]
