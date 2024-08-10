#!/bin/bash
apt-get update -y
apt-get install -y apache2 php php-curl libapache2-mod-php php-mysql jq
ufw allow 'Apache Full'

usermod -a -G azureuser azureuser

mkdir -p /var/www/html
chown -R azureuser:azureuser /var/www
chmod 2775 /var/www
find /var/www -type d -exec chmod 2775 {} \;
find /var/www -type f -exec chmod 0664 {} \;
cd /var/www/html
curl -s -H Metadata:true --noproxy "*" "http://169.254.169.254/metadata/instance?api-version=2021-02-01" | jq > index.html
sed -i '1i<pre>' index.html
sed -i '$a</pre>' index.html
curl https://raw.githubusercontent.com/Azure/vm-scale-sets/master/terraform/terraform-tutorial/app/index.php -O

# # Download and install Go
# curl -OL https://go.dev/dl/go1.22.6.linux-amd64.tar.gz
# tar -C /usr/local -xzf go1.22.6.linux-amd64.tar.gz
# echo "export PATH=$PATH:/usr/local/go/bin" >> /etc/profile
# source /etc/profile
#
# # Clone the GitHub repository
# git clone https://github.com/gvicentin/inf0500.git /opt/inf0500
#
# # Navigate to the repository directory
# cd /opt/inf0500/inf0554
#
# # Run the Go application
# make compile
# ./demo
