import pygame
from network import Network
from player import Player
import pickle

# TODO: options booleans for these settings
# TODO: random egg move every (60 / # egg moves) levels including level 1

# with open('data/moves.p', 'rb') as f:
#     moves = pickle.load(f)

width = 500
height = 500
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def redrawWindow(win, player, player2):
    win.fill((255, 255, 255))
    player.draw(win)
    player2.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    clock = pygame.time.Clock()
    p = n.getP()
    
    while run:
        clock.tick(60)
        p2 = n.send(p)
        for event in pygame.event.get():
            if(event.type == pygame.QUIT):
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p, p2)
                
if __name__=="__main__": 
    main() 