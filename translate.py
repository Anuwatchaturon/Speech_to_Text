from googletrans import Translator

#print(result.src) #The source language
#print(result.dest) #Destination language, which is set to English (en)
#print(result.origin) #Original text, that is 'Mitä sinä teet' in our example
#print(result.text) #Translated text, that will be 'what are you doing?' in our case
#print(result.pronunciation) # Pronunciation of the translated text

word = str(input('ข้อความ '))
src = str(input('เลือกภาษาต้นทาง '))
dest = str(input('เลือกภาษาปลายทาง '))
translator = Translator()
def translate():
    result = translator.translate(word, src= src, dest=dest)

    print(result.src)  # The source language
    print(result.origin)  # Original text, that is 'Mitä sinä teet' in our example
    print(result.dest)  # Destination language, which is set to English (en)
    print(result.text)  # Translated text, that will be 'what are you doing?' in our case

translate()
