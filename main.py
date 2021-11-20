from tkinter import *
from tkinter import messagebox

root=Tk()

def self():
     var=["12003354","12345"]
     if(var[0]==username.get() and var[1]==password.get()):
         loginFrame.destroy ()
         frame1.pack(fill=BOTH,side=LEFT)
         frame2.pack(expand=True,fill=BOTH)

     else:
         messagebox.showwarning("Incorrect Password","PLEASE ENTER THE PASSWORD CORRECTLY")
root.geometry("600x300")
global string2
string2=0
def add():
    global string1
    global string2
    string1=(float(entry1.get()))*(float(entry2.get()))
    string2=string2+string1
    labelFirst=Label(subFrame1,text=clicked.get())
    labelFirst.pack(side=TOP,fill=X)
    labelSecond=Label(subFrame2,text=entry1.get())
    labelSecond.pack(side=TOP,fill=X)
    labelThird=Label(subFrame3,text=string1)
    labelThird.pack(side=TOP,fill=X)


def total():
    global string2
    var=(string2*18)/100
    subFrame4.pack(fill=BOTH,side=LEFT,expand=True)
    label5 =Label( subFrame4,text="Including GST" ).pack()
    label=Label(subFrame4,text=string2+var).pack()

#LoginPage

loginFrame=LabelFrame(root,text="User login",bd=4)
loginFrame.pack(fill=BOTH)
label1=Label(loginFrame,text="Enter the username",padx=10,pady=20)
label1.pack()
username=Entry(loginFrame)
username.pack()
label2=Label(loginFrame,text="Enter the password",padx=10,pady=20).pack()
password=Entry(loginFrame)
password.pack()
button1=Button(loginFrame,text="log in",command=self).pack(padx=10,pady=20)

#MainShopPage


frame1=LabelFrame(root,text="Item details",padx=40,pady=10)
frame1.pack_forget()
frame2=LabelFrame(root,text="Total price ")
frame2.pack_forget()
label3=Label(frame1,text="Please Choose the Item Selected")
label3.pack()
subFrame1=LabelFrame(frame2,text="Item Selected")
subFrame1.pack(fill=BOTH,side=LEFT,expand=True)
subFrame2=LabelFrame(frame2,text="Quantity")
subFrame2.pack(fill=BOTH,side=LEFT,expand=True)
subFrame3=LabelFrame(frame2,text="Total")
subFrame3.pack(fill=BOTH,side=RIGHT,expand=True)
subFrame4=LabelFrame(frame1,text="Amount to pay")
subFrame4.pack_forget()
label3.pack(side=TOP,fill=Y)
clicked=StringVar()
list=OptionMenu(frame1,clicked,"Dairy Milk","Perk","Fuse","5 Star","Bournville","Dairy Milk Silk","MilkyBar","KitKat","Munch","Bar One","Lotte – Choco Pie","Pacari","Hershey – Brookside").pack()
label4=Label(frame1,text="Please enter the quantity of the product").pack()
entry1=Entry(frame1)
entry1.pack()
label5=Label(frame1,text="Please enter the price of the product").pack()
entry2=Entry(frame1)
entry2.pack()
button_add=Button(frame1,text="Add",command=add).pack()
button_total=Button(frame1,text="Generate Bill",command=total).pack()






root.mainloop()
