#!/bin/bash

echo "installing dependencies apache2 unzip zip wget git "
sudo apt update -y
depend1=" apt install apache2 -y"
depend2=" apt install unzip zip -y"
depend3=" apt install git -y"

$depend1
$depend2
$depend3

echo "creating a user and creating a group and adding user to the group"

read -p "username: " usr
echo "username you typed:$usr"
read -p "group name: " grp
echo "group name you typed:$grp"

sudo adduser $usr
sudo groupadd $grp
sudo usermod -aG $grp $usr

echo "showing disk space and memory usage"

memory="free -m"
disk="df -h"
date="date"
currentdir="pwd"
user="whoami"
os="cat /etc/os-release"

echo "memory is:"
$memory
echo "disk space is:"
$disk
echo "current date is:"
$date
echo "user is:"
$user
echo "os version:"
$os

echo "deploying a landing page template to server "
systemctl status apache2
if [ $? -eq 0 ]
then
    echo "apache2 is running successfully"
else
    echo "not running, starting and enabling it"
    systemctl start apache2
fi

echo "getting landing page"
wget https://raw.githubusercontent.com/trannguyenhan/solid-landing-page/main/solid.zip -O solid.zip

echo "unzipping landing page"
unzip solid.zip

echo "copying landing page to /var/www/html"
sudo cp -r solid/* /var/www/html/
systemctl restart apache2
