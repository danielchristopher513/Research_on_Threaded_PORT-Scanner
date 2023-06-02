# Research_on_Threaded_PORT-Scanner

## Threaded PORT-Scanner
### The Threaded PORT-Scanner is a Python script that allows you to scan for open ports on a target host. It utilizes multithreading to improve the scanning speed by concurrently checking multiple ports.

## Features
The Threaded PORT-Scanner includes the following features:

+ **Port Scanning**: The script can scan a range of ports on a target host to identify which ports are open and available for communication.

+ **Multithreading**: The script uses multithreading to scan multiple ports concurrently, making the scanning process faster.

+ **Hostname Configuration**: Based on given hostname script converts it to ipv4 to scan the ports.

+ **Simple Command-Line Interface**: The script provides a simple command-line interface for specifying the target host and port range to scan.

## Requirements
To run the Threaded PORT-Scanner, you need the following requirements:

+ **Python**: Make sure you have Python 3.x installed on your system. You can download Python from the official Python website: python.org.

+ **Python Libraries**: The script requires the socket,time and threading  libraries

## Usage
To use the Threaded PORT-Scanner, follow these steps:

+ Open a terminal or command prompt.

+ Navigate to the directory where the threaded_port_scanner.py file is located.

+ Run the script with the following command:
```
python threaded_port_scanner.py
```
Follow the prompts to enter the target host and specify the port range to scan.

Wait for the script to complete the scanning process.

View the results, which will display the open ports found on the target host.
