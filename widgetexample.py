from tkinter import *

window = Tk()
window.title("Tkinter Python")
window.minsize(width=600 , height=400)
window.config(padx=20,pady=20)
#label (text , metin oluşturma)
label=Label(text="my label")
label.config(bg="black")
label.config(fg="white")
label.config(padx=10,pady=10)
label.pack()


def button_clickend():
    print("button clickend")
    print(text.get("1.0",END))
    # 1 dediği hangi satırdan başladğı , 0 dediği hangi karakterden başladığı


#button
button = Button(text="button" , command = button_clickend)
button.config(padx=10,pady=10)
button.pack()
#entry
entry = Entry(width=20)
entry.pack()
entry.focus() # texte veya entry e dan başlayacağını belirler
#text
text = Text(width=30,height=10)
text.pack()
#scale (aşağı kaydır)
def scale_selected(value):
    print(value)
my_scale = Scale(from_= 0 , to = 50 , command=scale_selected)
my_scale.pack()

#spinbox
def spinbox_selected():
    print(my_spinbox.get())
my_spinbox = Spinbox(from_=0 , to=50 , command=spinbox_selected)
my_spinbox.pack()

#checkbutton
def checkbutton_selected():
    print(check_state.get())

check_state = IntVar()
my_checkbutton = Checkbutton(text="check",variable=check_state ,command=checkbutton_selected)
my_checkbutton.pack()
#radio button
def radio_selected(): # seçenek surma
    print(radio_checked_state.get())

radio_checked_state = IntVar()
my_radiobutton = Radiobutton(text="1. option",value=10,variable=radio_checked_state,command=radio_selected)
my_radiobutton_2 = Radiobutton(text="2. option",value=20,variable=radio_checked_state,command=radio_selected)
my_radiobutton.pack()
my_radiobutton_2.pack()

#listbox
def listbox_selected(event):
    print(my_listbox.get(my_listbox.curselection()))

my_listbox = Listbox()
name_list = ["Atil","ABC","KJF","DAŞMKAŞM","ALKCAŞMAŞ"]
for i in range(len(name_list)):
    my_listbox.insert(i,name_list[i])
my_listbox.bind('<<ListboxSelect>>',listbox_selected)
my_listbox.pack()

window.mainloop()