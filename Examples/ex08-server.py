# A simple socket server program to respond to what client says!

from socket import *
import time

def main():
	server = socket()
	addr = ('', 8000)
	server.bind(addr)
	server.listen(5)

	while True:
		print('Waiting for a client connection...')
		cl_sock, cl_addr = server.accept()
		print('Got a connection from a client at', cl_addr)
		cl_sock.send(bytes('Hi there!', 'utf-8'))
		cl_data = cl_sock.recv(1024)
		print('Client says...', cl_data)
		time.sleep(10)
		cl_sock.close() 
		print('Closed the connection for the client at', cl_addr)


if __name__ == '__main__':
	main()