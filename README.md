# Network Monitor

A simple command-line network monitoring tool built with Python.

## Features

- Ping a user-defined target
- Choose the number of packets to send
- Measure network latency
- Calculate minimum latency
- Calculate maximum latency
- Calculate average latency
- Calculate packet loss
- Display packets sent and received
- Detect whether the target responds
- Handle targets with 100% packet loss

## Technologies

- Python
- Windows Ping
- Git
- GitHub

## How It Works

The program uses the Windows `ping` command to send ICMP Echo Requests to a target.

It collects the Echo Replies and extracts the response time from each successful packet.

The program then calculates:

- Minimum latency
- Maximum latency
- Average latency
- Packet loss percentage
- Online/offline status

## How to Run

1. Make sure Python is installed.
2. Clone this repository.
3. Open the project folder in a terminal.
4. Run:


python main.py

Target examples:
Enter target: 8.8.8.8
Enter number of packets to send: 4