
__version__ = "2.02"

import app

try:
	app.SRAPS_APP_STUDENT().run()
except ModuleNotFoundError:
	pass
