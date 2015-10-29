import pygame
import os

class SoundEngine:
    pygame.mixer.init()
    MUSIC_CHANNEL = pygame.mixer.find_channel()
    PLAYING_SOUND_EFFECTS = dict()

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

    @staticmethod
    def startLoopedSoundEffect(title, force = False):
        if title in SoundEngine.PLAYING_SOUND_EFFECTS.keys() and not force:
            return #The effect is already playing

        SOUND_FILE = os.path.join(os.path.join(*list(['assets', 'sounds'] + [title])))
        channelToPlay = pygame.mixer.find_channel()
        if channelToPlay is not None:
            try:
                effectSound = pygame.mixer.Sound(file=SOUND_FILE)
                channelToPlay.play(effectSound, loops = -1)
                SoundEngine.PLAYING_SOUND_EFFECTS[title] = effectSound
            except Exception as e:
                print e
        else:
            print "Error: Could not find channel to play sound effect on."

    @staticmethod
    def stopLoopedSoundEffect(title):
        if title in SoundEngine.PLAYING_SOUND_EFFECTS.keys():
            SoundEngine.PLAYING_SOUND_EFFECTS[title].stop()
            del(SoundEngine.PLAYING_SOUND_EFFECTS[title])

    @staticmethod
    def playSoundEffect(title):
        SOUND_FILE = os.path.join(os.path.join(*list(['assets', 'sounds'] + [title])))
        channelToPlay = pygame.mixer.find_channel()
        if channelToPlay is not None:
            try:
                channelToPlay.play(pygame.mixer.Sound(file=SOUND_FILE   ))
            except Exception as e:
                print e
        else:
            print "Error: Could not find channel to play sound effect on."

        