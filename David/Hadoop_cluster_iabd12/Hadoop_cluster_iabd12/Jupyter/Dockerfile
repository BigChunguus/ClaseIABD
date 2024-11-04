# Dockerfile para Jupyter Notebook con acceso a HDFS a través del NameNode
FROM hadoop-base-image-iabd12:latest

USER root

# Define el log tag y directorios base
ENV LOG_TAG="[Jupyter Notebook]:"
ENV BASE_DIR=/opt/bd
ENV VENV_DIR=${BASE_DIR}/venv

# Instala Python, pip y crea un entorno virtual
RUN echo "$LOG_TAG Instalando Python, pip y Jupyter" && \
    apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-venv python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Crea un entorno virtual e instala Jupyter
RUN python3 -m venv ${VENV_DIR}
RUN ${VENV_DIR}/bin/pip install --upgrade pip && \
    ${VENV_DIR}/bin/pip install jupyter

# Configura las variables de entorno para Java y Hadoop
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV HADOOP_HOME=/opt/bd/hadoop
ENV HADOOP_CONF_DIR=${HADOOP_HOME}/etc/hadoop
ENV PATH=${PATH}:${HADOOP_HOME}/bin:${HADOOP_HOME}/sbin:${VENV_DIR}/bin

# Copia los archivos de configuración de Hadoop del NameNode
COPY --from=hadoop-namenode-image-iabd12 ${HADOOP_CONF_DIR} ${HADOOP_CONF_DIR}

# Cambia al usuario hdadmin
USER hdadmin

# Exponer el puerto 8888 para Jupyter Notebook
EXPOSE 8888

# Comando para iniciar Jupyter Notebook
CMD ["bash", "-c", "${VENV_DIR}/bin/jupyter-notebook --ip=0.0.0.0 --port=8888 --no-browser --allow-root"]
