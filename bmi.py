from tkinter import *
root=Tk()
root.title("BMI calculator")
root.configure(width=100,height=100)
root.configure(bg="black")
def calc():
    BMI=bmi_Val(mass.get(),height.get())
    Stat=getStatus()
    stat.set(Stat)
    bmi_Val.set(BMI,".2f")
def bmi_Val(mass,height):
    return  mass/height ** 2

def clear():
    stat.set('')
    bmi_Val.set('0.0')
    mas.delete(0,"end")
    heigh.delete(0, "end")

def getStatus():
    if bmi_Val.get()>40:
        return "You are Obese Class Number 3."
    elif bmi_Val.get()>35 or bmi_Val.get()<40:
        return "You are Obese Class Number 2."
    elif bmi_Val.get()>30 or bmi_Val.get()<35:
        return "You are Obese Class Number 1."
    elif bmi_Val.get()>25 or bmi_Val.get()<30:
        return "You are OverWeight."
    elif bmi_Val.get()>18.5 or bmi_Val.get()<25:
        return "You have Normal Weight."
    elif bmi_Val.get()>17 or bmi_Val.get()<18.5:
        return "You have Mild Thin."
    else:
        return "You have moderately Thin."

height=DoubleVar()
hlabel=Label(root,text="height",fg="red",bg="black",font=("Calibri 14 bold"),pady=5,padx=8)
heigh=Entry(root,textvariable=height)
hlabel.grid(row=2)
heigh.grid(row=2,column=1,columnspan=2,padx=5)
mass=DoubleVar()
wlabel=Label(root,text="Mass",fg="red",bg="black",font=("Calibri 14 bold"),pady=10,padx=2)
mas=Entry(root,textvariable=mass)
wlabel.grid(row=4)
mas.grid(row=4,column=1)
bmiVal=DoubleVar()
stat=StringVar()
bmi=Label(root,text="Bmi: ",fg="blue",bg="black",font=("Calibri 14 bold"),pady=10,padx=2,justify=LEFT)
status=Label(root,text="Status",fg="blue",bg="black",font=("Calibri 14 bold"),pady=10,padx=2,justify=LEFT)
statusMsg=Label(root,textvariable=stat,fg="white",bg="black",font=("Calibri 14 bold"),pady=10,padx=2,justify=LEFT)
bmiTotal=Label(root,textvariable=bmiVal,fg="white",bg="black",font=("Calibri 14 bold"),pady=10,padx=2,justify=LEFT)
bmi.grid(row=6)
status.grid(row=7)
bmiTotal.grid(row=6,column=1)
statusMsg.grid(row=7,column=1)
calc=Button(root,text="Calculate",fg="white",bg="black",font=("Calibri 12 bold"))
clear=Button(root,text="Reset",fg="white",bg="black",font=("Calibri 12 bold"))
calc.grid(row=8)
clear.grid(row=8,column=3)
root.mainloop()
