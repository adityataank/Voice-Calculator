from tkinter import *
import speech_recognition as sr
import pyaudio
from math import factorial
from PIL import ImageTk, Image

def command(txt):
    if 'factorial' not in txt :
        ans = eval(txt.strip())
        l3 = Label(root,text = '',font=('Arial',14)).place(x=10,y=260)
        l3 = Label(root,text = 'answer is : {}'.format(str(ans)),font=('Arial',14)).place(x=10,y=260)
    elif 'factorial' in txt :
        ss = txt.split()
        ans = factorial(int(ss[-1]))
        l3 = Label(root,text = '',font=('Arial',14)).place(x=10,y=260)
        l3 = Label(root,text = 'Answer : {}'.format(str(ans)),font=('Arial',18)).place(x=10,y=260)

def speak():
    r = sr.Recognizer()
    with sr.Microphone() as source :
        audio = r.record(source,duration=5)
        txt = r.recognize_google(audio)
        l2 = Label(root,text='You said : {}'.format(txt),font=('Calibri',14)).place(x=10,y=230)
        command(txt)
    
root = Tk()

root.title('VOICE CALCULATOR')
root.geometry('400x500')
l = Label(root,text = 'Voice Calculator',font=('Calibri',20)).place(x=113,y=20)
img = ImageTk.PhotoImage(Image.open('icons8-calculator-80.png'))
panel = Label(root,image = img).place(x=160,y=60)
bt = Button(root,text='Tap to Speak',font=('Calibri',14),command=speak).place(x=143,y=160)

root.mainloop()
