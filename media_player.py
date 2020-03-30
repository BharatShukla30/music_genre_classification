# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 20:58:36 2020

@author: mouseless
"""
import os
import pygame
import mutagen.mp3
from mutagen.id3 import ID3
import tkinter as tk
import PyQt5

root=tk.Tk()
root.minsize(300,300)

listofsongs = []
realnames = []

v = tk.StringVar()
songlabel = tk.Label(root,textvariable=v,width=35)
index=0
frame = tk.Frame(root)
frame.pack()


def calmsong(event):
    directory="mood/calm"
    directorychooser(directory)
def happysong(event):
    directory="mood/happy"
    directorychooser(directory)
def energeticsong(event):
    directory="mood/energetic"
    directorychooser(directory)
def anxsadsong(event):
    directory="mood/anxious_sad"
    directorychooser(directory)
def groovysong(event):
    directory="mood/groovy"
    directorychooser(directory)
def askmood():
    
    text = tk.Text(frame, height=2, width=30)
    text.insert(tk.INSERT, "Choose your mood:")
    text.pack()
    calmbutton = tk.Button(frame,text = 'Calm')
    calmbutton.pack()
    
    happybutton = tk.Button(frame,text = 'Happy')
    happybutton.pack()
    
    energeticbutton = tk.Button(frame,text='Energetic')
    energeticbutton.pack()
    
    anxsadbutton = tk.Button(frame,text='Anxious/sad')
    anxsadbutton.pack()
    
    groovybutton = tk.Button(frame,text='Groovy')
    groovybutton.pack()
    
    calmbutton.bind("<Button-1>",calmsong)
    happybutton.bind("<Button-1>",happysong)
    energeticbutton.bind("<Button-1>",energeticsong)
    anxsadbutton.bind("<Button-1>",anxsadsong)
    groovybutton.bind("<Button-1>",groovysong)
    
askmood()    


def directorychooser(directory):
    
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
            li_dir=directory.split("/")
            realdir = os.path.abspath(files)
            li=realdir.split("\\")
            li.insert(-1,"mood")
            li.insert(-1,li_dir[1])
            s="\\"
            realdir=s.join(li)
        
            audio = ID3(realdir)
            
            realnames.append(audio['TIT2'].text[0])


            listofsongs.append(realdir)


    
    

    try:
        pygame.mixer.music.load(listofsongs[0])
    except:
        print("No songs found")
    #frame.pack_forget()
    #pygame.mixer.music.play()

def updatelabel():
    global index # If you do not use global, new index variable will be defined
    global songname
    v.set(realnames[index]) # set our StringVar to the real name 
    #return songname

def nextsong(event):
    global index
    index += 1
    index=index%len(realnames)
    mp3 = mutagen.mp3.MP3(listofsongs[index])
    pygame.mixer.init(frequency=mp3.info.sample_rate)
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):
    global index
    index -= 1
    index=index%len(realnames)
    mp3 = mutagen.mp3.MP3(listofsongs[index])
    pygame.mixer.init(frequency=512)
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    #return songname


label = tk.Label(root,text='Music Player')
label.pack()

listbox = tk.Listbox(root)
listbox.pack()

#listofsongs.reverse()
realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()
#listofsongs.reverse()


nextbutton = tk.Button(root,text = 'Next Song')
nextbutton.pack()

previousbutton = tk.Button(root,text = 'Previous Song')
previousbutton.pack()

stopbutton = tk.Button(root,text='Stop Music')
stopbutton.pack()

nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop()
