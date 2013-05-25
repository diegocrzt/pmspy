import config
config.DEV = True
from pms import app
app.run(host="0.0.0.0", debug=True)