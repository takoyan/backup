#!/usr/bin/env python
# -*- coding: utf-8 -*-

def left(list):
    for i in range(len(list)):
        if(i==len(list)-1):
            return list
        if(list[i]==0):
            list[i], list[i+1]=list[i+1], list[i]
            print(list)
    return list
if(__name__=='__main__'):
    list=[1,0,2,3,0,0,5]
    list=left(list)
    print(list)
