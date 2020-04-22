import pygame


class UI:
    def __init__(self, screen, player, debug=False):
        self.screen = screen
        self.player = player
        self.details = self.player.get_details()
        self.debug = debug
        self.black = (0, 0, 0, 100)
        self.surface = pygame.Surface((100, 1200), pygame.SRCALPHA)
        self.rect = pygame.Rect((0, 0), (100, 1200))
        self.font = pygame.font.Font('assets/fonts/Cheap_Pine_Sans.otf', 30)

        self.w, self.h = pygame.display.get_surface().get_size()
        self.folder_image = pygame.image.load('assets/ui/folder.png')
        self.gear_image = pygame.image.load('assets/ui/gear.png')
        self.key_image = pygame.image.load('assets/ui/key.png')
        self.note_image = pygame.image.load('assets/ui/note.png')

        self.folder_image = pygame.transform.smoothscale(
            self.folder_image, (60, 60))
        self.gear_image = pygame.transform.smoothscale(
            self.gear_image, (60, 60))
        self.key_image = pygame.transform.smoothscale(self.key_image, (60, 60))
        self.note_image = pygame.transform.smoothscale(
            self.note_image, (60, 60))

        self.folder_rect = self.folder_image.get_rect()
        self.gear_rect = self.gear_image.get_rect()
        self.key_rect = self.key_image.get_rect()
        self.note_rect = self.note_image.get_rect()

        self.folder_rect.centerx = 50
        self.gear_rect.centerx = 50
        self.key_rect.centerx = 50
        # self.note_rect.centerx = 50

        self.gear_rect.centery = self.h * (1/6)
        self.folder_rect.centery = self.h * (2/6)
        self.key_rect.centery = self.h * (1/2)

        # self.note_rect.centery = 50

    def update(self):
        self.details = self.player.get_details()

        pygame.display.update()

    def render(self):
        # Put transparent rectangle at side of screen,
        # pygame.draw.rect(Surface, color, Rect, width=0)
        pygame.draw.rect(self.surface, self.black, self.surface.get_rect())
        self.screen.blit(self.surface, (0, 0))
        self.screen.blit(self.gear_image, self.gear_rect)
        self.screen.blit(self.folder_image, self.folder_rect)
        self.screen.blit(self.key_image, self.key_rect)
        white = (255, 255, 255)
        parts_surface = self.font.render(
            f"{self.details['Parts']}/4", True, white)
        folders_surface = self.font.render(
            f"{self.details['Folders']}/3", True, white)
        keys_surface = self.font.render(str(self.details['Keys']), True, white)

        parts_rect = parts_surface.get_rect()
        folders_rect = folders_surface.get_rect()
        keys_rect = keys_surface.get_rect()
        parts_rect.center = (50, self.h * (1/6) + 50)
        folders_rect.center = (50, self.h * (2/6) + 50)
        keys_rect.center = (50, self.h * (3/6) + 50)

        self.screen.blit(parts_surface, parts_rect)
        self.screen.blit(folders_surface, folders_rect)
        self.screen.blit(keys_surface, keys_rect)

        floor_surface = self.font.render(f"Floor {self.details['Floor']}", True, white)
        floor_rect = floor_surface.get_rect()
        floor_rect.center = (50, 35)
        self.screen.blit(floor_surface, floor_rect)