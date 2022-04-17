import os
class settings_conf():
	def logs():
		import settings_conf
		return settings_conf.logs
	def update():
		import settings_conf
		return settings_conf.update
	def accent():
		import settings_conf
		return settings_conf.accent
	def primary():
		import settings_conf
		return settings_conf.primary
logs = settings_conf.logs()
update = settings_conf.update()
accent = settings_conf.accent()
primary = settings_conf.primary()
getSettings =  lambda : {"logs": logs, "update": update, "accent": accent,"primary": primary}
def writeSettings (data,key):
	if "logs" == data:
		data_w = \
f"""
logs = {key}
update = {update}
accent = "{accent}"
primary = "{primary}"	"""	
	if "update" == data:
		data_w = f"""logs = {logs}	
update = {key}
accent = "{accent}"
primary = "{primary}"	"""
	if "accent" == data:
		data_w = f"""logs = {logs}	
update = {update}
accent = "{(key.split("."))[0]}"
primary = "{(key.split("."))[1]}"	"""
	if "primary" == data:
		data_w = f"""logs = {logs}	
update = {update}
accent = "{(key.split("."))[1]}"
primary = "{(key.split("."))[0]}"

"""
        # open file & write data_w
        file = open("settings_conf.py","w")
	file.write(data_w)
