# from tkinter import *

# root = Tk()

# def getvals():
#     print("Submitting form!!")
#     print(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservicevalue.get()}")

#     with open("record.txt","a") as f:
#         f.write(f"{namevalue.get(),phonevalue.get(),gendervalue.get(),emergencyvalue.get(),paymentvalue.get(),foodservicevalue.get()}")

# phonevalue = StringVar()
# gendervalue = StringVar()
# emergencyvalue = StringVar()
# paymentvalue= StringVar()
# foodservicevalue = IntVar())

# root.geometry("633x333")
# Label(root,text="Welcome to this page",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)

# name = Label(root,text="Name")
# phone = Label(root,text="PhoneNo.")
# gender = Label(root,text="Gender")
# emergency = Label(root,text="Emergency contact")
# payment = Label(root,text="Payment Mode")

# name.grid(row=1,column=2)
# phone.grid(row=2,column=2)
# gender.grid(row=3,column=2)
# emergency.grid(row=4,column=2)
# payment.grid(row=5,column=2)

# namevalue = StringVar()
# phonevalue = StringVar()
# gendervalue = StringVar()
# emergencyvalue = StringVar()
# paymentvalue= StringVar()
# foodservicevalue = IntVar()

# nameentry = Entry(root, textvariable=namevalue)
# phoneentry = Entry(root, textvariable=phonevalue)
# genderentry = Entry(root, textvariable=gendervalue)
# emergencyentry = Entry(root, textvariable=emergencyvalue)
# paymententry = Entry(root, textvariable=paymentvalue)

# nameentry.grid(row=1,column=3)
# phoneentry.grid(row=2,column=3)
# genderentry.grid(row=3,column=3)
# emergencyentry.grid(row=4,column=3)
# paymententry.grid(row=5,column=3)

# foodservice = Checkbutton(text="Want to prebook your meal?", variable=foodservicevalue).grid(row=6,column=3)

# Button(text="Submit",command=getvals).grid(row=7,column=3)


# root.mainloop()

from tkinter import *

root = Tk()

def getvals():
    print("Submitting form")

    print(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()} ")



    with open("record.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentmodevalue.get(), foodservicevalue.get()}\n ")



root.geometry("644x344")
#Heading
Label(root, text="Welcome to Harry Travels", font="comicsansms 13 bold", pady=15).grid(row=0, column=3)

#Text for our form
name = Label(root, text="Name")
phone = Label(root, text="Phone")
gender = Label(root, text="Gender")
emergency = Label(root, text="Emergency Contact")
paymentmode = Label(root, text="Payment Mode")

#Pack text for our form
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()


#Entries for our form
nameentry = Entry(root, textvariable=namevalue)
phoneentry = Entry(root, textvariable=phonevalue)
genderentry = Entry(root, textvariable=gendervalue)
emergencyentry = Entry(root, textvariable=emergencyvalue)
paymentmodeentry = Entry(root, textvariable=paymentmodevalue)

# Packing the Entries
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodeentry.grid(row=5, column=3)

#Checkbox & Packing it
foodservice = Checkbutton(text="Want to prebook your meals?", variable = foodservicevalue)
foodservice.grid(row=6, column=3)

#Button & packing it and assigning it a command
Button(text="Submit to Harry Travels", command=getvals).grid(row=7, column=3)



root.mainloop()