#Online multiplayer game client 
import pygame, socket, threading, json

#Define socket constatns to be used and altered
#DEST_IP should be of the form '192.168.1.*'
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345

class Connection():
    '''A socket connection class for players to connect to a server'''

    def __init__(self):
        '''Initialization for the Connection class'''
        pass


class Player():
    '''A player class the client can control'''
    def __init__(self, connetion):
        '''Initializetion of the Player class'''
        pass

    def set_player_info(self, player_info):
        '''Set the player info to the given information from the server'''
        pass

    def update(self):
        '''Update the player by changing their coordinates in the game'''

    def reset_player(self):
        ''''Reset player values for a new round on the client side'''
        pass

class Game():
    '''A game clas to handle all operations of gameplay'''
    def __init__(self, connection, player, total_players):
        pass

    def ready_game(self):
        pass

    def start_game(self):
        pass

    def reset_game(self):
        pass

    def send_player_info(self):
        '''Send specific info about this player to the server'''
        pass

    def receive_player_info(self):
        '''Receive player info from the server'''
        pass

    def receive_pregame_state(self):
        '''Receive all ìnormation about all players from the server during the game'''
        pass

    def process_game_state(self):
        '''Process the game state to update scores '''
        pass

    def update(self):
        '''Update the game'''
        pass

    def draw(self):
        '''Draw the game and all game assets to the window'''
        pass

#Create a connection and get wwindow information from the server

my_connection = Connection()

#initialize pygame
pygame.init()
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
ROUND_TIME = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
MAGENTA = (155, 0, 155)
FPS = 30
clock = pygame.time.Clock()

font = pygame.font.SysFont('gabriola', 28)

#Create a game window
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("~~Color Collide~~")

#Create player and game objects
my_player = Player(my_connection)
my_game = Game(my_connection, my_player, 4)

#The main game loop 
running = True
while running:
    #Check to see if the user wants to quit
    for even in pygame.event.get():
        if even.type == pygame.QUIT:
            running = False

    #Fill the surface 
    display_surface.fill(BLACK)

    #Update and draw classes
    my_player.update()
    my_game.update()
    my_game.draw()

    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)