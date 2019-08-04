from tkinter import *
from random import choice
import random
import string

root = Tk()
root.title("Password Generator")

answer_label =Label(root, text ="---")
answer_label.grid(row =0, column =0)

label1 =Label(root, text ="Enter Name:")
label1.grid(row =1, column =0)

txtbx =Entry(root)
txtbx.grid(row =1, column =1)

def find():
        if (txtbx.get() != ""):
                try:
                        ASCII=string.ascii_letters + string.digits + '@'
                        value=txtbx.get()
                        value_altered = ''.join(random.choice(ASCII) for letter in value)
                        answer_label.configure(text =value_altered)
                        status_label.configure(text ="successfully Generated")
                except:
                        status_label.configure(text ="invalid input, check your input types")
        else:
                status_label.configure(text ="fill in all the required fields")

button =Button(root, text="Generate", command= find)
button.grid(row =3, column =0, columnspan =2)

status_label =Label(root, height =5, width =25, bg ="black", fg ="#00FF00", text ="---", wraplength =150)
status_label.grid(row =4, column =0, columnspan =2)

root.mainloop()
