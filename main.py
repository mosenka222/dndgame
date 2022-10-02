import random
import pygame
import time
import mysql.connector
import socket
import requests
import hashlib

window = pygame.display.set_mode((1920, 1025), pygame.RESIZABLE)
WIDTH = window.get_width()
HEIGHT = window.get_height()
pygame.display.set_caption("Dungeons & Dragons", )
pygame.display.set_icon(pygame.image.load("images/icon.png"))
screen = pygame.Surface((1920, 1025))
icon_surf = pygame.image.load("images/icon.png")
screen.blit(icon_surf, (0, 0))
screen.get_width()
game = True
disconnect = False

# иниты
pygame.init()
clock = pygame.time.Clock()
FPS = 100

# текст
inp_txt = pygame.font.Font(None, 32)
error_txt = pygame.font.Font(None, 32)
title_txt = pygame.font.Font('fonts/algerian.ttf', 300)
characters_txt = pygame.font.Font(None, 50)
disconnect_txt = pygame.font.Font('fonts/algerian.ttf', 50)
disconnect_error_txt = pygame.font.Font('fonts/algerian.ttf', 25)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = inp_txt.render(text, True, self.color)
        self.active = False

    def handle_event(self, e):
        if e.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(e.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if e.type == pygame.KEYDOWN:
            if self.active:
                # if e.key == pygame.K_RETURN:
                #     print(self.text)
                #     self.text = ''
                if e.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += e.unicode
                self.txt_surface = inp_txt.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

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

def make_perec():
    result = ''
    symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    for sym in range(20):
        result += symbols[random.randint(0, 40)]
    return result

def con_roll(count, dice):
    roll_answer = 0
    for coco in range(count):
        roll_answer += random.randint(1, dice)
    return roll_answer

# буллевые переменные
menu = True
options = False
register = False
continue_screen = False
continue_touched = False
char_selector = False
mygame = False


wifitesturl = "https://google.com"
timeout = 5
try:
    request = requests.get(wifitesturl, timeout=timeout)
except (requests.ConnectionError, requests.Timeout) as exception:
    disconnect = True
    print("ok")

# цвета
disconnect_button_color = 'lightskyblue3'
back_button_color = 'deepskyblue'
reg_button_color = 'dodgerblue'
reg_button_color1 = 'dodgerblue2'
reg_button_color2 = 'dodgerblue2'
reg_button_color3 = 'dodgerblue2'
reg_button_color4 = 'dodgerblue2'
reg_button_color5 = 'dodgerblue2'
COLOR_INACTIVE = pygame.Color('lightskyblue3')
COLOR_ACTIVE = pygame.Color('dodgerblue2')
COLOR_HOVER = pygame.Color('deepskyblue')
background_color2 = (30, 30, 30)
new_char_color = COLOR_HOVER

# инпуты
input_box1 = InputBox(500, 250, 840, 32)
input_box2 = InputBox(500, 350, 840, 32)
input_box3 = InputBox(500, 450, 840, 32)
input_boxes = [input_box1, input_box2, input_box3]

# спрайты
disconnect_void = Sprite(878.5, 550, "images/void.png", 162.5, 50)
planks1 = Sprite(625, 345, "images/backgrounds/planks.png", 0, 0)
planks2 = Sprite(660, 400, "images/backgrounds/planks2.png", 0, 0)
planks3 = Sprite(625, 650, "images/backgrounds/planks.png", 0, 0)
planks4 = Sprite(1180, 400, "images/backgrounds/planks2.png", 0, 0)
string1 = Sprite(685, 0, "images/backgrounds/string.png", 0, 0)
string2 = Sprite(1180, 0, "images/backgrounds/string.png", 0, 0)
background = Sprite(0, 0, "images/backgrounds/menu_screen.png", 0, 0)
new_game_but = Sprite(600, 100, "images/buttons/menu/new_game.png", 275, 64)
continue_but = Sprite(600, 200, "images/buttons/menu/continue.png", 275, 64)

options_but = Sprite(600, 300, "images/buttons/menu/options.png", 275, 64)
music_plus_but = Sprite(750, 205, "images/options/up_arrow.png", 16, 16)
music_minus_but = Sprite(750, 285, "images/options/down_arrow.png", 16, 16)
sounds_plus_but = Sprite(750, 315, "images/options/up_arrow.png", 16, 16)
sounds_minus_but = Sprite(750, 395, "images/options/down_arrow.png", 16, 16)

titles_but = Sprite(600, 400, "images/buttons/menu/titles.png", 275, 64)
back_void = Sprite(100, 100, "images/void.png", 100, 100)
back_button = Sprite(116, 116, "images/buttons/reg_log/back_button.png", 64, 64)
reg_void = Sprite(500, 490, "images/void.png", 250, 50)
login_void = Sprite(500, 400, "images/void.png", 250, 50)

# музыка
pygame.mixer.music.load("musiс/theme.mp3")
pygame.mixer.music.load("musiс/char_builder_open.mp3")

theme = pygame.mixer.Sound('musiс/theme.mp3')
theme_played = False
char_builder_start = pygame.mixer.Sound("musiс/char_builder_open.mp3")
char_builder_start_played = False

# переменные
user = ''
username = ''
file = open("code/user.txt", "r")
user = str(file.read())
file.close()
for_count = 0
version = 'Alpha_1.0'
settings = open("code/settings.txt", "r")
musiс_set = settings.read().split("\n")
music = float(musiс_set[0])
sounds = float(musiс_set[1])
char_builder_loading = 0
characters = []
character_buts = []

# картинки
menu_background_img = pygame.image.load("images/backgrounds/menu_screen.png").convert_alpha()
new_game_but_hover_img = pygame.image.load("images/buttons/menu/new_game2.png").convert_alpha()
new_game_but_img = pygame.image.load("images/buttons/menu/new_game.png").convert_alpha()
continue_but_hover_img = pygame.image.load("images/buttons/menu/continue2.png").convert_alpha()
continue_but_img = pygame.image.load("images/buttons/menu/continue.png").convert_alpha()
options_but_hover_img = pygame.image.load("images/buttons/menu/options2.png").convert_alpha()
options_but_img = pygame.image.load("images/buttons/menu/options.png").convert_alpha()
titles_but_hover_img = pygame.image.load("images/buttons/menu/titles2.png").convert_alpha()
titles_but_img = pygame.image.load("images/buttons/menu/titles.png").convert_alpha()
forest_bg =

if not disconnect:
    try:
        cnx = mysql.connector.connect(user='root', password="root",
                                        host='localhost',
                                        database='database')
        cursor = cnx.cursor()
    except:
        disconnect = True

try:
    characters_ids = []
    cursor.execute("SELECT character_id, character_name, character_surname FROM characters WHERE character_owner_id = " + user)
    all_chars = []
    for all_char in cursor:
        all_chars.append(str(all_char[1] + " " + all_char[2]))
    cnx.commit()
except:
    pass

try:
    cursor.execute("SELECT player_mail FROM players WHERE player_id = " + user)
    for user_mail1 in cursor:
        user_mail = user_mail1[0]
except:
    pass

while game:

    # pygame.mouse.set_cursor(*pygame.cursors.diamond) romb
    # pygame.mouse.set_cursor(*pygame.cursors.broken_x) x
    # pygame.mouse.set_cursor(*pygame.cursors.ball) sphere


    # cursor.execute("UPDATE players SET player_progress = 'test' WHERE player_id = 5")

    # cnx.commit()
    #
    # query = ("SELECT player_name FROM players")
    # cursor.execute(query)
    # for (player_name) in cursor:
    #     print((player_name[0]))

    if register or continue_screen:
        pygame.key.set_repeat(0, 0)
    else:
        pygame.key.set_repeat(1, 1)

    if disconnect:
        background.img = pygame.image.load("images/backgrounds/tavern.jpg").convert_alpha()
        background.render(screen)
        if mp(disconnect_void):
            disconnect_button_color = COLOR_ACTIVE
        else:
            disconnect_button_color = COLOR_INACTIVE
        string1.render(screen)
        string2.render(screen)
        pygame.draw.rect(screen, 'dimgray', (735, 415, 450, 250))
        screen.blit(disconnect_error_txt.render(("Проблема с сетью!"), 1, COLOR_INACTIVE), (819.315, 425))
        screen.blit(disconnect_error_txt.render(("Поробуйте включить интернет"), 1, COLOR_INACTIVE), (740.25, 450))
        screen.blit(disconnect_error_txt.render(("и"), 1, COLOR_INACTIVE), (943.75, 475))
        screen.blit(disconnect_error_txt.render(("Пререподключиться"), 1, COLOR_INACTIVE), (825.5, 500))
        screen.blit(disconnect_txt.render(("ВЫЙТИ"), 1, disconnect_button_color), (878.75, 550))
        planks2.render(screen)
        planks4.render(screen)
        planks1.render(screen)
        planks3.render(screen)

    # if not disconnect:
        # data = player_socket.recv(1024)
        # data = data.decode()
        # print(data)

    pygame.mixer.Sound.set_volume(theme, music)
    pygame.mixer.Sound.set_volume(char_builder_start, music)

    if menu and not disconnect:
        if not theme_played:
            pygame.mixer.Sound.play(theme)
            theme_played = True
        background.img = menu_background_img
        background.render(screen)
        new_game_but.render(screen)
        continue_but.render(screen)
        options_but.render(screen)
        titles_but.render(screen)
        screen.blit(title_txt.render(("D&D"), 1, 'red'), (1250, 225))
        screen.blit(error_txt.render(("Version: " + version), 1, 'white'), (0, 0))
        if mp(new_game_but):
            new_game_but.img = new_game_but_hover_img
        else:
            new_game_but.img = new_game_but_img
        if mp(continue_but):
            continue_but.img = continue_but_hover_img
        else:
            continue_but.img = continue_but_img
        if mp(options_but):
            options_but.img = options_but_hover_img
        else:
            options_but.img = options_but_img
        if mp(titles_but):
            titles_but.img = titles_but_hover_img
        else:
            titles_but.img = titles_but_img

    if options:
        screen.fill(background_color2)
        screen.blit(characters_txt.render(("Настройки"), 1, 'white'), (870, 75))
        if mp(back_void):
            back_button_color = "dodgerblue"
        else:
            back_button_color = "deepskyblue"
        pygame.draw.rect(screen, back_button_color, (100, 100, 100, 100))
        back_button.render(screen)
        pygame.draw.line(screen, "white", [100, 100], [200, 100])
        pygame.draw.line(screen, "white", [200, 100], [200, 200])
        pygame.draw.line(screen, "white", [100, 100], [100, 200])
        pygame.draw.line(screen, "white", [100, 200], [200, 200])

        pygame.draw.rect(screen, COLOR_HOVER, (700, 200, 100, 100))
        pygame.draw.rect(screen, COLOR_HOVER, (700, 310, 100, 100))
        screen.blit(characters_txt.render((str(round(music * 100)) + "%"), 1, 'white'), (710, 235))
        screen.blit(characters_txt.render((str(round(sounds * 100)) + "%"), 1, 'white'), (710, 345))
        screen.blit(characters_txt.render(("Музыка"), 1, 'white'), (825, 235))
        screen.blit(characters_txt.render(("Звуки"), 1, 'white'), (825, 345))
        music_plus_but.render(screen)
        music_minus_but.render(screen)
        sounds_plus_but.render(screen)
        sounds_minus_but.render(screen)

    if register:
        screen.fill(background_color2)
        if mp(back_void):
            back_button_color = "dodgerblue"
        else:
            back_button_color = "deepskyblue"
        if mp(reg_void):
            reg_button_color = COLOR_ACTIVE
        else:
            reg_button_color = 'deepskyblue'
        pygame.draw.rect(screen, back_button_color, (100, 100, 100, 100))
        back_button.render(screen)
        pygame.draw.line(screen, "white", [100, 100], [200, 100])
        pygame.draw.line(screen, "white", [200, 100], [200, 200])
        pygame.draw.line(screen, "white", [100, 100], [100, 200])
        pygame.draw.line(screen, "white", [100, 200], [200, 200])
        screen.blit(inp_txt.render(("Твой Никнейм"), 1, COLOR_INACTIVE), (500, 225))
        screen.blit(inp_txt.render(("Твоя Почта"), 1, COLOR_INACTIVE), (500, 325))
        screen.blit(inp_txt.render(("Твой Пароль"), 1, COLOR_INACTIVE), (500, 425))
        pygame.draw.rect(screen, reg_button_color, (500, 490, 250, 50))
        screen.blit(inp_txt.render(("Зарегистрироваться"), 1, 'white'), (515, 505))

        for box in input_boxes:
            box.update()
            box.draw(screen)

    if continue_screen:
        screen.fill(background_color2)
        if mp(back_void):
            back_button_color = "dodgerblue"
        else:
            back_button_color = "deepskyblue"
        if mp(login_void):
            reg_button_color = COLOR_ACTIVE
        else:
            reg_button_color = 'deepskyblue'
        pygame.draw.rect(screen, back_button_color, (100, 100, 100, 100))
        back_button.render(screen)
        pygame.draw.line(screen, "white", [100, 100], [200, 100])
        pygame.draw.line(screen, "white", [200, 100], [200, 200])
        pygame.draw.line(screen, "white", [100, 100], [100, 200])
        pygame.draw.line(screen, "white", [100, 200], [200, 200])
        screen.blit(inp_txt.render(("Твоя почта"), 1, COLOR_INACTIVE), (500, 225))
        screen.blit(inp_txt.render(("Твой Пароль"), 1, COLOR_INACTIVE), (500, 325))
        pygame.draw.rect(screen, reg_button_color, (500, 400, 250, 50))
        screen.blit(inp_txt.render(("Войти"), 1, 'white'), (515, 415))

        input_box1.update()
        input_box1.draw(screen)
        input_box2.update()
        input_box2.draw(screen)
        if continue_touched:
            cursor.execute("SELECT player_perec FROM players WHERE player_mail = '" + input_box1.text + "'")
            for player_perec in cursor:
                perec = player_perec[0]
            cnx.commit()
            cursor.execute("SELECT player_id, player_password FROM players WHERE player_mail = '" + input_box1.text + "' AND player_password = '" + hashlib.sha1(str(input_box2.text + perec).encode()).hexdigest() + "'")
            for player_id in cursor:
                for_count += 1
            if for_count == 0:
                screen.blit(error_txt.render(("Такого пользователя нет!"), 1, 'red'), (800, 350))
            cnx.commit()

    if char_selector:
        pygame.mixer.Sound.stop(theme)
        if not char_builder_start_played:
            pygame.mixer.Sound.play(char_builder_start)
            char_builder_start_played = True
        screen.fill((30, 30, 30))
        screen.blit(characters_txt.render(("Ваши персонажи"), 1, 'white'), (815, 100))
        try:
            for char_name in all_chars:
                character_buts.append(COLOR_HOVER)
                pygame.draw.rect(screen, character_buts[len(characters)], (760, 200 + (len(characters) * 110), 400, 100))
                screen.blit(characters_txt.render((char_name), 1, 'white'), (765, 230 + (len(characters) * 110)))
                characters.append(Sprite(760, 200 + (len(characters) * 110), "images/void.png", 400, 100))
            for char in characters:
                if mp(char):
                    character_buts[characters.index(char)] = COLOR_ACTIVE
                else:
                    character_buts[characters.index(char)] = COLOR_HOVER
        except:
            pass

    window.blit(screen, (0, 0))
    screen.fill((255, 255, 255))

    if mygame:
        background.img =
        background.render(screen)

    pygame.display.flip()
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
            file = open("code/user.txt", "w")
            file.write(str(user))
            file.close()
        if register:
            for box in input_boxes:
                box.handle_event(e)
        if continue_screen:
            input_box1.handle_event(e)
            input_box2.handle_event(e)
            # file = open("data.txt", "w")
            # file.write(str(score))
            # file.close()

            # file = open("data.txt", "r")
            # score = int(file.read())
            # file.close()

            # file = open("data.txt", "w")
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                if disconnect:
                    if mp(disconnect_void):
                        game = False
                if menu:
                    if mp(new_game_but):
                        register = True
                        menu = False
                    if mp(continue_but):
                        if user == '':
                            continue_screen = True
                            menu = False
                        else:
                            cnx = mysql.connector.connect(user='root', password='root',
                                                          host='localhost',
                                                          database='database')
                            cursor = cnx.cursor()
                            cursor.execute("SELECT player_name FROM players WHERE player_id = " + user)
                            for player_id in cursor:
                                print("[" + time.ctime() + "] " + str(player_id[0]))
                                print("[" + time.ctime() + "] login succeful")
                                menu = False
                                char_selector = True
                                for_count += 1
                            if for_count == 0:
                                print("[" + time.ctime() + "] incorrect login")
                                menu = False
                                continue_screen = True
                            cnx.commit()

                            menu = False
                            char_selector = True

                            try:
                                characters_ids = []
                                cursor.execute(
                                    "SELECT character_id, character_name, character_surname FROM characters WHERE character_owner_id = " + user)
                                all_chars = []

                                for all_char in cursor:
                                    all_chars.append(str(all_char[1] + " " + all_char[2]))
                                cnx.commit()
                                print("[" + time.ctime() + "] characters loaded")

                            except:
                                print("[" + time.ctime() + "] characters didn't load")
                                pass
                    if mp(options_but):
                        menu = False
                        options = True

                if options:
                    if mp(back_void):
                        options = False
                        menu = True
                    if mp(music_plus_but):
                        if music + 0.05 < 1.01:
                            music += 0.05
                    if mp(music_minus_but):
                        if music - 0.05 > -0.01:
                            music -= 0.05
                    if mp(sounds_plus_but):
                        if sounds + 0.05 < 1.01:
                            sounds += 0.05
                    if mp(sounds_minus_but):
                        if sounds - 0.05 > -0.01:
                            sounds -= 0.05
                if register:
                    if mp(back_void):
                        register = False
                        menu = True
                    if mp(reg_void):
                        per = make_perec()
                        query = ("INSERT INTO players(player_name, player_password, player_mail, player_perec) VALUES ('" + input_box1.text + "', '" + hashlib.sha1(str(input_box3.text + per).encode()).hexdigest() + "', '" + input_box2.text + "', '" + per + "')")
                        cursor.execute(query)
                        cnx.commit()
                        cursor.execute("SELECT player_id FROM players WHERE player_name = '" + input_box1.text + "' AND player_mail = '" + input_box2.text + "' ORDER BY player_id DESC LIMIT 1")

                        for player_id in cursor:
                            user = player_id[0]
                            break

                        cnx.commit()
                        print("[" + time.ctime() + "] regestration succeful")
                        file = open("code/user.txt", "w")
                        file.write(str(user))
                        file.close()

                        input_box1.text = ''
                        input_box2.text = ''
                        input_box3.text = ''
                        register = False
                        char_selector = True
                        try:
                            cursor.execute(
                                "SELECT character_name, character_surname FROM characters WHERE character_owner_id = " + str(
                                    user))
                            all_chars = []
                            for all_char in cursor:
                                all_chars.append(str(all_char[0] + " " + all_char[1]))
                            print("[" + time.ctime() + "] characters loaded")
                        except:
                            print("[" + time.ctime() + "] characters loading failed")
                if continue_screen:
                    if mp(back_void):
                        continue_screen = False
                        menu = True
                    if mp(login_void):
                        continue_touched = True
                        cursor.execute("SELECT player_perec FROM players WHERE player_mail = '" + input_box1.text + "'")
                        for player_perec in cursor:
                            perec = player_perec[0]
                        cursor.execute("SELECT player_id, player_password FROM players WHERE player_mail = '" + input_box1.text + "' AND player_password = '" + hashlib.sha1(str(input_box2.text + perec).encode()).hexdigest() + "' AND player_banned = 0")
                        for player_id in cursor:
                            print("[" + time.ctime() + "] " + str(player_id[0]))
                            print("[" + time.ctime() + "] login succesful")
                            continue_screen = False
                            continue_touched = False
                            char_selector = True
                            for_count += 1

                            cursor.execute("SELECT player_id FROM players WHERE player_mail = '" + input_box1.text + "'")
                            for id in cursor:
                                user = id[0]
                            password = input_box2.text
                            file = open("code/user.txt", "w")
                            file.write(str(user))
                            file.close()
                            try:
                                cursor.execute("SELECT character_id character_name, character_surname FROM characters WHERE character_owner_id = " + str(user))
                                all_chars = []
                                for all_char in cursor:
                                    all_chars.append(str(all_char[1] + " " + all_char[2]))
                                print("[" + time.ctime() + "] characters loaded")
                            except:
                                print("[" + time.ctime() + "] characters loading failed")

                            try:
                                cursor.execute("SELECT player_mail FROM players WHERE player_id = " + user)
                                for user_mail1 in cursor:
                                    user_mail = user_mail1[0]
                            except:
                                pass
                        if for_count == 0:
                            print("[" + time.ctime() + "] incorrect login")

                        cnx.commit()

                        input_box1.text = ''
                        input_box2.text = ''
                        input_box3.text = ''
                if char_selector:
                    for char_b in characters:
                        if mp(char_b):
                            character = 6
                            mygame = True
                            char_selector = False
                            try:
                                player_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                                player_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                                player_socket.connect(('localhost', 9090))
                            except:
                                disconnect = True

        if char_selector:
            characters.clear()
        clock.tick(FPS)
try:
    cnx.close()
except:
    pass

settings = open("code/settings.txt", "w")
settings.write(str(str(music) + "\n" + str(sounds)))
settings.close()
pygame.quit()