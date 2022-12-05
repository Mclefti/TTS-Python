import tkinter as tk # used as GUI maker
import pygame # use to play sound in app
from gtts import gTTS # use to make .mp3 file


#App inherits from tkinter
class App(tk.Frame):

 def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        pygame.mixer.init()
        fh = open("sound.txt", "a")
        p_button = tk.PhotoImage(file = "p_but.png")


        #functions
        def saveText(): # save text at sound.txt
            fh = open("sound.txt", "w")
            txtbox_text = txtbox.get("1.0",'end-1c')
            fh.write(txtbox_text)
            fh.close()

        def createSoundFile(): #create .txt file
            fh = open("sound.txt", "r")
            myText = fh.read().replace("\n"," ")
            language = 'en'
            output = gTTS(text=myText, lang=language, slow=False)
            output.save("output.mp3") #play sound
            fh.close()
        
        def instant(): 
            pygame.mixer.music.unload()
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
        l1 = tk.Label(root, text="Text to Speech",bg="#d6ecf3",font=('Copperplate Gothic Bold',30))
        l1.pack(anchor="n",padx=20,pady=10, ipadx=100)

        txtbox = tk.Text(root,width=20,bg="#ffffea",font=('montserrat',13))
        txtbox.pack(anchor="n",fill=tk.X,padx=50,pady=10)

        bt1 =tk.Button(root, text="Play" ,bg="#d4f0f0",font=('Elephant',18),command=playSound)
        bt1.pack(side="left",padx=20,ipadx=50)

        bt2 =tk.Button(root, text="Stop",bg="#8fcaca",font=('Elephant',18),command=stopSound)
        bt2.pack(side="left",padx=20,ipadx=50)

        bt3 =tk.Button(root, text="Pause",bg="#cce2cb",font=('Elephant',18),command=pauseSound)
        bt3.pack(side="left",padx=20,ipadx=50)
        bt3 =tk.Button(root, text="Unpause",bg="#b6cfb6",font=('Elephant',18),command=unpauseSound)
        bt3.pack(side="left",padx=20,ipadx=50)

        bt4 =tk.Button(root, text="Instant",bg="#97c1a9",font=('Elephant',18),command=instant)
        bt4.pack(side="right",padx=60,ipadx=50)






if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720") # size of window
    root.title("Text to Speech") # window Tittle
    root.config(bg="#d6ecf3")
    App(root).pack(fill="both", expand=True)
    root.mainloop()

 
