#!/bin/bash

APP_DIR="/home/ec2-user/flask-song-auto-update"

# Navigate to app directory
cd $APP_DIR || exit 1

# Kill any running app.py process
pkill -f app.py || echo "No existing app.py process"

# Pull latest code
git pull origin main

# Install requirements if any
pip3 install -r requirements.txt || echo "No requirements file, skipping..."

# Start the app with nohup
nohup python3 app.py > app.log 2>&1 &
echo "App started in background"

