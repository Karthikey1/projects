# src/voice_input.py

import speech_recognition as sr

def listen_for_command():
    """Listen for a voice command and return it."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for command...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print(f"Command: {command}")
        return command
    except Exception as e:
        print(f"Error: {e}")
        return None
