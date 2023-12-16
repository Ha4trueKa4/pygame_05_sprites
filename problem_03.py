import os

import pygame
size = 600, 95
screen = pygame.display.set_mode(size)


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname).convert()
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)

    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Car(pygame.sprite.Sprite):
    image = load_image("car.png", "Black")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.screensize = size
        self.image = Car.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.going_right = True
        self.dist = 5

    def update(self, *args):
        if self.going_right and self.rect.right == self.screensize[0]:
            self.going_right = False
            self.image = pygame.transform.flip(self.image, True, False)
        elif not self.going_right and self.rect.left == 0:
            self.going_right = True
            self.image = pygame.transform.flip(self.image, True, False)

        if self.going_right:
            dx = self.dist
            dy = 0
            self.rect = self.rect.move(dx, dy)
        else:
            dx = -self.dist
            dy = 0
            self.rect = self.rect.move(dx, dy)


def main():
    FPS = 60
    clock = pygame.time.Clock()

    pygame.display.set_caption('Машинка едет!')

    all_sprites = pygame.sprite.Group()
    _ = Car(all_sprites, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(pygame.Color("white"))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()
