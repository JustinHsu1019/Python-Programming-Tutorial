import pygame
import sys

# 初始化 Pygame
pygame.init()

# 設定窗口大小
window_size = (360, 640)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("PyGame 小遊戲")

# 定義顏色
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# 紅色長方形的屬性
rect_width = 100  # 長方形的寬度
rect_height = 40  # 長方形的高度
rect_x = (window_size[0] - rect_width) / 2  # 初始X位置，使長方形居中
rect_y = 600 - rect_height  # 初始Y位置，使長方形底部恰好在黑線上
rect_speed = 5

# 物理參數
gravity = 0.5
jump_speed = -10
vertical_speed = 0

# 主循環
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 鍵盤輸入處理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rect_x > 0:
        rect_x -= rect_speed
    if keys[pygame.K_RIGHT] and rect_x < window_size[0] - rect_width:
        rect_x += rect_speed
    if keys[pygame.K_UP] and rect_y >= 600 - rect_height:
        vertical_speed = jump_speed

    # 更新長方形位置
    vertical_speed += gravity
    rect_y += vertical_speed
    if rect_y > 600 - rect_height:
        rect_y = 600 - rect_height
        vertical_speed = 0

    # 繪製
    screen.fill((255, 255, 255))  # 用白色填充窗口
    pygame.draw.line(screen, BLACK, (0, 600), (window_size[0], 600), 2)  # 繪製黑線
    pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))  # 繪製紅色長方形
    pygame.display.flip()

    # 控制遊戲更新速度
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
