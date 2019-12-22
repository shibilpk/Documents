#sublime text

    1. wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -
    2. echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list
    3. sudo apt update
    4. sudo apt-get install sublime-text

#atom editor
    1. Ubuntu
        a. sudo add-apt-repository ppa:webupd8team/atom
        b. sudo apt-get update
        c. sudo apt-get install atom
    2. Linux
        a. wget https://atom.io/download/deb -O atom.deb 
        b. sudo dpkg -i atom.deb	
	

#install gdebi
    • sudo apt install gdebi -y

#install git
    • sudo apt install git -y

#install gimp
    • sudo apt install gimp -y


Use administrator 
    1. sudo su

LAMP server	
    1. apt update
    2. apt-get install tasksel
    3. tasksel
    4. Press down arrow to LAMP Server and press SPACE to select the option
    5. Pres TAB and pres SPACE to select OK 
    6. sudo chmod -R 777 /etc/apache2/
    7. gedit /etc/apache2/sites-available/000-default.conf
    8. Change root directory to /var/www/
    9. service apache2 restart
    10. mkdir -p /var/www/talrop/
    11. chown -R talrop:talrop /var/www/talrop

PhpMyadmin
    1. apt update
    2. apt install phpmyadmin php-mbstring php-gettext
    3. Set password as phpmyadmin
    4. Warning: When the prompt appears, “apache2” is highlighted, but not selected. If you do not hit SPACE to select Apache, the installer will not move the necessary files during installation. Hit SPACE, TAB, and then ENTER to select Apache.
    5. phpenmod mbstring
    6. systemctl restart apache2
    7. mysql
    8. ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'phpmyadmin';
    9. FLUSH PRIVILEGES;
    10. To access localhost/phpmyadmin on browser
        a. Username : root
        b. Password : phpmyadmin
	

https://tecadmin.net/install-phpmyadmin-in-ubuntu/


{{{   Additional  needs comments needed to configuration LAMP
  
#sudo ln -s /etc/phpmyadmin/apache.conf /etc/apache2/conf-available/phpmyadmin.conf 
#systemctl restart apache2
#service apache2 reload
#sudo a2enconf phpmyadmin

Without using apt direct install
    •  cd /usr/share
    • wget https://files.phpmyadmin.net/phpMyAdmin/4.8.5/phpMyAdmin-4.8.5-all-languages.zip
    • unzip phpMyAdmin-4.8.5-all-languages.zip 
    • mv hpMyAdmin-4.8.5-all-languages phpmyadmin

### Debian based system and kali 
    • chown -R www-data:www-data /usr/share/phpmyadmin
    • chmod -R 755 /usr/share/phpmyadmin

### Redhat based system 
    • chown -R apache:apache /usr/share/phpmyadmin
    • chmod -R 755 /usr/share/phpmyadmin


Locating 

    • # sudo ln -s /usr/share/phpmyadmin/ /var/www/phpmyadmin
	
MYSQL
     
 # mysql -h localhost -u root
 # use mysql
	UPADATE mysql.user SET PASSWORD('root’) WHERE user = 'root';
		Or 
SET PASSWORD FOR root@localhost = PASSWORD('phpmyadmin');
flush privileges;
	exit

}}}


Apache rewrite module

    • sudo a2enmod rewrite
    • sudo systemctl restart apache2
    • sudo subl /etc/apache2/sites-available/000-default.conf
    • Paste following code just above </Virtualhost>
    • <Directory /var/www>
    	Options Indexes FollowSymLinks MultiViews
	AllowOverride All
	Require all granted
</Directory>
    • sudo systemctl restart apache2






Python virtualenv setup, phppgadmin
    1. apt install python python-dev libpq-dev python-setuptools
    2. apt install postgresql postgresql-contrib phppgadmin
    3. apt install python-pip
    4. pip install virtualenv virtualenvwrapper








	


