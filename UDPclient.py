import socket

target_host = "0.0.0.0"
target_port = 9998

#Creating socket object for tcp client with IPv4
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.connect((target_host, target_port))

client.send(b"ABCDEF")

data, addr = client.recvfrom(4096)

print(data.decode())
client.close()