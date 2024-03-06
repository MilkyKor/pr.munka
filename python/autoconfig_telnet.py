# Importing modules (getpass to check password, and telnetlib)

import getpass
import telnetlib

# Parameters for connection

HOST = "your_router_ip"
user = input("Enter your Telnet username: ")
password = getpass.getpass("Enter your Telnet password: ")

# Starting Telnet connection

tn = telnetlib.Telnet(HOST)

# Checking username and password

tn.read_until(b"Username: ")
tn.write(user.encode('utf8') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('utf8') + b"\n")

# Configuration (console, vty password, enable secret, service password-encryption)

tn.write(b"enable\n")
tn.write(b"configure terminal\n")
tn.write(b"line console 0\n")
tn.write(b"password cisco12345\n")
tn.write(b"login\n")
tn.write(b"exit\n")
tn.write(b"line vty 0 15\n")
tn.write(b"password cisco12345\n")
tn.write(b"login\n")
tn.write(b"exit\n")
tn.write(b"enable secret class12345\n")
tn.write(b"service password-encryption\n")
tn.write(b"exit\n")
tn.write(b"exit\n")

print(tn.read_all().decode('utf8'))

