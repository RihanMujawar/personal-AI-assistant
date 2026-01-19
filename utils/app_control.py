import os
import subprocess
import pyautogui
from utils.tts import speak

def open_application(app_name):
    speak(f"Opening {app_name}")
    # Map common application names to their Linux equivalents
    app_mapping = {
        "chrome": "google-chrome",
        "firefox": "firefox",
        "calculator": "gnome-calculator",
        "terminal": "gnome-terminal",
        "gedit": "gedit",
        "vlc": "vlc"
    }
    
    # Use the mapped name if available, otherwise use the original name
    linux_app_name = app_mapping.get(app_name.lower(), app_name.lower())
    
    try:
        subprocess.Popen([linux_app_name])
    except FileNotFoundError:
        speak(f"Sorry, I couldn't find {app_name}")

def close_application(app_name):
    try:
        # Map common application names to their Linux process names
        process_mapping = {
            "chrome": "chrome",
            "firefox": "firefox",
            "calculator": "gnome-calculator",
            "terminal": "gnome-terminal",
            "gedit": "gedit",
            "vlc": "vlc"
        }
        
        process_name = process_mapping.get(app_name.lower(), app_name.lower())
        subprocess.run(["pkill", process_name])
        speak(f"Closed {app_name}")
    except subprocess.CalledProcessError:
        speak(f"Failed to close {app_name}")

def minimize_window(app_name):
    # On Linux, window management is more complex and desktop environment dependent
    # We'll use a general approach with xdotool if available
    try:
        subprocess.run(["xdotool", "search", "--name", app_name, "windowminimize"], 
                      stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        speak("Window management tools not available")

def maximize_window(app_name):
    # On Linux, window management is more complex and desktop environment dependent
    # We'll use a general approach with xdotool if available
    try:
        subprocess.run(["xdotool", "search", "--name", app_name, "windowmaximize"], 
                      stderr=subprocess.DEVNULL)
    except FileNotFoundError:
        speak("Window management tools not available")