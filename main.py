import pygame

pygame.init()


#関数=======================================================================================================================================================
# グリッド線の描画
def draw_grid():
    for i in range(square_num):
        # 横線
        pygame.draw.line(screen, BLACK, (0, i * square_size), (screen_width, i * square_size), 3)
        # 縦線
        pygame.draw.line(screen, BLACK, (i * square_size, 0), (i * square_size, screen_height), 3)

# 盤面の描画
def draw_board():
    for row_index, row in enumerate(board):
        for col_index, col in enumerate(row):
            if col == 1:
                pygame.draw.circle(screen, BLACK, (col_index * square_size + 50,  row_index * square_size + 50), 45)
            elif col == -1:
                pygame.draw.circle(screen, WHITE, (col_index * square_size + 50,  row_index * square_size + 50), 45)

# 石を置ける場所の取得
def get_validation_positions():
    valid_position_list = []
    for row in range(square_num):
        for col in range(square_num):
            # 石を置いてないマスのみチェック
            if board[row][col] == 0:
                for vx, vy in vec_table:
                    x = vx + col
                    y = vy + row
                    # マスの範囲内、かつプレイヤーの石と異なる石がある場合、その方向は引き続きチェック
                    if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                        while True:
                            x += vx
                            y += vy
                            # プレイヤーの石と異なる色の石がある場合、その方向は引き続きチェック
                            if 0 <= x < square_num and 0 <= y < square_num and board[y][x] == -player:
                                continue
                            # プレイヤーの石と同色の石がある場合、石を置けるためインデックスを保存
                            elif 0 <= x < square_num and 0 <= y < square_num and board[y][x] == player:
                                valid_position_list.append((col, row))
                                break
                            else:
                                break
    return valid_position_list



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

# 盤面(黒：１、白：－１)
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, -1, 1, 0, 0, 0],
    [0, 0, 0, 1, -1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# プレイヤー
player = 1 # １が黒番

vec_table = [
    (-1, -1),   # 左上
    (0, -1),     # 上
    (1, -1),    # 右上
    (-1, 0),    # 左
    (1, 0),     # 右
    (-1, 1),    # 左下
    (0, 1),     # 下
    (1, 1)      # 右下
]




#メインループ=============================================================================================================================================================================================
run = True
while run:

    # 背景の塗りつぶし
    screen.fill(GREEN)

    # グリッド線の描画
    draw_grid()

    # 盤面の描画
    draw_board()

    # 石を置ける場所の取得
    vaalid_position_list = get_validation_positions()

    # 石を置ける場所の取得
    for x, y in vaalid_position_list:
        pygame.draw.circle(screen, YELLOW, (x * square_size + 50,  y * square_size + 50), 45, 3)






    # イベントの取得
    for event in pygame.event.get():
        # print(type(event))
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        # マウスクリック
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            x = mx // square_size
            y = my // square_size
            if board[y][x] == 0 and (x, y) in vaalid_position_list:

                # 石をひっくり返す



                board[y][x] = player
                player *= -1

    # 更新
    pygame.display.update()
    clock.tick(FPS)

#=============================================================================================================================================================================================

pygame.quit()