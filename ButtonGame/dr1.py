import tkinter
import random

window = tkinter.Tk()
window.minsize(550,550)
label = tkinter.Label(window, text="Score: 0")
label.place(x=0, y=0)
counter = 0
counter2 = 0
seconds = 30
label2 = tkinter.Label(window, text="Timer: %s" % seconds)
label2.place(x=0, y=20)

button = tkinter.Button(window, text="Start")
button2 = tkinter.Button(window, text="Bonus")
button.place(x=100, y=100)

def onClick():
    global counter2
    global counter
    global label
    global button
    if button2["text"] == "Bonus":
        button2.after(1000, onTimer)
        button2["text"] = "Get that BONUS"
        counter=counter2*2
    if button["text"] == "Start":
        button.after(1000, onTimer)
        button["text"] = "Click"
    counter2 += 1
    counter3=counter2+counter
    label["text"]="Score: %s" % counter3
    button.place(x=random.randint(0, 500), y=random.randint(0, 500))
    button2.place(x=random.randint(0, 1000), y=random.randint(0, 1000))
button.configure(command = onClick)
button2.configure(command= onClick)
def onTimer():
    global label2
    global button
    global button2
    global seconds
    seconds -= 1
    label2["text"] = "Timer: %s" % seconds
    if seconds <= 0:
        button.config(state='disabled')
    else:
        button.after(1000, onTimer)

window.mainloop()
