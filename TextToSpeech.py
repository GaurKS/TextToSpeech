
#from gtts import gTTS
#import os

#myTxt = " This is a random text. It is to judge the functionality of the made application "

#language = "en"

#output = gTTS(Text=myTxt, lang=language, slow=False)

#output.save("output.mp3")

#os.system("start output.mp3")


from typing import Text
from gtts import gTTS
mytxt = input("Enter your text for conversion : ")
tts = gTTS(mytxt, lang='hi')
tts.save('./desktop./YourAudio.mp3')
print("Program Finished Successfully...\nCheck for the audio file in your desktop")