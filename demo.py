# from google_trans_new import google_translator  
  
# translator = google_translator()  
# translate_text = translator.translate('สวัสดีจีน',lang_tgt='en')  
# print(translate_text)

# from tkinter import *

# imaginary_tech_root = Tk()

# # Width x Height
# imaginary_tech_root.geometry("644x434")

# # width, height
# imaginary_tech_root.minsize(300,100)

# # width, height
# imaginary_tech_root.maxsize(1200, 988)

# shakaib = Label(text="Shakaib is a good boy and this is his GUI")
# shakaib.pack()


# imaginary_tech_root.mainloop()

from tkinter import *
import PIL
from PIL import ImageTk
from PIL import Image

root = Tk()
root.geometry("600x300")
root.minsize(200,100)
# root.maxsize(1200,988)
root.title("Speech to text and text to speech in any language")



rootlabel = Label(text="Any text here")

title_label = Label(text='''If we need to work with other file formats,\n 
the Python Imaging Library contains classes that \n 
let you load images in over 30 formats and convert them to Tkinter-compatible image objects. \n 
So, in this case, we have to install the pillow library (if it is not installed in the system) \n
 by writing pip install pillow in the terminal and then write the code as follows:''',
  bg="blue", fg="white",padx=113,pady=94,font="Helvetica 9 bold", borderwidth=3, relief=SUNKEN)

title_label.pack(side=TOP,anchor="sw",fill=X)

# photo = PhotoImage(file="fbi.png" )

# image = Image.open("slika.jpg")
# photo = ImageTk.PhotoImage(image)
# photolabel = Label(image=photo)
# photolabel.pack()

rootlabel.pack()

root.mainloop()
