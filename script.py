import time
from ping3 import ping
from plyer import notification

# IP of the second PC
ip = input("Please enter the IP address of the second PC: ")

if ip:
    print(f"L'indirizzo IP inserito è: {ip}")
else:
    print("IP non valido!")

# Function to see if the second PC is online
def check_pc_online(ip):
    response = ping(ip)
    if response is not None:
        return True
    else:
        return False

# Function to send notification
def send_notification():
    notification.notify(
        title='Your PC is on!',
        message='The PC is online.',
        timeout=5  # duration of the notification
    )

# Monitoring cycle
while True:
    if check_pc_online(ip):
        send_notification()
        print(f"Il PC({ip}) è online")
        break  # Go out of the loop if the second PC is online
    else:
        print(f"Il PC con IP {ip} non è online, riprovo tra 5 secondi...")
    time.sleep(5)  # attempt 5 seconds before trying again