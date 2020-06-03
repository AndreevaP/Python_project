from logic import *
import pygame
import sys


def draw_interface(score, delta=0):
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font = pygame.font.SysFont("stxingkai", 70)  # шрифт
    font_score = pygame.font.SysFont("simsun", 48)
    font_delta = pygame.font.SysFont("simsun", 32)
    text_score = font_score.render("Score:", True, COLORS_TEXT)
    text_score_value = font_score.render(f"{score}", True, COLORS_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (175, 35))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, COLORS_TEXT)
        screen.blit(text_delta, (170, 65))
        pretty_print(mas)
    for row in range(BLOCKS):
        for column in range(BLOCKS):
            value = mas[row][column]
            text = font.render(f'{value}', True, BLACK)
            w = column * SIZE_BLOCK + (column + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))
            if value != 0:
                font_w, font_h = text.get_size()  # вычисляем размер текста
                text_x = w + (SIZE_BLOCK - font_w) / 2
                text_y = h + (SIZE_BLOCK - font_h) / 2
                screen.blit(text, (text_x, text_y))  # к экрану прикрепляем наш найденный текст


mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
COLORS_TEXT = (255, 127, 0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 0),
    16: (255, 235, 255),
    32: (255, 235, 128),
    64: (255, 235, 0),
    128: (255, 215, 255),
    256: (255, 215, 128),
    512: (255, 215, 0),
    1024: (255, 195, 255),
    2048: (255, 195, 128)
}

WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS + 1) * MARGIN
HEIGTH = WIDTH + 110
TITLE_REC = pygame.Rect(0, 0, WIDTH, 110)
score = 0

mas[1][2] = 2
mas[3][0] = 4
print(get_empty_list(mas))
pretty_print(mas)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption("2048")


def draw_intro():
    img2028 = pygame.image.load('og_image.png')
    a = 0
    font = pygame.font.SysFont("stxingkai", 90)  # шрифт
    text_welcome = font.render("Welcome!", True, WHITE)
    font_b = pygame.font.SysFont("stxingkai", 30)  # шрифт
    text_begin = font_b.render("Нажмите Enter для начала игры", True, WHITE)
    pressbutton = False
    while not pressbutton:
        for event in pygame.event.get():  # обработчик событий
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                a = 0
                if event.key == pygame.K_RETURN:
                    pressbutton = True
                break
        screen.blit(pygame.transform.scale(img2028, [470, 575]), [10, 10])
        screen.blit(text_welcome, (100, 100))
        screen.blit(text_begin, (90, 500))
        pygame.display.update()
    screen.fill(BLACK)


def draw_game_over():
    img2028 = pygame.image.load('12.jpg')
    font = pygame.font.SysFont("stxingkai", 90)  # шрифт
    text_game_over = font.render("Game over!", True, WHITE)
    while True:
        for event in pygame.event.get():  # обработчик событий
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        screen.fill(BLACK)
        screen.blit(pygame.transform.scale(img2028, [470, 570]), [10, 10])
        screen.blit(text_game_over, (70, 100))
        pygame.display.update()


draw_intro()
draw_interface(score)
pygame.display.update()
while is_zero_in_mas(mas) or can_move(mas):  # условие продолжения игры
    for event in pygame.event.get():  # обработчик событий
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)  # окно закроется
        elif event.type == pygame.KEYDOWN:
            delta = 0
            if event.key == pygame.K_LEFT:
                mas, delta = move_left(mas)
            elif event.key == pygame.K_RIGHT:
                mas, delta = move_right(mas)
            elif event.key == pygame.K_UP:
                mas, delta = move_up(mas)
            elif event.key == pygame.K_DOWN:
                mas, delta = move_down(mas)
            score += delta
            if is_zero_in_mas(mas):
                empty = get_empty_list(mas)
                random.shuffle(empty)
                random_num = empty.pop()
                x, y = get_index_from_number(random_num)
                mas = insert_2_or_4(mas, x, y)
                print(f'Мы запомнили элемент под номером {random_num}')
            draw_interface(score, delta)
            pygame.display.update()
draw_game_over()
