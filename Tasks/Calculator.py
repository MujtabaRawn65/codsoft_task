from tkinter import *

def appear(x):
    return lambda: results.insert(END, x)

def perform_calculation():
    expression = results.get()
    try:
        result = eval(expression)
        results.delete(0, END)  
        results.insert(END, result)
    except Exception:
        results.delete(0, END)  
        results.insert(END, "Error")

def clr():
    return results.delete(0,END)

calculator = Tk()
calculator.title('Calcualtor')
calculator.geometry('270x500')
calculator.configure(bg='gray')

screen = Frame(calculator, bd=2)
buttons = Frame(calculator, bd=2)
screen.grid(column=0, row=0, padx=25, pady=25, sticky='nsew')
buttons.grid(column=0, row=1, padx=25, pady=25)
buttons.configure(bg='gray')

calculator.columnconfigure(0, weight=1)
calculator.rowconfigure(0, weight=1)


numbers=["7", "8", "9", "4", "5", "6", "1", "2", "3"]

for index in range(9):
   row = index // 3  
   col = index % 3   
   n = numbers[index]
   Button(buttons, bg="White", text=n, width=5, height=2, command=appear(n)).grid(padx=5, pady=5, row=row, column=col)

zero= Button(buttons, bg="White", text="0", width=5, height=2, command=appear("0"))
zero.grid(padx=5, pady=5, column=1, row=3)

functions=["-", "+", "*", "/"]
for index in range(4):
    nop = functions[index]
    Button(buttons, bg="Yellow", text=nop, width=5, height=2,command=appear(nop)).grid(padx=5, pady=5, row=index%4, column=3) 

equals= Button(buttons, bg="Green", text="=", width=5, height=2,command=perform_calculation)
equals.grid(padx=5, pady=5, row=3, column=2) 

clear = Button(buttons,bg="Red", text="CLR", width=5, height=2, command=clr)
clear.grid(padx=5, pady=5, row=3, column=0)

numbers = StringVar()
results = Entry(screen, textvariable=numbers, width=30, font=80)
results.pack(expand=True, fill="both")

calculator.mainloop()