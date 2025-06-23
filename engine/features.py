from playsound import playsound
import os
import re
import pywhatkit as kit
from engine.command import speak
from engine.config import ASSISTANT_NAME
import eel
@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def opencommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()
    if query!="":
        speak("Opening " + query)
        os.system('start ' + query)
    else:
        speak("Not found")

def playyoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing " + search_term + "on youtube")
    kit.playonyt(search_term)

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None