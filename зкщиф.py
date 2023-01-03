# import time
# import pygame
#
#
# pygame.init()
# window = pygame.display.set_mode((800, 800))
# screen = pygame.Surface((800, 800))
# COLOR_INACTIVE = pygame.Color('lightskyblue3')
# COLOR_ACTIVE = pygame.Color('dodgerblue2')
# COLOR_HOVER = pygame.Color('deepskyblue')
# reg_txt = pygame.font.Font('../fonts/algerian.ttf', 32)
#
# class InputBox:
#
#     def __init__(self, x, y, w, h, text=''):
#         self.rect = pygame.Rect(x, y, w, h)
#         self.color = COLOR_INACTIVE
#         self.text = text
#         self.txt_surface = reg_txt.render(text, True, self.color)
#         self.active = False
#
#     def handle_event(self, e):
#         if e.type == pygame.MOUSEBUTTONDOWN:
#             if self.rect.collidepoint(e.pos):
#                 self.active = not self.active
#             else:
#                 self.active = False
#             self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
#         if e.type == pygame.KEYDOWN:
#             if self.active:
#                 if e.key == pygame.K_RETURN:
#                     print(self.text)
#                     self.text = ''
#                 elif e.key == pygame.K_BACKSPACE:
#                     self.text = self.text[:-1]
#                 else:
#                     self.text += e.unicode
#                 self.txt_surface = reg_txt.render(self.text, True, self.color)
#
#     def update(self):
#         width = max(200, self.txt_surface.get_width()+10)
#         self.rect.w = width
#
#     def draw(self, screen):
#         screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
#         pygame.draw.rect(screen, self.color, self.rect, 2)
#
#
#
# def main():
#     clock = pygame.time.Clock()
#     input_box1 = InputBox(100, 100, 140, 32)
#     input_box2 = InputBox(100, 300, 140, 32)
#     input_boxes = [input_box1, input_box2]
#     done = False
#
#     while not done:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 done = True
#             for box in input_boxes:
#                 box.handle_event(event)
#
#         for box in input_boxes:
#             box.update()
#
#         window.blit(screen, (0, 0))
#         screen.fill((30, 30, 30))
#         for box in input_boxes:
#             box.draw(screen)
#
#         pygame.display.flip()
#         clock.tick(60)
#
#
# if __name__ == '__main__':
#     main()
#     pygame.quit()

import googletrans
# from googletrans import Translator
# t = Translator()
# txt = t.translate("Hello", dest="ru")
# print(txt.text)
# print(round((1 - 10) / 2))
# print("Универсальное(1d8)".replace("Универсальное(", "").replace(")", ""))
import random
# a = 5
# print(int(a))

# roll_answer = 0
# for coco in range(2):
#     roll_answer += random.randint(1, 6)
# print(roll_answer)
#
# import socket
# h_name = socket.gethostname()
# IP_addres = socket.gethostbyname(h_name)
# print("Host Name is: " + h_name)
# print("Computer IP Address is: " + IP_addres)

# with open('test.txt', errors='ignore', encoding="utf-8") as fin, open('test.out', "w", encoding="utf-8") as fout:
#     for line in fin:
        # fout.write('{0}{1}\n'.format(line.rstrip('\n'), '<br>'))

# with open('draconic.txt', errors='ignore', encoding="utf-8") as fin, open('draconic.out', "w", encoding="utf-8") as fout:
#     for line in fin:
#         # line = line.replace("’", "'")
#         # line = line.replace("‘", "'")
#         # line = line.replace("’", "'")
#         # line = line.replace("вЂ™", "'")
#         line = line.split()
#         fout.write('{0} {1}\n'.format(line[0], line[1]))
#
import hashlib

print(hashlib.sha1(b'jojosus22NIlYDEYUMTLgSOXRbDkP').hexdigest())

# import pygame
#
# image = pygame.image.load('unknown.png')
#
# print(image.get_width(), image.get_height())
# def resize(img, percent):
#     size_x = img.get_width() / 100 * percent
#     size_y = img.get_height() / 100 * percent
#     return pygame.transform.scale(img, (size_x, size_y))
# print(image.get_width(), image.get_height())

map_parts = 544


map = ''
while map_parts != 0:
    map_select_part = random.randint(1, 6)
    if map_select_part == 1:
        map += 'B'
        map_parts -= 1
    elif map_select_part == 2:
        map += 'O'
        map_parts -= 1
    elif map_select_part == 3:
        map += 'L'
        map_parts -= 1
    elif map_select_part == 4:
        map += 'R'
        map_parts -= 1
    elif map_select_part == 5:
        map += 'T'
        map_parts -= 1
    elif map_select_part == 6:
        map += 'U'
        map_parts -= 1

import pygame

class Sprite:
    def __init__(self, x, y, img, width, height):
        self.x = x
        self.y = y
        self.original_img = pygame.image.load(img).convert_alpha()
        self.img = self.original_img
        self.angle = 0
        self.w = width
        self.h = height

    def render(self, pov):
        pov.blit(self.img, (self.x, self.y))

    def rotate(self, perc):
        self.img = pygame.transform.rotate(self.original_img, self.angle)
        self.angle += perc % 360

pygame.init()
window = pygame.display.set_mode((1920, 1025))
screen = pygame.Surface((1920, 1025))
reg_txt = pygame.font.Font('../fonts/algerian.ttf', 32)

x = 1
y = 1
part_col = 0

parts = []

print(map)

for img in map:
    if img == 'B':
        part = Sprite(x, y, "C:/Users/dgsiz/PycharmProjects/Dungeons & Dragons/images/backgrounds/game/forest/B.png", 59, 59)
    elif img == 'O':
        part = Sprite(x, y, "C:/Users/dgsiz/PycharmProjects/Dungeons & Dragons/images/backgrounds/game/forest/O.jpg", 59, 59)
    if img == 'L':
        part = Sprite(x, y, "C:/Users/dgsiz/PycharmProjects/Dungeons & Dragons/images/backgrounds/game/forest/L.jpg", 59, 59)
    if img == 'R':
        part = Sprite(x, y, "C:/Users/dgsiz/PycharmProjects/Dungeons & Dragons/images/backgrounds/game/forest/R.jpg", 59, 59)
    if img == 'T':
        part = Sprite(x, y, "C:/Users/dgsiz/PycharmProjects/Dungeons & Dragons/images/backgrounds/game/forest/T.jpg", 59, 59)
    if img == 'U':
        part = Sprite(x, y, "C:/Users/dgsiz/PycharmProjects/Dungeons & Dragons/images/backgrounds/game/forest/U.jpg", 59, 59)
    part_col += 1
    if part_col % 32 == 0:
        x = 1
        y += 60
    else:
        x += 60
    parts.append(part)



def p(o1, o2):
    if not (o2.x > o1.x + o1.w or o1.x > o2.x + o2.w or o2.y > o1.y + o1.h or o1.y > o2.y + o2.h):
        return True
    else:
        return False
def mp(o1):
    pos = pygame.mouse.get_pos()
    if not (pos[0] > o1.x + o1.w or pos[1] > o1.y + o1.h or pos[0] < o1.x or pos[1] < o1.y):
        return True
    else:
        return False

def move(angle, x, y, player):
    if angle == 'left':
        x -= 1
        for part in parts:
            if p(part, player):
                if map[parts.index(part) - 1] == 'B':
                    x += 1
    if angle == 'right':
        x += 1
        for part in parts:
            if p(part, player):
                if map[parts.index(part) + 1] == 'B':
                    x -= 1
    if angle == 'top':
        y -= 1
        for part in parts:
            if p(part, player):
                if map[parts.index(part) - 32] == 'B':
                    y += 1
    if angle == 'under':
        y += 1
        for part in parts:
            if p(part, player):
                if map[parts.index(part) + 32] == 'B':
                    y -= 1
    return x, y

def main():
    clock = pygame.time.Clock()
    done = False
    speed = 6
    pl_x = 0
    pl_z = 0
    pl = Sprite(pl_x, pl_z, "C:/Users/dgsiz/PycharmProjects/Dungeons & Dragons/images/characters/hendalf.png", 59, 59)

    while not done:
        pl.x = pl_x * 60 + 1
        pl.y = pl_z * 60 + 1
        pl.render(screen)

        for gor in range(18):
            pygame.draw.line(screen, 'black', (0, gor * 60), (1920, gor * 60))
        for vert in range(32):
            pygame.draw.line(screen, 'black', (vert * 60, 0), (vert * 60, 1080))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                for part in parts:
                    if mp(part):
                        if map[parts.index(part)] != 'B':
                            if event.key == pygame.K_d:
                                pl_x, pl_z = move('right', pl_x, pl_z, pl)
                            if event.key == pygame.K_a:
                                pl_x, pl_z = move('left', pl_x, pl_z, pl)
                            if event.key == pygame.K_s:
                                pl_x, pl_z = move('under', pl_x, pl_z, pl)
                            if event.key == pygame.K_w:
                                pl_x, pl_z = move('top', pl_x, pl_z, pl)

        window.blit(screen, (0, 0))
        screen.fill((30, 30, 30))

        pygame.display.flip()
        clock.tick(60)

        for part in parts:
            part.render(screen)
                # print('not ok')


if __name__ == '__main__':
    main()
    pygame.quit()
