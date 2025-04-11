#!/bin/bash

# Automatically retrieve project ID and zone (optional, not required to run Flask)
PROJECT_ID=$(gcloud config get-value project)
ZONE=$(gcloud config get-value compute/zone)

echo "🌍 Using Project ID:  $PROJECT_ID"
echo "📍 Using Zone:        $ZONE"

echo "📦 Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt

echo "🚀 Starting Flask app on port 8080..."
export FLASK_APP=app/main.py
flask run --host=0.0.0.0 --port=8080 &

# Wait a few seconds to give Flask time to start
sleep 3

echo ""
echo "🌐 Opening in Cloud Shell Web Preview..."
echo "👉 https://8080-dot-${PROJECT_ID}.dot-devshell.appspot.com"
