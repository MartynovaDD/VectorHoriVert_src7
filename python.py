from PIL import Image
from numpy import array

def func(InputFile1,InputFile2,OutputFile):
    try:
        background = Image.open(InputFile1,'r')
    except FileNotFoundError:
        print("Error! Cannot find file...")
        exit(-1)
    try:
        foreground = Image.open(InputFile2,'r')
    except FileNotFoundError:
        print("Error! Cannot find file...")
        exit(-1)
    fg_w, fg_h = foreground.size
    bg_w, bg_h = background.size
    offset = ((bg_w - fg_w) // 2, (bg_h - fg_h) // 2)
    background.paste(foreground, offset)
    background.save(OutputFile)
    
arg1 = input()
arg2 = input()
arg3 = input()
func(arg1,arg2,arg3)
