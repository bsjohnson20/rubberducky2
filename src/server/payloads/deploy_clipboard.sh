# Replace UUID with sed in clipboardWatch.py
sed -i "s/<REPLACE_UUID>/$(cat uuid.txt)/g" clipboardWatch.py

# copy script to root bin
cp clipboardWatch.py /bin/

# Allow script to run
chmod +x /bin/clipboardWatch.py

# load user from file: "user.txt"
user=$(cat user.txt)

# run script as user in cron

# crontab -u $user -l | { cat; echo "* * * * * /bin/clipboardWatch.py"; } | crontab -u $user -

# echo "* * * * * /bin/clipboardWatch.py" | sudo crontab -u $user -
echo "Deployed clipboardWatch.py as a cron job"
display=$(cat display.txt)
export DISPLAY=$display

# su - $user -c /bin/clipboardWatch.py &
nohup sudo -u $user -H sh -c "/bin/clipboardWatch.py" > /dev/null 2>&1 &
disown -a
# run script as user


echo "Clipboard Watcher Deployed without persistence as backup"