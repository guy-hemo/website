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

echo "🚀 Starting Flask app..."
# Run Flask on port 8080 — required for Cloud Shell Preview
FLASK_APP=app/main.py &
