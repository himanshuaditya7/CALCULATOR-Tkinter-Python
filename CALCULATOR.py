from tkinter import*
import tkinter as tk
def butnnclick(number):
    global operators
    operators = operators +str(number)
    text_Input.set(operators)
def btnclear():
    global operators
    operators=""
    text_Input.set("")
def btnequal():
    global operators
    sum = str(eval(operators))
    text_Input.set(sum)
    operators=""



atm = Tk()
atm.title('CALCULATOR')
operators =""
text_Input = StringVar()

txtDisplay = Entry(atm,font =('ariel',50,'bold'),textvariable=text_Input,bd=50,insertwidth =4,bg="green", justify = 'right').grid(columnspan=4)
btn1 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="1",command=lambda:butnnclick(1)).grid(row=1,column=0)
btn2 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="2",command=lambda:butnnclick(2)).grid(row=1,column=1)
btn3 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="3",command=lambda:butnnclick(3)).grid(row=1,column=2)
btn4 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="4",command=lambda:butnnclick(4)).grid(row=2,column=0)
btn5 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="5",command=lambda:butnnclick(5)).grid(row=2,column=1)
btn6 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="6",command=lambda:butnnclick(6)).grid(row=2,column=2)
btn7 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="7",command=lambda:butnnclick(7)).grid(row=3,column=0)
btn8 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="8",command=lambda:butnnclick(8)).grid(row=3,column=1)
btn9 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="9",command=lambda:butnnclick(9)).grid(row=3,column=2)
btn10 = Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="0",command=lambda:butnnclick(0)).grid(row=4,column=1)
btnclear1= Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="clear",command=btnclear).grid(row=1,column=3)
btncadd= Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="+",command=lambda:butnnclick("+")).grid(row=1,column=4)
btncsub= Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="-",command=lambda:butnnclick("-")).grid(row=2,column=3)
btncmul= Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="*",command=lambda:butnnclick("*")).grid(row=2,column=4)
btncdiv= Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="/",command=lambda:butnnclick("/")).grid(row=3,column=3)
btnsumup= Button(atm,padx=12,bd=8,fg="blue",font =('ariel',20,'bold'),text="ANSWER",command=btnequal).grid(row=4,column=3)








atm.mainloop()