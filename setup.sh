#!/bin/bash

PROJECT_ID=$(gcloud config get-value project --quiet)
ZONE=$(gcloud config get-value compute/zone --quiet)

echo "🌍 Using Project ID:  $PROJECT_ID"
echo "📍 Using Zone:        $ZONE"

echo "📦 Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt

if lsof -i:8080 > /dev/null; then
  echo "⚠️ Port 8080 is already in use. Skipping Flask start."
else
  echo "🚀 Starting Flask app on port 8080..."
  export FLASK_APP=app/main.py
  flask run --host=0.0.0.0 --port=8080 &
  sleep 3
fi

echo ""
echo "🌐 Opening in Cloud Shell Web Preview..."
echo "👉 https://8080-dot-${PROJECT_ID}.dot-devshell.appspot.com"
