import socket

client = socket.socket()
addr = (socket.gethostname(), 8000) # ideally this is remote server's addr
# try with your friend's IP address

print('My address is: ', addr)
client.connect(addr)

data = client.recv(1024) # bytes
print('Server:: ', str(data, 'utf-8')) # bytes to str

client.send(bytes('Hello Python!!', 'utf-8'))

print("That's all folks!")