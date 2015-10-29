import pygame

from buffalo import utils
from buffalo.scene import Scene
from buffalo.label import Label
from buffalo.button import Button
from soundEngine import SoundEngine

class Options(Scene):

    def on_escape(self):
        """
        Go back to the main menu.
        """
        self.go_to_main_menu()

    def update(self):
        pass

    def blit(self):
        pass

    def __init__(self):
        super(Options, self).__init__()
        self.BACKGROUND_COLOR = (0, 177, 50, 255)
        self.buttons.add(
            Button(
                (10, utils.SCREEN_H - 10),
                "Back",
                invert_y_pos=True,
                func=self.go_to_main_menu,
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2 - 10, utils.SCREEN_H/2 - 10),
                "Mute Music",
                invert_y_pos=True,
                func=self.mute_music,
            )
        )
        self.buttons.add(
            Button(
                (utils.SCREEN_W / 2 - 10, utils.SCREEN_H/2 + 50),
                "Play Music",
                invert_y_pos=True,
                func=self.play_music,
            )
        )

    def go_to_main_menu(self):
        utils.set_scene(
            Menu()
        )
    def mute_music(self):
        SoundEngine.setMusicVolume(0)
    def play_music(self):
        SoundEngine.setMusicVolume(1)


from menu import Menu
