import socket
import sys
from _thread import *
from player import Player
import pickle

server = "192.168.1.157"
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(2)
print("Server started. Waiting for a connection...")

players = [Player(0,0,50,50,(255,0,0)), Player(100, 100, 50, 50, (0,0,255))]
currentPlayer = 0

# What to do when detect a connection
def threaded_client(conn, player): 
    conn.sendall(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data
            if not data:
                print("Disconnected")
                break
            else: 
                reply = players[0] if (player == 1) else players[1]
                # print("Received:", data)
                # print("Sending:", reply)
            conn.sendall(pickle.dumps(reply))
        except: 
            break
    print("Lost connection")
    conn.close()

# Continuously listen for connections to accept
while True: 
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

