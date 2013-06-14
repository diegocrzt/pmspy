#!/bin/bash

set -e

DATABASE=$1

SOURCE=$2

if [ -z $DATABASE ] ; then
	DATABASE="pms"
fi

if [ -z $SOURCE ] ; then
	SOURCE="$DATABASE.dump.sql"
fi

echo "Restoring $SOURCE in $DATABASE"

sudo service postgresql restart

sudo -u postgres dropdb $DATABASE

sudo -u postgres createdb $DATABASE

echo "here"
sudo -u postgres psql $DATABASE < $SOURCE


