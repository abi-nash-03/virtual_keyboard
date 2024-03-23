import time

import whisper
import speech_recognition as sp
import pyttsx3
import os
from Keyboard import *
from global_hotkeys import *
from windowManager import *
from customKeys import *
import keyboard as kb

def voice_recognizer():
    recognizer = sp.Recognizer()
    while True:
        try:
            print("Available microphones:")
            print(sp.Microphone.list_microphone_names())
            with sp.Microphone() as mic:
                print("Adjusting noise...")
                # recognizer.adjust_for_ambient_noise(source, duration=1)
                recognizer.adjust_for_ambient_noise(mic, duration=2)
                result = get_data()
                print("Recording")
                audio = recognizer.listen(mic, phrase_time_limit=5)
                print("Record done...")
                try:
                    print("Recognizing the text...")
                    text = recognizer.recognize_google(audio)
                    print("Decoded Text: {}".format(text, kb))
                    print("getting notepad")
                    # result = get_data()
                    kb.write(func(text))
                except sp.UnknownValueError:
                    print("Google Speech Recognition could not understand the audio.")
                except sp.RequestError:
                    print("Could not request results from Google Speech Recognition service.")
                except sp.WaitTimeoutError as WTE:
                    print("Speech not detected within 2 seconds")
                except Exception as ex:
                    print("Error during recognition:", ex)

        except sp.UnknownValueError():
            continue


#some capslock case need to be checked
# func("hii my namabackspacee is abinash special two special one special two special one special two hash one hahii theresh one")
     # "tab space text next line in the new line capslock something in capitals "
     # "capslock small letters forward slash forward slash backward slash specialhiimynamabackspaceeisabinash2two1one2two1one2two1onehahiithereshone one special minus two special shift minus one")


# get_data()
# kb.send("browser_refresh")

def main_fn():
    voice_recognizer()


main_fn()
# func("HhiiII")