#!/bin/bash
# making a change for pr again
file_name=$1    
wait_time=$2

for secs in  $(seq 1 $wait_time)
do
    if [ -e "$file_name" ]; then
	 echo "File $file_name has arrived in server after $secs secconds"
	 exit 0

     else
	sleep 1
     fi
done
echo "Timeout"
