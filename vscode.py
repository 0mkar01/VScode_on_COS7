#! /usr/bin/python3
import os


CMD1 = 'sudo echo -e "[code] \nname=Visual Studio Code\nbaseurl=https://packages.microsoft.com/yumrepos/vscode\nenabled=1\ngpgcheck=1\ngpgkey=https://packages.microsoft.com/keys/microsoft.asc " > /etc/yum.repos.d/vscode.repo'

CMD = 'sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc'

CMD2 = 'sudo yum install code'

os.system(CMD)
os.system(CMD1)
os.system(CMD2)

