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


FLASK_APP=main.py python3 -m flask run --host=0.0.0.0 --port=$PORT  &
sleep 3

WEB_PREVIEW_URL="https://$PORT-$WEB_HOST"

if [[ -z "$WEB_PREVIEW_URL" ]]; then
  echo "Failed to fetch Web Preview URL. Please ensure Cloud Shell is running."
  exit 1
fi

# Display the correct Web Preview URL
echo "🌐 Opening in Cloud Shell Web Preview..."
echo "👉 $WEB_PREVIEW_URL"
# ANSI color codes
RED='\033[0;31m'
GREEN='\033[1;32m'
BLUE='\033[1;34m'
YELLOW='\033[1;33m'
BOLD='\033[1m'
RESET='\033[0m'

# Print a stylish banner and clickable link
echo -e ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
echo -e "${BOLD}${BLUE}🌐 Your Flask app is launching!${RESET}"
echo -e ""
echo -e "${YELLOW}👉 Preview URL:${RESET} ${BOLD}${BLUE}$WEB_PREVIEW_URL${RESET}"
echo -e ""
echo -e "${GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${RESET}"
