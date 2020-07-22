from tkinter import *
import parser

root=Tk()

root.title("Calculator")

i=0
def get_var(num):
    global i
    display.insert(i,num)
    i+=1

def get_opr(operator):
    global i
    length=len(operator)
    display.insert(i,operator)
    i+=length

def calculate():
    entire_string=display.get()
    try:
        a=parser.expr(entire_string).compile()
        result=eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"Error")
def calculate_fact(num):
    ans=1
    while(num>0):
        ans*=num
        num-=1
    return ans
def fact(num):

    if len(num)!=1:
        clear_all()
        display.insert(0,"Error")
    else:
        return calculate_fact(int(num))

def clear_all():
    display.delete(0,END)

def undo():
    entire_string=display.get()
    if len(entire_string):
        new_string=entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        display.insert(0,"Error")

root.configure(background='tomato')
root.geometry('460x360')
#adding the display option
display=Entry(root,font=('arial',20,'bold',),bd=30,insertwidth=2,bg="powder blue",justify='right')
display.grid(row=1,columnspan=6)

#adding buttons with numbers
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="1",bg="powder blue",command=lambda :get_var((1))).grid(row=2,column=0)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="2",bg="powder blue",command=lambda :get_var((2))).grid(row=2,column=1)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="3",bg="powder blue",command=lambda :get_var((3))).grid(row=2,column=2)

Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="4",bg="powder blue",command=lambda :get_var((4))).grid(row=3,column=0)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="5",bg="powder blue",command=lambda :get_var((5))).grid(row=3,column=1)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="6",bg="powder blue",command=lambda :get_var((6))).grid(row=3,column=2)

Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="7",bg="powder blue",command=lambda :get_var((7))).grid(row=4,column=0)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="8",bg="powder blue",command=lambda :get_var((8))).grid(row=4,column=1)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="9",bg="powder blue",command=lambda :get_var((9))).grid(row=4,column=2)


#adding operation buttons
Button(root,font=('arial',20,'bold'),padx=3,bd=4,text="AC",bg="powder blue",command=lambda:clear_all()).grid(row=5,column=0)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="0",bg="powder blue",command=lambda :get_var((0))).grid(row=5,column=1)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="=",bg="powder blue",command=lambda :calculate()).grid(row=5,column=2)

Button(root,font=('arial',20,'bold'),padx=8,bd=6,text="+",bg="powder blue",command=lambda:get_opr("+")).grid(row=2,column=3)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="-",bg="powder blue",command=lambda:get_opr("-")).grid(row=3,column=3)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="*",bg="powder blue",command=lambda:get_opr("*")).grid(row=4,column=3)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="/",bg="powder blue",command=lambda:get_opr("/")).grid(row=5,column=3)

Button(root,font=('arial',20,'bold'),padx=10,bd=6,text="pi",bg="powder blue",command=lambda:get_opr("*3.14")).grid(row=2,column=4)
Button(root,font=('arial',20,'bold'),padx=10,bd=6,text="%",bg="powder blue",command=lambda:get_opr("%")).grid(row=3,column=4)
Button(root,font=('arial',20,'bold'),padx=16,bd=8,text="(",bg="powder blue",command=lambda:get_opr("(")).grid(row=4,column=4)
Button(root,font=('arial',20,'bold'),padx=1,bd=6,text="exp",bg="powder blue",command=lambda:get_opr("**")).grid(row=5,column=4)

Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="<--",bg="powder blue",command=lambda:undo()).grid(row=2,column=5)
Button(root,font=('arial',20,'bold'),padx=18,bd=6,text="x!",bg="powder blue",command=lambda:fact(display.get())).grid(row=3,column=5)
Button(root,font=('arial',20,'bold'),padx=22,bd=8,text=")",bg="powder blue",command=lambda:get_opr(")")).grid(row=4,column=5)
Button(root,font=('arial',20,'bold'),padx=12,bd=6,text="^2",bg="powder blue",command=lambda:get_opr("**2")).grid(row=5,column=5)
root.mainloop()