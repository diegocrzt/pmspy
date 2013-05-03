
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
for FILE in  doc gendoc.sh test
do
	if [ -e $FILE ]
	then
		rm -rf $FILE
	fi
done
find . -name "*.pyc" -delete
cd $CWD

echo "parando apache2"
sudo service apache2 stop
if [ -d $DEPLOYDIR$PMS ]
then
	echo "$DEPLOYDIR$PMS borrando anterior..."
	sudo rm -rf $DEPLOYDIR$PMS
fi

echo "copiando config.py"
sudo cp $CWD/config.py $DEPLOYDIR

echo "desplegando el sistema"
sudo cp -r $TMP$PMS $DEPLOYDIR

echo "iniciando apache2"
sudo service apache2 start
