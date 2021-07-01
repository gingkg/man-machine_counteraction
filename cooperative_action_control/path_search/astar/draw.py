import pygame
import time


def draw_map(grid, path, pacman, food):
    # 初始化pygame
    pygame.init()
    # Pygame窗口
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255, 255, 255))
    # 标题
    pygame.display.set_caption("吃豆人")
    keep_going = True
    RED = (255, 0, 0)  # 红色，使用RGB颜色， 代表吃豆人
    GREEN = (0, 255, 0)  # 绿色， 代表食物
    BLUE = (0, 0, 255)  # 蓝色， 代表起点
    BLACK = (0, 0, 0)  # 黑色， 墙
    WHITE = (255, 255, 255)  # 白色

    radius = 5  # 半径
    width = 100
    height = 100

    # 画地图
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].value == '%':
                pygame.draw.rect(screen, BLACK, ((j * 100, i * 100), (width, height)))
                # pygame.draw.rect(screen, WHITE, ((i * 100, j * 100), (width, height)), width=1)
            else:
                pygame.draw.rect(screen, BLACK, ((j * 100, i * 100), (width, height)), width=1)
    # 起始位置
    pygame.draw.rect(screen, BLUE, ((pacman[1] * 100, pacman[0] * 100), (width, height)))
    # 食物
    pygame.draw.rect(screen, GREEN, ((food[1] * 100, food[0] * 100), (width, height)))

    # 绘制吃豆人行走路径
    for k in range(len(path)):
        if k == 0:
            pygame.draw.circle(screen, RED, (path[k].point[1]*100+50, path[k].point[0]*100+50), 40)
        elif k == (len(path)-1):
            if k-1 != 0:
                pygame.draw.rect(screen, RED, ((path[k-1].point[1] * 100, path[k-1].point[0] * 100), (width, height)))
            pygame.draw.circle(screen, RED, (path[k].point[1] * 100 + 50, path[k].point[0] * 100 + 50), 40)
        else:
            if k-1 != 0:
                pygame.draw.rect(screen, RED, ((path[k-1].point[1] * 100, path[k-1].point[0] * 100), (width, height)))
            pygame.draw.circle(screen, RED, (path[k].point[1] * 100 + 50, path[k].point[0] * 100 + 50), 40)
        pygame.display.update()
        time.sleep(0.5)

    # 循环
    while keep_going:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_going = False

        # 退出程序
    pygame.quit()

