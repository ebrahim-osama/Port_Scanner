## Introduction

Python Port Scanner is a command-line tool written in Python that allows users to scan for open ports on a specified host within a given range of port numbers. The tool uses multi-threading for faster performance and supports banner grabbing to identify services running on open ports.

**Note**: The banner grabbing functionality is still in development and may produce messy output, So it's commented out until fixed.

## Usage

To use the Python Port Scanner:

1. Simply clone the repository to your local machine

2. Run the script with the following command:

   ```bash
   python3 port_scanner.py <host> <start_port> <end_port>
   ```

   Replace `<host>`, `<start_port>`, and `<end_port>` with the appropriate values. For example:

   ```bash
   python3 port_scanner.py example.com 1 1000
   python3 port_scanner.py <IP> 1 1000
   ```

## Features

- **Multi-threaded Scanning**: Utilizes multi-threading to scan for open ports concurrently, improving performance.
- **Banner Grabbing**: Retrieves banner information from services running on open ports, helping to identify the type of service. (Work in progress)
- **Port Range Specification**: Supports specifying a range of port numbers to scan, allowing users to target specific ports.

## Installation

- Python Port Scanner requires Python 3 to be installed on your system.
- Clone the repo to your local machine



**Note:** Python Port Scanner is intended for educational purposes only. Use responsibly and respect the privacy and security of others.
