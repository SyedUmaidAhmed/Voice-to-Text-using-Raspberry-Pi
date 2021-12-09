import speech_recognition as sr
from time import sleep

r = sr.Recognizer()
mic = sr.Microphone()

while True:

    with mic as source:
        audio = r.listen(source)
    try:
        words = r.recognize_google(audio,language='en-IN')
        print(words)

        if words == "hello robot":
            print("Syed Umaid Ahmed")
            #Camera will see up
            
        if words == "follow me":
            #Tyres activataion
            print("Chalo CHalen")

        if words == "bring a glass of water":
            #STart Drifting and Go find object pick
            print("Chalo CHalen")

        if words == "exit":
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("...")
            sleep(1)
            print("Goodbye")
    except Exception as e:
        print("Try Again")
    
