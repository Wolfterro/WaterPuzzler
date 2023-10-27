import os

import pygame
import click

from src.drawer import Drawer
from src.puzzler import Puzzler


class Interactor(object):
    def __init__(self):
        pygame.init()
        self.__load_sounds()

        self.drawer = Drawer()
        self.puzzler = Puzzler()

        self.row_data = self.puzzler.get_row_data()
        self.sample = self.puzzler.get_sample()

    def start(self):
        self.__redraw_screen()
        self.get_wave_range_selection()

    def get_wave_range_selection(self):
        print("Which wave range will you adjust?")
        print("[A] - Wave A")
        print("[B] - Wave B")
        print("[C] - Wave C")
        print("[Q] - Quit")

        wave = click.getchar()
        if wave.upper() in ["A", "B", "C"]:
            self.__redraw_screen()
            self.interact_with_wave(wave=wave)
        elif wave.upper() == "Q":
            exit(0)
        else:
            self.__redraw_screen()
            self.get_wave_range_selection()

    def interact_with_wave(self, wave):
        print("Move to which direction?")
        print("[L] - Left")
        print("[R] - Right")
        print("[C] - Check")
        print("[Q] - Return")

        direction = click.getchar()
        if direction.upper() in ["L", "R"]:
            self.shift_wave_and_redraw(wave=wave, direction=direction)
        elif direction.upper() == "C":
            self.__compare()
        elif direction.upper() == "Q":
            self.__redraw_screen()
            self.get_wave_range_selection()
        else:
            self.__redraw_screen()
            self.interact_with_wave(wave=wave)

    def shift_wave_and_redraw(self, wave, direction):
        wave_option = getattr(self.puzzler, wave.upper())

        if direction.upper() == "L":
            self.__play_sound(sound_type="crank")
            self.puzzler.shift_left(puzzle_option=wave_option)
        else:
            self.__play_sound(sound_type="crank")
            self.puzzler.shift_right(puzzle_option=wave_option)

        self.__redraw_screen()
        self.interact_with_wave(wave=wave)

    # "Private" Methods
    # -----------------
    def __redraw_screen(self, cleared=False):
        os.system('cls||clear')

        self.drawer.draw_div("Sample")
        self.drawer.draw(row_data=self.sample)

        self.drawer.draw_div("Options")
        self.drawer.draw_puzzle_option(self.puzzler.A, "A")
        self.drawer.draw_puzzle_option(self.puzzler.B, "B")
        self.drawer.draw_puzzle_option(self.puzzler.C, "C")

        self.drawer.draw_div("Result")
        self.drawer.draw(row_data=self.row_data)
        self.drawer.draw_lights(cleared=cleared)

    def __compare(self):
        self.row_data = self.puzzler.get_row_data()
        self.__redraw_screen()

        if self.puzzler.compare(row_data=self.row_data, sample=self.sample):
            self.__redraw_screen(cleared=True)
            exit(0)
        else:
            self.get_wave_range_selection()

    def __load_sounds(self):
        for sound_type in ["crank", "select", "back", "clear"]:
            try:
                sound = pygame.mixer.Sound("assets/{}.wav".format(sound_type))
            except:
                sound = None

            setattr(self, "{}_sound".format(sound_type), sound)

    def __play_sound(self, sound_type):
        sound = getattr(self, "{}_sound".format(sound_type), None)
        if sound:
            pygame.mixer.Sound.play(sound)
