import random
import speech_recognition as speech_recog
import time

mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()

def gameplay():
    with mic as audio_file:
        print('Говорите')
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        print("You said: " + recog.recognize_google(audio, language="en-EN"))

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}

level_choose = input('Выберите уровень сложности(легкий, средний, сложный):')


if level_choose == 'легкий':
    print(random.choice(levels["easy"]))
    gameplay()

elif level_choose == 'средний':
    print(random.choice(levels["medium"]))
    gameplay()

elif level_choose == 'сложный':
    print(random.choice(levels["hard"]))
    gameplay()

else:
    print('Неверный ввод! Попробуйте еще раз')


