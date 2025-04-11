#!/bin/bash

PROJECT_ID=$(gcloud config get-value project --quiet)
ZONE=$(gcloud config get-value compute/zone --quiet)

echo "🌍 Using Project ID:  ${CLOUDSHELL_HOSTNAME}"
echo "📍 Using Zone:        $ZONE"

echo "📦 Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt

if lsof -i:8080 > /dev/null; then
  echo "⚠️ Port 8080 is already in use. Skipping Flask start."
else
  echo "🚀 Starting Flask app on port 8080..."
  export FLASK_APP=app/main.py &
  sleep 3
fi

echo ""
echo "🌐 Opening in Cloud Shell Web Preview..."
echo "👉 https://${PORT}-dot-${CLOUDSHELL_HOSTNAME}"
