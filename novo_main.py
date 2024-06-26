from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox

# Importing the 'Car' class from the 'Car' module
from Car import Car

# Importing the 'DatabaseManager' class from the 'DatabaseManager' module
from DatabaseManager import DatabaseManager

# Creating an instance of the DatabaseManager class
database = DatabaseManager()



# Center window

def centrar (jan, jan_l, jan_a):

    ecra_l = jan.winfo_screenwidth()
    ecra_a = jan.winfo_screenheight()
    posx = ecra_l//2 - jan_l//2
    posy = ecra_a//2 - jan_a//2
    jan.geometry(f'{jan_l}x{jan_a}+{posx}+{posy}')


# Create window

init = Tk()
in_l = 600
in_a = 600
centrar(init, in_l, in_a)
init['bg']=('Linen')
init.resizable(0,0)
init.wm_overrideredirect(True) 
init.focus_force()


def choice():

    global choice
    tema = combo.get()
    init.destroy()




# criar botões com imagem inicial

b0 = Button(init, text = "Introduzir nova viatura", command=lambda: click_botao(b0, 1), cursor = 'hand2', relief='groove',height= 3, width=25).pack(pady = 10)
b1 = Button(init, text = "Consultar / Atualizar viatura", command=lambda: click_botao(b1, 2), cursor = 'hand2', relief='groove',height= 3, width=25).pack(pady = 10)
b2 = Button(init, text = "Remover viatura", command=lambda: click_botao(b2, 3), cursor = 'hand2', relief='groove',height= 3, width=25).pack(pady = 10)
b3 = Button(init, text = "Listar viaturas", command=lambda: click_botao(b3, 4), cursor = 'hand2', relief='groove',height= 3, width=25).pack(pady = 10)
b4 = Button(init, text = "Sair", command=lambda: click_botao(b4, 5), cursor = 'hand2', relief='groove',height= 3, width=25).pack(pady = 10)


init.mainloop()

'''
root = Tk()
root.title("Viaturas Serviço")
root.geometry("750x350")

label1 = Label(root, text="Matrícula", width=20,
               height=2).grid(row=1, column=0)
label2 = Label(root, text="Data Matrícula", width=20,
               height=2).grid(row=2, column=0)
label3 = Label(root, text="Marca", width=20,
               height=2).grid(row=3, column=0)
label4 = Label(root, text="Modelo", width=20, height=2
               ).grid(row=4, column=0)
label5 = Label(root, text="Categoria", width=20,
               height=2).grid(row=5, column=0)
label6 = Label(root, text="Data Última Revisão", width=20,
               height=2).grid(row=6, column=0)
label7 = Label(root, text="Email a notificar", width=20, height=2
               ).grid(row=7, column=0)

label8 = Label(root, width=10, height=2).grid(row=7, column=2)
label9 = Label(root, width=10, height=2).grid(row=7, column=4)

e1 = Entry(root, width=30, borderwidth=5)
e1.grid(row=1, column=2)
e2 = Entry(root, width=30, borderwidth=5)
e2.grid(row=2, column=2)
e3 = Entry(root, width=30, borderwidth=5)
e3.grid(row=3, column=2)
e4 = Entry(root, width=30, borderwidth=5)
e4.grid(row=4, column=2)
e5 = Entry(root, width=30, borderwidth=5)
e5.grid(row=5, column=2)
e6 = Entry(root, width=30, borderwidth=5)
e6.grid(row=6, column=2)
e7 = Entry(root, width=30, borderwidth=5)
e7.grid(row=7, column=2)
'''

'''
def Register():
    First_Name = e1.get()
    dbFirst_Name = ""
    Select = "select count(*) from student where First_Name='%s'" % (First_Name)
    mycursor.execute(Select)
    result = mycursor.fetchall()
    for i in result:
        dbFirst_Name = i[0]
    if(str(First_Name) != str(dbFirst_Name)):
        Insert = "Insert into student(First_Name,Last_Name,Phone_Number,Age) values(%s,%s,%s,%s)"
        First_Name = e1.get()
        Last_Name = e2.get()
        Phone_Number = e3.get()
        Age = e4.get()
        if(First_Name != "" and Last_Name != "" and Phone_Number != ""and Age != ""):
            Value = (First_Name, Last_Name,
                     Phone_Number, Age)
            mycursor.execute(Insert, Value)
            mydb.commit()
            messagebox.askokcancel("Information", "Record inserted")
            e1.delete(0, 'end')
            e2.delete(0, 'end')
            e3.delete(0, 'end')
            e4.delete(0, 'end')
        else:
            if (First_Name == "" and Last_Name == "" and Phone_Number == "" and Age == ""):
                messagebox.askokcancel(
                    "Information", "New Entery Fill All Details")
            else:
                messagebox.askokcancel("Information", "Some fields left blank")
    else:
        messagebox.askokcancel("Information", "Record Already exists")


def ShowRecord():
    First_Name = e1.get()
    dbFirst_Name = ""
    Select = "select count(*) from student where First_Name='%s'" % (First_Name)
    mycursor.execute(Select)
    result1 = mycursor.fetchall()
    for i in result1:
        dbFirst_Name = i[0]

    if int(First_Name) == int(dbFirst_Name):
        Select1 = "select First_Name,Last_Name,Phone_Number,Age from student where First_Name='%s'" % (
            First_Name)
        mycursor.execute(Select1)
        result2 = mycursor.fetchall()
        First_Name = ""
        Last_Name = ""
        Phone_Number = ""
        Age = ""
        for i in result2:
            First_Name = i[0]
            Last_Name = i[1]
            Phone_Number = i[2]
            Age = i[3]
        e2.insert(0, Last_Name)
        e3.insert(0, Phone_Number)
        e4.insert(0, Age)

        #messagebox.showinfo("Info", First_Name)
    else:
        messagebox.askokcancel("Information", "No Record exists")


def Delete():
    First_Name = e1.get()
    Delete = "delete from student where First_Name='%s'" % (First_Name)
    mycursor.execute(Delete)
    mydb.commit()
    messagebox.showinfo("Information", "Record Deleted")
    e1.delete(0,  'end')
    e2.delete(0,  'end')
    e3.delete(0,  'end')
    e4.delete(0,  'end')


button1 = Button(root, text="Register", width=10, height=2,
                 command=Register).grid(row=5, column=1)
button2 = Button(root, text="Delete", width=10, height=2,
                 command=Delete).grid(row=5, column=0)
button4 = Button(root, text="Show record", width=10, height=2,
                 command=ShowRecord).grid(row=5, column=2)

root.mainloop()
'''
