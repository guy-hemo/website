#!/bin/bash

# Automatically retrieve project ID and zone
PROJECT_ID=$(gcloud config get-value project)
ZONE=$(gcloud config get-value compute/zone)

echo "Using Project ID: $PROJECT_ID"
echo "Using Zone: $ZONE"

echo "📦 Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt

echo "🚀 Starting Flask app on port 5000..."
python3 app/main.py &

# Expose the app to Web Preview
echo "🌐 Exposing Flask app via Web Preview..."
gcloud compute ssh --project $PROJECT_ID --zone $ZONE --command "python3 -m http.server 5000"
