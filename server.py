import threading
import socket

host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()
clients = []
username = []
passwords = {
    'nathan': '1234',
    'mordi': '5678',
    'kfir': '9123'
}


def broadcast(message):
    for client in clients:
        client.send(message)


# Function to handle clients connections


def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            un = username[index]
            broadcast(f'{username} has left the chat room!'.encode('utf-8'))
            username.remove(username)
            break


# Main function to receive the clients connection


def receive():
    while True:
        print('Server is running and listening ...')
        client, address = server.accept()
        print(f'connection is established with {str(address)}')
        client.send('username?'.encode('utf-8'))
        alias = client.recv(1024)
        username.append(username)
        clients.append(client)
        print(f'The username of this client is {username}'.encode('utf-8'))
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('you are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


if __name__ == "__main__":
    receive()


