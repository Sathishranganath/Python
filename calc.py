from tkinter import*

#Defining the operation taken when button is clicked.
def btnclick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
    

#Defining the operation for Clear Button
def btncleardisplay():
    global operator
    operator = ""
    text_input.set("")
    

#Defining the oepration for equal button which performs the oepration.
def btneqldisplay():
    global operator
    finval = str(eval(operator))
    text_input.set(finval)
    operator = ""
    

cal = Tk()
cal.title("My Calculator")
operator =""
text_input = StringVar()

#The Display board characteristics for display in UI,font , size, Input data type for the text area, border,
#width of the insert area
#Backgroud colour is light blue, justify is the alignment can be right, left, center etc
txtdisplay = Entry(cal, 
                   font=('arial',20, 'bold'),
                   textvariable =text_input, 
                   bd=30, 
                   insertwidth=4, 
                   bg="light blue", 
                   justify='right').grid(columnspan=4)

#Attributes of calculator - Buttons, Lambda function is used for performing calculation in python

btn7 = Button(cal,padx=16,pady=16, bd=8, fg="black", command = lambda:btnclick(7),bg="light blue",font=('arial',20, 'bold'),text="7").grid(row=1, column=0)
btn8 = Button(cal,padx=16,pady=16, bd=8, fg="black", command = lambda:btnclick(8),bg="light blue",font=('arial',20, 'bold'),text="8").grid(row=1, column=1)
btn9 = Button(cal,padx=16,pady=16, bd=8, fg="black", command = lambda:btnclick(9),bg="light blue",font=('arial',20, 'bold'),text="9").grid(row=1, column=2)
#Multiplication button
btnmul = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick("*"),bg="light blue",font=('arial',20, 'bold'),text="*").grid(row=1, column=3)
#####################################################################################################
btn4 = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick(4),bg="light blue",font=('arial',20, 'bold'),text="4").grid(row=2, column=0)
btn5 = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick(5),bg="light blue",font=('arial',20, 'bold'),text="5").grid(row=2, column=1)
btn6 = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick(6),bg="light blue",font=('arial',20, 'bold'),text="6").grid(row=2, column=2)
#Subtraction button
btnsub = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick("-"),bg="light blue",font=('arial',20, 'bold'),text="-").grid(row=2, column=3)
#####################################################################################################
btn1 = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick(1),bg="light blue",font=('arial',20, 'bold'),text="1").grid(row=3, column=0)
btn2 = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick(2),bg="light blue",font=('arial',20, 'bold'),text="2").grid(row=3, column=1)
btn3 = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick(3),bg="light blue",font=('arial',20, 'bold'),text="3").grid(row=3, column=2)
#Addition button
btnadd = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick("+"),bg="light blue",font=('arial',20,'bold'),text="+").grid(row=3, column=3)
#####################################################################################################
btn0 = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick(0),bg="light blue",font=('arial',20, 'bold'),text="0").grid(row=4, column=0)
btnclr = Button(cal,padx=16,pady=16, bd=8, fg="black",command = btncleardisplay ,bg="light blue",font=('arial',20, 'bold'),text="C").grid(row=4, column=1)
btneql = Button(cal,padx=16,pady=16, bd=8, fg="black",command = btneqldisplay,bg="light blue",font=('arial',20, 'bold'),text="=").grid(row=4, column=2)
#Addition button
btndiv = Button(cal,padx=16,pady=16, bd=8, fg="black",command = lambda:btnclick("/"),bg="light blue",font=('arial',20, 'bold'),text="/").grid(row=4, column=3)


cal.mainloop()