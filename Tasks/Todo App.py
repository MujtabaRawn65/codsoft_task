from tkinter import *

def addTodo():
    add = entry.get()
    if add:
        listbox.insert(END, add)
        entry.delete(0, END)


def removeTodo():
    try:
        remove_index = listbox.curselection()
        listbox.delete(remove_index)
    except:
        return

def updateTodo():
    try:
        update_index = listbox.curselection()
        updation = entry.get()
        if updation:
            removeTodo()
            listbox.insert(update_index, updation)
            entry.delete(0, END)
    except:
        return


def saveTodos():
    items = listbox.get(0, END)
    with open("Todos.txt", "w") as f:
        for item in items:
            f.write(item + "\n")



def load_saved_items():
    try:
        with open("Todos.txt", 'r') as f:
            items = f.readlines()
            for item in items:
                listbox.insert(END, item.strip())
    except:
        return


todo = Tk()
todo.title("Todo App")
todo.geometry("500x325")
todo.configure(bg='skyblue')

screen_frame = Frame(todo, bd=2)
screen_frame.grid(column=0, row=0, padx=20, pady=20, sticky='nsew')

button_frame = Frame(todo, bd=2)
button_frame.grid(row=0, column=1)
button_frame.configure(bg='skyblue')

screen_frame.columnconfigure(0, weight=1)
screen_frame.rowconfigure(0, weight=1)

listbox = Listbox(screen_frame, height=17, width=50)
listbox.pack(side = LEFT, fill = BOTH)
scrollbar = Scrollbar(screen_frame)
scrollbar.pack(side = RIGHT, fill = BOTH)
listbox.config(yscrollcommand = scrollbar.set)
scrollbar.config(command = listbox.yview)

entry = Entry(button_frame)
entry.pack()

add_button = Button(button_frame, text='Add Todo', command=addTodo)
add_button.pack(pady=4)

remove_button = Button(button_frame, text='Remove Todo', command=removeTodo)
remove_button.pack(pady=4)

update_button = Button(button_frame, text='Update Todo', command=updateTodo)
update_button.pack(pady=4)

save_button = Button(button_frame, text='Save Todos', command=saveTodos)
save_button.pack(pady=4)

load_saved_items()

todo.mainloop()