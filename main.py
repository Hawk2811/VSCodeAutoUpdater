# VSCodeAutoUpdater - Script to AutoUpdate VSCode in Portable instalations on Windows 
# main.py
import os
import wget
from zipfile import ZipFile

VSCodeURL = "https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-archive"
config_file = "install.cfg"
install_dir = ""




def installpackage(install):
        if os.path.isdir(install):
             pass
        else:
             os.makedirs(install)

        package = ZipFile("Update.zip","r")
        package.extractall(path=install)
        package.close()




def main():     
    wget.download(VSCodeURL,out="Update.zip")   
    if os.path.exists(config_file):
        file = open(config_file,"r")
        install_dir = file.read()
        installpackage(install_dir)
    else:
        installpackage("C:\\vscode")


main()