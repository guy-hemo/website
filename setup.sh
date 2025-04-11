#!/bin/bash

PROJECT_ID=$(gcloud config get-value project --quiet)
ZONE=$(gcloud config get-value compute/zone --quiet)
PORT=5000

echo "🌍 Using Project ID:  ${CLOUDSHELL_HOSTNAME}"
echo "📍 Using Zone:        $ZONE"

echo "📦 Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt


FLASK_APP=app/main.py python3 -m flask run --host=0.0.0.0 --port=$PORT  &
sleep 3

WEB_PREVIEW_URL="https://$PORT-$WEB_HOST"

if [[ -z "$WEB_PREVIEW_URL" ]]; then
  echo "Failed to fetch Web Preview URL. Please ensure Cloud Shell is running."
  exit 1
fi

# Display the correct Web Preview URL
echo "🌐 Opening in Cloud Shell Web Preview..."
echo "👉 $WEB_PREVIEW_URL"
