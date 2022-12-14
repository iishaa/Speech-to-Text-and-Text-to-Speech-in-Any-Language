import googletrans
from google_trans_new import google_translator
import speech_recognition as sr
import gtts
import playsound
import os


r = sr.Recognizer()


while True:
	with sr.Microphone() as source:
		
		convertion = gtts.gTTS("Type the language code you are going to speak",lang="en")
		convertion.save("lang.mp3")
		playsound.playsound("lang.mp3")
		os.remove("lang.mp3")
		langSpeak = input("Type the language code you are going to speak: ")

		
		convertion = gtts.gTTS("Type the language code to translate",lang="en")
		convertion.save("trans.mp3")
		playsound.playsound("trans.mp3")
		os.remove("trans.mp3")
		langInput = input("Type the language code to translate: ")

		print("Speak Now!!")
		convertion = gtts.gTTS("Speak Now",lang="en")
		convertion.save("speak.mp3")
		playsound.playsound("speak.mp3")
		os.remove("speak.mp3")
		
		r.adjust_for_ambient_noise(source,duration=1)
		voice = r.listen(source,timeout=9)
		try:
			text = r.recognize_google(voice,language=str(langSpeak))
			print(text)
			if(text == "exit"):
				break
		except sr.UnknownValueError:
			print("Could not understand")
		except sr.RequestError:
			print("Could not request result from google")



		# langInput = input("Type the language code to translate: ")
		translator = googletrans.Translator()
		translation = translator.translate(text, dest= str(langInput))
		print(translation.text)
		convertion = gtts.gTTS(translation.text,lang=str(langInput))
		convertion.save("hello.mp3")
		playsound.playsound("hello.mp3")
		os.remove("hello.mp3")

