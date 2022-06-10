import pygame

class Draw:
    def __init__(self, width, height, x):
        self.width = width
        self.height = height
        
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("List sorting visualiser")
        self.set_list(x)
    
    def set_list(self, x):
        self.list = x

def animationLoop():
    loop = True
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT():
                
    