#!/usr/bin/env python
# -*- coding: utf-8 -*-


import rospy
from std_msgs.msg import String
from pocketsphinx import LiveSpeech, get_model_path
import os


model_path=get_model_path()

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    r = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        speech = LiveSpeech(dic=os.path.join(model_path, 'zisyo.dict'))
        for i in speech:
            rospy.loginfo(i)
            pub.publish(str(i))
            r.sleep()

            
if __name__=='__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

