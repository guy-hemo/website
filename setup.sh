#!/bin/bash
echo "📦 Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip

pip3 install -r requirements.txt

echo "🚀 Starting Flask app..."
python3 app/main.py
