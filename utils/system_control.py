
import os
import subprocess
from utils.tts import speak

def shutdown_pc():
    speak("Shutting down")
    subprocess.run(["shutdown", "-h", "now"])

def restart_pc():
    speak("Restarting")
    subprocess.run(["reboot"])

def sleep_pc():
    speak("Sleeping now")
    subprocess.run(["systemctl", "suspend"])

