from pynput import keyboard
import speech_recognition as sr
from googletrans import Translator

import time
import keyboard

language = ['af','sq','am','ar','hy','az','eu','be','bn','bs',
            'bg','ca','ceb','ny','zh-cn','zh-tw','co','hr','cs','da',
            'nl','en','eo','et','tl','fi','fr','fy','gl','ka',
            'de','el','gu','ht','ha','haw','iw','hi','hmn','hu',
            'is','ig','id','ga','it','ja','jw','kn','kk','km',
            'ku','ky','lo','la','lv','lt','lb','mk','mg','ms'
            'ml','mt','mi','mr','mn','my','ne','no','ps','fa',
            'pl','pt','pa','ro','ru','gd','sr','st','sn','sd',
            'si','sk','sl','so','sm','es','su','sw','sv','tg',
            'ta','te','th','tr','uk','ur','uz','vi','cy','xh',
            'yi','yo','zu','fil','he''ko',]

def main():
    #while True:
        lan = str(input('choose language '))
        lanchoose.append(lan)
        if lan in language:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Please say something")
                audio = r.listen(source)
                print("Recognizing Now .... ")
                # recognize speech using google
                try:
                    print ("You have said" )
                    word = r.recognize_google(audio,None,lan)
                    textlist.append(word)
                    print(word)
                    print("Audio Recorded Successfully \n ")
                except Exception as e:
                    print("Error :  " + str(e))
                # write audio
                #with open("recorded.wav", "wb") as f:
                    #f.write(audio.get_wav_data())
        #elif lan == 'esc':
             #break

        else:
            print('No language')


def translate():
    src = lanchoose[0]
    dest = str(input('traget language '))
    translator = Translator()
    word = textlist[0]
    result = translator.translate(word, src= src, dest=dest)

    print(result.src)  # The source language
    print(result.origin)  # Original text, that is 'Mitä sinä teet' in our example
    print(result.dest)  # Destination language, which is set to English (en)
    print(result.text)  # Translated text, that will be 'what are you doing?' in our case

    tranlist.append(result)

def Timer():
    print("10 second")
    for i in range (10):
        print(10-i, end=' ')
        time.sleep(1)
    print()

lanchoose = []
textlist = []
tranlist = []

main()
#translate()
#Timer()
#print('ภาษาที่เลือก')
#print(lanchoose)
#print('คำแปล จาก translate')
#print(tranlist)

