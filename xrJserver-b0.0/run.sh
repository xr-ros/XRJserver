#!/bin/bash

main_dir=xrJserver-b0.0
project_path=$(cd `dirname $0`; pwd)
project_name="${project_path##*/}"

if [ $project_name != $main_dir ]
then
  cd /opt/xrapp/xrJserver-b0.0/
fi

nohup python3 main.py $* 2>&1 &
