#usr/bin/env/python

import Tkinter,math

bgcolor = "#333333"

class mainApp():
    tgp1 = tgp2 = 0
    def __init__(self):
        #MAIN WINDOW

        self.window = Tkinter.Tk()
        self.window.configure(background=bgcolor)
        self.window.wm_title("CGPA Calculator")
        self.window.geometry("1000x800")

        #HEADER
        self.h1 = Tkinter.Label(self.window, text="CGPA CALCULATOR", font=70, fg="White", bg=bgcolor).pack()

        #FIRST SEMESTER
        self.s1 = Tkinter.Label(self.window, text="First Semester", font=50, fg="White", bg=bgcolor)
        self.s1.place(x=30, y=100)
        self.sub = Tkinter.Label(self.window, text="Subject", fg="White", bg=bgcolor)
        self.sub.place(x=30, y=150)
        self.g = Tkinter.Label(self.window, text="Grades", fg="White", bg=bgcolor)
        self.g.place(x=400, y=150)
        self.c = Tkinter.Label(self.window, text="Credit", fg="White", bg=bgcolor)
        self.c.place(x=550, y=150)
        self.sub1 = Tkinter.Label(self.window, text="Subject 1", fg="White", bg=bgcolor)
        self.sub1.place(x=30, y=180)
        self.sub2 = Tkinter.Label(self.window, text="Subject 2", fg="White", bg=bgcolor)
        self.sub2.place(x=30, y=210)
        self.sub3 = Tkinter.Label(self.window, text="Subject 3", fg="White", bg=bgcolor)
        self.sub3.place(x=30, y=240)
        self.sub4 = Tkinter.Label(self.window, text="Subject 4", fg="White", bg=bgcolor)
        self.sub4.place(x=30, y=270)
        self.sub5 = Tkinter.Label(self.window, text="Subject 5", fg="White", bg=bgcolor)
        self.sub5.place(x=30, y=300)
        self.sub6 = Tkinter.Label(self.window, text="Subject 6", fg="White", bg=bgcolor)
        self.sub6.place(x=30, y=330)

        #SEM 1 ENTRY BOXES
        self.g1 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g1).place(x=400, y=180)
        self.g2 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g2).place(x=400, y=210)
        self.g3 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g3).place(x=400, y=240)
        self.g4 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g4).place(x=400, y=270)
        self.g5 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g5).place(x=400, y=300)
        self.g6 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g6).place(x=400, y=330)

        self.c1 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c1).place(x=550, y=180)
        self.c2 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c2).place(x=550, y=210)
        self.c3 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c3).place(x=550, y=240)
        self.c4 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c4).place(x=550, y=270)
        self.c5 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c5).place(x=550, y=300)
        self.c6 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c6).place(x=550, y=330)

        self.s1cgpa = Tkinter.Label(self.window, text="TCGPA", fg="white", bg=bgcolor)
        self.s1cgpa.place(x=850, y=250)
        self.s1cgpa1 = Tkinter.Label(self.window, text="0", fg="white", bg=bgcolor)
        self.s1cgpa1.place(x=920, y=250)


        #SECOND SEMESTER
        self.s2 = Tkinter.Label(self.window, text="Second Semester", font=50, fg="White", bg=bgcolor)
        self.s2.place(x=30, y=380)
        self.s2sub = Tkinter.Label(self.window, text="Subject", fg="White", bg=bgcolor)
        self.s2sub.place(x=30, y=430)
        self.s2g = Tkinter.Label(self.window, text="Grades", fg="White", bg=bgcolor)
        self.s2g.place(x=400, y=430)
        self.s2c = Tkinter.Label(self.window, text="Credit", fg="White", bg=bgcolor)
        self.s2c.place(x=550, y=430)
        self.sub7 = Tkinter.Label(self.window, text="Subject 1", fg="White", bg=bgcolor)
        self.sub7.place(x=30, y=460)
        self.sub8 = Tkinter.Label(self.window, text="Subject 2", fg="White", bg=bgcolor)
        self.sub8.place(x=30, y=490)
        self.sub9 = Tkinter.Label(self.window, text="Subject 3", fg="White", bg=bgcolor)
        self.sub9.place(x=30, y=520)
        self.sub10 = Tkinter.Label(self.window, text="Subject 4", fg="White", bg=bgcolor)
        self.sub10.place(x=30, y=550)
        self.sub11 = Tkinter.Label(self.window, text="Subject 5", fg="White", bg=bgcolor)
        self.sub11.place(x=30, y=580)
        self.sub12 = Tkinter.Label(self.window, text="Subject 6", fg="White", bg=bgcolor)
        self.sub12.place(x=30, y=610)


        #SEM 2 ENTRY BOXES
        self.g7 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g7).place(x=400, y=460)
        self.g8 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g8).place(x=400, y=490)
        self.g9 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g9).place(x=400, y=520)
        self.g10 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g10).place(x=400, y=550)
        self.g11 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g11).place(x=400, y=580)
        self.g12 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.g12).place(x=400, y=610)


        self.c7 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c7).place(x=550, y=460)
        self.c8 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c8).place(x=550, y=490)
        self.c9 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c9).place(x=550, y=520)
        self.c10 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c10).place(x=550, y=550)
        self.c11 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c11).place(x=550, y=580)
        self.c12 = Tkinter.StringVar()
        Tkinter.Entry(self.window, textvariable=self.c12).place(x=550, y=610)


        self.s2cgpa = Tkinter.Label(self.window, text="TCGPA", fg="white", bg=bgcolor)
        self.s2cgpa.place(x=850, y=550)
        self.s2cgpa2 = Tkinter.Label(self.window, text="0", fg="white", bg=bgcolor)
        self.s2cgpa2.place(x=920, y=550)

        #MAIN CGPA
        self.tgpa1 = Tkinter.Label(self.window, text="CGPA", fg="white", bg=bgcolor)
        self.tgpa1.place(x=500, y=670)
        self.tgpa2 = Tkinter.Label(self.window, text="0", fg="white", bg=bgcolor)
        self.tgpa2.place(x=580, y=670)
        self.buttontext = Tkinter.StringVar()
        self.buttontext.set("Calculate")
        Tkinter.Button(self.window, textvariable=self.buttontext, command=self.maincgpa).place(x=400, y=670)

        self.window.mainloop()


    def sem1(self):
        g1 = float(self.g1.get())
        g2 = float(self.g2.get())
        g3 = float(self.g3.get())
        g4 = float(self.g4.get())
        g5 = float(self.g5.get())
        g6 = float(self.g6.get())

        c1 = float(self.c1.get())
        c2 = float(self.c2.get())
        c3 = float(self.c3.get())
        c4 = float(self.c4.get())
        c5 = float(self.c5.get())
        c6 = float(self.c6.get())

        tc1 = c1+c2+c3+c4+c5+c6
        res = (((g1*c1)+(g2*c2)+(g3*c3)+(g4*c4)+(g5*c5)+(g6*c6))/tc1)
        newres = "{:.1f}".format(res) 
        self.s1cgpa1.configure(text=newres, fg="white", bg=bgcolor)
        return newres

    def sem2(self):
        g7 = float(self.g7.get())
        g8 = float(self.g8.get())
        g9 = float(self.g9.get())
        g10 = float(self.g10.get())
        g11 = float(self.g11.get())
        g12 = float(self.g12.get())

        c7 = float(self.c7.get())
        c8 = float(self.c8.get())
        c9 = float(self.c9.get())
        c10 = float(self.c10.get())
        c11 = float(self.c11.get())
        c12 = float(self.c12.get())

        tc2 = c7+c8+c9+c10+c11+c12
        res2 = (((g7*c7)+(g8*c8)+(g9*c9)+(g10*c10)+(g11*c11)+(g12*c12))/tc2)
        newres2 = "{:.1f}".format(res2)
        self.s2cgpa2.configure(text=newres2, fg="white", bg=bgcolor)
        return newres2

    def maincgpa(self):
        temp1 = float(self.sem1())
        temp2 = float(self.sem2())
        temp=((temp1+temp2)/2)
        newtemp = "{:.1f}".format(temp)        
        self.tgpa2.configure(text=newtemp, fg="white", bg=bgcolor)



mainApp()
