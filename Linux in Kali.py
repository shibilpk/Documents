Kali linus make solve unable to locate

    # sudo nano /etc/apt/sources.list

Repalce the code the following

deb http://http.kali.org/kali kali-rolling main contrib non-free
    # For source package access, uncomment the following line
    # deb-src http://http.kali.org/kali kali-rolling main contrib non-free
deb http://http.kali.org/kali sana main non-free contrib
deb http://security.kali.org/kali-security sana/updates main contrib non-free
    # For source package access, uncomment the following line
    # deb-src http://http.kali.org/kali sana main non-free contrib
    # deb-src http://security.kali.org/kali-security sana/updates main contrib non-free
deb http://old.kali.org/kali moto main non-free contrib
    # For source package access, uncomment the following line
    # deb-src http://old.kali.org/kali moto main non-free contrib


Press ctrl + O then press ctrl + x

    # sudo apt-get update



https://ourcodeworld.com/articles/read/961/how-to-solve-kali-linux-apt-get-install-e-unable-to-locate-package-checkinstall




1.Bluetooth problems fix 1

1. edit /etc/bluetooth/main.conf ---> and add
    subl /etc/bluetooth/main.conf
Code:

DisablePlugins=pnat
2. in a terminal use the following commands:
Code:

    touch /etc/bluetooth/link_key
    chmod 644 /etc/bluetooth/link_key
    /etc/init.d/bluetooth restart


2 .Bluetooth problems fix 2

    sudo lsmod | grep blue
    systemctl enable bluetooth.service
    systemctl start bluetooth.service
