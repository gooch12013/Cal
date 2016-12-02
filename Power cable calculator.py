from Tkinter import *
import tkMessageBox
import serial
import ttk
import time
import math
from PIL import Image, ImageTk
import math
#******** Def's **********

def quit_pressed(self):
    quit()

def doNothing():
    print ("lol i am doing nothing")


def cal1 ():
    val2 = 67.4
    s = ass.get()
    d = di.get()
    val1 = (float (d) * float(d) * 3.14 / 4)
    val2 = (float (s) * val1 )
    print val2
    print val1
    print "val2 Val is %s" %val2
    Arealable = Label(Main, text="Approximate diameter of %s of strands:" %s) .grid(row=3,columnspan=2, )
    Arealable2 = Label(Main, text= val2).grid(row=3, column=3, )
   # Arealable3  =  Label(Main, text= "0000 (4/0)").grid(row=, column=3,)
    if float(val2) >= 107:
        print "0000 (4/0)"
        Arealable3 = Label(Main, text="0000 (4/0)").grid(row=4, column=1, )
    elif float(val2) >= 85.0 and (val2) < 107:
        print "000 (3/0)"
        Arealable3 = Label(Main, text="000 (3/0)").grid(row=4, column=1, )
    elif float(val2) >= 67.4 and (val2) < 85.0:
        print "00 (2/0)"
        Arealable3 = Label(Main, text="00 (2/0").grid(row=4, column=1, )
    elif float(val2) >= 53.5 and (val2) < 67.4:
        print "0 (1/0)"
        Arealable3 = Label(Main, text="0 (1/0)").grid(row=4, column=1, )
    elif float(val2) >= 42.4 and (val2) < 53.5:
        print "1 AWG"
        Arealable3 = Label(Main, text="1 AWG").grid(row=4, column=1, )
    elif float(val2) >= 33.6 and (val2) < 42.4:
        print "2 AWG"
        Arealable3 = Label(Main, text="2 AWG").grid(row=4, column=1, )
    elif float(val2) >= 26.7 and (val2) < 33.6:
        print "3 AWG"
        Arealable3 = Label(Main, text="3 AWG").grid(row=4, column=1, )
    elif float(val2) >= 21.2 and (val2) < 26.7:
        print "4 AWG"
        Arealable3 = Label(Main, text="4 AWG").grid(row=4, column=1, )
    elif float(val2) >= 16.8 and (val2) < 21.2:
        print "5 AWG"
        Arealable3 = Label(Main, text="5 AWG").grid(row=4, column=1, )
    elif float(val2) >= 13.3 and (val2) < 16.8:
        print "6 AWG"
        Arealable3 = Label(Main, text="6 AWG").grid(row=4, column=1, )
    elif float(val2) >= 10.5 and (val2) < 13.3:
        print "7 AWG"
        Arealable3 = Label(Main, text="7 AWG").grid(row=4, column=1, )
    elif float(val2) >= 8.37 and (val2) < 10.5:
        print "8 AWG"
        Arealable3 = Label(Main, text="8 AWG").grid(row=4, column=1, )
    elif float(val2) >= 6.63 and (val2) < 8.37:
        print "9 AWG"
        Arealable3 = Label(Main, text="9 AWG").grid(row=4, column=1, )
    elif float(val2) >= 5.26 and (val2) < 6.63:
        print "10 AWG"
        Arealable3 = Label(Main, text="10 AWG").grid(row=4, column=1, )
    elif float(val2) >= 4.17 and (val2) < 5.26:
        print "11 AWG"
        Arealable3 = Label(Main, text="11 AWG").grid(row=4, column=1, )
    elif float(val2) >= 3.31 and (val2) < 4.17:
        print "12 AWG"
        Arealable3 = Label(Main, text="12 AWG").grid(row=4, column=1, )
    elif float(val2) >= 2.62 and (val2) < 3.31:
        print "13 AWG"
        Arealable3 = Label(Main, text="13 AWG").grid(row=4, column=1, )
    elif float(val2) >= 2.08 and (val2) < 2.62:
        print "14 AWG"
        Arealable3 = Label(Main, text="14 AWG").grid(row=4, column=1, )
    elif float(val2) >= 1.65 and (val2) < 2.08:
        print "15 AWG"
        Arealable3 = Label(Main, text="15 AWG").grid(row=4, column=1, )
    elif float(val2) >= 1.31 and (val2) < 1.65:
        print "16 AWG"
        Arealable3 = Label(Main, text="16 AWG").grid(row=4, column=1, )
    elif float(val2) >= 1.04 and (val2) < 1.31:
        print "17 AWG"
        Arealable3 = Label(Main, text="17 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.823 and (val2) < 1.04:
        print "18 AWG"
        Arealable3 = Label(Main, text="18 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.653 and (val2) < 0.823:
        print "19 AWG"
        Arealable3 = Label(Main, text="19 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.518 and (val2) < 0.653:
        print "20 AWG"
        Arealable3 = Label(Main, text="20 AWG)").grid(row=4, column=1, )
    elif float(val2) >= 0.410 and (val2) < 0.518:
        print "21 AWG"
        Arealable3 = Label(Main, text="21 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.326 and (val2) < 0.410:
        print "22 AWG"
        Arealable3 = Label(Main, text="22 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.258 and (val2) < 0.326:
        print "23 AWG"
        Arealable3 = Label(Main, text="23 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.205 and (val2) < 0.258:
        print "24 AWG"
        Arealable3 = Label(Main, text="24 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.162 and (val2) < 0.205:
        print "25 AWG"
        Arealable3 = Label(Main, text="25 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.129 and (val2) < 0.162:
        print "26 AWG"
        Arealable3 = Label(Main, text="26 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.102 and (val2) < 0.129:
        print "27 AWG"
        Arealable3 = Label(Main, text="27 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.0810 and (val2) < 0.102:
        print "28 AWG"
        Arealable3 = Label(Main, text="28 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.0642 and (val2) < 0.0810:
        print "29 AWG"
        Arealable3 = Label(Main, text="29 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.0509 and (val2) < 0.0642:
        print "30 AWG"
        Arealable3 = Label(Main, text="30 AWG").grid(row=4, column=1, )
    else:
        print "IDK"

def about1():

        tkMessageBox.showinfo('About',
                              'Hello \nSoftware Version is 1.0  \nIf you have any questions please contact me at \n'
                              'Dgooch@chauvetlighting.com ' )

#********END Def's **********


#******** Main Config **********

root = Tk()
root.iconbitmap(default='Icon3.png.ico')
menu = Menu(root)
root.config(menu=menu)
root.geometry('350x150+400+200')
root.title('Power cable calculator')

ass = StringVar()
di = StringVar()




#******** END Main Config **********


#******** Menu Config **********
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="Exit", command=menu.quit)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About" ,command=about1)




#******** END Menu Config **********


#******** Main program **********
Main = Frame (root)


titallable = Label (Main, text="").grid(row=0, )



dilable = Label (Main, text="Diameter of strand:").grid(row=1, )
dientry = Entry(Main, textvariable=di).grid(row=1, column=1)


asslable = Label (Main, text="Number of strands:").grid(row=2, )
assentry = Entry(Main, textvariable=ass).grid(row=2, column=1)

calbutton= ttk.Button (Main, text='OK', command=cal1).grid(row=2, column=3)



Main.pack(side=TOP, fill=X)

#******** END Main program **********

root.mainloop()