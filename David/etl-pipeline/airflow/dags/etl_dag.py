from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
import subprocess

def spark_etl():
    # Usamos docker exec para ejecutar el script en el contenedor spark
    container_name = "etl-pipeline-spark-1"  # Nombre del contenedor de Spark
    script_path = "/scripts/spark_etl.py"  # Ruta donde está el script dentro del contenedor (ajustado a la ruta del volumen)

    # Comando docker exec para invocar el script en el contenedor spark
    command = f"docker exec {container_name} /opt/spark/bin/spark-submit {script_path}"

    print(f"🔍 Ejecutando el comando: {command}")
    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            shell=True  # Especificamos shell=True porque estamos ejecutando un comando de bash
        )
        print("✅ Spark ETL completado correctamente.")
        print(result.stdout)  # Muestra la salida estándar de spark-submit
    except subprocess.CalledProcessError as e:
        print("❌ ERROR en Spark ETL:")
        print(e.stderr)  # Muestra el error si ocurre
        raise

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 2, 17),
    'retries': 1,
}

with DAG(
    'etl_pipeline',
    default_args=default_args,
    schedule_interval='@daily',  # Puedes cambiar la programación si es necesario
) as dag:

    # Tarea de extracción (simulada con un bash echo)
    extract = BashOperator(
        task_id='extract',
        bash_command='echo "🔍 Iniciando extracción de datos..." && sleep 2 && echo "✅ Extracción completada."',
    )

    # Tarea de transformación, ejecuta el script Spark ETL
    transform = PythonOperator(
        task_id='transform',
        python_callable=spark_etl,
    )

    # Tarea de carga (simulada con un bash echo)
    load = BashOperator(
        task_id='load',
        bash_command='echo "🔍 Iniciando carga en PostgreSQL..." && sleep 2 && echo "✅ Carga completada."',
    )

    # Definimos el orden de las tareas en la DAG
    extract >> transform >> load
