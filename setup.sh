#!/bin/bash

echo "📦 Installing dependencies..."
sudo apt-get update -y
sudo apt-get install -y python3-pip git openssh-client

# Step 1: Generate SSH key if it doesn't exist
if [ ! -f ~/.ssh/id_rsa ]; then
  echo "🔐 Generating SSH key..."
  ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa -N ""
fi

# Step 2: Add GitHub to known hosts to avoid prompt
echo "🌐 Adding GitHub to known SSH hosts..."
mkdir -p ~/.ssh
ssh-keyscan github.com >> ~/.ssh/known_hosts

# Step 3: Prompt user to add SSH key to GitHub
echo "📋 Your SSH Public Key:"
cat ~/.ssh/id_rsa.pub
echo "🔗 Visit https://github.com/settings/keys to add it as a new SSH key."
read -p "Press ENTER after you've added the key to your GitHub account..."

# Step 4: Clone the private repo
echo "📥 Cloning your private repo using SSH..."
git clone git@github.com:guy-hemo/website.git

cd website || exit 1

# Step 5: Install Python dependencies
pip3 install -r requirements.txt

# Step 6: Run the Flask app
echo "🚀 Starting Flask app..."
python3 app/main.py
