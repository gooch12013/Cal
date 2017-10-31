#python 3.4
from tkinter import *
import tkinter.ttk
import tkinter.messagebox
import tkinter.font
from tkinter import filedialog
import math
from fractions import gcd


#******** Main Config **********

main = Tk()
menu = Menu(main)
main.config(menu=menu)
main.iconbitmap(default='logo2.ico')
main.title('Chauvet Video Wall Calculator')
main.geometry('600x400')

S_FONT=("Verdana", 8,)
M_FONT=("Verdana", 10)
LL_FONT=("Helvetica", 12 ,'bold')
L_FONT= tkinter.font.Font(family='Helvetica',size=12, weight='bold')
helv36 = tkinter.font.Font(family='Helvetica',size=10, weight='bold')

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
Pn = IntVar()
V2 = []
Power=[]
Widthft = StringVar()
Heightft = StringVar()
Widthm = StringVar()
Heightm = StringVar()
Widthm.set(0)
Heightm.set(0)
NPW = StringVar()
NPH = StringVar()
TNP = StringVar()
NPH.set(0)
NPW.set(0)
TNC=StringVar()
Res = StringVar()
AR = StringVar()

def about1():
    tkinter.messagebox.showinfo('About',
                          'Hello \nSoftware Version V1.0, Python V2.7  \nIf you have any questions please contact me at \n'
                          'Dgooch@chauvetlighting.com ')

def quitprogram():
    main.destroy()
    quit()

#******** Menu Config **********
subMenu = Menu(menu,tearoff=0)
menu.add_cascade(label="File", menu=subMenu,)
subMenu.add_command(label="Exit", command=quitprogram)

helpMenu = Menu(menu,tearoff=0)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About" ,command=about1)

def cal_pg4():
    global V1
    if VP4.get() == 1:

        V1 = [104,208]
       # print(V1)
        return  V1

    elif VP4.get() == 2:

        V1 = [128,256]
       # print(V1)
        return V1
    elif VP4.get() == 3:

        V1 = [80,160]
        #print(V1)
        return V1
    else:
        w = VP4.get()
        #print(w)

def cal_pg5():
    global V2
    global Power
    if Pn.get() == 1:
        # 104 is pix wide 208 is pix high and 4 is number of panels in a case
        V2 = [104,208,4]
        # PL 120 | PL 230 | PL 208| amps 120 | amps 230 | amps 208 |Vertical Hang limit | Weight lb | Weight kg
        Power =[7, 13, 12, 2.3, 1.2, 1.3 ,23 ,27.6 ,12.5 ]
       # print(V2, Power)
        return  V2

    elif Pn.get() == 2:

        V2 = [128,256,4]
        # PL 120 | PL 230 | PL 208| amps 120 | amps 230 | amps 208 |Vertical Hang limit | Weight lb | Weight kg
        Power = [8,15,14,2.18,1.16,1.28, 16 ,28, 13]
        #print(V2, Power)
        return V2

    elif Pn.get() == 3:

        V2 = [80,160,4]
        # PL 120 | PL 230 | PL 208| amps 120 | amps 230 | amps 208 |Vertical Hang limit | Weight lb | Weight kg
        Power = [12,22,21,1.06,.60,.63,1,23,10.4]
        #print(V2, Power)
        return V2

    elif Pn.get() == 4:
        V2 = [104, 208, 4]
        # PL 120 | PL 230 | PL 208| amps 120 | amps 230 | amps 208 |Vertical Hang limit | Weight lb | Weight kg
        Power = [7, 12, 13, 2.05 , 1.19, 1.27 ,16 ,27.6 ,12.5 ]
        #print(V2, Power)
        return V2
    else:
        w = Pn.get()
        #print(w)

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
        print('1 Port Needed!')
        tkinter.messagebox.showinfo(title='Ports needed', message='you need 1 drivres and 1 port')
    elif float (CAL3) <= float (VPort) *2:
        tkinter.messagebox.showinfo(title= 'Ports needed', message= 'you need 1 drivres and 2 ports' )
    elif float (CAL3) <= float (VPort) *3:
        tkinter.messagebox.showinfo(title= 'Ports needed', message= 'you need 2 drivres and 3 port' )
    elif float (CAL3) <= float (VPort) *4:
        tkinter.messagebox.showinfo(title= 'Ports needed', message= 'you need 2 drivres and 4 ports' )
    elif float (CAL3) <= float (VPort) *5:
        tkinter.messagebox.showinfo(title= 'Ports needed', message= 'you need 3 drivres and 5 port' )

def wallmsg():
    def leavemini():
        popup.destroy()
    if  V1 == []:
        tkinter.messagebox.showinfo(title='Error', message='you need to select a Panel')

    else:
        L_FONT2 = tkinter.font.Font(family='Helvetica', size=12, weight='bold')

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
        Arealable8 = Label(popup, text="Drives Required:",font=LL_FONT).grid(row=5, padx=10, column=0,sticky='w' )
        Arealable9 = Label(popup, text=drives3,font=LL_FONT).grid(row=5, column=2, sticky='w')
        b1= tkinter.ttk.Button(popup, text= "Okay", command=leavemini).grid(row=10,columnspan=5, pady=10,sticky='n')





        popup.mainloop()

def wallmsg_pg5():
    def leavemini():
        popup.destroy()



    if  V2 == []:
        print("Leave min",V2)
        tkinter.messagebox.showinfo(title='Error', message='you need to select a Panel',)

    else:
        L_FONT2 = tkinter.font.Font(family='Helvetica', size=12, weight='bold')
        popup = Tk()
        popup.title("Your Video Wall Info!")
        popup.geometry('600x700')


        Wf = Widthft.get()
        Hf = Heightft.get()
        W = float(Wf)* 0.3048
        H = float(Hf)* 0.3048

        RW = math.trunc(W)*2
        RH = math.trunc(H)
        TP = RW * RH
        P_With = V2[0]
        P_Height = V2[1]
        # PL 120 | PL 230 | PL 208| amps 120 | amps 230 | amps 208 |Vertical Hang limit | Weight lb | Weight kg
        PL120= Power[0]
        PL230= Power[1]
        PL208= Power[2]
        amps120=Power[3]
        amps230=Power[4]
        amps208=Power[5]
        VHL= Power[6]
        Wlb=Power[7]
        Wkg=Power[8]
        PPC = V2[2]
        Cases1 = math.ceil(TP)
        Cases2 = math.ceil(Cases1/PPC)


        CAL = (RW) * int(P_With)
        CAL2 = (RH) * int(P_Height)
        CAL3 = CAL * CAL2  # Total LEDs For Wall
        CAL4 = CAL3 / float(VPort)
        CAL5 = "{0:.2f}".format(CAL4)
        CAL6 = float (CAL5) / 2

        ports = math.ceil(CAL4)
        ports2 = "{0:.0f}".format(ports)
        drives = float (ports2) / 2
        drives2 = math.ceil(drives)
        drives3 = "{0:.0f}".format(drives2)

        Resolution = CAL,"X", CAL2
        WIF= RW/2 * 3.2808399
        HIF= RH * 3.2808399

        R1= RW*P_With
        GCD1= gcd(RW*P_With,P_Height*RH)
        R2= R1/GCD1
        RD= "{0:.0f}".format(R2)

        R3= RH*P_Height
        GCD2 = gcd(RW*P_With,RH*P_Height)
        R4= R3/GCD2
        RD2 ="{0:.0f}".format(R4)
        AspectRatio = RD,"/",RD2

        PL120cal= math.ceil (TP / PL120)
        PL230cal = math.ceil (TP / PL230)
        PL208cal = math.ceil (TP / PL208)
        amps120Cal= math.ceil(TP * amps120)
        amps230Cal = math.ceil (TP * amps230)
        amps208Cal = math.ceil(TP * amps208)
        WlbCal= math.ceil(TP * Wlb)
        WkgCal = math.ceil(TP * Wkg)

        if RH > VHL:
            tkinter.messagebox.showinfo(title='Error', message='Warning you are Over Vertical Limit')

        titallable_pg4 = Label(popup, text="Your Video Wall Info",font=LL_FONT ).grid(row=0, columnspan=5,pady=20)

        Arealable1 = Label(popup, text="Wall Resolution:", font=LL_FONT).grid(row=1, padx=10, column=0, sticky='w')
        Arealable2 = Label(popup, text=Resolution, font=LL_FONT, ).grid(row=1, column=2, sticky='w')

        Arealable3 = Label(popup, text="Aspect Ratio:", font=LL_FONT).grid(row=2, padx=10, column=0, sticky='w')
        Arealable4 = Label(popup, text=AspectRatio, font=LL_FONT, ).grid(row=2, column=2, sticky='w')

        Arealable5 = Label(popup, text="Wall Width(pixels):",font=LL_FONT).grid(row=3,padx=10, column=0,sticky='w' )
        Arealable6 = Label(popup, text=CAL,font=LL_FONT, ).grid(row=3, column=2, sticky='w')

        Arealable7 = Label(popup, text="Wall Height(pixels):",font=LL_FONT).grid(row=4,padx=10, column=0, sticky='w')
        Arealable8 = Label(popup, text=CAL2,font=LL_FONT).grid(row=4, column=2,sticky='w')

        Arealable9 = Label(popup, text="Total LEDs For Wall:",font=LL_FONT).grid(row=5,padx=10, column=0,sticky='w')
        Arealable10 = Label(popup, text=CAL3,font=LL_FONT).grid(row=5, column=2, sticky='w')

        Arealable11 = Label(popup, text="Ports Required:",font=LL_FONT).grid(row=6,padx=10, column=0,sticky='w' )
        Arealable12 = Label(popup, text=ports2,font=LL_FONT).grid(row=6, column=2, sticky='w')

        Arealable13 = Label(popup, text="Drives Required:",font=LL_FONT).grid(row=7, padx=10, column=0,sticky='w' )
        Arealable14 = Label(popup, text=drives3,font=LL_FONT).grid(row=7, column=2, sticky='w')

        Arealable15 = Label(popup, text="Number of Panel Wide:", font=LL_FONT).grid(row=8, padx=10, column=0, sticky='w')
        Arealable16 = Label(popup, text=RW, font=LL_FONT, ).grid(row=8, column=2, sticky='w')

        Arealable17 = Label(popup, text="Number of Panel High:", font=LL_FONT).grid(row=9, padx=10, column=0,sticky='w')
        Arealable18 = Label(popup, text=RH, font=LL_FONT, ).grid(row=9, column=2, sticky='w')

        Arealable19 = Label(popup, text="Total number of Panels:", font=LL_FONT).grid(row=10, padx=10, column=0,sticky='w')
        Arealable20 = Label(popup, text=TP, font=LL_FONT, ).grid(row=10, column=2, sticky='w')

        Arealable21 = Label(popup, text="Total number of Cases:", font=LL_FONT).grid(row=11, padx=10, column=0, sticky='w')
        Arealable22 = Label(popup, text=Cases2, font=LL_FONT, ).grid(row=11, column=2, sticky='w')

        Arealable23 = Label(popup, text="Power circuit needed @ 120V:", font=LL_FONT).grid(row=12, padx=10, column=0,sticky='w')
        Arealable24 = Label(popup, text=PL120cal, font=LL_FONT, ).grid(row=12, column=2, sticky='w')

        Arealable25 = Label(popup, text="Power circuit needed @ 208V:", font=LL_FONT).grid(row=13, padx=10, column=0,sticky='w')
        Arealable26 = Label(popup, text=PL208cal, font=LL_FONT, ).grid(row=13, column=2, sticky='w')

        Arealable27 = Label(popup, text="Power circuit needed @ 230V:", font=LL_FONT).grid(row=14, padx=10, column=0,sticky='w')
        Arealable28 = Label(popup, text=PL230cal , font=LL_FONT, ).grid(row=14, column=2, sticky='w')

        Arealable29 = Label(popup, text="Total AMPS @ 120V:", font=LL_FONT).grid(row=15, padx=10, column=0,sticky='w')
        Arealable30 = Label(popup, text=amps120Cal, font=LL_FONT, ).grid(row=15, column=2, sticky='w')

        Arealable31 = Label(popup, text="Total Amps @ 208:", font=LL_FONT).grid(row=16, padx=10, column=0,sticky='w')
        Arealable32 = Label(popup, text= amps208Cal, font=LL_FONT, ).grid(row=16, column=2, sticky='w')

        Arealable33 = Label(popup, text="Total Amps @ 230:", font=LL_FONT).grid(row=17, padx=10, column=0,sticky='w')
        Arealable34 = Label(popup, text=amps230Cal, font=LL_FONT, ).grid(row=17, column=2, sticky='w')

        Arealable35 = Label(popup, text="Total Weight lb:", font=LL_FONT).grid(row=18, padx=10, column=0, sticky='w')
        Arealable36 = Label(popup, text=WlbCal, font=LL_FONT, ).grid(row=18, column=2, sticky='w')

        Arealable37 = Label(popup, text="Total Weight kg:", font=LL_FONT).grid(row=19, padx=10, column=0, sticky='w')
        Arealable39 = Label(popup, text=WkgCal, font=LL_FONT, ).grid(row=19, column=2, sticky='w')

        Arealable37 = Label(popup, text="Wall Width in Feet:", font=LL_FONT).grid(row=20, padx=10, column=0, sticky='w')
        Arealable39 = Label(popup, text=WIF, font=LL_FONT, ).grid(row=20, column=2, sticky='w')

        Arealable37 = Label(popup, text="Wall Height in Feet:", font=LL_FONT).grid(row=21, padx=10, column=0, sticky='w')
        Arealable39 = Label(popup, text=HIF, font=LL_FONT, ).grid(row=21, column=2, sticky='w')
        b1= tkinter.ttk.Button(popup, text= "Okay", command=leavemini).grid(row=30,columnspan=5, pady=10,sticky='n')

        def savefile1():

            Resolution1 = str(Resolution).replace("'","").replace("(","").replace(")","").replace(",","")
            AspectRatio1 = str(AspectRatio).replace("'","").replace("(","").replace(")","").replace(",","")
            CAL1= str(CAL)
            CAL22= str(CAL2)
            CAL32 = str(CAL3)
            ports22 = str(ports2)
            drives32 =str(drives3)
            RW2 =str(RW)
            RH2 = str(RH)
            TP2 = str(TP)
            Cases22= str(Cases2)
            PL120cal2 = str(PL120cal)
            PL208cal2 = str(PL208cal)
            PL230cal2 = str(PL230cal)
            amps120Cal2 = str(amps120Cal)
            amps208Cal2 = str(amps208Cal)
            amps230Cal2 = str (amps230Cal)
            WlbCal2 = str(WlbCal)
            WkgCal2 = str(WkgCal)
            WIF2 = str(WIF)
            HIF2 = str(HIF)
            A = str(AspectRatio)

            try:
                temp_file = tkinter.filedialog.asksaveasfile(initialdir="/", title="Save Project",
                                                             defaultextension='.txt',filetypes=(("text files", "*.txt"),
                                                                                                ("all files", "*.*")))

                if temp_file:
                    temp_file.write("Your Video Wall Info")
                    temp_file.write("\n")
                    temp_file.write("\n")
                    temp_file.write("Wall Resolution: ")
                    temp_file.write(Resolution1)
                    temp_file.write("\n")
                    temp_file.write("Aspect Ratio: ")
                    temp_file.write(AspectRatio1)
                    temp_file.write("\n")
                    temp_file.write("Wall Width(pixels): ")
                    temp_file.write(CAL1)
                    temp_file.write("\n")
                    temp_file.write("Wall Height(pixels): ")
                    temp_file.write(CAL22)
                    temp_file.write("\n")
                    temp_file.write("Total LEDs For Wall: ")
                    temp_file.write(CAL32)
                    temp_file.write("\n")
                    temp_file.write("Ports Required: ")
                    temp_file.write(ports22)
                    temp_file.write("\n")
                    temp_file.write("Drives Required: ")
                    temp_file.write(drives32)
                    temp_file.write("\n")
                    temp_file.write("Number of Panel Wide: ")
                    temp_file.write(RW2)
                    temp_file.write("\n")
                    temp_file.write("Number of Panel High: ")
                    temp_file.write(RH2)
                    temp_file.write("\n")
                    temp_file.write("Total number of Panels: ")
                    temp_file.write(TP2)
                    temp_file.write("\n")
                    temp_file.write("Total number of Cases: ")
                    temp_file.write(Cases22)
                    temp_file.write("\n")
                    temp_file.write("Power circuit needed @ 120V: ")
                    temp_file.write(PL120cal2)
                    temp_file.write("\n")
                    temp_file.write("Power circuit needed @ 208V: ")
                    temp_file.write(PL208cal2)
                    temp_file.write("\n")
                    temp_file.write("Power circuit needed @ 230V: ")
                    temp_file.write(PL230cal2)
                    temp_file.write("\n")
                    temp_file.write("Total AMPS @ 120V: ")
                    temp_file.write(amps120Cal2)
                    temp_file.write("\n")
                    temp_file.write("Total AMPS @ 208V: ")
                    temp_file.write(amps208Cal2)
                    temp_file.write("\n")
                    temp_file.write("Total AMPS @ 230V: ")
                    temp_file.write(amps230Cal2)
                    temp_file.write("\n")
                    temp_file.write("Total Weight lb: ")
                    temp_file.write(WlbCal2)
                    temp_file.write("\n")
                    temp_file.write("Total Weight kg: ")
                    temp_file.write(WkgCal2)
                    temp_file.write("\n")
                    temp_file.write("Wall Width in Feet: ")
                    temp_file.write(WIF2)
                    temp_file.write("\n")
                    temp_file.write("Wall Height in Feet: ")
                    temp_file.write(HIF2)
                    temp_file.write("\n")


                    temp_file.close()




            except:
                temp_file.close()
                tkinter.messagebox.showerror(title="oops!", message="unable to save")





        def saveas1():

            d = tkinter.filedialog.asksaveasfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("all files","*.*")))

            try:
                d.write(HIF)
            except:
                tkinter.messagebox.showerror(title="oops!", message="unable to save")

        b2 = tkinter.ttk.Button(popup, text="Save", command=savefile1).grid(row=31, columnspan=5, pady=10, sticky='n')




        popup.mainloop()

# gives weight to the cells in the grid
rows = 49
while rows < 50:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1

# Defines and places the notebook widget
nb = tkinter.ttk.Notebook(main)
nb.grid(row=1, column=0, columnspan=50, rowspan=49, sticky='NESW')

# Adds tab 5 of the notebook
page1 = tkinter.ttk.Frame(nb)
nb.add(page1, text='Video Wall in Feet')
titallable_pg5 = Label (page1, text="Video Wall Calculator",font=L_FONT).grid(row=0, columnspan=5,pady=20)
lable1_pg5 = Label (page1, text="Please pick a Panel", font=helv36).grid(row=1, column=1,   )
P5_check5 = Radiobutton(page1,text= "Vivid 4",font=helv36, variable=Pn , value=1,command=cal_pg5 ).grid(row=2, column=1, padx=50,sticky="w")
P4_check5 = Radiobutton(page1,text= "  F4  ",font=helv36, variable=Pn , value=4,command=cal_pg5 ).grid(row=3, column=1, padx=50,sticky="w")
F3_check5 = Radiobutton(page1,text= "  F3  ", font=helv36,variable=Pn, value=2, command=cal_pg5).grid(row=4, column=1,padx=50,sticky="w")
C6_check5 = Radiobutton(page1,text= "  C6  ", font=helv36,variable=Pn, value=3, command=cal_pg5).grid(row=5, column=1, padx=50,sticky="w" )

X15 = Label (page1, text="Wall Width in Feet:",font=helv36).grid(row=2, column=2)
X1E5 = Entry(page1, textvariable=Widthft,font=helv36).grid(row=2, column=3)
X25 = Label (page1, text="Wall Height in Feet",font=helv36).grid(row=3,column=2 )
X2E5 = Entry(page1, textvariable=Heightft,font=helv36).grid(row=3, column=3)
calbutton_pg45= tkinter.ttk.Button (page1, text='OK', command=wallmsg_pg5).grid(row=4, column=3)

# Adds tab 4 of the notebook
page2 = tkinter.ttk.Frame(nb)
nb.add(page2, text='Known Wall Size')
titallable_pg4 = Label (page2, text="Video Wall Calculator Using Know Panel Size",font=L_FONT).grid(row=0, columnspan=5,pady=20)
lable1_pg4 = Label (page2, text="Please pick a Panel", font=helv36).grid(row=1, column=1,   )
P4_check = Radiobutton(page2,text= "Vivid 4 / F4",font=helv36, variable=VP4 , value=1,command=cal_pg4 ).grid(row=2, column=1, padx=50,sticky="w")
F3_check = Radiobutton(page2,text= "  F3  ", font=helv36,variable=VP4, value=2, command=cal_pg4).grid(row=3, column=1,padx=50,sticky="w")
C6_check =Radiobutton(page2,text= "  C6  ", font=helv36,variable=VP4, value=3, command=cal_pg4).grid(row=4, column=1, padx=50,sticky="w" )
X1 = Label (page2, text="Number of Pamels Wide:",font=helv36).grid(row=2, column=2)
X1E = Entry(page2, textvariable=wallW,font=helv36).grid(row=2, column=3)
X2 = Label (page2, text="Number of Pamels High",font=helv36).grid(row=3,column=2 )
X2E = Entry(page2, textvariable=wallH,font=helv36).grid(row=3, column=3)
calbutton_pg4= tkinter.ttk.Button (page2, text='OK', command=wallmsg).grid(row=4, column=3)


main.mainloop()
