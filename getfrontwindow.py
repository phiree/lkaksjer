#!/usr/bin/env python
#-*-coding: utf-8 -*-
# 得到窗口标题
'''from win32gui import *
import timeit
import win32process
import time
from threading import *
'''
import datetime
import psutil,os,time,win32process
from win32gui import *
from win32api import *
from win32process import *
from psutil import *
from threading import Thread
class GetActivityInformation(Thread):
    #repeatedTimes=1
    def __init__(self):
        self.stopped=False
        self.frenquency=5
        #save to persistence frenquency
        self.saveAfterFrenqencyTimes=12 #refrenquency = frenquency*12=60 secends
        self.preProcess=''
        self.entryList=[]
        Thread.__init__(self)
    def run(self):
        while not self.stopped:
            self.GetFrontWindowInfo()
            #if repeatedTimes%saveAfterFrenqencyTimes==0:
            #   pass
            # for entry in self.entryList:
            print(self.entryList[-1])
            time.sleep(self.frenquency)
            #repeatedTimes=repeatedTimes+1
    def GetFrontWindowInfo(self):
            hwnd=GetForegroundWindow()
            pinfo= GetWindowThreadProcessId(hwnd)
            pname=''
            try:
                pname=psutil.Process(pinfo[1]).name
            except:
                pname='errwhengetname'

            wtext=GetWindowText(hwnd)
            if pname==self.preProcess:
                self.lastTime+=self.frenquency
            else:
                self.lastTime=0
            self.preProcess=pname
           # foreWindowText=GetClassName(hwnd)
            re=RecordEntry()
            re.pname=pname
            re.wtext=wtext
            re.lastTime=self.lastTime
            self.entryList.append(re)
if __name__=="__main__":
   info= GetActivityInformation()
   info.start()
   info.frenquency=4
class Persistence(Thread):
    '''save entry to server'''
    def __init__(self):
        pass
    def SaveToLocal(self):
        pass

class RecordEntry:
    def __init__(self):
       ''' self.pname=''
        self.wtext=''
        self.lastTime=0'''
       self.time=datetime.datetime.now()
    def __str__(self):
        return self.pname+'--'+self.wtext+'--'+str(self.lastTime)+'--'+str(self.time)
