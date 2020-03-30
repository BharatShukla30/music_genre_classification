# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 16:26:41 2020

@author: mouseless
"""
import librosa
import numpy as np

from pydub import AudioSegment

#change dictionary
def cd(di):
    dicti={}
    for i in di:
        dicti[di[i]]=i
    return dicti

# convert wav to mp3
def convert(directory,name):
    src = directory
    dst = "new_music/{0}.wav".format(name) 
    if src[-3:]!="wav":                                                           
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="wav")
        return dst
    else:
        return src

#module for extracting data from the music
def extraction(songname,song):
    y, sr = librosa.load(songname, mono=True, duration=30)
    chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
    spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
    spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
    rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
    zcr = librosa.feature.zero_crossing_rate(y)
    mfcc = librosa.feature.mfcc(y=y, sr=sr)
    to_append = f'{np.mean(chroma_stft)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)} '    
    for e in mfcc:
        to_append += f' {np.mean(e)}'
    return to_append