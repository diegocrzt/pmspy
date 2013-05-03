#!/bin/bash

if [ -d /var/www/pmspy/pms ]
then
	sudo rm -rf /var/www/pmspy/pms
fi

sudo cp -r pms /var/www/pmspy
