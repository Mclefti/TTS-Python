import tkinter as tk

root = tk.Tk()

root.geometry("500x500") # size of window
root.title("Text to Speech") # window Tittle

#label = text only
label = tk.Label(root, text="Text to Speech",font=('Arial',18))
label.pack(padx=20,pady=20)

button = tk.Button(root,text="Click Me!",font=("Arial",10))
button.pack()
#textbox == get text from here
textbox = tk.Text(root,font=('Arial',16))
textbox.pack(padx=20)


root.mainloop() # runner