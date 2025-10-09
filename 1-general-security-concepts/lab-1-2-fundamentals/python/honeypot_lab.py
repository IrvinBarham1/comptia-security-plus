from pathlib import Path
import socket
import threading
import datetime 
from log_encrypt import encrypt_log

HOST = "127.0.0.1"
PORT = 2222
LOG_FILE =  Path("honeypot_log.enc")

def handle_client (conn, addr):
    try: 
        try: 
            data = conn.recv(4000)
        except Exception:
            data = b""
        print(f"[+] Connection from {addr} ({len(data)} bytes)")
        encrypt_log(addr, data)

        body = b"Welcome, make yourself at home!"
        http_response = (
            b"HTTP/1.1 200 OK\r\n"
            b"Content-Type: text/plain\r\n"
            b"Content-Length: " + str(len(body)).encode() + b"\r\n"
            b"\r\n" + 
            body
        )
        conn.sendall(http_response)

    except Exception as e:
        print(f"[!] handle_client error from {addr}: {e}")
    finally:
        try:
            conn.close()
        except Exception:
            pass

def main():
    print(f"Honeypot is online on {HOST}:{PORT} (logs -> {LOG_FILE})")
    # Create TCP Socket: IPv4 Protocol, TCP
    with socket.socket (socket.AF_INET, socket.SOCK_STREAM) as s:
        # Allows quick reconnection to IP/port
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        s.settimeout(1.0)

        try:
            while True:
                try:
                    conn, addr = s.accept()
                except socket.timeout:
                    continue
                t = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
                t.start()
        except KeyboardInterrupt:
            print("\nYou got Honeypotted. Goodbye.")

if __name__ == "__main__":
    main() 