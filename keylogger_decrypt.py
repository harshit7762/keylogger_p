from cryptography.fernet import Fernet
# Load the encryption key (the same key used for encryption)
with open('encryption_key.key', 'rb') as f:
    key = f.read()
fernet = Fernet(key)
# Load the encrypted log data from the file
with open('keys.txt', 'rb') as f:
    encrypted_lines = f.readlines()
for enc_line in encrypted_lines:
    enc_line = enc_line.strip()  # Remove trailing newline bytes
    try:
        # Decrypt the encrypted line (bytes)
        decrypted_bytes = fernet.decrypt(enc_line)
        # Convert bytes to string
        decrypted_log = decrypted_bytes.decode()
        print(decrypted_log)  # This is the original timestamped keystroke log
    except Exception as e:
        print(f"Failed to decrypt a line: {e}")
