#!/bin/bash

DATABASE=$1
SOURCE=$2
COMENTARIO=$3

if [ -z $DATABASE ]
then
	DATABASE="pmstest" 
fi

if [ -z $SOURCE ]
then
	SOURCE="pms.database.sql"
fi

if [ -z $COMENTARIO ]
then
	COMENTARIO="Test Environment Database for The Project Manager System"	
fi

echo "Ejecutando $SOURCE en $DATABASE ($COMENTARIO)"

sudo service postgresql restart
sudo -u postgres dropdb $DATABASE
sudo -u postgres createdb $DATABASE "$COMENTARIO"
sudo -u postgres psql -d $DATABASE -f $SOURCE

