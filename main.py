import os
import sys
import pygame


def load_image(name, colorkey=None, transform=None):
    fullname = os.path.join("data/", name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('эээ стрелочник')
    screen = pygame.display.set_mode((400, 400))
    running = True
    all_sprites = pygame.sprite.Group()
    cursor = pygame.sprite.Sprite()
    cursor.image = load_image("arrow (1).png")
    cursor.rect = cursor.image.get_rect()
    all_sprites.add(cursor)
    pygame.mouse.set_visible(False)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if pygame.mouse.get_focused():
            x, y = pygame.mouse.get_pos()
            cursor.rect.x = x
            cursor.rect.y = y
            all_sprites.draw(screen)
        pygame.display.flip()
        screen.fill((0, 0, 0))
