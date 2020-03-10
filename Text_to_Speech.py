from gtts import gTTS
import os

def text_to_speech(name):
    new=[]
    x=""
    for i in range(0, len(name)):
        for j in range(0, 2):
            new.append(str(name[i][j]))

    for i in range(len(new)):
        x+=new[i]
        x+=" "
    tts = gTTS(text=x, lang='en')
    tts.save("good.mp3")
    
    
n=[["astha","16451"], ["palaak", "16465"], ["arunima","16MI535"]]
text_to_speech(n)
os.system("good.mp3")