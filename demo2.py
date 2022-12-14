from tkinter import *
from tkinter import ttk

# root = Tk()

# root.geometry("655x333")
# root.title("Python GUI")

# frame1 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
# frame1.pack(side= LEFT,fill=Y)

# frame2 = Frame(root, bg="grey", borderwidth=9,relief=SUNKEN)
# frame2.pack(side=TOP,fill=X)

# l1= Label(frame1,text="Project Tkinter GUI")
# l1.pack(pady=142)

# l2= Label(frame2,text="Welcome to this page",font="Helvetica 16 bold", fg="red",pady=22)
# l2.pack()

# root.mainloop()

win = Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Configure the color of the window
win.configure(bg='#65A8E1')

# Define the style for combobox widget
style = ttk.Style()
style.theme_use('xpnative')

# Define an event to close the window
def close_win(e):
   win.destroy()

# Add a label widget
label = ttk.Label(win, text="Eat, Sleep, Code and Repeat", font=('Times New Roman italic', 22), background="black", foreground="white")
label.place(relx=.5, rely=.5, anchor=CENTER)

win.mainloop()