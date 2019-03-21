from github_webhook import Webhook
from flask import Flask
from github import Github
from io import BytesIO

from credentials import *

import requests, os, ftplib, hashlib, glob

ftp_files_list = []
ftp_empty_dir_list = []

def isdir(ftp, name):
   try:
      ftp.cwd(name)
      ftp.cwd('..')
      return True
   except:
      return False

def list_ftp_files(ftp):
    dirs = ftp.nlst()
    for file in dirs:
        file_name = ftp.pwd() + '/' + file
        if not isdir(ftp, file_name):
            ftp_files_list.append(file_name[1:])

    for item in (path for path in dirs if path not in ('.', '..')):
        try:
            ftp.cwd(item)
            list_ftp_files(ftp)
            ftp.cwd('..')
        except:
            pass

def list_ftp_empty_dir(ftp):
    dirs = ftp.nlst()

    if len(dirs) == 0:
        ftp_empty_dir_list.append(ftp.pwd()[1:])

    for item in (path for path in dirs if path not in ('.', '..')):
        try:
            ftp.cwd(item)
            list_ftp_empty_dir(ftp)
            ftp.cwd('..')
        except:
            pass

app = Flask(__name__)
webhook = Webhook(app)

@webhook.hook()
def on_push(data):
    global ftp_files_list, ftp_empty_dir_list

    print("Update pushed, let's update the FTP!")

    github_api = Github(github_secret)
    github_repo = github_api.get_repo("WerWolv/EdiZon_ConfigsAndScripts")
    ftp_session = ftplib.FTP('werwolv.net', ftp_username, ftp_password)

    EdiZon_api_folder = "/api/edizon/v2/"

    contents = github_repo.get_contents("")

    github_files_list = []

    while len(contents) > 0:
        file_content = contents.pop(0)

        if file_content.type == "dir":
            contents.extend(github_repo.get_contents(file_content.path))
        else:
            file_content_path = file_content.path
            if file_content_path.startswith("Scripts"):
                file_content_path = "EdiZon/editor/" + file_content_path.replace("Scripts", "scripts")
            elif file_content_path.startswith("Configs"):
                file_content_path = "EdiZon/" + file_content_path.replace("Configs", "editor")
            elif file_content_path.startswith("Cheats"):
                file_content_path = "atmosphere/titles/" + file_content_path
                file_content_path = file_content_path.replace("titles/Cheats", "titles")

            file_dir = os.path.dirname(file_content_path)

            if len(file_dir) > 0 and not file_dir.startswith("Tools"):
                try:			
                    path = (EdiZon_api_folder + file_dir + '/')
                    i = 1
                    while i != -1:
                        i = path.find("/", i + 1)
                        try:
                            ftp_session.mkd(path[0:i + 1])
                        except:
                            pass
                except: 
                    pass

                file_buffer = BytesIO(requests.get(file_content.download_url).content)
                file_path   = EdiZon_api_folder + file_content_path
                file_size   = 0

                try:
                    file_size = ftp_session.size(file_path)
                except:
                    pass

                if file_size == 0:
                    path = (EdiZon_api_folder + file_dir + '/')
                    i = 1
                    while i != -1:
                        i = path.find("/", i + 1)
                        try:
                            ftp_session.mkd(path[0:i + 1])
                        except:
                            pass

                    ftp_session.storbinary("STOR " + file_path, file_buffer)
                    print(file_path + " created!")
                else:
                    print(file_path + " already exist!")

                    file_sha1 = hashlib.sha1(file_buffer.read()).hexdigest()

                    sha1 = hashlib.sha1()
                    ftp_session.retrbinary("RETR " + file_path, sha1.update)

                    if file_sha1 != sha1.hexdigest():
                        ftp_session.storbinary("STOR " + file_path, file_buffer)
                        print(file_path + " updated!")
                    else:
                        print(file_path + " is already up-to-date!")

                github_files_list.append(file_path) 

    print("Cleaning unneeded files/folders!")

    list_ftp_files(ftp_session)

    for file in ftp_files_list:
        if not file in github_files_list:
            ftp_session.delete(file)
            print(file + " don't exist anymore, deleted!")

    list_ftp_empty_dir(ftp_session)

    for dir in ftp_empty_dir_list:
        ftp_session.rmd(dir)
        print(dir + " is empty, deleted!")

    ftp_files_list = []
    ftp_empty_dir_list = []
    ftp_session.quit()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=12345)