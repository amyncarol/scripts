#!/bin/bash

if pidof -x rclone > /dev/null ###if clause not working.....
then
    echo "rclone already running"
    exit 1
fi
rclone sync /work/05018/tg843171/stampede2 box:stampede2_backup -v --log-file=/home1/05018/tg843171/rclone-upload.log
exit
