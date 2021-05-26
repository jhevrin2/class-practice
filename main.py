from basketball.player import Player
from settings import API_URL

if __name__ == '__main__':
    lebron = Player(name='Lebron', team='Lakers', number=23)
    announcement = lebron.announce_player()
    print(announcement, API_URL)
