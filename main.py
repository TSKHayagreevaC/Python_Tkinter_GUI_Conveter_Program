import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="This Is Label...", font=("Arial", 24, "bold", "italic"))
my_label.pack(expand=True)

import turtle

tim = turtle.Turtle()
tim.shape("turtle")
tim.write()

window.mainloop()
