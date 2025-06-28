import os
import speech_recognition as sr
import unicodedata
import random
import time

def oyente():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Habla...")
        r.adjust_for_ambient_noise(source)  # adjust for ambient noise
        audio = r.listen(source)
        return r.recognize_google(audio, language='es-CR')
"""  

    

niveles = {

"facil": ["agenda", "ami", "souris", "chat", "chien", "maison", "livre", "pomme", "soleil", "eau"],
"intermedio": ["ordinateur", "algorithme", "développeur", "bibliothèque", "fromage", "montagne", "voiture", "fenêtre", "chanson", "hôpital"],
"dificil": ["réseau neuronal", "apprentissage automatique", "intelligence artificielle", "développement durable", "responsabilité civile", "phénomène météorologique", "biodiversité", "gouvernement", "psychologie", "architecture"]
}

puntaje = 0



while True:
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Elige un nivel de dificultad: facil, intermedio o dificil o salir para terminar el juego")
        audio = r.listen(source)
    # recognize speech using Google Speech Recognition

    texto = r.recognize_google(audio, language='es-CR')
    texto_normalizado = unicodedata.normalize('NFKD', texto).encode("ascii","ignore").decode("utf-8")


    try:
        print("Pienso que dijiste: " + texto_normalizado)
        if texto_normalizado.lower() == "facil":
            print("Nivel facil")
            random_word = random.choice(niveles["facil"])
            print(f"Pronuncia: {random_word}")
            with sr.Microphone() as source:
                audioFr = r.listen(source)
            textoFr = r.recognize_google(audioFr, language='fr-FR')
            if textoFr.lower() == random_word:
                print("¡Correcto!")
                puntaje += 1
            else:
                print(f"Incorrecto")
        elif texto_normalizado.lower() == "intermedio":
            print("Nivel intermedio")
            random_word = random.choice(niveles["intermedio"])
            print(f"Pronuncia: {random_word}")
            with sr.Microphone() as source:
                audioFr = r.listen(source)
            textoFr = r.recognize_google(audioFr, language='fr-FR')
            if textoFr.lower() == random_word:
                print("¡Correcto!")
                puntaje += 1
            else:
                print(f"Incorrecto")
        elif texto_normalizado.lower() == "dificil":
            print("Nivel dificil")
            random_word = random.choice(niveles["dificil"])
            print(f"Pronuncia: {random_word}")
            with sr.Microphone() as source:
                audioFr = r.listen(source)
            textoFr = r.recognize_google(audioFr, language='fr-FR')
            if textoFr.lower() == random_word:
                print("¡Correcto!")
                puntaje += 1
            else:
                print(f"Incorrecto")
        elif texto_normalizado.lower() == "salir":
            print("Saliendo del juego")
            break
        else:
            print("Por favor, elige un nivel válido: facil, intermedio o dificil")
    except sr.UnknownValueError:
        print("No entendi lo que dijiste")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    print(f"Tu puntaje actual es: {puntaje}")
"""