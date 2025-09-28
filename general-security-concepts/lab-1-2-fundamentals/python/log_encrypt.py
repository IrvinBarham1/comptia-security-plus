from pathlib import Path
from cryptography.fernet import Fernet
import datetime
import os


KEY_FILE = Path("honey.key")
ENCRYPT_FILE = Path("honeypot_log.enc")


def create_key(key_path: Path) -> bytes:
    if key_path.exists() and (data := key_path.read_bytes()):
        return data
    key = Fernet.generate_key()
    key_path.write_bytes(key)
    try:
        os.chmod(key_path, 0o600)
    except Exception:
        pass
    return key

def encrypt_log(client_addr, data_bytes):
    ts = datetime.datetime.utcnow().isoformat() + "Z"
    plaintext = (
        f"{ts} - {client_addr} - {len(data_bytes)} bytes\n"
        f"DATA: {data_bytes!r}\n\n"
    ).encode("utf-8")
    key = create_key(KEY_FILE)
    f = Fernet(key)
    token = f.encrypt(plaintext)
    with ENCRYPT_FILE.open("ab") as f:
        f.write(token + b"\n")
    print(">>> Encrypted Honeypot Log")

def decrypt_log(): 
    key = KEY_FILE.read_bytes()
    f = Fernet(key)
    entries = []
    with ENCRYPT_FILE.open("rb") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try: 
                pt = f.decrypt(line)
                entries.append(pt.decode("utf-8", errors='replace'))
            except Exception as e:
                entries.append(f">>> Decryption Attempt Failed {e}")
    return entries
