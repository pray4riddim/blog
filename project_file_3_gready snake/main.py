import pygame
import random

# 初始化pygame
pygame.init()

# 设置窗口大小和标题
window_width = 960
window_height = 720
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇游戏")

# 加载贴图资源
background_image = pygame.image.load("background.png").convert()
snake_head_image = pygame.image.load("head.png").convert_alpha()
snake_body_image = pygame.image.load("body.png").convert_alpha()
food_image = pygame.image.load("food.png").convert_alpha()
start_button_image = pygame.image.load("start_button.png").convert_alpha()
history_button_image = pygame.image.load("history_button.png").convert_alpha()
quit_button_image = pygame.image.load("quit_button.png").convert_alpha()

# 定义游戏参数
snake_head_size = 60
snake_speed = 10

# 定义蛇类
class Snake:
    def __init__(self, head_image, body_image):
        self.head_image = pygame.transform.scale(head_image, (snake_head_size, snake_head_size))
        self.body_image = pygame.transform.scale(body_image, (snake_head_size, snake_head_size))
        self.head_direction = "right"
        self.body = [(5, 5), (4, 5), (3, 5)]  # 初始蛇身位置
        self.food = self.generate_food()  # 生成初始食物位置

    def update(self):
        # 获取按键事件
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_UP] and self.head_direction != "down":
            self.head_direction = "up"
        elif pressed_keys[pygame.K_DOWN] and self.head_direction != "up":
            self.head_direction = "down"
        elif pressed_keys[pygame.K_LEFT] and self.head_direction != "right":
            self.head_direction = "left"
        elif pressed_keys[pygame.K_RIGHT] and self.head_direction != "left":
            self.head_direction = "right"

        # 移动蛇头
        head_x, head_y = self.body[0]
        if self.head_direction == "up":
            head_y -= 1
        elif self.head_direction == "down":
            head_y += 1
        elif self.head_direction == "left":
            head_x -= 1
        elif self.head_direction == "right":
            head_x += 1

        self.body.insert(0, (head_x, head_y))  # 在蛇头前插入新的蛇身坐标
        self.body.pop()  # 删除蛇尾，实现移动效果

        # 检查是否吃到食物
        if self.body[0] == self.food:
            self.body.append(self.body[-1])  # 食物被吃掉后，蛇身增加一个单位
            self.food = self.generate_food()  # 生成新的食物位置

    def generate_food(self):
        while True:
            x = random.randint(0, window_width // snake_head_size - 1)
            y = random.randint(0, window_height // snake_head_size - 1)
            if (x, y) not in self.body:
                return x, y

    def draw(self, screen):
        # 绘制蛇身
        for segment in self.body:
            x, y = segment
            if segment == self.body[0]:
                screen.blit(self.head_image, (x * snake_head_size, y * snake_head_size))
            else:
                screen.blit(self.body_image, (x * snake_head_size, y * snake_head_size))

        # 绘制食物
        x, y = self.food
        screen.blit(food_image, (x * snake_head_size, y * snake_head_size))

class Button:
    def __init__(self, image, x, y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# 创建菜单按钮
start_button = Button(start_button_image, window_width // 2, window_height // 2 - 50)
history_button = Button(history_button_image, window_width // 2, window_height // 2)
quit_button = Button(quit_button_image, window_width // 2, window_height // 2 + 50)

# 游戏循环
running = True
menu = True
clock = pygame.time.Clock()
snake = Snake(snake_head_image, snake_body_image)  # 创建蛇对象

while running:
    clock.tick(snake_speed)  # 控制游戏帧率

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and menu:
            mouse_pos = pygame.mouse.get_pos()
            if start_button.is_clicked(mouse_pos):
                menu = False
            elif history_button.is_clicked(mouse_pos):
                print("打开历史记录")  # 在此处添加打开历史记录的逻辑
            elif quit_button.is_clicked(mouse_pos):
                running = False

    if menu:
        # 绘制菜单背景和按钮
        screen.blit(background_image, (0, 0))
        screen.blit(start_button.image, start_button.rect)
        screen.blit(history_button.image, history_button.rect)
        screen.blit(quit_button.image, quit_button.rect)
    else:
        # 游戏逻辑
        screen.blit(background_image, (0, 0))
        snake.update()  # 更新蛇的状态
        snake.draw(screen)  # 绘制蛇的图像

    pygame.display.flip()

pygame.quit()
