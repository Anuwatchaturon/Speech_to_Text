import speech_recognition as sr
import keyboard
import pyautogui

language = ["th","en","ru"]

def main():
    while True:
        lan = str(input("choose languages "))
        if lan != 'esc':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                if lan in language:
                    print("Please say something")
                    audio = r.listen(source)
                    print("Recognizing Now .... ")
                    # recognize speech using google
                    try:
                        print("You have said \n" + r.recognize_google(audio, None, lan))
                        print("Audio Recorded Successfully \n ")
                    except Exception as e:
                        print("Error :  " + str(e))
                # write audio
                    with open("recorded.wav", "wb") as f:
                        f.write(audio.get_wav_data())
                else:
                    print('No language')
        else:
            break

if __name__ == "__main__":
    main()
