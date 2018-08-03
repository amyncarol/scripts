#!/bin/bash

#if pidof -x rclone > /dev/null ###if clause not working.....
#then
#    echo "rclone already running"
#    exit 1
#fi
rclone sync /global/scratch/yaocai box:savio_backup -v --log-file=/global/home/users/yaocai/rclone-upload.log
exit
