import speech_recognition as sr

def Recibir_audio():
    # crea un objeto reconocedor de voz
    r = sr.Recognizer()

    # utiliza el micrófono como fuente de entrada
    with sr.Microphone() as source:
        print("Hable ahora...")
        # ajusta el ruido de fondo
        r.adjust_for_ambient_noise(source)
        
        # inicializa el texto escuchado
        texto = ""

        # escucha la voz del usuario hasta que se diga la palabra clave
        while True:
            # escucha la voz del usuario
            audio = r.listen(source)

            # utiliza el reconocedor de voz para transcribir la voz del usuario
            try:
                # obtiene el texto escuchado
                texto_escuchado = r.recognize_google(audio, language="es-ES")
                print(f"Escuchado: {texto_escuchado}")
                texto += texto_escuchado + "\n" # agrega el texto escuchado al texto total
                
                # verifica si se dijo la palabra clave para finalizar
                if "finalizar" in texto_escuchado:
                    return texto  # devuelve el texto que se ha escuchado y sale de la función
                
            except sr.UnknownValueError:
                print("No se pudo entender lo que dijo.")
            except sr.RequestError as e:
                print(f"No se pudo completar la solicitud: {e}")

