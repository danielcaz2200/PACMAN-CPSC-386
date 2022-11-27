import pygame
from pygame.locals import *
from sound import Sound
from timer import Timer
from settings import Settings
import os  # needed for highscore functionality


class GameController(object):
    def __init__(self):
        """Initialize class variables"""
        self.sound = Sound()
        self.settings = Settings()
        self.clock = pygame.time.Clock()
        self.font = "fonts/retro_font.ttf"

        # Main Menu Screen
        self.menu = True
        self.settings = Settings()
        self.screenSize = (self.settings.screenWidth,
                           self.settings.screenHeight)
        self.screen = pygame.display.set_mode(self.screenSize)
        menu_image_list = [pygame.transform.scale(pygame.image.load(
            f'images/chasing{n}.png'), (600, 160)) for n in range(16)]

        # To control menu
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.mid_w, self.mid_h = self.screenSize[0] / 2, self.screenSize[1] / 2
        self.startx, self.starty = self.mid_w, self.mid_h + 227
        self.highscorex, self.highscorey = self.mid_w, self.mid_h + 50 + 205
        self.exitx, self.exity = self.mid_w, self.mid_h + 70 + 215
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = -100
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.state = 'Start'
        self.menu_timer = Timer(frames=menu_image_list, wait=250)
        self.image_position_menu_y = self.mid_h + 80

        # Highscores
        self.highscorex, self.highscorey = self.mid_w, self.mid_h + 50 + 205
        self.highscoremenu = False
        self.highscore = None
        self.getHighScore()
        self.score = 0  # Starting score

    def draw_image(self, image, x, y):
        image_rect = image.get_rect()
        image_rect.center = (x, y)
        self.screen.blit(image, image_rect)

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font, size)
        text_surface = font.render(text, True, (255, 255, 255))  # White Font
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.screen.blit(text_surface, text_rect)

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

        pygame.display.update()

    def check_menu_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_RETURN:
                    self.START_KEY = True
                if key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if key == pygame.K_UP:
                    self.UP_KEY = True

    def move_cursor(self):
        if self.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.highscorex + self.offset, self.highscorey)
                self.state = 'Highscores'
            elif self.state == 'Highscores':
                self.cursor_rect.midtop = (
                    self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
        if self.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.exitx + self.offset, self.exity)
                self.state = 'Exit'
            elif self.state == 'Highscores':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Exit':
                self.cursor_rect.midtop = (
                    self.highscorex + self.offset, self.highscorey)
                self.state = 'Highscores'

    def check_menu_input(self):
        self.move_cursor()
        if self.START_KEY:
            if self.state == 'Start':
                self.sound.play_startup()
                self.menu = False
            elif self.state == 'Highscores':
                self.highscoremenu = True
            elif self.state == 'Exit':
                exit()
            self.menu = False
        if self.BACK_KEY:  # if we are in highscore menu
            self.highscoremenu = False
            self.menu = True

    def draw_cursor(self):
        self.draw_text("*", 20, self.cursor_rect.x, self.cursor_rect.y)

    def main_menu(self):
        self.menu = True
        while self.menu:
            self.check_menu_events()
            self.check_menu_input()

            self.screen.fill(self.settings.bg)
            pacman_image = pygame.transform.scale(
                pygame.image.load('images/Pacman image.JPG'), (350, 150))
            self.draw_image(pacman_image, self.mid_w, 100)

            self.draw_text('Play Game', 20, self.startx, 675)
            self.draw_text('High Scores', 20,
                           self.highscorex, 705)
            self.draw_text('Exit', 20, self.exitx, 735)

            self.draw_cursor()

            self.draw_image(self.menu_timer.imagerect(),
                            self.mid_w, self.image_position_menu_y)
            pygame.display.update()

            self.reset_keys()

    def getHighScore(self):
        # Check if hiscore.txt already exists
        if os.path.exists('hiscore.txt'):
            with open('hiscore.txt', 'r') as f:
                highscore = int(f.readline())
                self.highscore = highscore
        else:
            self.highscore = 0  # Default if high score does not exist

        return self.highscore

    def get_highscore_string(self):
        curr_high_score = f'Current high score is {self.getHighScore()}'
        return curr_high_score

    def highscore_menu(self):
        self.highscoremenu = True
        while self.highscoremenu:
            self.check_menu_events()
            self.check_menu_input()

            self.screen.fill((0, 0, 0))

            curr_high_score = self.get_highscore_string()
            self.draw_text(curr_high_score, 15, self.mid_w, self.mid_h)
            self.draw_text('Press backspace to exit', 15,
                           self.mid_w, self.mid_h + 20)
            pygame.display.update()

            self.reset_keys()
