# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 01:04:24 2020

@author: mouseless
"""

import numpy as np
import pickle
import os 
import functionality as fu



#artist music add module
def artist(art_name,model,scaler,di):
    song_name=input("Song name: ")
    song_dir=input("Enter song's directory: ")
    
    #convert song into .wav
    song_dir_wav=fu.convert(song_dir,song_name)
    song_dir_li=song_dir.split("/")
    
    #feature extraction
    feat=fu.extraction(song_dir_wav,song_name)
    li=feat.split()                      #this is a list
    to_append=li
    to_append=np.array(to_append)      #to_append is an array
    to_append=scaler.transform(np.array(to_append.reshape(1,-1)))
   
    #to_append=to_append.reshape(1,-1)
    labeled=model.predict(to_append)
    labeled=labeled.tolist()
    
    #adding files into folders based on mood
    if di[labeled[0]]!="anxious/sad":
        os.replace(song_dir,"mood/{0}/{1}".format(di[labeled[0]],song_dir_li[-1]))
    else:
        os.replace(song_dir,"mood/anxious_sad/{0}".format(song_dir_li[-1]))
    return 0




#main    
model,scaler,di=pickle.load(open('models/random_forest.pkl','rb'))
di=fu.cd(di)
choice=0
while choice!=3:
    print("Enter choice:",end="\n")
    print("1. Artist",end="\n")
    print("2. Listener",end="\n")
    print("3. Exit",end="\n")
    choice=int(input())
    if choice==1:
        stri=input("Enter artist name: ")
        artist(stri,model,scaler,di)
    elif choice==2:
       exec(open('media_player.py').read())
    else:
        exit
