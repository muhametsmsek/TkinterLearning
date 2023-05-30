import tkinter
#window
window =tkinter.Tk()
window.title("Python Tkinter")
window.minsize(width=450,height=300)

def click_button():
    user_input = my_entry.get() # ne yazarsak str olarak verir
    print(user_input)

#label (kullanıcıyıa metin göstermek)
my_label = tkinter.Label(text="this is a label", font=('Arial',20,"italic"))
my_label.config(bg="black",fg="white")
#my_label.pack(side="top")
#my_label.place(x = 0 ,y=0) #konum belirtmek için pack e alternatif
my_label.grid(row=0,column=0) # grid de konum belirlemek için bir alternatif
#button (buton oluşturmak)
my_button = tkinter.Button(text="this is a button", command=click_button) # command butona basınca ne olsun
#my_button.pack(side="top")
#my_button.place(x =225-44 , y =150-13)
#my_button.update()
#print(my_button.winfo_height())
#print(my_button.winfo_width())
my_button.grid(row=1,column=1)
#entry (kullanıcıya bir şey yazdırma )
my_entry =tkinter.Entry(width=20)
#my_entry.pack()
#my_entry.place(x= 199 , y = 199)
#print(my_entry.winfo_height())
#print(my_entry.winfo_width())
my_entry.grid(row=2,column=1)



window.mainloop()
