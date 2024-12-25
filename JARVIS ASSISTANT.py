import os
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import tkinter as tk
import math

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            update_status("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'JARVIS' in command:
                command = command.replace('JARVIS', '')
                print(command)
    except Exception as e:
        print(f"Error: {e}")
        return ""
    return command

def open_application(app_name):
    try:
        if 'notepad' in app_name:
            os.system('notepad')
        elif 'calculator' in app_name:
            os.system('calc')
        elif 'command prompt' in app_name or 'cmd' in app_name:
            os.system('start cmd')
        elif 'file explorer' in app_name:
            os.system('explorer')
        elif 'chrome' in app_name or 'browser' in app_name:
            os.system('start chrome')
        elif 'paint' in app_name:
            os.system('mspaint')
        elif 'word' in app_name:
            os.system('start winword')
        elif 'excel' in app_name:
            os.system('start excel')
        elif 'powerpoint' in app_name:
            os.system('start powerpnt')
        elif 'settings' in app_name:
            os.system('start ms-settings:')
        elif 'device manager' in app_name:
            os.system('start devmgmt.msc')
        elif 'store' in app_name:
            os.system('start ms-windows-store:')
        elif 'maps' in app_name:
            os.system('start bingmaps:')
        elif 'media player' in app_name:
            os.system('start mswindowsmusic:')
        elif 'photos' in app_name:
            os.system('start ms-photos:')
        else:
            talk(f"Sorry, I can't open {app_name} right now.")
    except Exception as e:
        print(f"Error: {e}")
        talk("An error occurred while opening the application.")

def describe_capabilities():
    capabilities = (
        "I am JARVIS, your voice assistant. I can perform the following functions: "
        "play music or videos on YouTube, tell the current time, provide information from Wikipedia, "
        "tell jokes, open local applications like Notepad, Calculator, File Explorer, Chrome, Paint, Word, Excel, etcetera, "
        "You can say 'stop' or 'thank you' to end our session."
    )
    talk(capabilities)

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '').strip()
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The current time is ' + current_time)
    elif 'who is' in command or 'what is' in command:
        person = command.replace('who is', '').replace('what is', '').strip()
        info = wikipedia.summary(person, sentences=2)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
    elif 'open' in command:
        app_name = command.replace('open', '').strip()
        open_application(app_name)
    elif 'who are you' in command or 'what can you do' in command:
        describe_capabilities()
    elif 'exit' in command or 'stop' in command or 'thank you' in command:
        talk("Goodbye! Have a great day!")
        root.destroy()
        exit()
    else:
        talk("I didn't understand that. Can you repeat?")

def update_status(message):
    status_label.config(text=message)
    root.update()

def animate_snake():
    global angle
    canvas.delete("all")

    # Neon "snake" effect
    num_segments = 20
    for i in range(num_segments):
        theta = angle + (i * math.pi / 10)
        x = 250 + 100 * math.cos(theta)
        y = 250 + 100 * math.sin(theta)
        color_intensity = int(255 * (i / num_segments))
        color = f"#{color_intensity:02x}{255 - color_intensity:02x}ff"
        canvas.create_oval(x - 10, y - 10, x + 10, y + 10, fill=color, outline="")

    angle += 0.1
    root.after(50, animate_snake)

def initiate_welcome_and_listen():
    update_status("Welcome to JARVIS. Initializing...")
    talk("Welcome! I am JARVIS, your voice assistant. How can I help you today?")
    while True:
        run_alexa()

# GUI Setup
root = tk.Tk()
root.title("JARVIS Voice Assistant")
root.geometry("500x500")
root.configure(bg="#0f0f1f")

canvas = tk.Canvas(root, width=500, height=400, bg="#0f0f1f", highlightthickness=0)
canvas.pack()

status_label = tk.Label(root, text="Initializing...", font=("Helvetica", 12), fg="white", bg="#0f0f1f")
status_label.pack(pady=10)

listener = sr.Recognizer()
engine = pyttsx3.init()
angle = 0
animate_snake()
root.after(1000, initiate_welcome_and_listen)
root.mainloop()
