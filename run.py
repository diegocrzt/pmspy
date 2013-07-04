#!/usr/bin/python

import config
config.DEV = True
from pms import app
app.run("0.0.0.0",debug=True)
