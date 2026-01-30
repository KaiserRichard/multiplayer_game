# Online multiplayer game server
import socket, threading, json, time

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345

ROOM_SIZE = 400
PLAYER_SIZE = 20
ROUND_TIME = 45
FPS = 15
TOTAL_PLAYERS = 4

while ROOM_SIZE % PLAYER_SIZE != 0:
    PLAYER_SIZE += 1


class Connection:
    def __init__(self):
        self.encoder = "utf-8"
        self.header_length = 10
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((HOST_IP, HOST_PORT))
        self.server_socket.listen()


class Player:
    def __init__(self, player_id):
        self.player_id = player_id


class Game:
    def __init__(self, connection):
        self.connection = connection
        self.player_count = 0
        self.player_objects = []
        self.player_sockets = []

    def connect_players(self):
        while self.player_count < TOTAL_PLAYERS:
            player_socket, player_address = self.connection.server_socket.accept()

            # SEND ROOM_SIZE
            header = str(len(str(ROOM_SIZE)))
            header = header.ljust(self.connection.header_length)
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(str(ROOM_SIZE).encode(self.connection.encoder))

            # SEND ROUND_TIME
            header = str(len(str(ROUND_TIME))).ljust(self.connection.header_length)
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(str(ROUND_TIME).encode(self.connection.encoder))

            # SEND FPS
            header = str(len(str(FPS))).ljust(self.connection.header_length)
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(str(FPS).encode(self.connection.encoder))

            # SEND TOTAL_PLAYERS
            header = str(len(str(TOTAL_PLAYERS))).ljust(self.connection.header_length)
            player_socket.send(header.encode(self.connection.encoder))
            player_socket.send(str(TOTAL_PLAYERS).encode(self.connection.encoder))

            self.player_count += 1
            player = Player(self.player_count)
            self.player_objects.append(player)
            self.player_sockets.append(player_socket)

            print(f"Player {self.player_count} connected from {player_address}")

        print("All players connected. Server running...")

        # KEEP SERVER ALIVE (tutorial assumption)
        while True:
            time.sleep(1)


# ---- START SERVER ----
my_connection = Connection()
my_game = Game(my_connection)

print("Server is listening for incoming connections...")
my_game.connect_players()
