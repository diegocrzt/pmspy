#!/bin/bash

set -e

DATABASE=$1

SOURCE=$2

if [ -z $DATABASE ] ; then
	DATABASE="pms"
	echo "uso: $(basename $0) database source.sql" >&2
	exit -1
fi

if [ -z $SOURCE ] ; then
	SOURCE="$DATABASE.dump.sql"
	echo "uso: $(basename $0) database source.sql" >&2
	exit -1
fi

echo "Restoring $SOURCE in $DATABASE"

sudo service postgresql restart

sudo -u postgres dropdb $DATABASE

sudo -u postgres createdb $DATABASE

sudo -u postgres psql $DATABASE < $SOURCE


