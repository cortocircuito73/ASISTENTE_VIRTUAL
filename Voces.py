import pyttsx3, time

tts=pyttsx3.init()
voices=tts.getProperty('voices')
tts.setProperty('voice',voices[1].id)
tts.say('suscribete a corto circuito 73')
tts.say('no olvides dejar tu like, comentar y compartirlo con tus amigos')
tts.runAndWait()


'''i=0
for voice in voices:
	print(voice)
	tts.setProperty('voice',voices[i].id)
	tts.say('buenos dias')
	tts.runAndWait()
	time.sleep(1)
	i+=1
	'''