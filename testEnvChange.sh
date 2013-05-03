#!/bin/bash

set -e 

TMP=/tmp/
DEPLOYDIR=/var/www/pmspy/
PMS=pms


if [ -d $TMP$PMS ]
then
	echo "$TMP$PMS borrando anterior..."
	rm -rf $TMP$PMS
fi

cp -r $PMS $TMP
CWD=$(pwd)
cd $TMP$PMS
echo "borrando archivos innecesarios..."
rm -rf doc gendoc.sh droptables.sql test
find . -name "*.pyc" -delete
cd $CWD

echo "parando apache2"
sudo service apache2 stop
if [ -d $DEPLOYDIR$PMS ]
then
	echo "$DEPLOYDIR$PMS borrando anterior..."
	sudo rm -rf $DEPLOYDIR$PMS
fi

echo "desplegando el sistema"
sudo cp -r $PMS $DEPLOYDIR

echo "iniciando apache2"
sudo service apache2 start
