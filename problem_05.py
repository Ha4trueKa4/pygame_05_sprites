import os
import pygame


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


def main():
    FPS = 120
    size = 600, 300
    speed = 200
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Game over!')
    clock = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    gameover = pygame.sprite.Sprite(all_sprites)
    gameover.image = load_image('gameover.png')
    gameover.rect = gameover.image.get_rect()
    gameover.rect.x = -gameover.rect.width

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color("blue"))
        if gameover.rect.x + speed / FPS <= 0:
            gameover.rect.x += speed / FPS
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()


if __name__ == '__main__':
    main()