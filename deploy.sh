#!/bin/bash
APP_DIR="/home/ec2-user/flask-song-auto-update"

cd $APP_DIR || exit 1

pkill -f app.py || echo "No app.py process found"
git pull origin main
pip3 install -r requirements.txt || echo "No requirements file found"

# Use sudo to bind to port 80
sudo nohup python3 app.py > app.log 2>&1 &
echo "App restarted successfully"

