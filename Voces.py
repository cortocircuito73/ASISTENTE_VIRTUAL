import pyttsx3, time

tts=pyttsx3.init()
voices=tts.getProperty('voices')

i=0
for voice in voices:
	print(voice)
	tts.setProperty('voice',voices[i].id)
	tts.say('buenos dias')
	tts.runAndWait()
	time.sleep(1)
	i+=1
