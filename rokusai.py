#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave
import pyaudio
from scipy import fromstring, int16
import numpy as np
from matplotlib import pyplot

CHUNK=1024
p=pyaudio.PyAudio()

filename = "121_dr_bpm080_4-4_rock.wav"
wf=wave.open(filename, "rb")

stream=p.open(	format = pyaudio.paInt16,
		channels = 1,
		rate = 44100,
		frames_per_buffer = CHUNK,
		input = True,
		output = True)
#リアルタイム録音再生
while stream.is_active():
    try:
        input=stream.read(CHUNK)
        num_data=fromstring(input, dtype=int16)
        print(num_data)
        list=np.array(num_data)
        output=stream.write(list)
        pyplot.plot(list)
        pyplot.draw()
        pyplot.pause(0.05)
        pyplot.cla()
    except KeyboardInterrupt:
        pyplot.close()
        break


if(wf.getnchannels()==2):
    left=num_data[::2]
    right=num_data[1::2]

wf.close()
stream.stop_stream()
stream.close()
p.terminate()
