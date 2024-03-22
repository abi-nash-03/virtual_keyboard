import time

import whisper
import speech_recognition as sp
import pyttsx3
import os
from Keyboard import *
from windowManager import *
import keyboard as kb

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

# func('HIi my name is abinash enter this is some sample note save')
# func('hii tab text')
# get_data()
# time.sleep(2)
# kb.send('1')
# kb.send('+')
# kb.send('2')
# kb.send('*')
# kb.send('5')
# kb.send('escape')
# kb.press_and_release('P, Y, T, H, O, N')

# result = get_data()
# kb.write("google")
# kb.send('2')
# kb.send('shift+8')
# kb.send('3')
# kb.send('enter')
# kb.send('page_up')
# print(result)

# record all keyboard clicks until esc is clicked
# print("recordin events")
# events = kb.record('esc')
# play these events
# print("printing events")
# kb.play(events)
# print all typed strings in the events
# print(list(kb.get_typed_strings(events)))

# kb.read_hotkey()
# print("key = ",kb.key_to_scan_codes('F4'))
# print("key read")
# kb.send('backspack')
# print("entered")help
# "ctrl+shift+p"
# get_data()
# kb.send('ctrl+p')
# time.sleep(5)
# kb.send('enter')
# func("help")
# get_data()
# kb.send("caps_lock")
# str = "sdrgbdnefkpskmr"
# for i in str:
#     kb.send(i)
# kb.send("volume_down")
# while True:
#     get_data()
#     time.sleep(10)