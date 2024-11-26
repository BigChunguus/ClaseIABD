# Para ejecutar este Dockerfile, posicionate en consola en el directorio donde tengas este arvhivo y lanza
# este comando: docker build -t hadoop-resourcemanager-image-iabd12 .
# Me conecto al Hub de Docker para bajarme una imagen de Ubuntu Server, sencilla y la última versión.
FROM hadoop-base-image-iabd12:latest


# Dockerfile para el ResourceManager
# Switch to root user
USER root

# Define valores de entorno
ENV HADOOP_VERSION=3.3.6
ENV LOG_TAG="[Resourcemanager Hadoop_${HADOOP_VERSION}]:"
ENV BASE_DIR=/opt/bd
ENV HADOOP_HOME=${BASE_DIR}/hadoop/
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop/

# Crea directorio para los ficheros de log
RUN echo "$LOG_TAG Crea directorio para los ficheros de log" && \
    mkdir ${HADOOP_HOME}/logs

# Copia los ficheros de configuracion
RUN echo "$LOG_TAG Copia los ficheros de configuracion y el script de inicio"
COPY Config-files/core-site.xml ${HADOOP_CONF_DIR}/core-site.xml
COPY Config-files/yarn-site-resourcemanager.xml ${HADOOP_CONF_DIR}/yarn-site.xml
COPY Config-files/mapred-site-resourcemanager.xml ${HADOOP_CONF_DIR}/mapred-site.xml

# Script de inicio 
COPY Config-files/start-daemons-resourcemanager.sh ${BASE_DIR}/start-daemons.sh

# Establece permisos
RUN chmod +x ${BASE_DIR}/start-daemons.sh && \
    chown -R hdadmin:hadoop ${BASE_DIR}

# EXPOSE PORTS

# ResourceManager ports
EXPOSE 8030 8031 8032 8033 8088 8090  

# Crea el usuario no privilegiado
RUN useradd -u 2000 luser

# Cambia al usuario hdadmin
USER hdadmin

# Define valores de entorno
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/
ENV HADOOP_HOME=${BASE_DIR}/hadoop/
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop/
ENV PATH=${PATH}:${HADOOP_HOME}/bin/:${HADOOP_HOME}/sbin/


WORKDIR ${HADOOP_HOME}

RUN echo "$LOG_TAG Iniciando demonios"
CMD ["/opt/bd/start-daemons.sh"]
