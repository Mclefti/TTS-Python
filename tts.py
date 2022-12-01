from gtts import gTTS
import os

#Input getting from test.txt
fh = open("test.txt", "r")
myText = fh.read().replace("\n"," ")

language = 'en'

output = gTTS(text=myText, lang=language, slow=False)


output.save("output.mp3") #play sound
fh.close()
os.system("start output.mp3")