#!/bin/bash
trap 'kill -HUP -$$' exit

# Activate virtualenv
# . myenv/bin/activate

./client.py 2222 wss://example.com/ws/ &
while true
do
	ssh -p 2222 localhost -vCND 1080
	sleep 1
done
