# Para ejecutar este Dockerfile, posicionate en consola en el directorio donde tengas este arvhivo y lanza
# este comando: docker build -t hadoop-base-image .
# Me conecto al Hub de Docker para bajarme una imagen de Ubuntu Server, sencilla y la última versión.
FROM ubuntu:latest 

###############################################################################################################
# Con la imagen ya bajada voy a indicar una serie de cambios/configuraciones sobre esta imagen se ubuntu server
###############################################################################################################
# Cambio a usuario root, es decir, que todos los cambios que realizaré en esta imagen será como usuario root
USER root

# Defino una variables de entorno:
##################################
# HADOOP_VERSION = 3.3.6                                La versión de Hadoop a instalar.
# BASE_DIR = /opt/bd                                    EL directorio donde se va a instalr Haddop.
# LOG_TAG = "[BASE Hadoop_${HADOOP_VERSION}]:"          La etiqueta para los log del sistema.
# REPOSITORY = https://dlcdn.apache.org/hadoop/common   El repositorio donde se bajará Haddop.
#
ENV HADOOP_VERSION 3.3.6
ENV BASE_DIR /opt/bd
ENV LOG_TAG "[BASE Hadoop_${HADOOP_VERSION}]:"
ENV REPOSITORY https://dlcdn.apache.org/hadoop/common


# PASO 1: Actualiza el S.O, instalo Java, python3, curl, iputils y limpio y borro.
RUN echo "$LOG_TAG Actualizando e instalando paquetes básicos" && \
    apt-get update && \
    apt-get install -y --no-install-recommends openjdk-8-jre python3 curl locales iputils-ping nano && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists

# Genera locales, para que trabajemos con teclado español
RUN echo "$LOG_TAG Creando locales" && \
    locale-gen es_ES.UTF-8 && update-locale LANG=es_ES.UTF-8

# Crea un directorio para la instalación en /opt/bd: 
RUN mkdir -p ${BASE_DIR}
    
# Cambio a directorio /opt/bd 
WORKDIR ${BASE_DIR}

# Descarga la última versión 3.3.6 Hadoop en /opt/bd: REalizo un enlace símbolico
RUN echo "$LOG_TAG Descargando Hadoop" && \
    curl -fLO "${REPOSITORY}/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz"  && \
    tar xzvf hadoop-${HADOOP_VERSION}.tar.gz && \
    ln -s hadoop-${HADOOP_VERSION} hadoop && \
    rm hadoop-${HADOOP_VERSION}.tar.gz


# Crea un grupo hadoop y un usuario hdadmin para ejecutar los diferentes demonios de Hadoop (HDFS y YARN).
# Cambia el propietario del directorio de hadoop 
RUN groupadd -r hadoop && \
    #useradd -r -u 1001 -g hadoop -d ${BASE_DIR} -s /bin/bash hue && \
    useradd -r -g hadoop -d ${BASE_DIR} -s /bin/bash hdadmin
    
# Crea directorio para los ficheros de log
#RUN mkdir ${HADOOP_HOME}/logs

# Establece permisos de la carpeta de instalación de haddop para que sea dueño el nuevo usuario 
# hdamin con el grupo hadoop. Para así poder ejecutar todos los demonios con este usuario y no con el root 
RUN chown -R hdadmin:hadoop ${BASE_DIR}
#RUN chmod -R 770 ${BASE_DIR}
