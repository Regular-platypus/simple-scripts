#!/bin/bash
while true
do
    # Get current time
    current_time=$(date +"%H:%M")

    if [[ "$current_time" > "22:59" && "$current_time" < "23:59" ]]
    then
        ping -c 1 192.168.29.100 >/dev/null 2>&1

        if [ "$?" -eq 0 ]
        then
            ssh user@192.168.29.100 "sudo shutdown now"
        fi
    fi

    sleep 6000
done
