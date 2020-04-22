import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.walking = False
        self.screen = screen
        self.images = []
        self.standing_image = pygame.image.load('assets/characters/boy.png')
        self.x = 5
        self.y = 600
        for x in range(0, 5):
            print(x)
            i = pygame.image.load(f'assets/characters/boy_{x}.png')
            self.images.append(pygame.transform.flip(i, True, False))

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 155, 395)
        self.feet_coords = (self.rect.center[0] - 300, self.rect.center[1])
        print(self.feet_coords)
        surface = pygame.Surface((320, 240), pygame.SRCALPHA)

        black = (0, 0, 0, 20)
        size = (0, 0, 220, 100)
        
        # self.ellipse_rect.
        self.ellipse = pygame.draw.ellipse(surface, black, size)
        self.surface2 = pygame.transform.rotate(surface, -60)
        # oldrect = self.surface2.get_rect()
        # oldrect.topright = self.feet_coords
        # self.surface2.convert_alpha()
        # alp

    def update(self):
        self.screen.blit(self.surface2, self.feet_coords)
        if self.walking:
            self.index += 1
            # if self.index >= len(self.images):
            if self.index >= 12:
                self.index = 0
            self.x += 6
            self.rect = pygame.Rect(self.x, self.y, 155, 395)
            self.image = self.images[self.index//3]
            self.feet_coords = (self.rect.center[0] - 300, self.rect.center[1]-30)
        else:
            self.index = 0
            self.image = self.standing_image
        
