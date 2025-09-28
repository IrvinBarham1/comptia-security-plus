from log_encrypt import decrypt_log

entries = decrypt_log()
for e in entries: 
    print("--- Decyrpted Entry ---")
    print(e)