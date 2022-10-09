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
        self.img_human = pygame.image.load("ChildBase_Light.png").convert_alpha()    # 载入人物图片
        self.surf = self.img_human.subsurface((16, 0, 16, 32))                       # 裁剪人物图片
        self.rect = self.surf.get_rect(center=(400, 300))                            # 初始化定位人物中心位置
        self.rect = self.img_human.get_rect()
        self.rect2 = pygame.Rect(0, 0, self.rect.width // 3, self.rect.height // 4)


    def update(self, keys):
        n = 1
        if keys[pygame.K_LEFT]:
            self.surf = self.img_human.subsurface((16, 32, 16, 32))
            self.rect.move_ip((-3, 0))
        if keys[pygame.K_RIGHT]:
            self.surf = self.img_human.subsurface((16, 64, 16, 32))
            self.rect.move_ip((3, 0))
        if keys[pygame.K_UP]:
            self.surf = self.img_human.subsurface((16, 96, 16, 32))
            self.rect.move_ip((0, -3))
        if keys[pygame.K_DOWN]:
            self.surf = self.img_human.subsurface((16, 0, 16, 32))
            self.rect.move_ip((0, 3))

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
    pygame.init()                               # 初始化
    pygame.display.set_caption("Pygame_Demo")   # title
    win = pygame.display.set_mode((800, 600))   # 设置窗口大小
    clock = pygame.time.Clock()                 # 创建时钟对象

    bg = Bg()                                   # 绘制背景
    human = Human()                             # 绘制人物

    all_sprites = [bg, human]                   # 全部精灵
    running = True                              # 控制循环
    while running:                              # 开始循环
        for event in pygame.event.get():        # 捕捉事件
            if event.type == pygame.QUIT:       # 事件类型等于退出
                running = False                 # 则执行退出
        keys = pygame.key.get_pressed()         # 捕获键盘按钮
        human.update(keys)                      # 把按钮传给人物，更新动画

        for sprite in all_sprites:              # 遍历所有精灵
            win.blit(sprite.surf, sprite.rect)  # 窗口.绘制精灵

        clock.tick(30)                          # 设置每秒30帧
        pygame.display.flip()                   # 更新显示


if __name__ == '__main__':
    main()

