#!/bin/bash

set -e

DATABASE=$1
DESTINATION=$2

if [ -z $DATABASE ]
then
	DATABASE="pms"
fi

if [ -z $DESTINATION ]
then
	DESTINATION="$DATABASE.dump.sql"
fi

echo "Dump $DATABASE in $DESTINATION"

sudo -u postgres pg_dump $DATABASE -O > $DESTINATION
