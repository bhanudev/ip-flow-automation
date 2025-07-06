# IP Flow Automation Simulator

This is a Python-based simulation tool that automates the process of running a shell-based IP generation flow.

## Features

- Command-line interface using `argparse`
- Simulated tool execution via shell script
- Retry mechanism (up to 3 attempts)
- Logs each attempt
- Generates metadata and status files
- Simulates output file creation

## How to Run

1. Make the shell script executable:

```bash
chmod +x ip_tool_simulator.sh

2.Run the script with Python:

python3 main.py --ip-name USB_3_0 --out-dir ./output

Output

logs/: log of the run

metadata/: job details in JSON format

status/: success or failure result

generated_output/: dummy Verilog and tool log files

Project Purpose
This project is built for practicing infrastructure-level automation using Python and Shell scripting.
