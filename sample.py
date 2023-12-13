import os
import random
import pygame


size = width, height = 800, 600
screen = pygame.display.set_mode(size)


def load_image(name, color_key=None):
    path = os.path.join("data", name)
    if not os.path.isfile(path):
        raise ValueError(f"Файл {path} не найден")
    image = pygame.image.load(path)
    if color_key is not None:
        if color_key == -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    else:
        image = image.convert_alpha()
    return image


class Bomb(pygame.sprite.Sprite):
    image = load_image("bomb.png")
    image_boom = load_image("boom.png")

    def __init__(self, group, x, y):
        super().__init__(group)
        self.image = Bomb.image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, *args):
        if self.image != Bomb.image_boom:
            dx = random.randrange(3) - 1
            dy = random.randrange(3) - 1
            self.rect = self.rect.move(dx, dy)
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.image = Bomb.image_boom


def main():
    all_sprites = pygame.sprite.Group()

    for _ in range(20):
        _ = Bomb(all_sprites, random.randrange(width), random.randrange(height))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                all_sprites.update(event)

        screen.fill(pygame.Color("white"))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
