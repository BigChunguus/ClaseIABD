# Usa la imagen oficial de Spark de Bitnami (puedes elegir otra imagen si lo prefieres)
FROM bitnami/spark:3.3

# Cambiar al usuario root para tener permisos
USER root

# Copiar el script Spark ETL dentro del contenedor
COPY /spark/scripts/spark_etl.py /scripts/spark_etl.py

# Darle permisos de ejecución al script
RUN chmod +x /scripts/spark_etl.py

# Asegúrate de que Spark esté configurado correctamente (agrega más configuraciones si es necesario)
# El contenedor se ejecutará con el usuario root por defecto (o el que elijas) y con los permisos adecuados.
