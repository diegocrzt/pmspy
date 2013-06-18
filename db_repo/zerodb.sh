#!/bin/bash
# Drop and Create again a Database

DATABASE=$1

set -e

if [ -z $DATABASE ]
then
	echo "uso: $(basename $0) nombre_db" >&2
	exit -1
fi

sudo service postgresql restart

sudo -u postgres dropdb $DATABASE

sudo -u postgres createdb $DATABASE

