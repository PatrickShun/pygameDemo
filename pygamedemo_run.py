# coding:utf-8

import pygame


class Main(object):
    def __init__(self, title, height, width, Fps=60):
        self.height = height
        self.width = width
        self.title = title
        self.Fps = Fps
        self.main()
        self.vars()
        self.events()

    def main(self):
        pygame.init()                               # 初始化pygame
        pygame.mixer.init()                         # 背景音乐初始化
        pygame.display.set_caption(self.title)      # 设置窗口标题
        self.screen = pygame.display.set_mode([self.height, self.width])  # 将屏幕赋值为全局变量方便调用


    def events(self):
        pygame.mixer.music.play(-1, 0)              # 播放背景音乐（-1是循环播放，0是从0秒开始播放）
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            # 将背景图片载入到窗口0，0的位置。
            self.screen.blit(self.New_Default_Background_Pic, (0, 0))
            # 刷新背景（如果不刷新屏幕就不更新）
            pygame.display.update()

    def vars(self):
        # 导入图片；
        self.Old_Default_Background_Pic = pygame.image.load("bg_page.jpg")
        # 将图片缩放到与窗口一样大；
        self.New_Default_Background_Pic = pygame.transform.scale(self.Old_Default_Background_Pic, (self.height, self.width))
        pygame.image.load("bg_page.jpg")
        self.Old_Default_Background_Music = pygame.mixer.music.load("rainy-season.mp3")


if __name__ == "__main__":
    Main("Pixel World", 1280, 768)


