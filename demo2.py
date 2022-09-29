import pygame


class Bg(pygame.sprite.Sprite):
    def __init__(self):
        super(Bg, self).__init__()
        bg_small = pygame.image.load("bg.png").convert_alpha()
        grass_land = bg_small.subsurface((0, 0, 128, 128))
        self.surf = pygame.transform.scale(grass_land, (800, 600))
        self.rect = self.surf.get_rect(left=0, top=0)  # 左上角


class Human(pygame.sprite.Sprite):
    def __init__(self):
        super(Human, self).__init__()
        img_human = pygame.image.load("ChildBase_Light.png").convert_alpha()
        self.surf = img_human.subsurface((0, 0, 16, 40))
        self.surf = img_human.subsurface((0, 0, 16, 40))
        self.surf = img_human.subsurface((0, 0, 16, 40))
        self.surf = img_human.subsurface((0, 0, 16, 40))
        self.rect = self.surf.get_rect(center=(400, 300))  # 中心位置

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.rect.move_ip((-2, 0))
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip((2, 0))
        if keys[pygame.K_UP]:
            self.rect.move_ip((0, -2))
        if keys[pygame.K_DOWN]:
            self.rect.move_ip((0, 2))
        # 防止跑出界面
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600

def main():
    pygame.init()
    pygame.display.set_caption("Pygame_Demo")
    win = pygame.display.set_mode((800, 600))

    bg = Bg()
    human = Human()

    all_sprites = [bg, human]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        human.update(keys)

        for sprite in all_sprites:
            win.blit(sprite.surf, sprite.rect)

        pygame.display.flip()


if __name__ == '__main__':
    main()

