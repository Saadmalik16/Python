import time
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.Spvoice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("Hye Saad,  How Are you ?")
    time.sleep(5)
    speak("Welcome to the PUBG Mobile")