#python 2.7
from Tkinter import *
import ttk
import tkMessageBox
import tkFont
import math

#******** Main Config **********

main = Tk()
menu = Menu(main)
main.config(menu=menu)
main.title('Chauvet DJ Calculator')
main.geometry('500x300+50+50')

S_FONT=("Verdana", 8,)
M_FONT=("Verdana", 10)
LL_FONT=("Helvetica", 12 ,'bold')
L_FONT= tkFont.Font(family='Helvetica',size=12, weight='bold')
helv36 = tkFont.Font(family='Helvetica',size=10, weight='bold')


ass = StringVar()
di = StringVar()
amps_pg2 = StringVar()
volts_pg2 = StringVar()
watts_pg2 = StringVar()
amps_pg3 = StringVar()
volts_pg3 = StringVar()
PF_pg3 = StringVar()
watts_pg3 = StringVar()
fval = StringVar()
watts_val_pg2 = StringVar()



Vport_over=12451840
VPort = 655360
VividDrive23N_Port_Count = 2
wallW = StringVar()
wallH = StringVar()
wallW.set(1)
wallH.set(1)

VP4= IntVar()
VF3= IntVar()
VC6 = IntVar()

P4 = [104,208]
F4 = [104,208]
F3 = [128,256]
C6 =  [80,160]
V1 =  []
VividDrive23N = V1

def about1():
    tkMessageBox.showinfo('About',
                          'Hello \nSoftware Version V1.0, Python V2.7  \nIf you have any questions please contact me at \n'
                          'Dgooch@chauvetlighting.com ')

#******** Menu Config **********
subMenu = Menu(menu,tearoff=0)
menu.add_cascade(label="File", menu=subMenu,)
subMenu.add_command(label="Exit", command=quit)

helpMenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About" ,command=about1)

def test():
    global V1
    if VP4.get() == 1:
        global V1
        V1 = [104,208]
        print V1
        return  V1

    elif VP4.get() == 2:
        global V1
        V1 = [128,256]
        print V1
        return V1
    elif VP4.get() == 3:
        global V1
        V1 = [80,160]
        print V1
        return V1
    else:
        w = VP4.get()
        print w
def test2():
    global V1
    print  V1
def cal1 ():
    val2 = 67.4
    s = ass.get()
    d = di.get()
    val1 = (float (d) * float(d) * 3.14 / 4)
    val2 = (float (s) * val1 )
    #print val2
    #print val1
    #print "val2 Val is %s" %val2
    Arealable = Label(page1, text="Approximate diameter of %s of strands:" %s,font=helv36) .grid(row=3,columnspan=2, )
    Arealable2 = Label(page1, text= val2,font=helv36).grid(row=3, column=3, )
   # Arealable3  =  Label(Main, text= "0000 (4/0)").grid(row=, column=3,)
    if float(val2) >= 107:
        #print "0000 (4/0)"
        Arealable3 = Label(page1, text="0000 (4/0)",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 85.0 and (val2) < 107:
        #print "000 (3/0)"
        Arealable3 = Label(page1, text="000 (3/0)",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 67.4 and (val2) < 85.0:
        #print "00 (2/0)"
        Arealable3 = Label(page1, text="00 (2/0",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 53.5 and (val2) < 67.4:
        #print "0 (1/0)"
        Arealable3 = Label(page1, text="0 (1/0)",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 42.4 and (val2) < 53.5:
        #print "1 AWG"
        Arealable3 = Label(page1, text="1 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 33.6 and (val2) < 42.4:
        #print "2 AWG"
        Arealable3 = Label(page1, text="2 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 26.7 and (val2) < 33.6:
        #print "3 AWG"
        Arealable3 = Label(page1, text="3 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 21.2 and (val2) < 26.7:
        #print "4 AWG"
        Arealable3 = Label(page1, text="4 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 16.8 and (val2) < 21.2:
        #print "5 AWG"
        Arealable3 = Label(page1, text="5 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 13.3 and (val2) < 16.8:
        #print "6 AWG"
        Arealable3 = Label(page1, text="6 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 10.5 and (val2) < 13.3:
        #print "7 AWG"
        Arealable3 = Label(page1, text="7 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 8.37 and (val2) < 10.5:
        #print "8 AWG"
        Arealable3 = Label(page1, text="8 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 6.63 and (val2) < 8.37:
        #print "9 AWG"
        Arealable3 = Label(page1, text="9 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 5.26 and (val2) < 6.63:
        #print "10 AWG"
        Arealable3 = Label(page1, text="10 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 4.17 and (val2) < 5.26:
        #print "11 AWG"
        Arealable3 = Label(page1, text="11 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 3.31 and (val2) < 4.17:
        #print "12 AWG"
        Arealable3 = Label(page1, text="12 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 2.62 and (val2) < 3.31:
        #print "13 AWG"
        Arealable3 = Label(page1, text="13 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 2.08 and (val2) < 2.62:
        #print "14 AWG"
        Arealable3 = Label(page1, text="14 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 1.65 and (val2) < 2.08:
        #print "15 AWG"
        Arealable3 = Label(page1, text="15 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 1.31 and (val2) < 1.65:
        #$print "16 AWG"
        Arealable3 = Label(page1, text="16 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 1.04 and (val2) < 1.31:
        #print "17 AWG"
        Arealable3 = Label(page1, text="17 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.823 and (val2) < 1.04:
        #print "18 AWG"
        Arealable3 = Label(page1, text="18 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.653 and (val2) < 0.823:
        #print "19 AWG"
        Arealable3 = Label(page1, text="19 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.518 and (val2) < 0.653:
        #print "20 AWG"
        Arealable3 = Label(page1, text="20 AWG)",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.410 and (val2) < 0.518:
        #print "21 AWG"
        Arealable3 = Label(page1, text="21 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.326 and (val2) < 0.410:
        #print "22 AWG"
        Arealable3 = Label(page1, text="22 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.258 and (val2) < 0.326:
        #print "23 AWG"
        Arealable3 = Label(page1, text="23 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.205 and (val2) < 0.258:
        #print "24 AWG"
        Arealable3 = Label(page1, text="24 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.162 and (val2) < 0.205:
        #print "25 AWG"
        Arealable3 = Label(page1, text="25 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.129 and (val2) < 0.162:
        #print "26 AWG"
        Arealable3 = Label(page1, text="26 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.102 and (val2) < 0.129:
        #print "27 AWG"
        Arealable3 = Label(page1, text="27 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.0810 and (val2) < 0.102:
        #print "28 AWG"
        Arealable3 = Label(page1, text="28 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.0642 and (val2) < 0.0810:
        #print "29 AWG"
        Arealable3 = Label(page1, text="29 AWG",font=helv36).grid(row=4, column=1, )
    elif float(val2) >= 0.0509 and (val2) < 0.0642:
        #print "30 AWG"
        Arealable3 = Label(page1, text="30 AWG",font=helv36).grid(row=4, column=1, )
    else:
        print "IDK"
        Arealable3 = Label(page1, text="IDK", font=helv36).grid(row=4, column=1, )
def Reset_pg1():
    amps_pg2 = 0
    volts_pg2 = 0
    #print ('Reset')
    #Arealable2 = Label(page1, text= '                ').grid(row=3, column=1, )
    #Arealable2 = Label(page1, text='                ').grid(row=4, column=1, )
    #Arealable2 = Label(page1, text='                ').grid(row=4, column=2, )
    #Arealable2 = Label(page1, text='                ').grid(row=4, column=2, )
    #Arealable2.selection_clear()
def AtoW():
    amps = amps_pg2.get()
    volts = volts_pg2.get()
    watts_pg2 =  float (amps) * float(volts)
    watts_val_pg2.set(watts_pg2)
    return watts_val_pg2
def Reset_pg2():
    amps_pg2 = 0
    volts_pg2 = 0
    #print ('Reset')
    Arealable2 = Label(page2, text= '                ').grid(row=3, column=2, )
def Reset_pg3():
    amps_pg3 = 0
    volts_pg3 = 0
    #print ('Reset')
def wallcal ():



    W = wallW.get()
    H = wallH.get()
    P_With = V1[0]
    P_Height = V1[1]
    CAL = int(W) * int(P_With)
    CAL2 = int (H) * int (P_Height)
    CAL3 = CAL * CAL2 #Total LEDs For Wall
    CAL4 = CAL3 / float (VPort)
    CAL5 = "{0:.2f}".format(CAL4)



    Arealable = Label(page4, text="Wall Width(pixels)").grid(row=3, columnspan=7, )
    Arealable2 = Label(page4, text=CAL).grid(row=3, column=8, )
    Arealable2 = Label(page4, text="Wall Height(pixels)").grid(row=4, columnspan=7, )
    Arealable3 = Label(page4, text=CAL2).grid(row=4, column=8 )
    Arealable4 = Label(page4, text="Total LEDs For Wall").grid(row=5, columnspan=7, )
    Arealable5 = Label(page4, text=CAL3).grid(row=5, column=8, )
    Arealable6 = Label(page4, text="Ports Required").grid(row=6, columnspan=7, )
    Arealable7 = Label(page4, text=CAL5).grid(row=6, column=8, )

    if float (CAL3) <= float (VPort):
        print '1 Port Needed!'
        tkMessageBox.showinfo(title='Ports needed', message='you need 1 drivres and 1 port')
    elif float (CAL3) <= float (VPort) *2:
        tkMessageBox.showinfo(title= 'Ports needed', message= 'you need 1 drivres and 2 ports' )
    elif float (CAL3) <= float (VPort) *3:
        tkMessageBox.showinfo(title= 'Ports needed', message= 'you need 2 drivres and 3 port' )
    elif float (CAL3) <= float (VPort) *4:
        tkMessageBox.showinfo(title= 'Ports needed', message= 'you need 2 drivres and 4 ports' )
    elif float (CAL3) <= float (VPort) *5:
        tkMessageBox.showinfo(title= 'Ports needed', message= 'you need 3 drivres and 5 port' )
def resetpg4():
    Arealable2 = Label(page4, text='          ').grid(row=3, column=2, )
    Arealable2 = Label(page4, text='          ').grid(row=4, column=2, )
    Arealable2 = Label(page4, text='                ').grid(row=5, column=2, )
    Arealable2 = Label(page4, text='                              ').grid(row=6, column=2, )
def wallmsg():
    def leavemini():
        popup.destroy()
    if  V1 == []:
        tkMessageBox.showinfo(title='Error', message='you need to select a Panel')

    else:
        L_FONT2 = tkFont.Font(family='Helvetica', size=12, weight='bold')

        popup = Tk()

        popup.title("Your Video Wall Info!")
        #popup.geometry('400x300')

        W = wallW.get()
        H = wallH.get()
        P_With = V1[0]
        P_Height = V1[1]
        CAL = int(W) * int(P_With)
        CAL2 = int(H) * int(P_Height)
        CAL3 = CAL * CAL2  # Total LEDs For Wall
        CAL4 = CAL3 / float(VPort)
        CAL5 = "{0:.2f}".format(CAL4)
        CAL6 = float (CAL5) / 2
        ports = math.ceil(CAL4)
        ports2 = "{0:.0f}".format(ports)
        drives = float (ports2) / 2
        drives2 = math.ceil(drives)
        drives3 = "{0:.0f}".format(drives2)
        #print "drive b4 round",drives
        #print "drive after round", drives2
        #print "drive after .- - stripted", drives3

        titallable_pg4 = Label(popup, text="Your Video Wall Info",font=LL_FONT ).grid(row=0, columnspan=5,pady=20)
        #Arealable0 = Label(pu, text="Your Video Wall Info!",font=L_FONT).grid(row=0, column=0,padx=50,sticky="w"  )
        Arealable = Label(popup, text="Wall Width(pixels):",font=LL_FONT).grid(row=1,padx=10, column=0,sticky='w' )
        Arealable2 = Label(popup, text=CAL,font=LL_FONT, ).grid(row=1, column=2, sticky='w')
        Arealable2 = Label(popup, text="Wall Height(pixels):",font=LL_FONT).grid(row=2,padx=10, column=0, sticky='w')
        Arealable3 = Label(popup, text=CAL2,font=LL_FONT).grid(row=2, column=2,sticky='w')
        Arealable4 = Label(popup, text="Total LEDs For Wall:",font=LL_FONT).grid(row=3,padx=10, column=0,sticky='w')
        Arealable5 = Label(popup, text=CAL3,font=LL_FONT).grid(row=3, column=2, sticky='w')
        Arealable6 = Label(popup, text="Ports Required:",font=LL_FONT).grid(row=4,padx=10, column=0,sticky='w' )
        Arealable7 = Label(popup, text=ports2,font=LL_FONT).grid(row=4, column=2, sticky='w')
        Arealable8 = Label(popup, text="Derives Required:",font=LL_FONT).grid(row=5, padx=10, column=0,sticky='w' )
        Arealable9 = Label(popup, text=drives3,font=LL_FONT).grid(row=5, column=2, sticky='w')
        b1= ttk.Button(popup, text= "Okay", command=leavemini).grid(row=10,columnspan=5, pady=10,sticky='n')





        popup.mainloop()
def AtoW_AC():

    amps = amps_pg3.get()
    volts = volts_pg3.get()
    PF = PF_pg3.get()
    watts_pg3 =  float (PF) * float(amps) * float(volts)
    #fval= watts_pg3
    fval.set(watts_pg3)
    return fval
# gives weight to the cells in the grid
rows = 49
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
titallable_pg1 = Label (page1, text="Area of Conductors",font=L_FONT).grid(row=0, columnspan=3,pady=20)
dilable = Label (page1, text="Diameter of strand:",font=helv36).grid(row=1, )
dientry = Entry(page1, textvariable=di,font=helv36).grid(row=1, column=1)
asslable = Label (page1, text="Number of strands:",font=helv36).grid(row=2, )
assentry = Entry(page1, textvariable=ass,font=helv36).grid(row=2, column=1)
calbutton= ttk.Button (page1, text='OK', command=cal1).grid(row=2, column=3)

# Adds tab 2 of the notebook
page2 = ttk.Frame(nb)
nb.add(page2, text='DC Amps to Watts')
titallable_pg2 = Label (page2, text="DC Amps to Watts",font=L_FONT).grid(row=0, columnspan=3,pady=20)
amps_able_pg2 = Label (page2, text="Enter current in amps:",font=helv36).grid(row=1,sticky='w' )
amps_entry_pg2 = Entry(page2, textvariable=amps_pg2,font=helv36).grid(row=1, column=1)
volts_lable_pg2 = Label (page2, text="Enter voltage in volts:",font=helv36).grid(row=2, sticky='w' )
volts_entry_pg2 = Entry(page2, textvariable=volts_pg2,font=helv36).grid(row=2, column=1)
calbutton_pg2= ttk.Button (page2, text='OK', command=AtoW,).grid(row=2, column=3)
Arealable_pg2 = Label(page2, text="Power result in watts:" ,font=helv36).grid(row=5, columnspan=1,sticky='w'  )
Arealable2_pg2 = Label(page2, textvariable=watts_val_pg2,font=helv36 ).grid(row=5, column=1,sticky='w'  )

# Adds tab 3 of the notebook
page3 = ttk.Frame(nb)
nb.add(page3, text='AC Amps to Watts',)
titallable_pg3 = Label (page3, text="AC Amps to Watts",font=L_FONT).grid(row=0, columnspan=3,pady=20)
amps_able_pg3 = Label (page3, text="Enter current in amps:",font=helv36).grid(row=1,sticky='w' )
amps_entry_pg3 = Entry(page3, textvariable=amps_pg3,font=helv36).grid(row=1, column=1)
volts_lable_pg3 = Label (page3, text="Enter voltage in volts:",font=helv36).grid(row=2, sticky='w' )
volts_entry_pg3 = Entry(page3, textvariable=volts_pg3,font=helv36).grid(row=2, column=1)
PF_lable_pg3 = Label (page3, text="Please enter power factor from 0 to 1:",font=helv36).grid(row=3,sticky='w'  )
PF_entry_pg3 = Entry(page3, textvariable=PF_pg3,font=helv36).grid(row=3, column=1)
calbutton_pg3= ttk.Button (page3, text='OK', command=AtoW_AC,).grid(row=3, column=3)
Arealable_pg3 = Label(page3, text="Power result in watts:" ,font=helv36).grid(row=5, columnspan=1,sticky='w'  )
Arealable2_pg3 = Label(page3, textvariable=fval,font=helv36 ).grid(row=5, column=1,sticky='w'  )

# Adds tab 4 of the notebook
page4 = ttk.Frame(nb)
nb.add(page4, text='Video Wall')
titallable_pg4 = Label (page4, text="Video Wall Calculator",font=L_FONT).grid(row=0, columnspan=5,pady=20)
lable1_pg4 = Label (page4, text="Please pick a Panel", font=helv36).grid(row=1, column=1,   )
P4_check = Radiobutton(page4,text= "Vivid 4 / F4",font=helv36, variable=VP4 , value=1,command=test ).grid(row=2, column=1, padx=50,sticky="w")
F3_check = Radiobutton(page4,text= "  F3  ", font=helv36,variable=VP4, value=2, command=test).grid(row=3, column=1,padx=50,sticky="w")
C6_check =Radiobutton(page4,text= "  C6  ", font=helv36,variable=VP4, value=3, command=test).grid(row=4, column=1, padx=50,sticky="w" )
X1 = Label (page4, text="Wall Width:",font=helv36).grid(row=2, column=2)
X1E = Entry(page4, textvariable=wallW,font=helv36).grid(row=2, column=3)
X2 = Label (page4, text="Wall Height",font=helv36).grid(row=3,column=2 )
X2E = Entry(page4, textvariable=wallH,font=helv36).grid(row=3, column=3)
calbutton_pg4= ttk.Button (page4, text='OK', command=wallmsg).grid(row=4, column=3)

main.mainloop()
