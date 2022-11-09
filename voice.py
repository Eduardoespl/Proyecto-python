from gtts import gTTS
import os

text = 'Probando probando 1 2 3'

language = 'es-us'

speech = gTTS(text=text, lang=language, slow=False)

speech.save('texto.mp3')

os.system("start texto.mp3")