###login page
from tkinter import*
root=Tk()
root.geometry('800x800')
root.title('login')
a=Label(root,text="Welcome to FIKA",font=("Arial",18,"bold"))
a.pack()
b=Label(root,text=" ")
b.pack()
e=Label(root,text="username: ")
e.pack()
f=Entry(root)
f.pack()
g=Label(root,text="email: ")
g.pack()
h=Entry(root)
h.pack()
i=Label(root,text="password: ")
i.pack()
j=Entry(root)
j.pack()
root1=Tk()
root1.geometry('800x800')
root1.title('sign in')
k=Label(root,text="Did you forget your password ?",font=("Arial",10,"bold"))
k.pack()
def login():
    print("username=",f.get())
    print("email=",h.get())
    print("password=",j.get())
l=Button(root,text="login",command=login)
l.pack()
m=Label(root,text="Kindly sign up if you are not a member")
m.pack()
n1=Label(root1,text="country:")
n1.pack()
o=Entry(root1)
o.pack()
p=Label(root1,text="phone number:")
p.pack()
q=Entry(root1)
q.pack()
r=Label(root1,text="name:")
r.pack()
s=Entry(root1)
s.pack()
t=Label(root1,text="date of birth:")
t.pack()
u=Entry(root1)
u.pack()
v=Label(root1,text="email:")
v.pack()
w=Entry(root1)
w.pack()
def sign():
    print("country:",o.get())
    print("phone number:",q.get())
    print("name: ", s.get())
    print("date of birth: ",u.get())
    print("email: ", w.get())
n=Button(root1,text="sign up",font=("Times New Roman",10),command=sign)
n.pack()
root.mainloop()

##import tkinter as tk
##from tkinter import messagebox
##import datetime
##
##class HotelManagement:
##    def __init__(self, root):
##        self.root = root
##        self.root.title("Hotel Management System")
##
##        # Create main frames
##        self.frame1 = tk.Frame(self.root)
##        self.frame1.pack(fill="both", expand=True)
##
##        self.frame2 = tk.Frame(self.root)
##        self.frame2.pack(fill="both", expand=True)
##
##        # Create labels and entries
##        self.label1 = tk.Label(self.frame1, text="Room Number")
##        self.label1.pack()
##        self.entry1 = tk.Entry(self.frame1)
##        self.entry1.pack()
##
##        self.label2 = tk.Label(self.frame1, text="Guest Name")
##        self.label2.pack()
##        self.entry2 = tk.Entry(self.frame1)
##        self.entry2.pack()
##
##        self.label3 = tk.Label(self.frame1, text="Room Type")
##        self.label3.pack()
##        self.entry3 = tk.Entry(self.frame1)
##        self.entry3.pack()
##
##        self.label4 = tk.Label(self.frame1, text="Check-In Date")
##        self.label4.pack()
##        self.entry4 = tk.Entry(self.frame1)
##        self.entry4.pack()
##
##        self.label5 = tk.Label(self.frame1, text="Check-Out Date")
##        self.label5.pack()
##        self.entry5 = tk.Entry(self.frame1)
##        self.entry5.pack()
##
##        self.label6 = tk.Label(self.frame1, text="Room Status")
##        self.label6.pack()
##        self.entry6 = tk.Entry(self.frame1)
##        self.entry6.pack()
##
##        # Create buttons
##        self.button1 = tk.Button(self.frame2, text="Check-In", command=self.check_in)
##        self.button1.pack()
##
##        self.button2 = tk.Button(self.frame2, text="Check-Out", command=self.check_out)
##        self.button2.pack()
##
##        self.button3 = tk.Button(self.frame2, text="View Rooms", command=self.view_rooms)
##        self.button3.pack()
##
##        self.button4 = tk.Button(self.frame2, text="View Guests", command=self.view_guests)
##        self.button4.pack()
##
##        self.button5 = tk.Button(self.frame2, text="Update Room Status", command=self.update_room_status)
##        self.button5.pack()

   
