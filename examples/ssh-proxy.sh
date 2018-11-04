#!/bin/bash
trap 'kill -HUP -$$' exit

# Activate virtualenv
# . myenv/bin/activate

python3 -m wspm.client 2222 wss://example.com/ws/ &
while true
do
	ssh -p 2222 localhost -vCND 1080
	sleep 1
done
