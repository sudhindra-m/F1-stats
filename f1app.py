from tkinter import *
from functools import partial
from tkinter import ttk, messagebox

import mysql.connector as mc
c=mc.connect(host="localhost",user="root",passwd="mysql",database="f1apptest1")
cr=c.cursor()



#main page
top = Tk()  
top.geometry("1268x705")

top.title("Home Page")
top.configure(bg="black")
bg=PhotoImage(file=r"C:\Users\DELL\Desktop\COLLEGE PROJECTS (SRM)\bg.png")
bg_label=Label(top,image=bg)
bg_label.place(x=1,y=1)

welcome = Label(top,text = "Welcome to F1STATS").place(x=500,
                                                               y=5)
   



   




#sign in func   
def signin():
    
    #sign in homepage
    def homepage():
        
        hp=Toplevel(top)
        hp.geometry("953x500")
        hp.title("Home Page")
        si.geometry("587x320")
        hp.configure(bg="black")
        bg=PhotoImage(file=r"C:\Users\DELL\Desktop\COLLEGE PROJECTS (SRM)\hp.png")
        bg_label=Label(hp,image=bg).place(x=1,y=1)

        
        #input stats
        def inp():
            def inp1():
                name = nvar.get()
                origin = ovar.get()
                join = jvar.get()
                cno = cnovar.get()
                start = stvar.get()
                champ = chpvar.get()
                wins = wvar.get()
                pod = podvar.get()
                pole = pvar.get()
                fast = fvar.get()
                gs = gvar.get()
                points = ptsvar.get()
                ovr = ovrvar.get()
                datalog=(name,origin,join,cno,start,champ,wins,pod,pole,fast,gs,points,ovr)
                
                cr.execute("insert into stats values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", datalog)
                c.commit()
            ip=Toplevel(top)
            ip.title("Input Page")
            ip.geometry("1335x682")
            ip.configure(bg="black")
            bg=PhotoImage(file=r"C:\Users\DELL\Desktop\COLLEGE PROJECTS (SRM)\inp.png")
            bg_label=Label(ip,image=bg).place(x=1,y=1)

            nvar=StringVar()
            ovar=StringVar()
            jvar=IntVar()
            cnovar=IntVar()
            stvar=IntVar()
            chpvar=IntVar()
            wvar=IntVar()
            podvar=IntVar()
            pvar=IntVar()
            fvar=IntVar()
            gvar=IntVar()
            ptsvar=IntVar()
            ovrvar=IntVar()


            
            i1 = Label(ip, text = "Input Statistics below:").place(x = 25,y = 10)
            i2 = Label(ip, text = "Name:").place(x = 250,y = 50)
            i3 = Label(ip, text = "Place of origin:").place(x = 250,y = 100)
            i4 = Label(ip, text = "Year of joining:").place(x = 250,y = 150)
            i5 = Label(ip, text = "Car number:").place(x = 250,y = 200)
            i6 = Label(ip, text = "Total starts:").place(x = 250,y = 250)
            i7 = Label(ip, text = "Career Championships:").place(x = 250,y = 300)
            i8 = Label(ip, text = "Career Wins:").place(x = 250,y = 350)
            i9 = Label(ip, text = "Career Podiums:").place(x = 250,y = 400)
            i10 = Label(ip, text = "Career Pole Positions:").place(x = 250,y = 450)
            i11 = Label(ip, text = "Career Fastest Laps:").place(x = 250,y = 500)
            i12 = Label(ip, text = "Career GrandSlams:").place(x = 250,y = 550)
            i13 = Label(ip, text = "Total Points:").place(x = 250,y = 600)
            i14 = Label(ip, text = "Overall Rating:").place(x = 250,y = 650)

            name = Entry(ip,textvariable=nvar).place(x = 550, y = 50)
            origin = Entry(ip,textvariable=ovar).place(x = 550, y = 100)
            join = Entry(ip,textvariable=jvar).place(x = 550, y = 150)
            cno = Entry(ip,textvariable=cnovar).place(x = 550, y = 200)
            start = Entry(ip,textvariable=stvar).place(x = 550, y = 250)
            champ = Entry(ip,textvariable=chpvar).place(x = 550, y = 300)
            wins = Entry(ip,textvariable=wvar).place(x = 550, y = 350)
            pod = Entry(ip,textvariable=podvar).place(x = 550, y = 400)
            pole = Entry(ip,textvariable=pvar).place(x = 550, y = 450)
            fast = Entry(ip,textvariable=fvar).place(x = 550, y = 500)
            gs = Entry(ip,textvariable=gvar).place(x = 550, y = 550)
            points = Entry(ip,textvariable=ptsvar).place(x = 550, y = 600)
            ovr = Entry(ip,textvariable=ovrvar).place(x = 550, y = 650)

            inpstat = Button(ip,
                  text = "Input into database",width=25,command=inp1).place(x = 1000,
                                           y = 650)

            
            

            
            ip.mainloop()


        #view stats
        def viewst():

            vi=Toplevel(top)
            vi.title("View Statistics")
            vi.geometry("1318x607")
            vi.configure(bg="black")
            bg=PhotoImage(file=r"C:\Users\DELL\Desktop\COLLEGE PROJECTS (SRM)\vst.png")
            bg_label=Label(vi,image=bg).place(x=1,y=1)

            
            #constructors champs
            def cc():
                c=Toplevel(top)
                c.title("Constructors Championships")
                c.geometry("1463x695")
                c.configure(bg="black")
                
                bg_label=Label(c,image=bg).place(x=1,y=1)

                def y22():
                    tt=Toplevel(top)
                    tt.title("2022 Constructors Champions")
                    tt.geometry("1305x717")
                    tt.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\2022cc.png")
                    bg_label=Label(tt,image=bg).place(x=1,y=1)

                    tt.mainloop()


                def y21():
                    to=Toplevel(top)
                    to.title("2021 Constructors Champions")
                    to.geometry("1303x718")
                    to.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\2021cc.png")
                    bg_label=Label(to,image=bg).place(x=1,y=1)

                    to.mainloop()


                def y20():
                    t=Toplevel(top)
                    t.title("2020 Constructors Champions")
                    t.geometry("1305x726")
                    t.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\2020cc.png")
                    bg_label=Label(t,image=bg).place(x=1,y=1)

                    t.mainloop()


                def y19():
                    tn=Toplevel(top)
                    tn.title("2019 Constructors Champions")
                    tn.geometry("1298x728")
                    tn.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\2019cc.png")
                    bg_label=Label(tn,image=bg).place(x=1,y=1)

                    tn.mainloop()


                def y18():
                    te=Toplevel(top)
                    te.title("2018 Constructors Champions")
                    te.geometry("1302x726")
                    te.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\2018cc.png")
                    bg_label=Label(te,image=bg).place(x=1,y=1)

                    te.mainloop()



                    



                twentytwo = Button(c,
                  text = "2022 constructor champions",width=28,command=y22).place(x = 1250,
                                           y = 100)

                twentyone = Button(c,
                  text = "2021 constructor champions",width=28,command=y21).place(x = 1050,
                                           y = 100)

                twenty = Button(c,
                  text = "2020 constructor champions",width=28,command=y20).place(x = 850,
                                           y = 100)

                nineteen = Button(c,
                  text = "2019 constructor champions",width=28,command=y19).place(x = 650,
                                           y = 100)

                eighteen = Button(c,
                  text = "2018 constructor champions",width=28,command=y18).place(x = 450,
                                           y = 100)

            

                c.mainloop()

                
            ccview = Button(vi,
                  text = "View constructor champions",width=32,command=cc).place(x = 1000,
                                           y = 100)


            #stats
            def dc():
                dc=Toplevel(top)
                dc.title("World Drivers Champion")
                dc.geometry("1437x722")
                dc.configure(bg="black")
                bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\wdchp.png")
                bg_label=Label(dc,image=bg).place(x=1,y=1)

                def wy22():
                    tt=Toplevel(top)
                    tt.title("2022 Drivers Champion")
                    tt.geometry("1306x725")
                    tt.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\2022wdc.png")
                    bg_label=Label(tt,image=bg).place(x=1,y=1)

                    tt.mainloop()


                def wy21():
                    tt=Toplevel(top)
                    tt.title("2021 Drivers Champion")
                    tt.geometry("1306x731")
                    tt.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\wdc21.png")
                    bg_label=Label(tt,image=bg).place(x=1,y=1)

                    tt.mainloop()

                def wy20():
                    tt=Toplevel(top)
                    tt.title("2020 Drivers Champion")
                    tt.geometry("1306x731")
                    tt.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\wdc20.png")
                    bg_label=Label(tt,image=bg).place(x=1,y=1)

                    tt.mainloop()


                def wy19():
                    tt=Toplevel(top)
                    tt.title("2019 Drivers Champion")
                    tt.geometry("1478x731")
                    tt.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\wdc19.png")
                    bg_label=Label(tt,image=bg).place(x=1,y=1)

                    tt.mainloop()


                def wy18():
                    tt=Toplevel(top)
                    tt.title("2018 Drivers Champion")
                    tt.geometry("1478x731")
                    tt.configure(bg="black")
                    bg=PhotoImage(file=r"C:\Users\sudhi\Pictures\Saved Pictures\wdc18.png")
                    bg_label=Label(tt,image=bg).place(x=1,y=1)

                    tt.mainloop()

                    
                w22 = Button(dc,
                  text = "WDC 2022",width=10,command=wy22).place(x = 1000,
                                           y = 200)
                w21 = Button(dc,
                  text = "WDC 2021",width=10,command=wy21).place(x = 1000,
                                           y = 250)
                w20 = Button(dc,
                  text = "WDC 2020",width=10,command=wy20).place(x = 1000,
                                           y = 300)
                w19 = Button(dc,
                  text = "WDC 2019",width=10,command=wy19).place(x = 1000,
                                           y = 350)
                w18 = Button(dc,
                  text = "WDC 2018",width=10,command=wy18).place(x = 1000,
                                           y = 400)
                



                dc.mainloop()

                
                
            wdcview = Button(vi,
                  text = "View world drivers champions",width=32,command=dc).place(x = 1000,
                                           y = 200)



            #mainstats
            def mstats():
                dashemp=Tk()
                dashemp.title("Driver statistics")
                dashemp.geometry("1478x760")
                dashemp.config(bg="white")
                
                class Filter_Data:
                    def __init__(self, dashemp):

                        
                        self.C_Frame=Frame(dashemp,bd=5,relief=RIDGE)
                        self.C_Frame.place(x=40, y=150,width=1100,height=500)
                        scrolly=Scrollbar(self.C_Frame, orient=VERTICAL)
                        scrollx=Scrollbar(self.C_Frame, orient=HORIZONTAL)
                        self.post=ttk. Treeview(self.C_Frame, columns=("name","place_of_origin","year_of_joining","car_number","total_starts","career_championships","career_wins",
                                                                       "career_podiums","career_pole_positions","career_fastest_laps","career_grand_slams","total_points","overall_rating"))
                        scrollx.pack(side=BOTTOM, fill=X)
                        scrolly.pack(side=RIGHT,fill=Y)
                        scrollx.config(command=self.post.xview)
                        scrolly.config(command=self.post.yview)
                        self.post.heading("name",text="Driver Name")
                        self.post.heading("place_of_origin",text="Place of Origin")
                        self.post.heading("year_of_joining",text="Year of joining")
                        self.post.heading("car_number",text="Car Number")
                        self.post.heading("total_starts",text="Total Starts")
                        self.post.heading("career_championships",text="Career Championships")
                        self.post.heading("career_wins",text="Career Wins")
                        self.post.heading("career_podiums",text="Career Podiums")
                        self.post.heading("career_pole_positions",text="Career Pole Positions")
                        self.post.heading("career_fastest_laps",text="Career Fastest Laps")
                        self.post.heading("career_grand_slams",text="Career Grand Slams")
                        self.post.heading("total_points",text="Total Points")
                        self.post.heading("overall_rating",text="Overall Rating")
                        
                        self.post["show"]='headings'
                        self.post.column("name",width=150)
                        self.post.column("place_of_origin",width=100)
                        self.post.column("year_of_joining",width=100)
                        self.post.column("car_number",width=100)
                        self.post.column("total_starts",width=100)
                        self.post.column("career_championships",width=100)
                        self.post.column("career_wins",width=250)
                        self.post.column("career_podiums",width=250)
                        self.post.column("career_pole_positions",width=250)
                        self.post.column("career_fastest_laps",width=250)
                        self.post.column("career_grand_slams",width=250)
                        self.post.column("total_points",width=250)
                        self.post.column("overall_rating",width=250)
                        self.post.pack(fill=BOTH, expand=1)
                        #self.show()
                    
                        c=mc.connect(host= "localhost", user="root", passwd="mysql", database= "f1apptest1")
                        cur=c.cursor()
                        try:
                            
                            cur.execute("SELECT * FROM stats")
                            row= cur.fetchall() 
                            #print (row)
                            
                            if len(row)>0:
                                self.post.delete(*self.post.get_children())
                                for i in row:
                                    self.post.insert('', END, values=i)
                            else:
                                self.post.delete(*self.post.get_children())
                        except Exception as ex:
                            messagebox.showerror("Error",f"Error due to {str(ex)}")        

                obj=Filter_Data(dashemp)
                dashemp.mainloop()
                

            
            mainstatsview = Button(vi,
                  text = "View driver statistics",width=32,command=mstats).place(x = 1000,
                                           y = 300)



            def cmp():
                dashemp=Tk()
                dashemp.title("Compare Statistics")
                dashemp.geometry("1478x760")
                dashemp.config(bg="white")
                
                class Filter_Data:
                    def __init__(self, dashemp):

                        
                        self.C_Frame=Frame(dashemp,bd=5,relief=RIDGE)
                        self.C_Frame.place(x=40, y=150,width=1100,height=500)
                        scrolly=Scrollbar(self.C_Frame, orient=VERTICAL)
                        scrollx=Scrollbar(self.C_Frame, orient=HORIZONTAL)
                        self.post=ttk. Treeview(self.C_Frame, columns=("name","overall_rating"))
                        scrollx.pack(side=BOTTOM, fill=X)
                        scrolly.pack(side=RIGHT,fill=Y)
                        scrollx.config(command=self.post.xview)
                        scrolly.config(command=self.post.yview)
                        self.post.heading("name",text="Driver Name")
                        self.post.heading("overall_rating",text="Overall Rating")
                        
                        self.post["show"]='headings'
                        self.post.column("name",width=150)
                        self.post.column("overall_rating",width=250)
                        self.post.pack(fill=BOTH, expand=1)
                        #self.show()
                    
                        c=mc.connect(host= "localhost", user="root", passwd="mysql", database= "f1apptest1")
                        cur=c.cursor()
                        try:
                            
                            cur.execute("SELECT name,overall_rating FROM stats")
                            row= cur.fetchall() 
                            #print (row)
                            
                            if len(row)>0:
                                self.post.delete(*self.post.get_children())
                                for i in row:
                                    self.post.insert('', END, values=i)
                            else:
                                self.post.delete(*self.post.get_children())
                        except Exception as ex:
                            messagebox.showerror("Error",f"Error due to {str(ex)}")        

                obj=Filter_Data(dashemp)
                dashemp.mainloop()
                

            
            mainstatsview = Button(vi,
                  text = "View driver statistics",width=32,command=cmp).place(x = 1000,
                                           y = 400)



            vi.mainloop()

        
            

        view = Button(hp,
                  text = "View Statistics",width=24,command=viewst).place(x = 700,
                                           y = 150)

        inp = Button(hp,
                  text = "Input Statistics",width=24,command=inp).place(x = 700,
                                           y = 250)

        cmp = Button(hp,
                  text = "Compare Drivers",width=24,command=cmp).place(x = 700,
                                           y = 350)
       
        

        hp.mainloop()
        
        
        
    def verify():
        username1= username.get()
        password1= password.get()
        datalog=(username1, password1)
        cr.execute("select * from usrpwd")
        logdet=cr.fetchall()
        
        
        if logdet[0]==datalog:
                
                
            homepage()
        elif logdet[1]==datalog:
            homepage()

        elif logdet[2]==datalog:
            homepage()
        elif logdet[3]==datalog:
            homepage()
        elif logdet[4]==datalog:
            homepage()
        elif logdet[5]==datalog:
            homepage()
        elif logdet[6]==datalog:
            homepage()
        elif logdet[7]==datalog:
            homepage()
        elif logdet[8]==datalog:
            homepage()
        elif logdet[9]==datalog:
            homepage()
            
        else:
            print("Invalid username/password")
            
    
    
            
    si= Toplevel(top)
    si.title("Sign In")
    si.geometry("450x300")
    lab = Label(si, text = "Sign In:").place(x = 25,y = 15)
    uname = Label(si, text = "Username").place(x = 25,y = 50)
    passwo = Label(si, text = "Password").place(x = 25, y = 90)

    username=StringVar()
    password=StringVar()
    
    uentry = Entry(si,textvariable=username).place(x = 90, y = 50)  
  
  
    pentry = Entry(si,textvariable=password,show="*").place(x = 90, y = 90)

    signin = Button(si,
                  text = "Sign in",width=7,command=verify).place(x = 25,
                                           y = 130)
    

    

    
    


    

#create acc 
def ca():
    def ca2():
            e1= uvar.get()
            e2= pvar.get()
            datalog=(e1,e2)
            
            cr.execute("insert into usrpwd values(%s,%s)", datalog)
            c.commit()
    ca=Toplevel(top)
    ca.title("Create an account")
    ca.geometry("450x300")
    lab=Label(ca,text = "Create an account: ").place(x=25,y=15)
    uvar=StringVar()
    pvar=StringVar()
    uname = Label(ca, text = "Enter a username").place(x = 25,y = 50)
    password = Label(ca, text = "Create a password").place(x = 25, y = 90)
    e1 = Entry(ca,textvariable=uvar).place(x = 150, y = 50)  
  
  
    e2 = Entry(ca,textvariable=pvar).place(x = 150, y = 90)

    
    create = Button(ca,
                  text = "Create account",width=20,command=ca2).place(x = 25,
                                           y = 130)

    
sign_in = Button(top,
                  text = "Sign in",width=7,command=signin).place(x = 480,
                                           y = 60)

Create = Button(top,
                text="Create new account",
                             width = 20,command=ca).place(x = 570,
                                               y = 60)

top.mainloop()

