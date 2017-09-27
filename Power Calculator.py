#python 2.7
from Tkinter import *
import ttk
import tkMessageBox


#******** Main Config **********

main = Tk()
menu = Menu(main)
main.config(menu=menu)
main.title('Power Calculator')
main.geometry('500x200')

ass = StringVar()
di = StringVar()
amps_pg2 = StringVar()
volts_pg2 = StringVar()
watts_pg2 = StringVar()
amps_pg3 = StringVar()
volts_pg3 = StringVar()
PF_pg3 = StringVar()
watts_pg3 = StringVar()

def about1():
    tkMessageBox.showinfo('About',
                          'Hello \nSoftware Version is 1.0 Python 2.7  \nIf you have any questions please contact me at \n'
                          'Dgooch@chauvetlighting.com ')

#******** Menu Config **********
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)

subMenu.add_command(label="Exit", command=menu.quit)

helpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About" ,command=about1)



def cal1 ():
    val2 = 67.4
    s = ass.get()
    d = di.get()
    val1 = (float (d) * float(d) * 3.14 / 4)
    val2 = (float (s) * val1 )
    print val2
    print val1
    print "val2 Val is %s" %val2
    Arealable = Label(page1, text="Approximate diameter of %s of strands:" %s) .grid(row=3,columnspan=2, )
    Arealable2 = Label(page1, text= val2).grid(row=3, column=3, )
   # Arealable3  =  Label(Main, text= "0000 (4/0)").grid(row=, column=3,)
    if float(val2) >= 107:
        print "0000 (4/0)"
        Arealable3 = Label(page1, text="0000 (4/0)").grid(row=4, column=1, )
    elif float(val2) >= 85.0 and (val2) < 107:
        print "000 (3/0)"
        Arealable3 = Label(page1, text="000 (3/0)").grid(row=4, column=1, )
    elif float(val2) >= 67.4 and (val2) < 85.0:
        print "00 (2/0)"
        Arealable3 = Label(page1, text="00 (2/0").grid(row=4, column=1, )
    elif float(val2) >= 53.5 and (val2) < 67.4:
        print "0 (1/0)"
        Arealable3 = Label(page1, text="0 (1/0)").grid(row=4, column=1, )
    elif float(val2) >= 42.4 and (val2) < 53.5:
        print "1 AWG"
        Arealable3 = Label(page1, text="1 AWG").grid(row=4, column=1, )
    elif float(val2) >= 33.6 and (val2) < 42.4:
        print "2 AWG"
        Arealable3 = Label(page1, text="2 AWG").grid(row=4, column=1, )
    elif float(val2) >= 26.7 and (val2) < 33.6:
        print "3 AWG"
        Arealable3 = Label(page1, text="3 AWG").grid(row=4, column=1, )
    elif float(val2) >= 21.2 and (val2) < 26.7:
        print "4 AWG"
        Arealable3 = Label(page1, text="4 AWG").grid(row=4, column=1, )
    elif float(val2) >= 16.8 and (val2) < 21.2:
        print "5 AWG"
        Arealable3 = Label(page1, text="5 AWG").grid(row=4, column=1, )
    elif float(val2) >= 13.3 and (val2) < 16.8:
        print "6 AWG"
        Arealable3 = Label(page1, text="6 AWG").grid(row=4, column=1, )
    elif float(val2) >= 10.5 and (val2) < 13.3:
        print "7 AWG"
        Arealable3 = Label(page1, text="7 AWG").grid(row=4, column=1, )
    elif float(val2) >= 8.37 and (val2) < 10.5:
        print "8 AWG"
        Arealable3 = Label(page1, text="8 AWG").grid(row=4, column=1, )
    elif float(val2) >= 6.63 and (val2) < 8.37:
        print "9 AWG"
        Arealable3 = Label(page1, text="9 AWG").grid(row=4, column=1, )
    elif float(val2) >= 5.26 and (val2) < 6.63:
        print "10 AWG"
        Arealable3 = Label(page1, text="10 AWG").grid(row=4, column=1, )
    elif float(val2) >= 4.17 and (val2) < 5.26:
        print "11 AWG"
        Arealable3 = Label(page1, text="11 AWG").grid(row=4, column=1, )
    elif float(val2) >= 3.31 and (val2) < 4.17:
        print "12 AWG"
        Arealable3 = Label(page1, text="12 AWG").grid(row=4, column=1, )
    elif float(val2) >= 2.62 and (val2) < 3.31:
        print "13 AWG"
        Arealable3 = Label(page1, text="13 AWG").grid(row=4, column=1, )
    elif float(val2) >= 2.08 and (val2) < 2.62:
        print "14 AWG"
        Arealable3 = Label(page1, text="14 AWG").grid(row=4, column=1, )
    elif float(val2) >= 1.65 and (val2) < 2.08:
        print "15 AWG"
        Arealable3 = Label(page1, text="15 AWG").grid(row=4, column=1, )
    elif float(val2) >= 1.31 and (val2) < 1.65:
        print "16 AWG"
        Arealable3 = Label(page1, text="16 AWG").grid(row=4, column=1, )
    elif float(val2) >= 1.04 and (val2) < 1.31:
        print "17 AWG"
        Arealable3 = Label(page1, text="17 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.823 and (val2) < 1.04:
        print "18 AWG"
        Arealable3 = Label(page1, text="18 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.653 and (val2) < 0.823:
        print "19 AWG"
        Arealable3 = Label(page1, text="19 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.518 and (val2) < 0.653:
        print "20 AWG"
        Arealable3 = Label(page1, text="20 AWG)").grid(row=4, column=1, )
    elif float(val2) >= 0.410 and (val2) < 0.518:
        print "21 AWG"
        Arealable3 = Label(page1, text="21 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.326 and (val2) < 0.410:
        print "22 AWG"
        Arealable3 = Label(page1, text="22 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.258 and (val2) < 0.326:
        print "23 AWG"
        Arealable3 = Label(page1, text="23 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.205 and (val2) < 0.258:
        print "24 AWG"
        Arealable3 = Label(page1, text="24 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.162 and (val2) < 0.205:
        print "25 AWG"
        Arealable3 = Label(page1, text="25 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.129 and (val2) < 0.162:
        print "26 AWG"
        Arealable3 = Label(page1, text="26 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.102 and (val2) < 0.129:
        print "27 AWG"
        Arealable3 = Label(page1, text="27 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.0810 and (val2) < 0.102:
        print "28 AWG"
        Arealable3 = Label(page1, text="28 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.0642 and (val2) < 0.0810:
        print "29 AWG"
        Arealable3 = Label(page1, text="29 AWG").grid(row=4, column=1, )
    elif float(val2) >= 0.0509 and (val2) < 0.0642:
        print "30 AWG"
        Arealable3 = Label(page1, text="30 AWG").grid(row=4, column=1, )
    else:
        print "IDK"

def AtoW():
    amps = amps_pg2.get()
    volts = volts_pg2.get()
    watts_pg2 =  float (amps) * float(volts)
    #print watts_pg2
    Arealable = Label(page2, text="Power result in watts:" ).grid(row=3, columnspan=1, )
    Arealable2 = Label(page2, text=watts_pg2 ) .grid(row=3, column=2, )
    rest_button_pg2 = ttk.Button(page2, text='Reset', command=Reset_pg2).grid(row=3, column=3)

def Reset_pg2():
    amps_pg2 = 0
    volts_pg2 = 0
    #print ('Reset')
    Arealable2 = Label(page2, text= '                ').grid(row=3, column=2, )

def AtoW_AC():
    amps = amps_pg3.get()
    volts = volts_pg3.get()
    PF = PF_pg3.get()
    watts_pg3 =  float (PF) * float(amps) * float(volts)
    #print watts_pg2
    Arealable = Label(page3, text="Power result in watts:" ).grid(row=5, columnspan=1, )
    Arealable2 = Label(page3, text=watts_pg3 ) .grid(row=5, column=2, )
    rest_button_pg3 = ttk.Button(page3, text='Reset', command=Reset_pg3).grid(row=5, column=3)

def Reset_pg3():
    amps_pg3 = 0
    volts_pg3 = 0
    #print ('Reset')

    Arealable2 = Label(page3, text= '         ').grid(row=5, column=2, )


# gives weight to the cells in the grid

rows = 0
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

# Adds tab 1 of the notebook
page1 = ttk.Frame(nb)
nb.add(page1, text='Area of Conductors')
titallable = Label (page1, text="").grid(row=0, )
dilable = Label (page1, text="Diameter of strand:").grid(row=1, )
dientry = Entry(page1, textvariable=di).grid(row=1, column=1)
asslable = Label (page1, text="Number of strands:").grid(row=2, )
assentry = Entry(page1, textvariable=ass).grid(row=2, column=1)
calbutton= ttk.Button (page1, text='OK', command=cal1).grid(row=2, column=3)


# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='DC Amps to Watts')

titallable_pg2 = Label (page2, text="").grid(row=0, )
amps_able_pg2 = Label (page2, text="Enter current in amps:").grid(row=1, )
amps_entry_pg2 = Entry(page2, textvariable=amps_pg2).grid(row=1, column=1)
volts_lable_pg2 = Label (page2, text="Enter voltage in volts:").grid(row=2, )
volts_entry_pg2 = Entry(page2, textvariable=volts_pg2).grid(row=2, column=1)
calbutton_pg2= ttk.Button (page2, text='OK', command=AtoW).grid(row=2, column=3)




# Adds tab 3 of the notebook
page3 = ttk.Frame(nb)
nb.add(page3, text='AC Amps to Watts')
titallable_pg3 = Label (page3, text="").grid(row=0, )
amps_able_pg3 = Label (page3, text="Enter current in amps:").grid(row=1, )
amps_entry_pg3 = Entry(page3, textvariable=amps_pg3).grid(row=1, column=1)
volts_lable_pg3 = Label (page3, text="Enter voltage in volts:").grid(row=2, )
volts_entry_pg3 = Entry(page3, textvariable=volts_pg3).grid(row=2, column=1)
PF_lable_pg3 = Label (page3, text="Please enter power factor from 0 to 1:").grid(row=3, )
PF_entry_pg3 = Entry(page3, textvariable=PF_pg3).grid(row=3, column=1)
calbutton_pg3= ttk.Button (page3, text='OK', command=AtoW_AC).grid(row=3, column=3)







main.mainloop()
