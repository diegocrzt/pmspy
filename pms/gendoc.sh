#!/bin/bash

find . -name "*.pyc" -delete
if [ -x /usr/bin/epydoc ]
then
	#epydoc * -o doc
	epydoc *.py modelo/* test/*  vista/* --introspect-only --no-sourcecode -o doc/
fi

