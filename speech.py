from tkinter import *
import tkinter as tk
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Di algo: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-MX')
        print('Dijiste : {}'.format(text))
    except:
        print('No se entendio nada')

# Intentar agregar una interfaz con el tkinter