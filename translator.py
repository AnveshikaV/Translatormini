from tkinter import *
from tkinter import ttk
from googletrans import LANGUAGES, Translator

def change(text, src , dest):
    text1 = text 
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text1, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0,END)
    textget = change(text= masg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Tranlator")
root.geometry("500x600")
root.config(bg="grey")

lab_txt = Label(root,text= "Translator",font=("Time New Roman", 40, "bold"))
lab_txt.place(x=100, y=40, height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)


lab_txt = Label(root,text= "Source text",font=("Time New Roman", 20, "bold"), fg="Black", bg="grey")
lab_txt.place(x=100, y=100, height=20,width=300)

Sor_txt = Text(frame,font=("Time New Roman", 10, "bold"))
Sor_txt.pack()
Sor_txt.place(x=10, y=130, height=100,width=480)


list_text = list(LANGUAGES.values())

comb_sor= ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10,y=300,height=40,width=150)
comb_sor.set("en")

button_change = Button(frame, text= "Translate", relief=RAISED, command=data)
button_change.place(x=170,y=300, height=40,width=150)

comb_dest= ttk.Combobox(frame, value=list_text)
comb_dest.place(x=330,y=300,height=40,width=150)
comb_dest.set("en")

lab_txt = Label(root,text= "Dest text",font=("Time New Roman", 20, "bold"), fg="Black", bg="grey")
lab_txt.place(x=100, y=350, height=20,width=300)

dest_txt = Text(frame, font=("Time New Roman",10,"bold"))
dest_txt.pack()
dest_txt.place(x=10,y=400,height=150,width=480)

root.mainloop()