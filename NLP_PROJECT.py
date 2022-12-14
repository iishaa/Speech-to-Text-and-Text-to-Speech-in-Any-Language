
from tkinter import *
from tkinter.messagebox import showinfo
import gtts
from gtts import gTTS
import speech_recognition as sr
import googletrans
from google_trans_new import google_translator
import os
import playsound

mainwindow= Tk()
mainwindow.title('Text-To-Speech and Speech-To-Text Converter')
mainwindow.geometry('500x500')
mainwindow.resizable(0, 0)
mainwindow.configure(bg='aqua')

r = sr.Recognizer()

def speak(text1):
	language = 'en'
	speech = gTTS(text = text1, lang = language, slow = False)
	speech.save("text.mp3")
	playsound.playsound("text.mp3")
	os.remove("text.mp3")

	
 
def recordvoice(text):
    while True:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=1)
            voice=r.listen(source,timeout=9)
            try:    
                text1 = r.recognize_google(voice,language="en")
                print(text1)
                text.insert(END,text1 + "\n")
                break
            except sr.UnknownValueError:
                print("Could not understand")
            except sr.RequestError:
                print("Could not request result from google")



def TextToSpeech():   
	texttospeechwindow = Toplevel(mainwindow)
	texttospeechwindow.title('Text-to-Speech Converter')
	texttospeechwindow.geometry("500x500")
	texttospeechwindow.configure(bg='Blue')

	Label(texttospeechwindow, text='Text-to-Speech Converter', font=("Comic Sans MS", 15), bg='aqua').place(x=130)

	text = Text(texttospeechwindow, height=5, width=30, font=12)
	text.place(x=80, y=60)

	speakbutton = Button(texttospeechwindow, text='LISTEN', bg='coral', command=lambda: speak(str(text.get(1.0, END))))
	speakbutton.place(x=220, y=200)

	transbtn = Button(texttospeechwindow, text = "TRANSLATE", bg= 'coral',command = lambda: trans(str(text.get(1.0, END))))
	transbtn.place(x=210,y=300)

	transvalue = StringVar()
	translang = Label(texttospeechwindow, text="Enter Language Code:",font=("Comic Sans MS", 11), bg= 'coral')
	translang.place(x=75,y=250)
	transentry = Entry(texttospeechwindow, textvariable=transvalue,font=("Comic Sans MS", 11), bg= 'coral')
	transentry.place(x=255,y=250)

	 

	def trans(text1):
		translator = googletrans.Translator()
		translation = translator.translate(text1, dest=transvalue.get())
		print(translation.text)
		text.insert(END,translation.text)
		convertion = gtts.gTTS(translation.text,lang=transvalue.get())
		convertion.save("hello.mp3")
		playsound.playsound("hello.mp3")
		os.remove("hello.mp3")

	



def SpeechToText():
	speechtotextwindow = Toplevel(mainwindow)
	speechtotextwindow.title('Speech-to-Text Converter')
	speechtotextwindow.geometry("500x500")
	speechtotextwindow.configure(bg='pink')

	Label(speechtotextwindow, text='Speech-to-Text Converter', font=("Comic Sans MS", 15), bg='IndianRed').place(x=130)

	text = Text(speechtotextwindow, font=12, height=5, width=30)
	text.place(x=70, y=100)

	recordbutton = Button(speechtotextwindow, text='RECORD', bg='Sienna', command=lambda:  recordvoice(text))
	recordbutton.place(x=200, y=50)

	transpeakbtn = Button(speechtotextwindow, text = "TRANSLATE", bg= 'coral',command = lambda: speak1(str(text.get(1.0, END))))
	transpeakbtn.place(x=210,y=300)

	transvalue = StringVar()
	translang = Label(speechtotextwindow, text="Enter Language Code:",font=("Comic Sans MS", 11), bg= 'coral')
	translang.place(x=75,y=250)
	transentry = Entry(speechtotextwindow, textvariable=transvalue,font=("Comic Sans MS", 11), bg= 'coral')
	transentry.place(x=255,y=250)

	def speak1(text1):
		translator = googletrans.Translator()
		translation = translator.translate(text1, dest=transvalue.get())
		print(translation.text)
		text.insert(END,translation.text + "\n")
		convertion = gtts.gTTS(translation.text,lang=transvalue.get())
		convertion.save("save.mp3")
		playsound.playsound("save.mp3")
		os.remove("save.mp3")
		
		# text.delete("1.0",END)


#main window 
Label(mainwindow, text='Text-To-Speech and Speech-To-Text Converter',
     font=('Times New Roman', 16), bg='red', wrap=True, wraplength=450).place(x=50, y=0)
 
texttospeechbutton = Button(mainwindow, text='Text-To-Speech Conversion', font=('Comic Sans MS', 16), bg='Yellow', command=TextToSpeech)
texttospeechbutton.place(x=100, y=150)
 
speechtotextbutton = Button(mainwindow, text='Speech-To-Text Conversion', font=('Comic Sans MS', 16), bg='Yellow', command=SpeechToText)
speechtotextbutton.place(x=100, y=250)
 
mainwindow.update()
mainwindow.mainloop()