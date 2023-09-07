from tkinter import *
import secrets as srt
import string as str

def pass_generate():
    try:
        lenght = int(pass_int.get())
        alphabet = str.ascii_letters + str.digits
        password = ''.join(srt.choice(alphabet) for i in range(lenght))
        pass_entry.insert(END, password)
    except:
        return 'Error'


def reset():
    pass_entry.delete(0, END)


pass_gene = Tk()
pass_gene.title("Password Generator")
pass_gene.geometry("280x300")
pass_gene.configure(bg='mediumspringgreen')

frame = Frame(pass_gene)
frame.pack(fill=BOTH)
frame.configure(bg='mediumspringgreen')

label_main = Label(frame, font=("Couri er", 18, "italic", "bold"), text='Password Generator', bg='mediumspringgreen')
label_main.pack(fill=BOTH)

label_user = Label(frame, font=("Times", 16, "bold", 'italic'), text='Username:', bg='mediumspringgreen')
label_user.pack(fill=BOTH)

username = StringVar()
username.set("Muhammad Mujtaba Rawn")
name = Entry(frame, textvariable= username, state=DISABLED, font=("Times", 14, 'italic'), highlightthickness=2, bd=2)
name.pack(ipadx=30, ipady=2)

label_lenght = Label(frame, font=("Times", 16, "bold", 'italic'), text='Password Lenght:', bg='mediumspringgreen')
label_lenght.pack(fill=BOTH)

pass_int = Entry(frame, font=("Times", 14, 'italic'), highlightthickness=2, bd=2)
pass_int.pack(ipadx=30, ipady=2)

pasword = Label(frame, font=("Times", 16, "bold", 'italic'), text='Generated Password', bg='mediumspringgreen')
pasword.pack(fill=BOTH)

var_password = StringVar()
pass_entry = Entry(frame, font=("Times", 14, 'italic'), highlightthickness=2, bd=2, textvariable=var_password)
pass_entry.pack(ipadx=30, ipady=2)

enter_button = Button(frame, text='Generate', font=14, highlightthickness=2, bd=2, command=pass_generate, bg='gray')
enter_button.pack_configure()

reset_button = Button(frame, text='Reset', font=14, highlightthickness=2, bd=2, command=reset, bg='olive')
reset_button.pack_configure()

pass_gene.mainloop()