#!/bin/bash
APP_DIR="/home/ec2-user/flask-song-auto-update"

cd $APP_DIR || exit 1

# Kill running app
pkill -f app.py || echo "No app.py process found"

# Pull the latest changes
git pull origin main

# Install requirements
pip3 install -r requirements.txt || echo "No requirements file found"

# Run app
nohup python3 app.py > app.log 2>&1 &
echo "App restarted successfully"

