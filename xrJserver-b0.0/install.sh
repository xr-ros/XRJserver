#!/bin/bash

sname=xrJserver
version=b0.0
user=$(whoami)


cd  ..

if [ ! -d /opt/xrapp  ]
then 
	sudo mkdir /opt/xrapp
fi
	
sudo cp -r $sname-$version /opt/xrapp/

cd /opt/xrapp/$sname-$version/
sudo ln -s run.sh xrjserver
sudo cp xrjserver /usr/bin/
#sudo cp xrJserver.service /lib/systemd/system/

sudo chmod 666 /opt/xrapp/xrJserver-b0.0/pid/main.pid
sudo chmod 777 /opt/xrapp/xrJserver-b0.0/xrJserver/data
sudo chmod 777 /opt/xrapp/xrJserver-b0.0/log
sudo setfacl -m d:u:$user:rw /opt/xrapp/xrJserver-b0.0/xrJserver/data
sudo setfacl -m d:u:$user:rw /opt/xrapp/xrJserver-b0.0/log
sudo chmod 777 /opt/xrapp/xrJserver-b0.0/xrJserver/data
sudo rm -f /opt/xrapp/xrJserver-b0.0/xrJserver/data/*
sudo rm -f /opt/xrapp/xrJserver-b0.0/log/*
