#!/usr/bin/env bash
# A script that sets up web servers for the deployment of web_static

# Install Nginx if not already installed
if ! command -v nginx &> /dev/null; then
	sudo apt-get update
	sudo apt-get install -y nginx
fi

# Create necessary directories. The -p flag creates parent directories if they don't exist
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

# Create a fake HTML file
echo "<html><head></head><body>AirBnB Clone Web Static Test</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# Create or recreate symbolic link
sudo rm -rf /data/web_static/current	# -rf: force remove files and folders (recursively)
sudo ln -s /data/web_static/releases/test /data/web_static/current	# -s: create symbolic link

# Give ownership of /data/ to ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/		# -R: recursive

# Update Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
nginx_config="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static {" "$nginx_config"; then
	sudo sed -i '/server_name _;/a \
	\ \ \ \ location /hbnb_static {\n \
	\ \ \ \ \ \ \ \ alias /data/web_static/current/;\n \
	\ \ \ \ \ \ \ \ index index.html;\n \
	\ \ \ \ }' "$nginx_config"
fi

# Restart Nginx
sudo service nginx restart
