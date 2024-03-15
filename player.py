import pygame 

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color 
        self.distance = 3 # move distance

    # draw rectangle on canvas win based on stored rect
    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))

    # handle keypress
    def move(self):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT]):
            self.x -= self.distance
        if(keys[pygame.K_RIGHT]):
            self.x += self.distance
        if(keys[pygame.K_UP]):
            self.y -= self.distance
        if(keys[pygame.K_DOWN]):
            self.y += self.distance
        # otherwise no movement