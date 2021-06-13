import pyttsx3 as speaker
import speech_recognition as sr
import operator as main_calculator
engine = speaker.init('sapi5')
voices = engine.getProperty('voices')
#print("hi")
#print(voices)
engine.setProperty('voices', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
while True:
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            speak("hello i am your mathematical speech calculator you can start asking basic question for example 3 plus 3")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            my_string = r.recognize_google(audio)
            print(my_string)
        def get_sum(op):
            return {
                '+': main_calculator.add,
                '-': main_calculator.sub,
                'x': main_calculator.mul,
                'divided': main_calculator.__truediv__ 
            }[op]
        def eval(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_sum(oper)(op1, op2)
        speak('the answer is')
        speak(eval(*(my_string.split())))
    except Exception as e:
        print('sorry sir somthing went wrong')
        speak('sorry sir somthing went wrong')