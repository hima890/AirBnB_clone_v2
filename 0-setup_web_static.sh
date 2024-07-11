#!/bin/bash

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

# Update Nginx configuration if the block is not already present
if ! grep -q "location /hbnb_static/" /etc/nginx/sites-available/default; then
    echo "Adding location block to Nginx configuration"
    sudo sed -i '/server_name _;/a \
\\n\
\tlocation /hbnb_static/ {\
\n\t\talias /data/web_static/current/;\
\n\t}\
\n' /etc/nginx/sites-available/default
else
    echo "Location block already exists in Nginx configuration"
fi

# Add the domain name to the server_name directive if not already there
if ! grep -q "server_name mydomainname.tech;" /etc/nginx/sites-available/default; then
    echo "Updating server_name in Nginx configuration"
    sudo sed -i '/server_name _;/s/_;/ ibrahimhanafideveloper.tech;/' /etc/nginx/sites-available/default
else
    echo "Server name already set in Nginx configuration"
fi

# Test the Nginx configuration
sudo nginx -t

# Restart Nginx
if [ $? -eq 0 ]; then
    echo "Restarting Nginx"
    sudo systemctl restart nginx
else
    echo "Nginx configuration test failed"
fi

echo "Setup completed successfully!"
