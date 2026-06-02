from classes import *
import pygame
pygame.init()
import socket as s
import pickle
import threading as t

server = s.socket(s.AF_INET, s.SOCK_STREAM)

host = s.gethostbyname(s.gethostname())
port = 8000

server.bind((host, port))

server.listen(2)
print(f'Server listening on {host}')

clients = []
clientData = []
clientNum = 0

def handle_client(conn, num):
    global clientNum
    clients.append(conn)
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            clientData[num] = data
            conn.send(pickle.dumps(clientData))
        except:
            clientNum -= 1
            conn.close()
            clients.remove(conn)
            try:
                clientData.pop(num)
            except:
                ...
            print(f'client disconnected {clientNum}')
            break

while True:
    conn, addr = server.accept()
    t.Thread(target=handle_client, args=(conn, clientNum)).start()
    clientNum += 1