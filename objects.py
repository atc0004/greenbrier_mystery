
import pygame


class Objects(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, screen, debug=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect().move(pos)
        self.screen=screen
        # self.area = self.screen.get_rect()
        self.debug=debug
        # self.center=pos
        self.x = pos[0]
        self.y = pos[1]

    def update(self):
        print("Method not overridden")


class Interactable(Objects):
    def __init__(self, pos, image_path, screen, disappears, debug = False):
        Objects.__init__(self, pos, image_path, screen, debug)
        self.interactable=True
        self.clicked=False

    def update(self):
        print("Override OnClick method.")

    def onclick(self):
        print("Override OnClick method.")


class Box(Objects):
    def __init__(self, pos, image_path, screen, debug = False):
        Objects.__init__(self, pos, image_path, screen, debug)

    def update(self):
        if self.debug:
            pygame.draw.circle(self.screen, (255, 111, 111),
                               self.rect.center, 4)


class Painting(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug = False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)

    def update(self):
        if self.clicked:
            print("Painting clicked")

    def onclick(self):
        self.clicked=True


class Chair(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug = False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)
        self.originalPos = True
        self.oX = self.rect.x
        self.oY = self.rect.y
    def update(self):
        if self.clicked:
            if self.originalPos is False:
                self.rect.x = self.oX
                self.rect.y = self.oY
                originalPos = True
            if(self.rect.x > 1200 or self.rect.y > 550):
                self.rect.x -= 1
                self.rect.y -= 1
                
            else:
                self.originalPos = False
                self.clicked = False
                
    def onclick(self):
        self.clicked=True

class Document(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug = False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)

    def update(self):
        if self.clicked:
            print("Document clicked")
            #display text blurb/info
            #dissappear
    def onclick(self):
        self.clicked=True
    
class Key(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug = False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)

    def update(self):
        if self.clicked:
            print("Key clicked")
            #dissapear
            #add key to player inventory 
            
    def onclick(self):
        self.clicked=True