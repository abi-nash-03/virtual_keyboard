import keyboard as kb
from windowManager import *

arr = ["enter", "left", "right", "up", "down","escape", "volume up", "volume down", "plus", "minus", "multiply","divide",
       "save", "tab", "comma", "dot","question mark","backspace", "select all", "space", "print", "screenshot", "caps lock", "exit",
       "unod", "redo"]
char_arr = ["enter", "left","right", "up", "down", "escape", "volume_up", "volume_down", '+', '-', '*', '/',
            'ctrl+s', 'tab', ',', '.', '?', 'backspace', 'ctrl+a', "space", "ctrl+p", "windows+print_screen", "caps_lock", "alt+f4",
            "ctrl+z", "ctrl+shift+z"]

volume = ["volume up", "volume down", "mute"]
volume_arr = ["volume_up", "volume_down", "volume_mute"]

special = ["special one", "special two", "special three", "special four", "special five", "special six", "special seven",
           "special eight", "special nine", "special zero"]
special_arr = ["shift+1", "shift+2", "shift+3", "shift+4", "shift+5", "shift+6", "shift+7", "shift+8",
               "shift+9", "shift+0"]

num = ["hash one", "hash two", "hash three", "hash four", "hash five","hash six", "hash seven", "hash eight",
       "hash nine", "hash zero"]
num_arr = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

arr += volume
char_arr += volume_arr

arr += special
char_arr += special_arr

arr += num
char_arr += num_arr


def clear_all():
    kb.send('ctrl+a')
    kb.send('backspace')


def add_custom_hotkeys():
    kb.add_hotkey('space+c', clear_all)


#Abbrivated text can be expanded with a space key press
def add_abbreviation():
    kb.add_abbreviation('//', 'This is a sample abbrivated text')
    kb.add_abbreviation('hru', 'How are you?')
    kb.add_abbreviation('wfh', 'Work from home')
    kb.add_abbreviation('eod', 'End of the Day')


def func(text):
    # print("Original = ", text)
    # kb.add_hotkey('space', lambda: print('space was pressed!'))
    add_custom_hotkeys()
    add_abbreviation()
    # kb.wait()
    # kb.wait()
    text = text.lower()

    if text.find('help') != -1:
        help(arr, char_arr)
    else:
        text = text.split(" ")
        key_words(text, arr, char_arr)


def backspace(text):
    idx = text.find('backspace')
    front = text[:idx-1]
    end = text[idx+9:]
    text = front+end
    return text


def splCharacters(text):
    sample_arr = ["special one", "special two", "special three", "special four", "special five", "special six", "special seven",
           "special eight", "special nine", "special zero"]
    sample_char_arr = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    for i in range(0, len(sample_arr)):
        while text.find(sample_arr[i]) != -1:
            l  = len(sample_arr[i])
            idx = text.find(sample_arr[i])
            first = text[:idx]
            last = text[idx+l:]
            text = first+sample_char_arr[i]+last

    return text


def splCharactersOthers(text):
    arr = ["special minus one", "special minus two", "special minus three", "special minus four", "special minus five", "special minus six",
           "special minus seven", "special minus eight", "special minus nine", "special minus zero", "special shift minus one", "special shift minus two"
           "special shift minus three", "special shift minus four", "special shift minus five", "special shift minus six", "special shift minus seven", "special shift minus eight"
           "special shift minus nine", "special shift minus zero"]

    char_arr = ["=", "-", "\\", "]", "[", "'", ";", "/", ".", ",", "|", "}", "{", "\"", ":", "?", ">", "<"]
    for i in range(0, len(arr)):
        while text.find(arr[i]) != -1:
            l = len(arr[i])
            idx = text.find(arr[i])
            first = text[:idx]
            last = text[idx+l:]
            text = first+char_arr[i]+last
    return text


def numbers(text):
    num_text = ["hash one", "hash two", "hash three", "hash four", "hash five", "hash six", "hash seven", "hash eight", "hash nine", "hash zero"]
    num_val = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    for i in range(0, len(num_text)):
        while text.find(num_text[i]) != -1:
            l = len(num_text[i])
            idx = text.find(num_text[i])
            first = text[:idx]
            last = text[idx+l:]
            text = first+num_val[i]+last
    return text


def tabSpace(text):
    key = "tab space"
    l = len(key)
    while(text.find(key) != -1):
        idx = text.find(key)
        if(idx != -1):
            first = text[:idx]
            last = text[idx+l:]
            text = first+"   "+last
    return text


def nextLine(text):
    key = "next line"
    idx = text.find(key)
    l = len(key)
    if(idx != -1):
        first = text[:idx]
        last = text[idx+l:]
        text = first+"\n"+last
    return text


def caps(text):
    key = "caps lock"
    idx = text.lower().find(key)
    l = len(key)
    if(idx != -1):
        first = text[:idx]
        # print("first = ", first)
        last = text[idx+l:]
        lastIdx = last.find(key)
        if(lastIdx != -1):
            capsWord = last[:lastIdx]
            capsWord = capsWord.strip()
            capsWord = capsWord.upper()
            last = capsWord + last[lastIdx+l:]
        else:
            last = last.upper()
        text = first+last

    return text


def slash(text):
    key1 = 'forward slash'
    key2 = 'backward slash'
    while(text.find(key1) != -1 or   text.find(key2) != -1):
        if(text.find(key1) != -1):
            idx1 = text.find(key1)
            first = text[:idx1]
            last = "/"+text[idx1+len(key1):]
            text = first+last
        if(text.find(key2) != -1):
            idx2 = text.find(key2)
            first = text[:idx2]
            last = '\\'+text[idx2+len(key2):]
            text = first+last
    return text


def calculator(text):
    keys = ['divide', 'multiply', 'add', 'subtract']
    for i in keys:
        if(text.find(i) != -1):
            kb.send(i+'_key')


def key_words(text, arr, char_arr):
    get_data()
    # print('text before', text)

    text = reform_text(text, arr)

    print('text = ',text)
    for i in range(0, len(text)):
        if(text[i] in arr):
            # print(text[i])
            idx = arr.index(text[i])
            kb.send(char_arr[idx])
            print(char_arr[idx])
        elif(text[i].lower() == 'copy'):
            kb.send('ctrl+a')
            kb.send('ctrl+c')
        elif(text[i].lower() == 'paste'):
            kb.send('right')
            kb.send('ctrl+v')
        else:
            for j in text[i]:
                kb.send(j)
        # kb.send('space')


def reform_text(text, keys):
    res = []
    n = len(text)
    i = 0
    while i < n:
        key = ""
        if(i+1 < len(text)):
            key = text[i]+" "+text[i+1]
        if(key in keys):
            res.append(key)
            i += 2
        else:
            res.append(text[i])
            i += 1
    return res


def help(arr, keys):
    for i in range(0, len(arr)):
        print(arr[i]," --> ", keys[i])