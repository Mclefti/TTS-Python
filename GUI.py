import tkinter as tk
import pygame
from gtts import gTTS
from playsound import playsound
import os

pygame.mixer.init()
fh = open("sound.txt", "a")

root = tk.Tk()
root.geometry("1280x720") # size of window
root.title("Text to Speech") # window Tittle

#functions
def saveText():
    fh = open("sound.txt", "w")
    txtbox_text = txtbox.get("1.0",'end-1c')
    fh.write(txtbox_text)
    fh.close()

def createSoundFile():
    fh = open("sound.txt", "r")
    myText = fh.read().replace("\n"," ")
    language = 'en'
    output = gTTS(text=myText, lang=language, slow=False)
    output.save("output.mp3") #play sound
    fh.close()

def instant():
    saveText()
    createSoundFile()
    playSound()

def playSound():
    pygame.mixer.music.load("output.mp3")
    pygame.mixer.music.play(loops=0)
def stopSound():
    pygame.mixer.music.stop()
def pauseSound():
    pygame.mixer.music.pause()
def unpauseSound():
    pygame.mixer.music.unpause()


#label = text only
l1 = tk.Label(root, text="Text to Speech",font=('Arial',18))
l1.pack(anchor="n",padx=25,pady=10)

txtbox = tk.Text(root,width=20,bg="white",font=('Arial',13))
txtbox.pack(anchor="n",fill=tk.X,padx=50,pady=50)

bt1 =tk.Button(root, text="Play",bg="green",font=('Times New Roman',18),command=playSound)
bt1.pack(side="left",padx=10,ipadx=50)

bt2 =tk.Button(root, text="Stop",bg="green",font=('Times New Roman',18),command=stopSound)
bt2.pack(side="left",padx=10,ipadx=50)

bt3 =tk.Button(root, text="Pause",bg="green",font=('Times New Roman',18),command=pauseSound)
bt3.pack(side="left",padx=10,ipadx=50)
bt3 =tk.Button(root, text="Unpause",bg="green",font=('Times New Roman',18),command=unpauseSound)
bt3.pack(side="left",padx=10,ipadx=50)

bt4 =tk.Button(root, text="Instant",bg="green",font=('Times New Roman',18),command=instant)
bt4.pack(side="right",padx=10,ipadx=50)









root.mainloop() # runner