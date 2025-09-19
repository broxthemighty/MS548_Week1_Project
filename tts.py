import sys
if not sys.warnoptions:
    import warnings

def speak(text_to_speak):
    import pyttsx3

    converter_tts_engine = pyttsx3.init()

    converter_tts_engine.setProperty('rate', 150)

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

speak("""
      Daisy, Daisy
Give me your answer do
I'm half crazy
All for the love of you
It won't be a stylish marriage
""")