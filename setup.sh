#!/bin/bash

echo "📦 Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip git openssh-client


# Step 1: Install Python dependencies
pip3 install -r requirements.txt

# Step 2: Run the Flask app
echo "🚀 Starting Flask app..."
python3 app/main.py
