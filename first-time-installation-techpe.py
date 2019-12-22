﻿# - Commenting

sudo su # Enter Computer Password


#sublime text

    wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -

    echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list

    sudo apt update
    sudo apt-get install sublime-text


#install gdebi

    sudo apt install gdebi -y


#install git

    sudo apt install git -y




#install gimp

    sudo apt install gimp -y

    sudo apt-get install tasksel -y

#Tasksel

#select lamp server

    • install lamp


    gedit /etc/apache2/sites-available/000-default.conf #change root directory to /var/www/
    sudo service apache2 restart sudo mkdir -p /var/www/techpe/ chown -R talrop:talrop /var/www/techpe

#phpMyadmin
    sudo apt-get update
    sudo apt-get install phpmyadmin -y

    sudo apt-get update

    sudo apt-get install postgresql postgresql-contrib phppgadmin

    sudo su

    apt install python python-dev libpq-dev python-setuptools -y
    apt install postgresql postgresql-contrib phppgadmin -y
    sudo apt install python-pip -y
    pip install virtualenv virtualenvwrapper


#Python 3 install

    sudo apt-get update

    sudo apt-get install python3-distutils -y

    sudo apt-get install python3.6

#Venv change

    virtualenv venv -p python3

    pip install django

#Changes in project

    main/“on_delete=models.CASCADE” added in models.py users/“on_delete=models.CASCADE” added in models.py

    Reverse changed:- from django.urls import reverse

#install(uninstall before installing)

    pip install django-registration-redux

#main_app urls

    url(r'^app/users/', include(('users.urls', 'users'), namespace="users")),





For getting emmet in sublime text 3 Preferences->package-settings->package-control->settings-user #insert the following json key value "channels": [

    "https://packagecontrol.io/channel_v3.json",

    "https://erhan.in/channel_v3.json"

    ]



#react-native

    install npm LTS


# Install react-native

    sudo apt install npm

    sudo npm install -g react-native-cli

    React Native requires a recent version of the Java SE Development Kit (JDK)

    sudo add-apt-repository ppa:linuxuprising/java

    sudo apt-get update

    sudo apt install oracle-java11-installer sudo apt install oracle-java11-set-default




    apt install default-jre
    apt install openjdk-11-jre-headless
    apt install openjdk-8-jre-headless



#Install Android Studio

    sudo add-apt-repository ppa:maarten-fonville/android-studio sudo apt install android-studio

    sudo apt update


#error permission denied for /dev/kvm

    sudo ​apt install qemu-kvm
    sudo adduser​ talrop kvm
    sudo chown​ talrop /dev/kvm



# Configure the ANDROID_HOME environment variable

        a) Add the following lines to your ​$HOME/.bash_profile​config file:


export ​ANDROID_HOME​=​$HOME​/Android/sdk export ​PATH​=​$PATH​:$ANDROID_HOME/emulator export ​PATH​=​$PATH​:$ANDROID_HOME/tools export ​PATH​=​$PATH​:$ANDROID_HOME/tools/bin export ​PATH​=​$PATH​:$ANDROID_HOME/platform-tools

        b) source $HOME/.bash_profile

        c) echo $PATH




    4. Create React Native application


​react-​native​ init ProjectName /* project name should be Camel Case */

    cd ProjectName

    react-native run​-​android

Exit error

    echo fs.inotify.max_user_watches=524288 | sudo tee -a /etc/sysctl.conf && sudo sysctl -p
