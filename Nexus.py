from ast import Import
import string
import speech_recognition as sr
import pyaudio
import fun
import gtts
from playsound import playsound

end = False
while(end == False):
    texto = fun.Ouvindo()
    fun.Falando(texto)
    if(texto == 'sair' or texto == 'encerrar'):
        break