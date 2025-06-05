import subprocess

def speak(text):
    subprocess.run([
        "powershell",
        "-Command",
        f"Add-Type -AssemblyName System.Speech; "
        f"(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')"
    ])

if __name__ == "__main__":
    print("Welcome to Fast RoboSpeaker (PowerShell-based)")
    while True:
        x = input("Enter what you want me to speak : ")
        if x.lower() == "q":
            speak("Bye Bye Friends")
            break
        speak(x)
        
 # type: ignore