# Online multiplayer game client
import pygame, socket, threading, json

DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345


class Connection:
    def __init__(self):
        self.encoder = "utf-8"
        self.header_length = 10
        self.player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.player_socket.connect((DEST_IP, DEST_PORT))


class Player:
    def __init__(self, connection):
        self.connection = connection

    def set_player_info(self, player_info):
        pass

    def update(self):
        pass

    def reset_player(self):
        pass


class Game:
    def __init__(self, connection, player, total_players):
        self.connection = connection
        self.player = player
        self.total_players = total_players

    def update(self):
        pass

    def draw(self):
        pass


# ---- RECEIVE GAME CONFIG FROM SERVER (TUTORIAL STYLE) ----
my_connection = Connection()

packet_size = my_connection.player_socket.recv(
    my_connection.header_length
).decode(my_connection.encoder)
room_size = int(
    my_connection.player_socket.recv(int(packet_size))
    .decode(my_connection.encoder)
)

packet_size = my_connection.player_socket.recv(
    my_connection.header_length
).decode(my_connection.encoder)
round_time = int(
    my_connection.player_socket.recv(int(packet_size))
    .decode(my_connection.encoder)
)

packet_size = my_connection.player_socket.recv(
    my_connection.header_length
).decode(my_connection.encoder)
fps = int(
    my_connection.player_socket.recv(int(packet_size))
    .decode(my_connection.encoder)
)

packet_size = my_connection.player_socket.recv(
    my_connection.header_length
).decode(my_connection.encoder)
total_players = int(
    my_connection.player_socket.recv(int(packet_size))
    .decode(my_connection.encoder)
)

# ---- PYGAME SETUP ----
pygame.init()

WINDOW_WIDTH = room_size
WINDOW_HEIGHT = room_size
BLACK = (0, 0, 0)
FPS = fps
clock = pygame.time.Clock()

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Color Collide~~")

my_player = Player(my_connection)
my_game = Game(my_connection, my_player, total_players)

# ---- MAIN LOOP ----
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill(BLACK)
    my_player.update()
    my_game.update()
    my_game.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
