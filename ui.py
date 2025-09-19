import sys
if not sys.warnoptions:
    import warnings

def speak(text_to_speak):
    import pyttsx3

    converter_tts_engine = pyttsx3.init()

    converter_tts_engine.setProperty('rate', 100)

    converter_tts_engine.setProperty('volume', 0.7)

    voice_list = converter_tts_engine.getProperty('voices')

    for each_voice in voice_list:
        print("\n\v ***Voice:***")
        print("ID: %s" % each_voice.id)
        print("Name: %s" % each_voice.name)
        print("Age: %s" % each_voice.age)
        print("Gender: %s" % each_voice.gender)
        print("Languages: %s" % each_voice.languages)

    converter_tts_engine.say(text_to_speak)

    converter_tts_engine.runAndWait()

"""speak("
      Daisy, Daisy
Give me your answer do
I'm half crazy
All for the love of you
")"""

try:
    import tkinter as tk
    from tkinter import ttk
except ImportError:
    tk = None

if tk is not None:
    def _on_speak(event=None):

        text = entry.get().strip()

        if not text:
            text = "I'm half crazy" 

        speak(text)

root = tk.Tk()

root.title("TTS")

frm = ttk.Frame(root, padding=12)

frm.grid(sticky="nsew")

root.columnconfigure(0, weight=1)

root.rowconfigure(0, weight=1)

ttk.Label(frm, text="give me something to say:").grid(row=0, column=0, sticky="w")

entry = ttk.Entry(frm, width=60)
entry.grid(row=1, column=0, padx=(0.8), pady=(4,8), sticky="ew")
entry.insert(0, "Greetings, no need to worry")

speak_btn = ttk.Button(frm, text="Speak", comman=_on_speak)
speak_btn.grid(row=1, column=1, sticky="e")

entry.bind("<Return>", _on_speak)

frm.columnconfigure(0, weight=1)
root.mainloop()