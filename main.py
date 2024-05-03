import pyttsx3
from pocketsphinx import LiveSpeech
from graphics.home import start_window
from logic.task_executor import task_executor_main

def takeAudioInput():
    print("Listening...")
    speech = LiveSpeech()
    for phrase in speech:
        phrase_text = str(phrase).lower()
        if phrase_text == ""or  phrase_text == " ":
            continue
        print("Heard:", phrase_text)
        if phrase_text == "exit" or phrase_text == "quit" or phrase_text == "goodbye" or phrase_text == "bye" or phrase_text == "stop":
            break
        elif phrase_text == "hello" or phrase_text == "hi" or phrase_text == "hey":
            engine = pyttsx3.init()
            engine.say("Hello, how can I help you?")
            engine.runAndWait()
        else:
            task_executor_main(phrase_text)

def takeTextInput():
    while True:
        user_input = input("Enter a command: ")
        if user_input == "" or user_input == " ":
            continue
        if user_input == "exit" or user_input == "quit" or user_input == "goodbye" or user_input == "bye" or user_input == "stop":
            break
        task_executor_main(user_input)

def main():
    # This is for triggering the command line version of the application
    takeTextInput()
    # This is for triggering the voice version of the application
    # takeAudioInput()
        
    

if __name__ == "__main__":
    # This is for triggering the gui version of the application
    # start_window(main)
    main()
