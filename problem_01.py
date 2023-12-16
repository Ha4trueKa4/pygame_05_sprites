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
    size = 400, 300
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Свой курсор мыши')

    # группа, содержащая все спрайты
    all_sprites = pygame.sprite.Group()
    arrow = pygame.sprite.Sprite(all_sprites)
    arrow.image = load_image('arrow.png')
    arrow.rect = arrow.image.get_rect()
    # создайте спрайт с картинкой arrow.png
    # и добавьте его в группу all_sprites

    # скрываем системный курсор
    pygame.mouse.set_visible(False)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEMOTION:
                arrow.rect.x = event.pos[0]
                arrow.rect.y = event.pos[1]

        screen.fill(pygame.Color("black"))
        if pygame.mouse.get_focused():
            all_sprites.draw(screen)
        # рисуем курсор только если он в пределах окна

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()