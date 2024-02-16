import gtts
import playsound
text=input("Enter a Smoting here :")
sound=gtts.gTTS(text,lang='en')
sound.save("welcome.mp3")
playsound.playsound("welcome.mp3")