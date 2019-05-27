from github_webhook import Webhook
from flask import Flask
from github import Github
from io import BytesIO
import os
import threading
import time
import shutil
import zipfile

import requests, os, ftplib, hashlib, glob

from fix_readme import fixReadme

app = Flask(__name__)
webhook = Webhook(app)

update = False

@webhook.hook()
def on_push(data):
	global update
	print("SeeS")
	update = True

def zipdir(path, ziph):
    # ziph is zipfile handle
    exclude = set(["info", "GitHub", "upload.php", "versionlist.php", "build.zip"])
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in exclude]
        files[:] = [f for f in files if f not in exclude]
        for file in files:
            ziph.write(os.path.join(root, file), os.path.join(root, file)[3:])
            print(os.path.join(root, file))
	
def updateLoop():
	global update
	
	while True:
		while update:
			update = False
			print("Pulling changes")
			os.system("git pull")
			
			print("Deleting Folders")
			shutil.rmtree("../switch/EdiZon")
			shutil.rmtree("../atmosphere")
			
			print("Copying save editor scripts")
			shutil.copytree("Configs", "../switch/EdiZon/editor")
			shutil.copytree("Scripts", "../switch/EdiZon/editor/scripts")
			
			print("Copying cheats")
			shutil.copytree("Cheats", "../atmosphere/titles")
			
			print("Zipping release")
		
			if os.path.exists("./../build.zip"):
				os.remove("./../build.zip")
			zipf = zipfile.ZipFile('./../build.zip', 'w', zipfile.ZIP_DEFLATED)
			zipdir('./..', zipf)
			zipf.close()
			
			print("Fixing cheats readme")
			fixReadme()
			
			os.system("git add *")
			os.system("git commit -m \"Added new cheats to readme.\"")
			os.system("git push")
			
			print("Done!")
		time.sleep(1)

if __name__ == "__main__":
	threading.Thread(target=updateLoop).start()
	app.run(host="0.0.0.0", port=12345)
