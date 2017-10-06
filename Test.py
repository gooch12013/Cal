from Tkinter import *

counter = 0

Main= Tk()

def fun1():
    global counter
    counter += 1
    label1.config(text=counter)
    print ( counter)

def fun2 ():
    global counter
    counter -= 1
    label1.config(text=counter)
    print ( counter)
def clear():
    label1.config(text=0.0 END)

label1=Label (Main, text="HOHO")
button1 =Button(Main, text="+ 1", command=fun1)
button2 =Button(Main, text="- 1", command=fun2)
button3=Button(Main,text='Clear', command=clear)



label1.pack()
button1.pack()
button2.pack()


Main.geometry('400x400+100+100')
Main.mainloop()
