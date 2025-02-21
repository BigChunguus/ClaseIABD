from pyspark.sql import SparkSession

# Iniciar sesión de Spark
spark = SparkSession.builder \
    .appName("ETL Pipeline") \
    .getOrCreate()

# Leer datos
input_path = "/data/input/Ventas.csv"  # Ruta relativa a tu volumen montado
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Transformaciones
df_transformed = df.withColumn("ingreso_total", df["cantidad"] * df["precio_unitario"])

# Guardar resultados
output_path = "/data/output/ventas_transformadas"  # Ruta de salida en el volumen montado
df_transformed.write.csv(output_path, header=True)

# Detener sesión de Spark
spark.stop()
