#!/bin/bash

HADOOP_HOME=/opt/bd/hadoop/

SERVICE1=${HADOOP_HOME}/bin/hdfs
DAEMON1=datanode

SERVICE2=${HADOOP_HOME}/bin/yarn
DAEMON2=nodemanager

# Iniciamos el demonio del DataNode y chequeamos si ha arrancado
${SERVICE1} --daemon start ${DAEMON1}
status=$?
if [ $status -ne 0 ]; then
  echo "No pudo inicializar el servicio ${DAEMON1}: $status"
  exit $status
fi

# Iniciamos el demonio del NodeManager y chequeamos si ha arrancado
${SERVICE2} --daemon start ${DAEMON2}
status=$?
if [ $status -ne 0 ]; then
  echo "No pudo inicializar el servicio ${DAEMON2}: $status"
  exit $status
fi

# Mientras ambos demonio estén vivos, el contenedor sigue activo
while true
do 
  sleep 10
  if ! ps aux | grep ${DAEMON1} | grep -q -v grep
  then
      echo "El demonio ${DAEMON1}  ha fallado"
      exit 1
  fi
  if ! ps aux | grep ${DAEMON2} | grep -q -v grep
  then
      echo "El demonio ${DAEMON2}  ha fallado"
      exit 1
  fi
done
