

from tkinter import *
import math
import tkinter.messagebox
 
input_root = Tk()
input_root.title("Scientific calc1ulator")
input_root.configure(background = 'gray')
input_root.resizable(width=False, height=False)
input_root.geometry("450x568+450+90")
calc1 = Frame(input_root)
calc1.grid()
 
class Calc():
    def __init__(self):
        self.sum1=0
        self.present=''
        self.input=True
        self.input_check=False
        self.op=''
        self.output=False
 
    def numberInput(self, num):
        self.output=False
        input1=test_disp.get()
        input2=str(num)
        if self.input:
            self.present = input2
            self.input=False
        else:
            if input2 == '.':
                if input2 in input1:
                    return
            self.present = input1+input2
        self.display(self.present)
 
    def sum1Sum(self):
        self.output=True
        self.present=float(self.present)
        if self.input_check==True:
            self.mainFunction()
        else:
            self.sum1=float(test_disp.get())
 
    def display(self, value):
        test_disp.delete(0, END)
        test_disp.insert(0, value)
 
    def mainFunction(self):
        if self.op == "add":
            self.sum1 += self.present
        if self.op == "sub":
            self.sum1 -= self.present
        if self.op == "multi":
            self.sum1 *= self.present
        if self.op == "divide":
            self.sum1 /= self.present
        if self.op == "mod":
            self.sum1 %= self.present
        self.input=True
        self.input_check=False
        self.display(self.sum1)
 
    def operation(self, op):
        self.present = float(self.present)
        if self.input_check:
            self.mainFunction()
        elif not self.output:
            self.sum1=self.present
            self.input=True
        self.input_check=True
        self.op=op
        self.output=False
 
    def clearScreen(self):
        self.output = False
        self.present = "0"
        self.display(0)
        self.input=True
 
    def clearAllEntry(self):
        self.clearScreen()
        self.sum1=0
 
    def pi(self):
        self.output =  False
        self.present = math.pi
        self.display(self.present)
 
    def tau(self):
        self.output =  False
        self.present = math.tau
        self.display(self.present)
 
    def e(self):
        self.output =  False
        self.present = math.e
        self.display(self.present)
 
    def mathPM(self):
        self.output = False
        self.present = -(float(test_disp.get()))
        self.display(self.present)
 
    def squared(self):
        self.output = False
        self.present = math.sqrt(float(test_disp.get()))
        self.display(self.present)
 
    def cos(self):
        self.output = False
        self.present = math.cos(math.radians(float(test_disp.get())))
        self.display(self.present)
 
    def cosh(self):
        self.output = False
        self.present = math.cosh(math.radians(float(test_disp.get())))
        self.display(self.present)
 
    def tan(self):
        self.output = False
        self.present = math.tan(math.radians(float(test_disp.get())))
        self.display(self.present)
 
    def tanh(self):
        self.output = False
        self.present = math.tanh(math.radians(float(test_disp.get())))
        self.display(self.present)
 
    def sin(self):
        self.output = False
        self.present = math.sin(math.radians(float(test_disp.get())))
        self.display(self.present)
 
    def sinh(self):
        self.output = False
        self.present = math.sinh(math.radians(float(test_disp.get())))
        self.display(self.present)
 
    def log(self):
        self.output = False
        self.present = math.log(float(test_disp.get()))
        self.display(self.present)
 
    def exp(self):
        self.output = False
        self.present = math.exp(float(test_disp.get()))
        self.display(self.present)
 
    def acosh(self):
        self.output = False
        self.present = math.acosh(float(test_disp.get()))
        self.display(self.present)
 
    def asinh(self):
        self.output = False
        self.present = math.asinh(float(test_disp.get()))
        self.display(self.present)
 
    def expm1(self):
        self.output = False
        self.present = math.expm1(float(test_disp.get()))
        self.display(self.present)
 
    def lgamma(self):
        self.output = False
        self.present = math.lgamma(float(test_disp.get()))
        self.display(self.present)
 
    def degrees(self):
        self.output = False
        self.present = math.degrees(float(test_disp.get()))
        self.display(self.present)
 
    def log2(self):
        self.output = False
        self.present = math.log2(float(test_disp.get()))
        self.display(self.present)
 
    def log10(self):
        self.output = False
        self.present = math.log10(float(test_disp.get()))
        self.display(self.present)
 
    def log1p(self):
        self.output = False
        self.present = math.log1p(float(test_disp.get()))
        self.display(self.present)
 
sum_value = Calc()
 
test_disp = Entry(calc1, font=('Helvetica',20,'bold'),
                   bg='black',fg='white',
                   bd=30,width=28,justify=RIGHT)
test_disp.grid(row=0,column=0, columnspan=4, pady=1)
test_disp.insert(0,"0")
 
numbers = "123456789"
i=0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc1, width=6, height=2,
                          bg='black',fg='white',
                          font=('Helvetica',20,'bold'),
                          bd=4,text=numbers[i]))
        btn[i].grid(row=j, column= k, pady = 1)
        btn[i]["command"]=lambda x=numbers[i]:sum_value.numberInput(x)
        i+=1
       
clear_btn = Button(calc1, text=chr(67),width=6,
                  height=2,bg='light blue',
                  font=('Helvetica',20,'bold')
                  ,bd=4, command=sum_value.clearScreen
                 ).grid(row=1, column= 0, pady = 1)
 
clear_all_button = Button(calc1, text=chr(67)+chr(69),
                     width=6, height=2,
                     bg='light blue',
                     font=('Helvetica',20,'bold'),
                     bd=4,
                     command=sum_value.clearAllEntry
                    ).grid(row=1, column= 1, pady = 1)
 
sq_button = Button(calc1, text="\u221A",width=6, height=2,
               bg='light blue', font=('Helvetica',
                                       20,'bold'),
               bd=4,command=sum_value.squared
              ).grid(row=1, column= 2, pady = 1)
 
add_button = Button(calc1, text="+",width=6, height=2,
                bg='light blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:sum_value.operation("add")
                ).grid(row=1, column= 3, pady = 1)
 
Sub_button = Button(calc1, text="-",width=6,
                height=2,bg='light blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:sum_value.operation("sub")
                ).grid(row=2, column= 3, pady = 1)
 
Mul_button = Button(calc1, text="x",width=6,
                height=2,bg='light blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:sum_value.operation("multi")
                ).grid(row=3, column= 3, pady = 1)
 
Div_button = Button(calc1, text="/",width=6,
                height=2,bg='light blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:sum_value.operation("divide")
                ).grid(row=4, column= 3, pady = 1)
 
Zero_button = Button(calc1, text="0",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=lambda:sum_value.numberInput(0)
                 ).grid(row=5, column= 0, pady = 1)
 
dot_button = Button(calc1, text=".",width=6,
                height=2,bg='light blue',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:sum_value.numberInput(".")
                ).grid(row=5, column= 1, pady = 1)
Pm_button = Button(calc1, text=chr(177),width=6,
               height=2,bg='light blue', font=('Helvetica',20,'bold'),
               bd=4,command=sum_value.mathPM
              ).grid(row=5, column= 2, pady = 1)
 
Equal_button = Button(calc1, text="=",width=6,
                   height=2,bg='light blue',
                   font=('Helvetica',20,'bold'),
                   bd=4,command=sum_value.sum1Sum
                  ).grid(row=5, column= 3, pady = 1)
# ROW 1 :
Pi_button = Button(calc1, text="pi",width=6,
               height=2,bg='black',fg='white',
               font=('Helvetica',20,'bold'),
               bd=4,command=sum_value.pi
              ).grid(row=1, column= 4, pady = 1)
 
Cos_button = Button(calc1, text="Cos",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=sum_value.cos
               ).grid(row=1, column= 5, pady = 1)
 
Tan_button = Button(calc1, text="tan",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=sum_value.tan
               ).grid(row=1, column= 6, pady = 1)
 
Sin_button = Button(calc1, text="sin",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=sum_value.sin
               ).grid(row=1, column= 7, pady = 1)
 
# ROW 2 :
pi2_button = Button(calc1, text="2pi",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=sum_value.tau
               ).grid(row=2, column= 4, pady = 1)
 
cosh_button = Button(calc1, text="Cosh",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=sum_value.cosh
                ).grid(row=2, column= 5, pady = 1)
 
tanh_button = Button(calc1, text="tanh",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=sum_value.tanh
                ).grid(row=2, column= 6, pady = 1)
 
sinh_button = Button(calc1, text="sinh",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=sum_value.sinh
                ).grid(row=2, column= 7, pady = 1)
 
# ROW 3 :
log_button = Button(calc1, text="log",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=sum_value.log
               ).grid(row=3, column= 4, pady = 1)
 
exp_button = Button(calc1, text="exp",width=6, height=2,
                bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=sum_value.exp
               ).grid(row=3, column= 5, pady = 1)
 
mod_button = Button(calc1, text="Mod",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=lambda:sum_value.operation("mod")
                ).grid(row=3, column= 6, pady = 1)
 
E_button   = Button(calc1, text="e",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=sum_value.e
               ).grid(row=3, column= 7, pady = 1)
 
# ROW 4 :
log_button10 = Button(calc1, text="log10",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=sum_value.log10
                 ).grid(row=4, column= 4, pady = 1)
 
Cos_button   = Button(calc1, text="log1p",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=sum_value.log1p
                 ).grid(row=4, column= 5, pady = 1)
 
exp_buttonm1 = Button(calc1, text="expm1",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd = 4,command=sum_value.expm1
                 ).grid(row=4, column= 6, pady = 1)
 
gamma_button = Button(calc1, text="gamma",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=sum_value.lgamma
                 ).grid(row=4, column= 7, pady = 1)
# ROW 5 :
log_button2 = Button(calc1, text="log2",width=6,
                 height=2,bg='black',fg='white',
                 font=('Helvetica',20,'bold'),
                 bd=4,command=sum_value.log2
                ).grid(row=5, column= 4, pady = 1)
 
deg_button = Button(calc1, text="deg",width=6,
                height=2,bg='black',fg='white',
                font=('Helvetica',20,'bold'),
                bd=4,command=sum_value.degrees
               ).grid(row=5, column= 5, pady = 1)
 
acosh_button = Button(calc1, text="acosh",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=sum_value.acosh
                 ).grid(row=5, column= 6, pady = 1)
 
asinh_button = Button(calc1, text="asinh",width=6,
                  height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'),
                  bd=4,command=sum_value.asinh
                 ).grid(row=5, column= 7, pady = 1)
 
display_button = Label(calc1, text = "Scientific calc1ulator",
                   font=('Helvetica',30,'bold'),
                   bg='black',fg='white',justify=CENTER)
 
display_button.grid(row=0, column= 4,columnspan=4)
 
def Exit():
    Exit = tkinter.messagebox.askyesno("Scientific calc1ulator",
                                        "Do you want to exit?")
    if Exit>0:
        input_root.destroy()
        return
 
def Scientific():
    input_root.resizable(width=False, height=False)
    input_root.geometry("945x568+0+0")
 
 
def Standard():
    input_root.resizable(width=False, height=False)
    input_root.geometry("480x568+0+0")
 
Menu_bar = Menu(calc1)
 
# Menu_bar1 :
Menu_fle = Menu(Menu_bar, tearoff = 0)
Menu_bar.add_cascade(label = 'File', menu = Menu_fle)
Menu_fle.add_command(label = "Standard", command = Standard)
Menu_fle.add_command(label = "Scientific", command = Scientific)
Menu_fle.add_separator()
Menu_fle.add_command(label = "Exit", command = Exit)
 
# Menu_bar2 :
Menu_edit = Menu(Menu_bar, tearoff = 0)
Menu_bar.add_cascade(label = 'Edit', menu = Menu_edit)
Menu_edit.add_command(label = "Cut")
Menu_edit.add_command(label = "Copy")
Menu_edit.add_separator()
Menu_edit.add_command(label = "Paste")
 
input_root.config(menu=Menu_bar)
 
input_root.mainloop()