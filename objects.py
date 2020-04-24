
import pygame


class Objects(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, screen, debug=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect().move(pos)
        self.screen = screen
        # self.area = self.screen.get_rect()
        self.debug = debug
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]

    def update(self):
        print("Method not overridden")


class Interactable(Objects):
    def __init__(self, pos, image_path, screen, disappears, debug=False):
        Objects.__init__(self, pos, image_path, screen, debug)
        self.interactable = True
        self.clicked = False

    def update(self):
        print("Override OnClick method.")

    def onclick(self):
        print("Override OnClick method.")


class Box(Objects):
    def __init__(self, pos, image_path, screen, debug=False):
        Objects.__init__(self, pos, image_path, screen, debug)

    def update(self):
        if self.debug:
            pygame.draw.circle(self.screen, (255, 111, 111),
                               self.rect.center, 4)


class Painting(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug=False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)

    def update(self):
        if self.clicked:
            print("Painting clicked")

    def onclick(self):
        self.clicked = True
