FROM ubuntu:latest
LABEL mantianer="genio <acruza02@educantabria.es>"

# Cambio a usuario root, es decir, que todos los cambios que realizaré en esta imagen será como
# usuario root
USER root

# Defino unas variables de entorno:

##################################
# SPARK_VERSION=3.5.0 La versión de Apache Spark a instalar.
# BASE_DIR = /opt/bd EL directorio donde se va a instalar Spark.
# REPOSITORY = https://dlcdn.apache.org/spark El repositorio donde se bajará Spark.
#

ENV SPARK_VERSION=3.5.3
ENV BASE_DIR=/opt/bd
ENV LOG_TAG="[BASE Spark_${SPARK_VERSION}]:"
ENV REPOSITORY=https://dlcdn.apache.org/spark
ENV HADOOP_VERSION=3


# PASO 1: Actualiza el S.O, instalo Java, python3, curl, iputils y limpio y borro.

RUN echo "$LOG_TAG Actualizando e instalando paquetes básicos" && \
apt-get update && \
apt-get install -y --no-install-recommends openjdk-8-jre python3 curl locales iputils-ping && \
apt-get clean && \
rm -rf /var/lib/apt/lists

# Genera locales, para que trabajemos con teclado español

RUN echo "$LOG_TAG Creando locales" && \
locale-gen es_ES.UTF-8 && update-locale LANG=es_ES.UTF-8

# Crea un directorio para la instalación en /opt:

RUN mkdir -p ${BASE_DIR}

# Cambio a directorio /opt/bd

WORKDIR ${BASE_DIR}

# Descarga la última versión 3.5.0 Spark en /opt/bd: REalizo un enlace símbolico

RUN echo "$LOG_TAG Descargando Apache Spark" && \
curl -fLO "${REPOSITORY}/spark-${SPARK_VERSION}/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz" && \
tar xzvf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
ln -s spark-${SPARK_VERSION}-bin-hadoop$HADOOP_VERSION spark && \
rm spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz

# Crea un grupo spark y un usuario spadmin para ejecutar los diferentes demonios de Spark (master,
# worker, etc). Cambia el propietario del directorio de spark

RUN groupadd -r spark && \
useradd -r -g spark -d ${BASE_DIR} -s /bin/bash spadmin

# Crea directorio para los ficheros de log
#RUN mkdir ${HADOOP_HOME}/logs
# Establece permisos de la carpeta de instalación de spark para que sea dueño el nuevo usuario
# spadmin con el grupo spark. Para así poder ejecutar todos los demonios con este usuario y no con el
# root

RUN chown -R spadmin:spark ${BASE_DIR}

# Exponer el puerto 7077 para el master Spark y 8080 para la UI

EXPOSE 7077 8080

# Cambio a directorio /opt/bd

WORKDIR ${BASE_DIR}/spark-${SPARK_VERSION}-bin-hadoop$HADOOP_VERSION/sbin