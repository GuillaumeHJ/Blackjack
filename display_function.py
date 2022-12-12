from model import *
import pygame
from pygame.locals import *
from PIL import Image
import numpy as np

pygame.init()
black = (0, 0, 0)
white = (255, 255, 255)
grey = (200, 200, 200)
black_grey = (100, 100, 100)
red = (255, 0, 0)
black_red = (200, 0, 0)
font = pygame.font.Font(pygame.font.get_default_font(), 36)


class Images:
    def __init__(self, x, y, name_file):
        self._x = x
        self._y = y
        self._image = pygame.image.load(name_file).convert_alpha()

    def reshape(self, width, height):
        self._image = pygame.transform.scale(self._image, (width, height))

    def display(self, window):
        window.blit(self._image, (self._x, self._y))


class Rectangle():
    def __init__(self, x, y, width, height, color, text, text_color, font):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self._color = color
        self._text = text
        self._text_color = text_color
        self._font = font

    def display(self, window):
        # Object text
        object_text = pygame.font.Font.render(self._font, self._text, True, self._text_color)
        text_ini_width, text_ini_height = object_text.get_size()

        # Resize object text
        coef = min((self._width - (self._height / 2)) / text_ini_width,
                   (self._height - (self._height / 2)) / text_ini_height)
        text_width = coef * text_ini_width
        text_height = coef * text_ini_height
        object_text = pygame.transform.scale(object_text, (text_width, text_height))

        # Display
        button = pygame.Rect(self._x - (self._width / 2), self._y - (self._height / 2), self._width, self._height)
        pygame.draw.rect(window, self._color, button)
        text_rect = object_text.get_rect(center=(self._x, self._y))
        window.blit(object_text, text_rect)

    def set_text(self, new_text):
        self._text = new_text


class Button(Rectangle):
    def __init__(self, x, y, width, height, color, text, text_color, font, cover_color):
        super().__init__(x, y, width, height, color, text, text_color, font)
        self._cover_color = cover_color

    # def __init__(self, x, y, width, height, color, text, text_color, font):
    #     super().__init(x, y, width, height, color, text, text_color, font)
    #     self._cover_color = self._color

    def covered(self, event):  # true si couvert false sinon
        if event.type == MOUSEMOTION:
            if (self._x + (self._width / 2)) > event.pos[0] > self._x - (self._width / 2) and \
                    self._y - (self._height / 2) < event.pos[1] < (self._y + (self._height / 2)):
                return True
        return False

    def display(self, window, event):
        if self.covered(event):
            temp_color = self._color
            self._color = self._cover_color
            super().display(window)
            self._color = temp_color

        else:
            super().display(window)

    def click(self, event):  # true si click false sinon
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if event.pos[0] < (self._x + (self._width / 2)) and event.pos[0] > self._x - (self._width / 2) and \
                        event.pos[1] > self._y - (self._height / 2) and event.pos[1] < (self._y + (self._height / 2)):
                    return True
        return False


class disp_cards():
    def __init__(self, card, x, y, width, height):
        self._x = x
        self._y = y
        self._card = card
        col = card.color()
        r = card.rank()
        name_file = str(r) + "_" + col + ".png"
        self._im_card = pygame.image.load(name_file).convert_alpha()

    def resize(self, new_width, new_height):
        self._im_card = pygame.transform.scale(self._im_card, (new_width, new_height))

    def repos(self, new_x, new_y):
        self._x = new_x
        self._y = new_y

    def display(self, window):
        window.blit(self._im_card, (self._x, self._y))


def init_display(window_width=1000):
    # chargement image fond pour recuperer la taille
    im_fond = Image.open('fond_vert.jpg')
    fond_width, fond_height = im_fond.size

    # Ouverture de la fenetre Pygame
    prop_fond = window_width / fond_width
    fond_width = int(prop_fond * fond_width)
    fond_height = int(prop_fond * fond_height)

    # dim rect
    white_rect_width = fond_width
    white_rect_height = white_rect_width / 15
    white_rect_x = 0
    white_rect_y = fond_height
    white_rect = pygame.Rect(white_rect_x, white_rect_y, white_rect_width, white_rect_height)

    window_height = fond_height + white_rect_height
    window = pygame.display.set_mode((window_width, window_height))

    return window, window_height,window_width, white_rect, white_rect_height


def init_page_nb_players(window_width, window_height):
    Rect_page_nb_joueurs = []

    ### TITRE ###
    title_blackjack_font = pygame.font.Font(pygame.font.get_default_font(), 36)
    title_blackjack = Rectangle(window_width / 2, window_height / 5, window_width / 2, window_height / 6, black,
                                "BlackJack", white, title_blackjack_font)
    Rect_page_nb_joueurs += [title_blackjack]

    ### QUESTION ###
    question_font = pygame.font.Font(pygame.font.get_default_font(), 36)
    question = Rectangle(window_width / 2, 2 * window_height / 5, window_width / 3, window_height / 6, white,
                         "Nombre de joueurs :", black, question_font)
    Rect_page_nb_joueurs += [question]

    ### NB JOUEURS ###
    buttons_nb_player_size = int(window_width // 9)
    buttons_nb_players = np.empty((6), dtype=Button)

    for k in range(3):
        x = (5 / 2) * buttons_nb_player_size + (2 * k * buttons_nb_player_size)
        y1 = int(3 * window_height / 5)
        y2 = int(4 * window_height / 5)
        buttons_nb_players[k] = Button(x, y1, buttons_nb_player_size, buttons_nb_player_size, grey, str(k + 1), black,
                                       font, black_grey)
        buttons_nb_players[k + 3] = Button(x, y2, buttons_nb_player_size, buttons_nb_player_size, grey, str(k + 4),
                                           black, font, black_grey)

    return Rect_page_nb_joueurs, buttons_nb_players


def init_page_name_player(window_width, window_height):
    Rect_page_nom_joueur = []
    Butt_page_nom_joueur = []

    button_retour = Button(window_width / 10, window_height / 14, window_width / 10, window_height / 14, red, "RETOUR",
                           black, font, black_red)
    button_IA = Button(window_width * (1 / 2 - 1 / 9), window_height / 2, window_width / 8, window_height / 12, grey,
                       "IA", black, font, black_grey)
    button_humain = Button(window_width * (1 / 2 + 1 / 9), window_height / 2, window_width / 8, window_height / 12,
                           grey, "HUMAIN", black, font, black_grey)

    Butt_page_nom_joueur += [button_retour, button_IA, button_humain]

    rect_num_joueur = Rectangle(window_width / 2, window_height / 4, window_width / 3, window_height / 10, white,
                                "Joueur k", black, font)
    rect_nom_joueur = Rectangle(window_width / 2, 3 * window_height / 4, window_width / 3, window_height / 10, grey,
                                " ", black, font)

    Rect_page_nom_joueur += [rect_num_joueur, rect_nom_joueur]

    return Butt_page_nom_joueur, Rect_page_nom_joueur


type_joueur = -1


def get_nb_players(window, window_width, window_height, white_rect, white_rect_height, Rect_page_nb_joueurs,
                   buttons_nb_players):
    activated = True
    while activated:
        for event in pygame.event.get():
            for elem in Rect_page_nb_joueurs:
                elem.display(window)
            for k in range(len(buttons_nb_players)):
                buttons_nb_players[k].display(window, event)
                if buttons_nb_players[k].click(event):
                    nb_players = k + 1
                    window.fill(white)
                    activated = False
                    return True, nb_players

            if event.type == QUIT:
                pygame.quit()
                activated = False
                return False, 0
            pygame.display.flip()


def get_name_players(nb_players, window, window_width, window_height, white_rect, white_rect_height,
                     Butt_page_nom_joueur, Rect_page_nom_joueur):
    activated = True
    window.fill(white)
    user_text = " "
    i = 0
    type_joueur = -1
    Joueurs = [[] for j in range(nb_players)]
    while activated:
        for event in pygame.event.get():
            if i == nb_players:
                activated = False
                return True, Joueurs
            else:
                window.fill(white)
                Rect_page_nom_joueur[0].set_text("Joueur " + str(i + 1))
                Rect_page_nom_joueur[0].display(window)
                for elem in Butt_page_nom_joueur:
                    elem.display(window, event)

                if Butt_page_nom_joueur[2].click(event):
                    type_joueur = 0
                elif Butt_page_nom_joueur[1].click(event):
                    type_joueur = 1
                    Joueurs[i] = [1]
                    i += 1
                    type_joueur = -1
                elif type_joueur == 0:
                    Rect_page_nom_joueur[1].display(window)
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            if len(user_text) == 1:
                                user_text = " "
                            else:
                                user_text = user_text[:-1]
                        elif event.key == pygame.K_RETURN:
                            Joueurs[i] = [0, user_text.lstrip(" ")]
                            i += 1
                            type_joueur = -1
                            user_text = " "
                        else:
                            user_text += event.unicode
                        Rect_page_nom_joueur[1].set_text(user_text)
                elif Butt_page_nom_joueur[0].click(event):
                    if i == 0:
                        window.fill(white)
                        return False, 0
                    else:
                        i -= 1
                elif event.type == QUIT:
                    pygame.quit()
                    activated = False
                    return None, 0
                pygame.display.flip()



def get_start(WINDOWS):
    [window, window_height,window_width, white_rect, white_rect_height] = WINDOWS
    Rect_page_nb_joueurs, buttons_nb_players = init_page_nb_players(window_width, window_height)
    Butt_page_nom_joueur, Rect_page_nom_joueur = init_page_name_player(window_width, window_height)

    window_open = True
    page_nb_joueurs = True
    page_name_players = False
    while window_open:
        window.fill(white)
        if page_nb_joueurs:
            test, nb_players = get_nb_players(window, window_width, window_height, white_rect, white_rect_height,
                                              Rect_page_nb_joueurs, buttons_nb_players)
            page_nb_joueurs = False
            page_name_players = True
            window_open = test
        elif page_name_players:
            test, players = get_name_players(nb_players, window, window_width, window_height, white_rect,
                                             white_rect_height, Butt_page_nom_joueur, Rect_page_nom_joueur)
            if test == None:
                window_open = False
            else:
                page_name_players = False
                page_nb_joueurs = not test
                if test:
                    return (nb_players, players)


        elif window_open:
            for event in pygame.event.get():
                if event.type == QUIT:
                    window_open = False
                    pygame.quit()
                    return (None)