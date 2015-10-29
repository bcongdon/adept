import pygame
import os

class SoundEngine:
    pygame.mixer.init()
    MUSIC_CHANNEL = pygame.mixer.find_channel()

    @staticmethod
    def playMusic(title, numLoops=-1):
        SOUND_FILE = os.path.join(os.path.join(*list(['assets', 'sounds', 'music'] + [title])))
        print SOUND_FILE
        try:
            musicSound = pygame.mixer.Sound(file=SOUND_FILE)
            if musicSound is not None:
                SoundEngine.MUSIC_CHANNEL.play(musicSound,loops=numLoops)
        except Exception as e:
            print("Error: Music asset \"" + title + "\" does not exist.")
            print(e)

    @staticmethod
    def setMusicVolume(vol):
        SoundEngine.MUSIC_CHANNEL.set_volume(vol)

    @staticmethod
    def stopAllSounds():
        pygame.mixer.stop()

        