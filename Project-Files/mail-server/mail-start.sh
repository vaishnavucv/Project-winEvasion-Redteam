#!/bin/bash

# Stop all containers with the mailhog/mailhog image
docker ps -a | grep mailhog/mailhog | awk '{print $1}' | xargs -r docker stop

# Remove all containers with the mailhog/mailhog image
docker ps -a | grep mailhog/mailhog | awk '{print $1}' | xargs -r docker rm

# Run a new MailHog container
sudo docker run -d -p 8025:8025 -p 1025:1025 mailhog/mailhog
clear
echo ""
echo "Mail Server Starting in ==>  http://nuvelab.io:8025/"
echo "For sending mail use python script in /home/labuser/Tools/sent.py"