import app

try:
	app.SRAPS_APP_STUDENT().run()
except ModuleNotFoundError:
	pass
