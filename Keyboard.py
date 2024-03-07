import keyboard as kb
from windowManager import *
def func(text):
    # print("Original = ", text)
    text = text.lower()
    text = text.split(" ")
    key_words(text)
    # print(text)
    # text = backspace(text)
    # text = splCharacters(text)
    # text = splCharactersOthers(text)
    # text = numbers(text)
    # text = tabSpace(text)
    # text = nextLine(text)
    # text = caps(text)
    # text = slash(text)

    # result = get_data()
    # kb.write(text)
    # print(text)
    # return text

def backspace(text):
    idx = text.find('backspace')
    front = text[:idx-1]
    end = text[idx+9:]
    text = front+end
    return text

def splCharacters(text):
    arr = ["special one", "special two", "special three", "special four", "special five", "special six", "special seven",
           "special eight", "special nine", "special zero"]
    char_arr = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
    for i in range(0, len(arr)):
        while text.find(arr[i]) != -1:
            l  = len(arr[i])
            idx = text.find(arr[i])
            first = text[:idx]
            last = text[idx+l:]
            text = first+char_arr[i]+last

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


def key_words(text):
    get_data()
    # print('text before', text)
    arr = ["special one", "special two", "special three", "special four", "special five", "special six", "special seven",
           "special eight", "special nine", "special zero", "hash one", "hash two", "hash three", "hash four", "hash five",
           "hash six", "hash seven", "hash eight", "hash nine", "hash zero", "enter", "left", "right", "up", "down", "escape", "volume up",
           "volume down", "plus", "minus", "multiply", "divide"]
    char_arr = ["shift+1", "shift+2", "shift+3", "shift+4", "shift+5", "shift+6", "shift+7", "shift+8",
                "shift+9", "shift+0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "enter", "left",
                "right", "up", "down", "escape", "volume_up", "volume_down", '+', '-', '*', '/']
    text = reform_text(text, arr)

    print('text = ',text)
    for i in range(0, len(text)):
        if(text[i] in arr):
            # print(text[i])
            idx = arr.index(text[i])
            kb.send(char_arr[idx])
            print(char_arr[idx])
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
