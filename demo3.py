from tkinter import *

def getvals():
    print(f"The value of user is {uservalue.get()}")
    print(f"the value of password is {passwordvalue.get()}")

root = Tk()
root.geometry("655x400")
root.title("Tkinter")

user = Label(root,text="UserName")
password = Label(root,text="Password")
user.grid()
password.grid(row=1)

uservalue = StringVar()
passwordvalue = StringVar()

userentry = Entry(root,textvariable="uservalue")
passwordentry = Entry(root,textvariable="passwordvalue")

userentry.grid(row=0,column=1)
passwordentry.grid(row=1,column=1)

Button(text="submit", command=getvals).grid()
root.mainloop()

# from tkinter import *

# def getvals():
#     print(f"The value of username is {uservalue.get()}")
#     print(f"The value of password is {passvalue.get()}")


# root = Tk()
# root.geometry("655x333")

# user = Label(root, text="Username")
# password = Label(root, text="Password")
# user.grid()
# password.grid(row=1)

# # Variable classes in tkinter
# # BooleanVar, DoubleVar, IntVar, StringVar

# uservalue = StringVar()
# passvalue = StringVar()

# userentry = Entry(root, textvariable = uservalue)
# passentry = Entry(root, textvariable = passvalue)

# userentry.grid(row=0, column=1)
# passentry.grid(row=1, column=1)

# Button(text="Submit", command=getvals).grid()

# root.mainloop()