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

def main():
    run = True
    clock = pygame.time.Clock()
    
    a_list = [1,2,3,4,5,6]
    draw_info = Draw(800, 600, a_list)
    
    while run: 
        clock.tick(60)
        pygame.display.update()
        
        for i in pygame.event.get():
            if i == pygame.QUIT:
                run = False 
    pygame.quit()

if __name__ == "__main__":
    main()