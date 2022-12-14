import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.ttk import Combobox
from PIL import ImageTk,Image

import googletrans
from google_trans_new import google_translator
import speech_recognition as sr
import gtts
import playsound
import os



root = Tk()
root.title("Speech to Text")
root.geometry("900x450")
# root.resizable(False,False)

def speak():
    with sr.Microphone() as source:
        convertion = gtts.gTTS("Type the language code you are going to speak",lang="en")
        convertion.save("lang.mp3")
        playsound.playsound("lang.mp3")
        os.remove("lang.mp3")
        langSpeak = speakvalue.get()

def trans():
    with sr.Microphone() as source:
        convertion = gtts.gTTS("Type the language code to translate",lang="en")
        convertion.save("trans.mp3")
        playsound.playsound("trans.mp3")
        os.remove("trans.mp3")
        langInput = transvalue.get()



    
def getvals():
    print("Speak Now!!")
    convertion = gtts.gTTS("Speak Now",lang="en")
    convertion.save("speak.mp3")
    playsound.playsound("speak.mp3")
    os.remove("speak.mp3")
    
    print(speakvalue.get(),transvalue.get())
    r = sr.Recognizer()
    with sr.Microphone() as source:

        r.adjust_for_ambient_noise(source,duration=1)
        voice = r.listen(source,timeout=9)
        try:
            text = r.recognize_google(voice,language=speakvalue.get())
            print(text)
            textbox.insert(1.0,text)

            #textbox=print(text)
            # if(text == "exit"):
            #     break
        except sr.UnknownValueError:
            print("Could not understand")
        except sr.RequestError:
            print("Could not request result from google")

        translator = googletrans.Translator()
        translation = translator.translate(text, dest= transvalue)
        print(translation.text)
        convertion = gtts.gTTS(translation.text,lang=transvalue)
        convertion.save("hello.mp3")
        playsound.playsound("hello.mp3")
        os.remove("hello.mp3")    


#icon
icon = PhotoImage(file="E:\\MCA 3RD SEM\\Complete Web Development\\nlpProject\\SpeechToTextChatCircle1.png")
root.iconphoto(False,icon)

#top frame
top_frame= Frame(root,bg="#0197f6",width=900,height=100)
top_frame.place(x=0,y=0)
top_frame.pack(fill=X)

#logo
logo = PhotoImage(file="E:\\MCA 3RD SEM\\Complete Web Development\\nlpProject\\images5.png")
Label(top_frame,image=logo,bg="sea green",width=90,height=82,pady=50).place(x=10,y=5)

Label(top_frame,text="Speech To Text - Text To Speech in Different Language",bg="#0197f6",fg="black",font="arial 18 bold").place(x=105,y=30)

speaklang = Label(root,text="Speaking language",font="arial 15",bg="light blue",fg="black")
speaklang.place(x=50,y=125)
speakbtn = Button(text="Speak",font="arial 15",bg="light blue",fg="black",command=speak).place(x=50,y=175)


translang = Label(root,text="Translation language",font="arial 15",bg="light blue",fg="black")
translang.place(x=500,y=125)
Button(text="trans",font="arial 15",bg="light blue",fg="black",command=trans).place(x=500,y=175)


#enter language
speakvalue = StringVar()
transvalue = StringVar()

speakEntry = Entry(root,textvariable=speakvalue,font="arial 15",bg="light grey")
speakEntry.place(x=250,y=125)



transEntry = Entry(root,textvariable=transvalue,font="arial 15",bg="light grey")
transEntry.place(x=700,y=125) 




Button(text="Done",font="arial 15",bg="light blue",fg="black",command=getvals).place(x=1025,y=125)

#text box
textbox = Text(root,font="Robot 15",bg="light grey",relief=GROOVE,wrap=WORD)
textbox.place(x=75,y=325,width=500,height=250)

textbox = Text(root,font="Robot 15",bg="light grey",relief=GROOVE,wrap=WORD)
textbox.place(x=950,y=325,width=500,height=250)


#Label of text box
Label(root,text="Speaking Language",bg="light blue",fg="black",font="arial 18").place(x=100,y=289)

Label(root,text="Translated Language",bg="light blue",fg="black",font="arial 18").place(x=975,y=289)




# trans()



root.mainloop()

