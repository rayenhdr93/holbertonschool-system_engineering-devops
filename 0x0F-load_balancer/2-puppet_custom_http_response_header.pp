#!/usr/bin/env bash
# custom http with puppet
exec {'p':
command  => 'sudo apt-get update
sudo apt-get -y install nginx
sudo sed -i "17i\        add_header X-Served-By $HOSTNAME;" /etc/nginx/nginx.conf
sudo /etc/init.d/nginx restart',
provider => shell,
}