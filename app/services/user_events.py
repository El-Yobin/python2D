import pygame
import sys


class UserEvents:
    mouse_is_pressed = False
    mouse_drag = False
    mouse_drag_start_pos = None
    mouse_current_pos = None

    def update(self):
        self.update_events()
        self.update_mouse()

    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update_mouse(self):
        self.mouse_current_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed(3)[0]:
            self.mouse_is_pressed = True
            if not self.mouse_drag:
                self.mouse_drag = True
                self.mouse_drag_start_pos = pygame.mouse.get_pos()
        else:
            if self.mouse_is_pressed:
                self.mouse_is_pressed = False
            if self.mouse_drag:
                self.mouse_drag = False

