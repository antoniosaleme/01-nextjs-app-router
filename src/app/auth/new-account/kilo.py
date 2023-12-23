import os
import subprocess
from telegram import Bot
import asyncio

# Telegram Bot Configuration
TOKEN = ''
bot = Bot(token=TOKEN)
CHAT_ID = ''

# Detected devices storage
detected_devices = set()

# Function to scan the network with Nmap
def scan_network():
    # Replace '192.168.1.0/24' with your network range
    result = subprocess.check_output(['nmap', '-sn', '192.168.1.0/24'])
    devices_output = result.decode('utf-8')
    devices = set()

    # Add logic to parse devices_output and extract identifiers (IPs or MACs)
    # Customize this parsing based on your Nmap output

    return devices

# Asynchronous function to send a message to Telegram
async def send_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Asynchronous function to scan and notify
async def scan_and_notify():
    global detected_devices
    while True:
        current_scan = scan_network()
        new_devices = current_scan - detected_devices
        disconnected_devices = detected_devices - current_scan

        # Notify for new devices
        for device in new_devices:
            await send_message(f"New device detected: {device}")
            detected_devices.add(device)

        # Notify for disconnected devices
        for device in disconnected_devices:
            await send_message(f"Device disconnected: {device}")
            detected_devices.remove(device)

        await asyncio.sleep(60)  # Scan every 60 seconds

# Asynchronous main function
async def main():
    await send_message("Network monitoring script is now running.")
    await scan_and_notify()

# Run the script
if __name__ == "__main__":
    asyncio.run(main())




import os
import subprocess
from telegram import Bot
import asyncio

# Telegram Bot Configuration
TOKEN = ''
bot = Bot(token=TOKEN)
CHAT_ID = ''

# Detected devices storage
detected_devices = set()

# Function to scan the network with Nmap
def scan_network():
    # Replace '192.168.1.0/24' with your network range
    result = subprocess.check_output(['nmap', '-sn', '192.168.1.0/24'])
    devices_output = result.decode('utf-8')
    devices = set()

    # Add logic to parse devices_output and extract identifiers (IPs or MACs)
    # Example: Parse each line and look for IP addresses or MAC addresses
    # This is a placeholder and needs to be customized for your specific output

    return devices

# Asynchronous function to send a message to Telegram
async def send_message(message):
    await bot.send_message(chat_id=CHAT_ID, text=message)

# Asynchronous function to scan and notify
async def scan_and_notify():
    global detected_devices
    while True:
        current_scan = scan_network()
        new_devices = current_scan - detected_devices
        for device in new_devices:
            await send_message(f"New device detected: {device}")
            detected_devices.add(device)
        await asyncio.sleep(60)  # Scan every 60 seconds

# Asynchronous main function
async def main():
    await send_message("Network monitoring script is now running.")
    await scan_and_notify()

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
