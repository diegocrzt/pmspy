#!/usr/bin/python

import config
config.DEV = True
from pms import app
app.run(debug=True)
