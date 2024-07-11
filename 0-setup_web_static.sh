#!/usr/bin/env bash
# A Bash script that sets up your web servers for the deployment of web_static.

# Update package list and install Nginx
sudo apt-get update
sudo apt-get install -y nginx

# Create the directories if they don't already exist
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# Create the fake HTML file with simple content
echo "<html>
  <head>
  </head>
  <body>
    <h1>Welcome to your test page!</h1>
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# Create the symbolic link, remove it if it already exists
if [ -L /data/web_static/current ]; then
    sudo rm /data/web_static/current
fi
sudo ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
sudo sed -i '/server_name _;/a \\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

# Restart Nginx
sudo service nginx restart

echo "Setup completed successfully!"
