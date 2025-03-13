Rubber Ducky Payload
=====================

Rubber Ducky server and script combo

## Overview

Linux focused scripts to deploy and exploit vulnerabilities within the UWE linux vm. Using a fastapi server to retrieve executables/scripts and exfiltrate data to POST endpoints.

## Usage
Clone this repository and navigate to the root directory.
Run make to generate the script for the Rubber Ducky USB device.
Load the script onto the Rubber Ducky USB device.
Insert the Rubber Ducky USB device into a target computer.
The script will execute and download additional payloads from the FastAPI server.
FastAPI Server
The FastAPI server is used to provide additional payloads to the Rubber Ducky USB device. The server is set up using the src/server/main.py file and provides endpoints for the payload to interact with.

Payloads
clipboardWatch.py: Watches the clipboard for sensitive information and exfiltrates it to the FastAPI server.
Notes
This payload is for educational purposes only and should not be used for malicious activities.
The FastAPI server should be run on a secure network and should not be exposed to the internet.
The GitHub Gist URL and the FastAPI server URL should be configured securely to prevent unauthorized access.