#!/bin/bash

find . -name "*.pyc" -delete
if [ -x /usr/bin/epydoc ]
then
	epydoc * -o doc
fi

