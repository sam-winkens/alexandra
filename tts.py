# tts.py
# a text to speech using the tkinter application framework
# Samuel Winkens, 2023

import tkinter as tk
import pyttsx3

# setting up window settings
window = tk.Tk()
window.title('Text-To-Speech')
window.geometry('900x450')
window.resizable(False,False)
window.configure(bg='#305065')

# setting up the pyttsx3 engine and assigning properties
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 130)
engine.setProperty('voice', voices[0].id)

# event function to speak the inputted text
def speak():
    text=text_entry.get('1.0', 'end')
    engine.say(text)
    engine.runAndWait()

# add icon image(change later)...
image_icon = tk.PhotoImage(file='images/speak.png')
window.iconphoto(False,image_icon)

# setting up top FRAME over the base window
top_frame = tk.Frame(window,bg='white', width=900, height=40)
top_frame.place(x=0, y=0)

# text for application
label = tk.Label(top_frame, text='TEXT TO SPEECH', font='arial 20 bold', bg='white', fg='black')
label.place(x=0, y=0)

# text entry for user to input text
text_entry = tk.Text(window, font='Robote 20', bg='white', relief='groove', wrap='word')
text_entry.place(x=10, y=150, width=500, height=250)

# button to call the speak event function
speak_button = tk.Button(window, text='Speak', compound='left', font='arial 20 bold', command=speak)
speak_button.place(x=675,y=240)

window.mainloop()
input()