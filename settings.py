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
        def gra():
        	import settings_conf
        	return settings_conf.gra                
logs = settings_conf.logs()
update = settings_conf.update()
accent = settings_conf.accent()
primary = settings_conf.primary()
gra = settings_conf.gra()
getSettings =  lambda : {"logs": logs, "update": update, "accent": accent,"primary": primary,"gra":gra}
def writeSettings (data,key):
        if "logs" == data:
                data_w = \
f"""
logs = {key}
update = {update}
accent = "{accent}"
primary = "{primary}"  
gra = "{gra}" """     
        if "update" == data:
                data_w = f"""logs = {logs}      
update = {key}
accent = "{accent}"
primary = "{primary}"  
gra = "{gra}" """
        if "accent" == data:
                data_w = f"""logs = {logs}      
update = {update}
accent = "{(key.split("."))[0]}"
primary = "{(key.split("."))[1]}"     
gra = "{gra}"  """
        if "primary" == data:
                data_w = f"""logs = {logs}      
update = {update}
accent = "{(key.split("."))[1]}"
primary = "{(key.split("."))[0]}"
gra = "{gra}"
"""
        if "gra" == data:
        		data_w = f"""
logs = {logs}
update = {update}
accent = "{accent}"
primary = "{primary}"  
gra = "{key}" """ 		      
        # open file & write data_w
        file = open("settings_conf.py","w")
        file.write(data_w)
