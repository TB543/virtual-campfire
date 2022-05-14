readme = open("readme.txt", "w")
readme.write("2021 Virtual Campfire:\n\nWith school being virtual during the 2020-2021 school year, there is no paper "
             "to burn, only word docs, pdfs, etc.\nSo I made this program to \"burn\" all these files\n\nHow To "
             "Use:\n\n1. drag and drop the files you want to \"burn\" into the window\n2. the fire will light up "
             "proportonal to the size of the file and then be deleted when the fire goes out\n3. remember to make "
             "copies of any of the files you want to keep, as they cannot be recovered once deleted, they will not "
             "even go into the recycling bin\n4. DO NOT move, rename, or modify the mov files or the program will not "
             "work (they can be moved, as long as they stay in the same folder as the python file)\n5. please DO NOT "
             "try to \"burn\" more than one file at a time, or try to \"burn\" one before the previous file has "
             "finished or it may glitch out the program\n6. by running this program you agree to the terms that the "
             "creator of this program is not responsible for the accidental deleting of any files") 
readme.close()

import os
from threading import Timer
from tkinter import *
try:
    from tkinterdnd2 import DND_FILES, TkinterDnD
    from tkvideo import tkvideo
except:
    imports = open("imports.bat", "w")
    imports.write("@echo off\npip install tkinterdnd2\npip install tkVideo")
    imports.close()
    os.system('imports.bat')
    os.remove('imports.bat')
    from tkinterdnd2 import DND_FILES, TkinterDnD
    from tkvideo import tkvideo


def end():
    global file

    label2.pack_forget()
    label1.pack()
    os.remove(file)


def file_drop(event):
    global file

    file = str(event.data).replace("{", "").replace("}", "")
    wait = 0
    label1.pack_forget()
    label2.pack()

    for value in range(int(int(os.path.getsize(str(event.data).replace("{", "").replace("}", "")))/7000) + 1):
        wait += 1

    if wait > 10:
        wait = 10

    timer = Timer(wait, end)
    timer.start()


file = ""

window = TkinterDnD.Tk()
window.title("Fire")
window.geometry("1920x1080")
window.attributes('-fullscreen', True)

window.drop_target_register(DND_FILES)
window.dnd_bind("<<Drop>>", file_drop)

label1 = Label(window)
label1.pack()
label2 = Label(window)

fire_off = tkvideo("fire off.mov", label1, loop=1, size=(1920, 1080))
fire_on = tkvideo("fire on.mov", label2, loop=1, size=(1920, 1080))
fire_off.play()
fire_on.play()

window.mainloop()
