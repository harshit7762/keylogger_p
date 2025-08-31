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

SWITCH

if with keyboard Key.esc sets the ESC key as the kill switch which when pressed will sth lopping.

Note:

Melware often har kell switches for testing. Analysts can search for there as potential Weak points to terminate execution.

writing Encrypted Logs

Drepane
