import random
import speech_recognition as speech_recog
import time

mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}

level_choose = input('Выберите уровень сложности(легкий, средний, сложный):')



if level_choose == 'легкий':
    chosen_word = random.choise(levels['easy'])
    print(chosen_word)
elif level_choose == 'средний':
    chosen_word = random.choise(levels['medium'])
    print(chosen_word)
elif level_choose == 'сложный':
    chosen_word = random.choise(levels['hard'])
    print(chosen_word)
else:
    print('Неверный ввод! Попробуйте еще раз')

with mic as audio_file:
    print('Говорите')
    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)
    recognised_word = recog.recognize_google(audio, language="en-EN")
    print('Вы сказали', recognised_word)

if recognised_word == chosen_word:
    print ('Слово произнесено правильно!')
else:
    print('Увы, слово произнесено неправильно!')
