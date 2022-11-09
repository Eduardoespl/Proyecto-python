from gtts import gTTS
import os
import speech_recognition as sr

language = 'es-us'

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Di algo: ')
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language='es-MX')
        print('Dijiste : {}'.format(text))
    except:
        print('No se entendio nada')

speech = gTTS(text=text, lang=language, slow=False)
speech.save('test.mp3')
os.system("start test.mp3")