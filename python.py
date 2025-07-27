#!/usr/bin/python3
import os
print("installing important dependencies")
os.system("sudo apt update -y")
os.system("sudo apt install apache2")
os.system("sudo apt install unzip zip -y")
os.system("sudo apt install wget && apt install git -y")

print("adding user and creating a group then adding user to the group")
usr=input("enter name of the user:")
grp=input("enter group to create:")
os.system("sudo adduser {}".format(usr))
os.system("sudo groupadd {}".format(grp))
os.system("sudo usermod -aG {} {}".format(grp,usr))

print("printing disk space ,memory usage,cuurent user,os version,date,and cuurent dir")
print("memory usage:")
os.system("free -m")
print("disk usage:")
os.system("df -h")
print("cuurent date:")
os.system("date")
print("current working dir:")
os.system("pwd")
print("cuurent user:")
os.system("whoami")
print("os version:")
os.system("cat /etc/os-release")

print("deploying a landing page on server using python script")
is_active=os.system("systemctl status apache2")

if is_active!=0:
    os.system("apache2 is running")
else:
    print("starting the service")
    os.system("systemctl start apache2")

os.system("wget wget https://raw.githubusercontent.com/trannguyenhan/solid-landing-page/main/solid.zip -O solid.zip")

os.system("unzip solid.zip")
os.system("sudo cp -r solid/* /var/www/html/")
os.system("systemctl restart apache2")

print("end of python script")
