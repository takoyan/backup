#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave
import pyaudio
from scipy import fromstring, int16
import numpy as np
from matplotlib import pyplot

def left(list):
    for i in range(len(list)):
        if(i==len(list)-1):
            return list
        if(list[i]==0):
            list[i], list[i+1]=list[i+1], list[i]
            print(list)
    return list

CHUNK =1024
filename = "121_dr_bpm080_4-4_rock.wav"
filename2 = "025_dr_bpm160_4-4_rock.wav"

p =pyaudio.PyAudio()
wf=wave.open(filename, "rb")
wf2=wave.open(filename2, "rb")

stream=p.open(format=p.get_format_from_width(wf.getsampwidth()),
              channels=wf.getnchannels(),
              rate=wf.getframerate(),
              output=True)


stream2=p.open(format=p.get_format_from_width(wf2.getsampwidth()),
              channels=wf2.getnchannels(),
              rate=wf2.getframerate(),
              output=True)
data2=wf2.readframes(CHUNK)


data=wf.readframes(CHUNK)

num_data=fromstring(data, dtype=int16)
num_data2=fromstring(data, dtype=int16)
#num_data=left(num_data)

#ただのwav再生
while data !='':
    list=np.array(num_data)
    list2=np.array(num_data2)
    stream.write(list2)
    data=wf.readframes(CHUNK)
    data2=wf.readframes(CHUNK)
    num_data=fromstring(data, dtype=int16)
    num_data2=fromstring(data2, dtype=int16)


"""リアルタイム録音再生
while stream.is_active():
    try:
        input=stream.read(CHUNK)
        num_data=fromstring(input, dtype=int16)
        print(num_data)
        list=np.array(num_data)
        #input =input*100
        #list=np.array(input)
        #output=stream.write(list)
        pyplot.plot(list)
        pyplot.draw()
        pyplot.pause(0.05)
        pyplot.cla()
    except KeyboardInterrupt:
        pyplot.close()
        break


list=np.array(num_data)
print(list)
pyplot.plot(data)
pyplot.show()

if(wf.getnchannels()==2):
    left=num_data[::2]
    right=num_data[1::2]
#stream.write(list)
"""
wf.close()
stream.stop_stream()
stream.close()
p.terminate()



