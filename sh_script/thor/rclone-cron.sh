#!/bin/bash

if pidof -x rclone > /dev/null ###if clause not working.....
then
    echo "rclone already running"
    exit 1
fi
rclone sync /home/yaocai box:thor_home_backup -v --log-file=/home/yaocai/rclone-upload.log
exit
