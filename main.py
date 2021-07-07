import pygame
from app.scene import Scene
from instances import set_display

pygame.init()
set_display(pygame.display.set_mode((800, 600)))
scene = Scene()


def run():
    while True:
        scene.update()
        scene.show()


if __name__ == '__main__':
    run()
