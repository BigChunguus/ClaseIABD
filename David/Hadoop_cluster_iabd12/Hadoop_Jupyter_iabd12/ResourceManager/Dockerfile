FROM hadoop-base-image-iabd12:latest

USER root

ENV HADOOP_VERSION=3.3.6
ENV LOG_TAG="[Resourcemanager Hadoop_${HADOOP_VERSION}]"
ENV BASE_DIR=/opt/bd
ENV HADOOP_HOME=${BASE_DIR}/hadoop/
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop/

RUN echo "$LOG_TAG Crea directorio para los ficheros de log" && \
    mkdir ${HADOOP_HOME}/logs

RUN echo "$LOG_TAG Copia los ficheros de configuracion y el script de inicio"
COPY Config-files/core-site.xml ${HADOOP_CONF_DIR}/core-site.xml
COPY Config-files/yarn-site-resourcemanager.xml ${HADOOP_CONF_DIR}/yarn-site.xml
COPY Config-files/mapred-site-resourcemanager.xml ${HADOOP_CONF_DIR}/mapred-site.xml

COPY Config-files/start-daemons-resourcemanager.sh ${BASE_DIR}/start-daemons.sh

RUN chmod +x ${BASE_DIR}/start-daemons.sh && \
    chown -R hdadmin:hadoop ${BASE_DIR}

EXPOSE 8030 8031 8032 8033 8088 8090

RUN useradd -u 2000 luser

USER hdadmin

ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
ENV HADOOP_HOME=${BASE_DIR}/hadoop/
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop/
ENV PATH=${PATH}:${HADOOP_HOME}/bin/:${HADOOP_HOME}/sbin/

WORKDIR ${HADOOP_HOME}

RUN echo "$LOG_TAG Iniciando demonios"
CMD ["/opt/bd/start-daemons.sh"]
