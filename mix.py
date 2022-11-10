from gtts import gTTS #Esta es la libreria que hace funcionar el texto a voz
import os #Llama a las funciones realizadas por el sistema operativo
import speech_recognition as sr #Libreria para reconocer la voz y convertirla en texto

language = 'es-us' #Se establece el lenguaje del lector del texto

r = sr.Recognizer() #Se asigna en r la funcion de reconocer la voz de la libreria

with sr.Microphone() as source: #Se tomara el microfono de nuestro dispositivo como fuente
    print('Di algo: ') #Mensaje para indicar cuando hablar
    audio = r.listen(source) #Indicación para que se escuche el texto ingresado por el usuario

    try:
        text = r.recognize_google(audio, language='es-MX')  #Guardamos el texto reconocido por la herramienta
                                                #de google, en los parametros se ingresa la fuente y el idioma
        print('Dijiste : {}'.format(text)) #Se escribe en texto lo que dijimos
    except:
        print('No se entendio') #En caso de error en algun proceso se muestra este texto

speech = gTTS(text=text, lang=language, slow=False) #Para que lea nuestro texto reconocido este se debe pasar
                                #como parametro, asi como el lenguaje y la velocidad
speech.save('test.mp3') #Se guarda el texto en un archivo de voz con un nombre establecido
os.system("start test.mp3") #Se le indica al sistema operativo que abra el archivo creado