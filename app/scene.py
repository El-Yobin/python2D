import pygame
from app.services.user_events import UserEvents
from app.objects.line import Line
from instances import get_display


class Scene:
    def __init__(self):
        self.display = get_display()
        self.line_is_drawing = False
        self.temporary_line = None
        self.events = UserEvents()
        self.lines = []

    def update(self):
        self.events.update()
        self.check_for_drawing()

    def show(self):
        self.display.fill("#000000")
        self.show_lines()
        if self.line_is_drawing:
            self.draw_temporary_line()

        pygame.display.update()

    def draw_temporary_line(self):
        self.temporary_line = Line(
            "#FFFFFF",
            self.events.mouse_drag_start_pos,
            self.events.mouse_current_pos
        )
        self.temporary_line.show()

    def show_lines(self):
        for line in self.lines:
            line.show()

    def check_for_drawing(self):
        if self.events.mouse_drag:
            self.line_is_drawing = True
        elif self.line_is_drawing:
            self.line_is_drawing = False
            self.lines.append(self.temporary_line)
