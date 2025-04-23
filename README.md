



# Rubber Ducky SCN Assignment Luna J
=====================

Rubber Ducky script and it's payloads for SCN

23008809

## Overview
------------

A project designed to not only execute code on a system, but exploit for root, utilise root to leave a backdoor and exfiltrate data out. Purely designed as a demo project, with no actual malicious intent other than against the VMs to test against.

## Files
--------

* `pyproject.toml`: The project's configuration file, which specifies the build system and dependencies.
* `src/ducky/runroot.sh`: A shell script that is executed by the Rubber Ducky USB device to set up the environment and run the payload.
* `src/server/main.py`: The main entry point for the FastAPI server, which provides additional payloads to the Rubber Ducky USB device.
* `src/server/payloads/clipboardWatch.py`: A payload that watches the clipboard for sensitive information and exfiltrates it to the FastAPI server.
* `src/ducky/rootEXEC.py`: A Python script that is executed by the Rubber Ducky USB device to perform additional tasks and interact with the FastAPI server.
* `Makefile`: makefile which prepares ducky script, copies and updates ip and vars in scripts. 

## UV requirements
* `pyproject.toml: requirements used for the fastapi server, you can use the docker container instead to have everything precompiled

Use: ```uv sync``` to setup package requirements

## Usage
-----

1. Clone this repository and navigate to the root directory.
2. Run `make` to generate the script for the Rubber Ducky USB device.
3. Load the .dd script onto Ducky
4. Insert the Rubber Ducky USB device into a target computer.
5. The script will execute and download additional payloads from the FastAPI server.

## FastAPI Server
----------------

Fastapi servers exfiltration endpoints as well as payload downloads

## Payloads
------------

* `clipboardWatch.py`: Watches the clipboard for sensitive information and exfiltrates it to the FastAPI server.
* `analyser.py`: Exfiltrates data about targeted machine

## Mitre Framework mappings
- FastAPI:
- -  Non-Standard Port (10000 http) https://attack.mitre.org/techniques/T1571/
- DuckyUSB: 
- - Replication Through Removable Media https://attack.mitre.org/techniques/T1091/
- RubbyDucky.sh
- -  https://attack.mitre.org/techniques/T1132/  Data Encoding - Standard Encoding 
- - - Uses Base64 decoding on two payloads
- Traitor: 
- - Exploitation for Privilege Escalation https://attack.mitre.org/techniques/T1068/
- - CVE: Dirty Pipe https://nvd.nist.gov/vuln/detail/cve-2022-0847
- runroot.sh 
- - Account Manipulation: SSH Authorized Keys https://attack.mitre.org/techniques/T1098/004
- - Command and Scripting Interpreter: Unix Shell https://attack.mitre.org/techniques/T1059/004/
- - Scheduled Task/Job: Cron https://attack.mitre.org/techniques/T1053/003/
- - Indicator Removal: File Deletion https://attack.mitre.org/techniques/T1070/004/
- clipboardWatch.py:
- - Clipboard Data https://attack.mitre.org/techniques/T1115/
- - Could have had CRON job but difficult to setup with DISPLAY and GTK.
- analyser.py:
- - Automated Collection https://attack.mitre.org/techniques/T1119/
- - System Information Discovery https://attack.mitre.org/techniques/T1082/
- - Command and Scripting Interpreter: Python https://attack.mitre.org/techniques/T1059/006/

## Projects used

- Traitor tool used for automated root execution.
    - Galvin, L. (2025) liamg/traitor. Go [online]. Available from: https://github.com/liamg/traitor [Accessed 16 March 2025].
- FastAPI server import for malicious server.
    - Ramírez, S. (2025) FastAPI. Python [online]. Available from: https://github.com/fastapi/fastapi [Accessed 17 March 2025].
- PyExpect - Used for interfacing with the Traitor root escalation
    - Anon. (2025). Python [online]. Available from: https://github.com/pexpect/pexpect [Accessed 16 March 2025].

