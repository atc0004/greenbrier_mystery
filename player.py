import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.walking = False
        self.images = []
        self.x = 5
        self.y = 500
        for x in range(0, 5):
            print(x)
            i = pygame.image.load(f'assets/characters/boy_{x}.png')

            self.images.append(pygame.transform.flip(i, True, False))

        self.index = 0
        self.image = self.images[self.index]

        self.rect = pygame.Rect(self.x, self.y, 155, 395)

    def update(self):
        if self.walking:
            self.index += 1
            # if self.index >= len(self.images):
            if self.index >= 12:
                self.index = 0
            self.x += 6
            self.rect = pygame.Rect(self.x, self.y, 155, 395)
            self.image = self.images[self.index//3]
        else:
            self.index = 0
            self.image = self.images[self.index]
