#!/bin/bash

set -e 

TMP=/tmp/
DEPLOYDIR=/var/www/pmspy/
SRC=pmspy
PMS=pms
TAG=$1

# Control de parámetros de entrada
if [ -z $1 ]
then
        echo "Debe especificar un tag"
        exit 1
fi

# Directorio Temporal, almacena el proyecto listo para copiarse al directorio
# del Servidor Web
if [ -d $TMP$PMS ]
then
        echo "$TMP$PMS borrando anterior..."
        rm -rf $TMP$PMS
fi
# Directorio temporal fuente para hacer el checkout, contiene todos los ficheros
# contiene todos los ficheros del proyecto
if [ -d $TMP$SRC ]
then
        echo "$TMP$SRC borrando anterior..."
        rm -rf $TMP$SRC
fi

# Se copia el contenido local de desarrollo al directorio temporal fuente
cp -R ../$SRC $TMP
CWD=$(pwd)
cd $TMP$SRC
# CHECKOUT DEL TAG ELEGIDO
echo "Checkout del TAG: $TAG"
git stash
git checkout $TAG -q

# Se copia del temporal fuente al temporal para limpieza
cp -R $PMS $TMP
#CWD=$(pwd)
cd $TMP$PMS

# Limpieza (se eliminan ficheros no necesarios en el servidor web
echo "borrando archivos innecesarios..."
for FILE in  doc gendoc.sh test
do
        if [ -e $FILE ]
        then
                rm -rf $FILE
        fi
done
find . -name "*.pyc" -delete
cd $CWD

# Copiado los ficheros se detiene el servidor web para eliminar cualquier versión
# anterior del proyecto
echo "parando apache2"
sudo service apache2 stop
if [ -d $DEPLOYDIR$PMS ]
then
        echo "$DEPLOYDIR$PMS borrando anterior..."
        sudo rm -rf $DEPLOYDIR$PMS
fi

# Se copia el fichero de configuración, se despliega el proyecto y se reinicia el servidor
# web, al final del proceso la aplicación ya está lista y en ejecución
echo "copiando config.py"
sed "s/= True/= False/" config.py > ${TMP}config.py
sudo cp ${TMP}config.py $DEPLOYDIR
rm ${TMP}config.py


echo "desplegando el sistema"
sudo cp -r $TMP$PMS $DEPLOYDIR

echo "iniciando apache2"
sudo service apache2 start

