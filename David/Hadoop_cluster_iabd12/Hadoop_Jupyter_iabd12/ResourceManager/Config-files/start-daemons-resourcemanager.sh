#!/bin/bash

HADOOP_HOME=/opt/bd/hadoop/
SERVICE=${HADOOP_HOME}/bin/yarn
DAEMON=resourcemanager

# Iniciamos el demonio del resourcemanager y chequeamos si ha arrancado
${SERVICE} --daemon start ${DAEMON}
status=$?
if [ $status -ne 0 ]; then
  echo "No pudo inicializar el servicio ${DAEMON}: $status"
  exit $status
fi

# Mientras el demonio esté vivo, el contenedor sigue activo
while true
do 
  sleep 10
  if ! ps aux | grep ${DAEMON} | grep -q -v grep
  then
      echo "El demonio ${DAEMON}  ha fallado"
      exit 1
  fi
done
