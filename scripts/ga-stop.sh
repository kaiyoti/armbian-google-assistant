#!/bin/bash


result=`ps aux | grep googl[e]samples | awk {'print $2'}`
if [ -n "$result" ]; then
        echo "Found Google Assistant service with pid of $result"
        kill -9 $result
else
        echo "No Google Assistance service found"
fi

script=`ps aux | grep ga-star[t] | awk {'print $2'}`
if [ -n "$script" ]; then
        echo "Found ga-start script with pid of $script"
        kill -9 $script
else
        echo "No ga-start script found"
fi

exit 0

