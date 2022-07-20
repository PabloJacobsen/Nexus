import speech_recognition as sr
import pyaudio
import gtts
from playsound import playsound

def Ouvindo():
    rec = sr.Recognizer()
    with sr.Microphone() as mic:
        rec.adjust_for_ambient_noise(mic)
        print("Escutando...")
        try:
            audio = rec.listen(mic)
            texto = rec.recognize_google(audio, language="pt-BR")
            return texto
        except:
            print('Voz não reconhecida, tente novamente!')

def Falando(frase):
    fala = gtts.gTTS(frase, lang='pt-br')
    fala.save('fala.mp3')
    playsound('fala.mp3')