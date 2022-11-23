import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import os
import sys
from tkinter import *
from functools import partial

def validateLogin(username, password):
	print("username entered :", username.get())
	print("password entered :", password.get())
	return

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Tkinter Login Form - pythonexamples.org')

#username label and text entry box
usernameLabel = Label(tkWindow, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  

validateLogin = partial(validateLogin, username, password)

#login button
loginButton = Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)  

tkWindow.mainloop()


engine= pyttsx.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    print('computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >=0 and currentH < 12:
        speak('Good Morning')

    if currentH >=12 and currentH < 18:
        speak('Good Afternoon')

    if currentH >=18 and currentH !=0:
        speak('Good Evening')

greetMe()

speak('hello Sir I am your digital assistant')
speak('how may i help you ?')

def myCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')

    except sr.UnknownValueError:
        speak('Sorry Sir i didn\'t get that! Try typing the command')
        query = str(input('command ' ))
    return query

if __name__=='__main__':

    while True:

        query = myCommand();
        query = query.lower()

        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.com')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif 'book train tickets ' in query:
            speak('just a moment sir')
            webbrowser.open('www.irctc.com')

        elif 'book hotel' in query :
            speak('ok sir')
            webbrowser.open('www.oyo.com')


        elif "what\'s up" in query or "how are you" in query:
            stMsgs = ['just doing my things','I am fine','Nice','Nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()

        elif 'facebook' in query:
            speak ('ok sir')
            webbrowser.open('www.facebook.com')

        else:
            query = query
            speak('searching...')
            try:
                results=wikipedia.summary(query, sentances=2)
                speak('got it.')
                speak ('Wikipedia says - ')
                speak(results)

            except:
                webbrowser.open('https://www.google.com/search?q=',query)
        speak('Next Command Sir')
            


 





    
        
        
