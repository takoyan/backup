#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pocketsphinx import LiveSpeech, get_model_path
model_path=get_model_path()

speech = LiveSpeech(dic=os.path.join(model_path, 'zisyo.dict'))
for i in speech:
    print(i)
