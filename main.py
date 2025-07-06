# ip_flow_automation/main.py

import argparse
import subprocess
import logging
import time
import json
import os
from datetime import datetime


def setup_logging(ip_name):
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, f"{ip_name}_run.log")
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    return log_file


def run_tool(ip_name, out_dir):
    os.makedirs(out_dir, exist_ok=True)
    os.makedirs("metadata", exist_ok=True)
    os.makedirs("status", exist_ok=True)

    log_file = setup_logging(ip_name)

    for attempt in range(3):
        try:
            logging.info(f"Attempt {attempt+1}: Running CAD tool simulation for IP: {ip_name}")
            result = subprocess.run(["bash", "ip_tool_simulator.sh"], check=True)
            logging.info("Tool execution successful")

            metadata = {
                "ip_name": ip_name,
                "status": "success",
                "timestamp": datetime.now().isoformat(),
                "log_file": log_file
            }
            with open(f"metadata/{ip_name}_metadata.json", "w") as f:
                json.dump(metadata, f, indent=4)

            with open(f"status/{ip_name}_status.txt", "w") as f:
                f.write("SUCCESS")

            return

        except subprocess.CalledProcessError as e:
            logging.error(f"Attempt {attempt+1} failed: {e}")
            time.sleep(3)

    with open(f"status/{ip_name}_status.txt", "w") as f:
        f.write("FAILED")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IP Flow Automation Script")
    parser.add_argument('--ip-name', required=True, help='Name of the IP block')
    parser.add_argument('--out-dir', required=True, help='Output directory')
    args = parser.parse_args()

    run_tool(args.ip_name, args.out_dir)
