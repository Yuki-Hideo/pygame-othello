import pygame

pygame.init()


#関数=======================================================================================================================================================
def draw_grid():
    # グリッド線の描画
    for i in range(square_num):
        # 横線
        pygame.draw.line(screen, BLACK, (0, i * square_size), (screen_width, i * square_size), 3)
        # 縦線
        pygame.draw.line(screen, BLACK, (i * square_size, 0), (i * square_size, screen_height), 3)



#=======================================================================================================================================================
# create window
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("オセロ")

# マスの設定
square_num = 8
square_size = screen_width // square_num

# fpsの設定
FPS = 60
clock = pygame.time.Clock()

# 色の設定
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


#メインループ=============================================================================================================================================================================================
run = True
while run:

    # 背景の塗りつぶし
    screen.fill(GREEN)

    # グリッド線の描画
    draw_grid()


    # イベントの取得
    for event in pygame.event.get():
        # print(type(event))
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    # 更新
    pygame.display.update()
    clock.tick(FPS)

#=============================================================================================================================================================================================

pygame.quit()