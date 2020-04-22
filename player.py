import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen):
        super(Player, self).__init__()
        self.walking = False
        self.screen = screen
        self.images = []
        self.standing_image = pygame.image.load('assets/characters/boy.png')
        self.x = 120
        self.y = 600
        for x in range(0, 5):
            print(x)
            i = pygame.image.load(f'assets/characters/boy_{x}.png')
            self.images.append(pygame.transform.flip(i, True, False))

        # Player details, for now it just has the demo stuff

        self.details = {
            'Parts':  2,
            'Folders': 1,
            'Keys': 1,
            'Floor': 2,
            'Time': 1961
        }

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(self.x, self.y, 155, 395)
        self.feet_coords = (self.rect.center[0] - 300, self.rect.center[1])
        print(self.feet_coords)
        surface = pygame.Surface((320, 240), pygame.SRCALPHA)

        black = (0, 0, 0, 20)
        size = (0, 0, 220, 100)

        self.ellipse = pygame.draw.ellipse(surface, black, size)
        self.surface2 = pygame.transform.rotate(surface, -60)

    def update(self):
        self.screen.blit(self.surface2, self.feet_coords)
        if self.walking:
            self.index += 1
            # if self.index >= len(self.images):
            if self.index >= 12:
                self.index = 0
            if self.x <= 900:
                self.x += 8
            self.rect = pygame.Rect(self.x, self.y, 155, 395)
            self.image = self.images[self.index//3]
            self.feet_coords = (
                self.rect.center[0] - 300, self.rect.center[1]-30)
        else:
            self.index = 0
            self.image = self.standing_image

    def get_details(self):
        return self.details
