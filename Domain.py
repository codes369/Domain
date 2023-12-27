# codes
import socket

domain = input("Domain : ").lower()

domain = domain.replace("http://", "")
domain = domain.replace("https://", "")
domain = domain.replace("www.", "")

if domain[-3:] == "org" or domain[-3:] == "com" or domain[-3:] == "net":
    whois_server = "whois.internic.net"
else:
    whois_server = "whois.iana.org"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((whois_server, 43))

s.send((domain + "\r\n").encode())

msg = s.recv(10000)

print(msg.decode())
