import pyttsx3

# Text 2 Speech
t2s = pyttsx3.init()

# Voz español
voices = t2s.getProperty('voices')
t2s.setProperty('voice', voices[-1].id)

saludo = """ 
    Hola, a todos. Mi nombre Crecencio García.
    Bienvenidos al diplomado de programación Python.
"""

t2s.say(saludo)
t2s.runAndWait()