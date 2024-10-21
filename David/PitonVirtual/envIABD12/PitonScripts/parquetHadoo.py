from hdfs import InsecureClient

hdfs_url = 'http://localhost:9870'
hdfs_user = 'hdadmin'
client = InsecureClient(hdfs_url, user=hdfs_user)

archivo_local = '..\\..\\..\\..\\David2\\2019-Nov.csv'
ruta_destino_hdfs = '/user/hdadmin/2019-Nov.csv'
# Cargar el archivo desde el equipo local a HDFS
try:
    with open(archivo_local, 'rb') as file:
        client.write(ruta_destino_hdfs, file)
        print(f"Archivo {archivo_local} cargado a HDFS en {ruta_destino_hdfs}")
except Exception as e:
    print(f"Error al cargar el archivo a HDFS: {e}")