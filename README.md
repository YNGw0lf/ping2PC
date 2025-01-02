# README.md

## Monitoring the Status of a Remote PC

This Python script allows you to monitor the status of a second (remote) PC by periodically checking if it is reachable using the ICMP protocol (ping). When the remote PC comes online, the program sends a desktop notification and terminates.

### Requirements
To use this script, you need:
- **Python 3.x** installed on your system.
- The following Python packages:
  - [`ping3`](https://pypi.org/project/ping3/): for pinging the remote PC.
  - [`plyer`](https://pypi.org/project/plyer/): for sending desktop notifications.

You can install them with the command:
```bash
pip install ping3 plyer
```

### How It Works

1. **IP Address Input:**
   - The user provides the IP address of the remote PC to be monitored.
   - If the IP address is not provided, the program returns an error.

2. **Monitoring:**
   - The script uses the `ping3` module to send ICMP requests to the specified IP address.
   - If the PC responds to the ping, it means it is online, and the script sends a desktop notification.
   - If the PC is not online, the program waits 5 seconds before trying again.

3. **Desktop Notification:**
   - When the remote PC becomes reachable, the `plyer` module generates a desktop notification with the message: `"The PC is online."`.
   - After sending the notification, the program terminates.

### How to Run the Script
1. Save the code in a file, e.g., `script.py`.
2. Run the script via terminal or Python IDE:
   ```bash
   python script.py
   ```
3. Enter the IP address of the remote PC when prompted.

### Note
- Ensure the remote PC responds to ICMP (ping) requests. You may need to configure the firewall on the remote PC to allow ping.
- The program automatically stops when the remote PC becomes reachable.