from tkinter import *
import os

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=10, pady=20)

# Label
my_label = Label(text="This Is Label...", font=("Arial", 24, "bold", "italic"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")
# my_label.place(x=100, y=0)
# my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


# Button

def button_clicked():
    print("I Got Clicked...")
    new_text = input.get()
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=new_text)


button = Button(text="Click Me", command=button_clicked)
button.pack()
# button.grid(column=1, row=1)

# new_button = Button(text="New Button")
# new_button.grin(column=2, row=0)



# Entry

input = Entry(width=25)
input.insert(END, string="Some Text To Begin With")
input.pack()
input.get()

# input.grid(column=3, row=2)

# Text

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example Of Multi-Line Text Entry...")
print(text.get("1.0", END))
text.pack()


# Spin Box

def spinbox_used():
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale

def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Check Button

def checkbutton_used():
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is On ?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radio Button

def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=1, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# List Box

def listbox_used(event):
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
names = ["Akhilesh", "Bhaskar", "Chandra", "Dheeraj"]

for item in names:
    listbox.insert(names.index(item), item)
listbox.bind("<<ListBoxSelected>>", listbox_used)
listbox.pack()
window.mainloop()

# import turtle
#
# tim = turtle.Turtle()
# tim.shape("turtle")
# tim.write("Some Text...", font=("Times New Roman", 50, "bold"))

window.mainloop()
