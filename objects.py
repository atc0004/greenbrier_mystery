
import pygame


class Objects(pygame.sprite.Sprite):
    def __init__(self, pos, image_path, screen, debug=False):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_path).convert_alpha()
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
        if self.disappears:
            self.kill()
        print("Override OnClick method.")


class Item:
    def __init__(self, name):
        self.name = name


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
        self.max_move = 40
        self.moved = 0

    def update(self):
        if self.clicked:
            # print("Painting clicked")
            if self.moved < self.max_move:
                self.rect.x -= 2
                self.moved += 1

    def onclick(self):
        if not self.clicked:
            self.clicked = True
            return Gear(self.pos, 'assets/ui/gear.png', self.screen, True)


class Gear(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug=False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 50))

    def update(self):
        if self.clicked:
            print("Clicked Gear")

    def onclick(self):
        if not self.clicked:
            self.clicked = True
            self.kill()
            return GearItem()
        # Need to give player aonother Gear
        # return Gear?(self.pos, 'assets/ui/gear.png', self.screen, True, )


class GearItem(Item):
    def __init__(self):
        Item.__init__(self, "Parts")
        self.name = "Parts"


class Chair(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug=False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)
        self.max_move = 40
        self.moved = 0

    def update(self):
        if self.clicked:
            if self.moved < self.max_move:
                self.rect.x -= 1
                self.rect.y -= 1
                self.moved += 1
        

    def onclick(self):
        if not self.clicked:
            self.clicked = True

            return Document((self.rect.right-75, self.rect.centery), 'assets/ui/folder.png', self.screen, True)


class Document(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug=False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, (50, 50))

    def update(self):
        if self.clicked:
            print("clicked, not closed")

    def onclick(self):
        if not self.clicked:
            self.clicked = True
            self.kill()
            return DocumentItem()


class DocumentItem(Item):
    def __init__(self):
        Item.__init__(self, "Folders")
        self.name = "Folders"


class Key(Interactable):
    def __init__(self, pos, image_path, screen, disappears, debug=False):
        Interactable.__init__(self, pos, image_path, screen, disappears, debug)

    def update(self):
        if self.clicked:
            print("Key clicked")
            # dissapear
            # add key to player inventory

    def onclick(self):
        self.clicked = True
