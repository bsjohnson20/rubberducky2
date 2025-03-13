#!/bin/bash
cd e3c7d56524bcba9a0eff319676611d5f

# run git
git add .
git commit -m "Updated rubbyDucky.sh"

# increment revision number
revNum=$(cat ../builder/revisionNum.txt)
echo $((revNum+1)) > ../builder/revisionNum.txt
ssh-agent bash -c 'ssh-add ../rubbyducky; git push git@gist.github.com:e3c7d56524bcba9a0eff319676611d5f.git'

echo "uploaded to gist"
