from tkinter import *
import math
#make b value for plus func, make = func, add condition for equal func to
#make sure that the plus has been pressed.


win=Tk()
var=""
A=0
operator=""
sum=0
data=StringVar()
L=Label(win,textvariable=data,font=("Verdana",40),background="#ffffff")
L.pack(expand=False,fill="both")

def one_button():
    global var
    var=var+"1"
    data.set(var)
def two_button():
    global var
    var=var+"2"
    data.set(var)
def three_button():
    global var
    var=var+"3"
    data.set(var)
def four_button():
    global var
    var=var+"4"
    data.set(var)
def five_button():
    global var
    var=var+"5"
    data.set(var)
def six_button():
    global var
    var=var+"6"
    data.set(var)
def seven_button():
    global var
    var=var+"7"
    data.set(var)
def eight_button():
    global var
    var=var+"8"
    data.set(var)
def nine_button():
    global var
    var=var+"9"
    data.set(var)
def zero_button():
    global var
    var=var+"0"
    data.set(var)
def plus_button():
  global A,var,operator,sum
  if (sum>0):
      var=str(sum)
#  A=int(var)
  var=var+"+"
  operator="+"
  data.set(var)
def minus_button():
  global A,var,operator
  A=int(var)
  var=var+"-"
  operator="-"
  data.set(var)
def times_button():
  global A,var,operator
  A=int(var)
  var=var+"*"
  operator="*"
  data.set(var)
def divide_button():
  global A,var,operator
  A=int(var)
  var=var+"/"
  operator="/"
  data.set(var)
def Clear():
  global A,var,operator
  var=""
  A=0
  operator=""
  data.set(var)
def equal():
    global A,var,operator
    if (operator=="+"):
        A=int(var.split("+")[0])
        B=int(var.split("+")[1])
        sum=A+B
        data.set(sum)
 #       A=sum
    if (operator=="-"):
        B=int(var.split("-")[1])
        sum=A-B
        data.set(sum)
    if (operator=="*"):
        B=int(var.split("*")[1])
        sum=A*B
        data.set(sum)
    if (operator=="/"):
        B=int(var.split("/")[1])
        if (B==0):
            data.set("ERROR OCCURRED")
        else:
            sum=A/B
            data.set(sum)
    
    
        
row1=Frame(win)
row1.pack()
row2=Frame(win)
row2.pack()
row3=Frame(win)
row3.pack()
row4=Frame(win)
row4.pack()


B1=Button(row1,text="1",command=one_button)
B1.pack(side=LEFT)
B2=Button(row1,text="2",command=two_button)
B2.pack(side=LEFT)
B3=Button(row1,text="3",command=three_button)
B3.pack(side=LEFT)
B4=Button(row1,text="+",command=plus_button)
B4.pack(side=LEFT)

B5=Button(row2,text="4",command=four_button)
B5.pack(side=LEFT)
B6=Button(row2,text="5",command=five_button)
B6.pack(side=LEFT)
B7=Button(row2,text="6",command=six_button)
B7.pack(side=LEFT)
B8=Button(row2,text="-",command=minus_button)
B8.pack(side=LEFT)

B9=Button(row3,text="7",command=seven_button)
B9.pack(side=LEFT)
B10=Button(row3,text="8",command=eight_button)
B10.pack(side=LEFT)
B11=Button(row3,text="9",command=nine_button)
B11.pack(side=LEFT)
B12=Button(row3,text="*",command=times_button)
B12.pack(side=LEFT)

B13=Button(row4,text="0",command=zero_button)
B13.pack(side=LEFT)
B14=Button(row4,text="=", command=equal)
B14.pack(side=LEFT)
B15=Button(row4,text="C",command=Clear)
B15.pack(side=LEFT)
B16=Button(row4,text="/",command=divide_button)
B16.pack(side=LEFT)



win.mainloop()


