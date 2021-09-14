import speech_recognition as speech
import subprocess
import datetime
import pyautogui
import sounddevice as sd
from scipy.io.wavfile import write
# import playsound
# from gtts import gTTS, lang, tts

# def capture(k):
#     x = str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S"))
#     x += k
#     pyautogui.screenshot().save('Temp\\Capture\\'+ x +'.jpg')  

# frequency record avg [44100 - 48000]
frame = 44100
# second
time = 2
data = speech.Recognizer()
print('start')
with speech.Microphone() as source:
    while True:
        # print('listening')
        
        print("record")
        audio = data.listen(source)
        
        try:
            sound = str(data.recognize_google(audio, None,'th'))
            # tts = gTTS(text=sound, lang="th")
            print('said : '+sound)
            
            if sound.find("ตอบอะไร") >= 0:
                subprocess.run("tasklist /fi \"STATUS eq RUNNING\" > running.txt", shell=True)
                
                with open("running.txt", 'r') as f:
                    x = f.read()

                subprocess.run("del \"running.txt\"", shell=True)
                    # print(x.find("Discord"))
                if (x.find("TeamSpeak") >= 0 ) or (x.find("Skype") >=0 ) or (x.find("Discord") >= 0):
                    print("detect")
                    
                    with open("Temp/log_interrupt.txt", 'a') as f:
                        f.write('\n'+str(datetime.datetime.now().strftime("%d %b %Y_%H%M%S")) + ':' + sound+'\n')
                else:
                    print("pass")

        except:
            # print('-------')
            pass
        # audio = ""
