
#!/bin/bash

set -e 

TMP=/tmp/
DEPLOYDIR=/var/www/pmspy/
PMS=pms
TAG=$1

if [ -z $1 ]
then
        echo "Debe especificar un tag"
        exit 1
fi


if [ -d $TMP$PMS ]
then
        echo "$TMP$PMS borrando anterior..."
        rm -rf $TMP$PMS
fi
if [ -d $TMP$SRC ]
then
        echo "$TMP$SRC borrando anterior..."
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
sed "s/= True/= False/" config.py > ${TMP}config.py
sudo cp ${TMP}config.py $DEPLOYDIR
rm ${TMP}config.py

echo "desplegando el sistema"
sudo cp -r $TMP$PMS $DEPLOYDIR

echo "iniciando apache2"
sudo service apache2 start
