#!/bin/bash
$(sudo echo -e '[code]
name=Visual Studio Code 
baseurl=https://packages.microsoft.com/yumrepos/vscode 
enabled=1 
gpgcheck=1 
gpgkey=https://packages.microsoft.com/keys/microsoft.asc' > /etc/yum.repos.d/vscode.repo)
$(sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc)
$(sudo yum install code)
