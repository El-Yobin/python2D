import pygame
from app.objects.object import GameObject


class Line(GameObject):

    def __init__(self, color, start, end):
        super().__init__()
        self.color = color
        self.start = start
        self.end = end

    def show(self):
        pygame.draw.line(self.display, self.color, self.start, self.end)
