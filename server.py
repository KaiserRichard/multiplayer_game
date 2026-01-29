#Online multiplayer game client 
import socket, threading, json, time
#Network configuration

HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345

#Game configuration
ROOM_SIZE = 400
PLAYER_SIZE = 20
ROUND_TIME = 45
FPS = 15
TOTAL_PLAYERS = 4                   

#Ensure room and player sizes align
while ROOM_SIZE % PLAYER_SIZE != 0:
    PLAYER_SIZE += 1

class Connection():
    def __init__(self):
        pass

class Player():
    def __init__(self, player_id):
        self.player_id  = player_id
    
    def set_player_info(self, info):
        pass

    def reset_player(self):
        '''Set the player info to given info from the client'''
        pass

    def reset_player(self):
        '''Reset player values for a new round on the server side'''
        pass

class Game():
    '''A class to handle all the operations of gameplay'''
    def __init__(self, connection):
        '''Initialzation of the Game class'''

    def connect_players(self):
        '''Conect any incoming players to the game server'''
        pass

    def broadcast(self):
        '''Broadcast information to all connected players'''
        pass

    def ready_game(self, player, player_socket):
        '''Ready the game to be played'''
        pass

    def reset_game(self, player):
        '''Restart the game and wipe information for a specific player'''
        pass

    def send_player_infor(self, player, player_socket):
        '''Send specific information about this player to the given client'''
        pass

    def receive_pregrame_player_info(self, player, player_socket):
        '''Receive specific info about this player pregame'''
        pass

    def receive_game_player_info(self, play):
        '''Receive spefici info about this player during the game'''
        pass

    def process_game_state(self, player, player_socket):
        '''Process the given player info and update the games state'''
        pass

    def send_game_state(self, player_socket):
        '''Send the current game state of all players to this given player'''
        pass

#Start the server
my_connection = Connection()
my_game = Game(my_connection)
#Server is listening to incoming connections
print("Server is listening to incoming connections....")
my_game.connect_players()