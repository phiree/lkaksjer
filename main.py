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
import psutil,os,time
from  GetFrontWindow import *
from threading import *
from persistenceFactory import *
entryList=[]
class GetActivityInformation(Thread):
    #repeatedTimes=1
   
    def __init__(self):
        Thread.__init__(self)
        self.stopped=False
        self.frenquency=5
        #save to persistence frenquency
        self.saveAfterFrenqencyTimes=12 #refrenquency = frenquency*12=60 secends
        self.preProcess=''
        self.totalEntry=0
       

    def run(self):
        while not self.stopped:
            frontWindowInfo=wininfoFactory().GetFrontWindowInfo()
            #print(dir (wininfoFactory()))
            pname=frontWindowInfo[0]
            wtext=frontWindowInfo[1]
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
            lock=Lock()
            lock.acquire()
            entryList.append(re)
            lock.release()
            self.totalEntry=self.totalEntry+len(entryList)
            #if repeatedTimes%saveAfterFrenqencyTimes==0:
            #   pass
            # for entry in self.entryList:
            print(entryList[-1])
            time.sleep(self.frenquency)
            #repeatedTimes=repeatedTimes+1
class PersistenceThread(Thread):
    '''save entry to server'''
    
    def __init__(self):
        Thread.__init__(self)

    def SaveToLocal(self,entryList):
        print("-----save start------")
        CreatePersistence("sqlite").SaveToLocal(entryList)
        entryList=[]
        print(len(entryList))

class RecordEntry:
    def __init__(self):
       ''' self.pname=''
        self.wtext=''
        self.lastTime=0'''
       self.time=datetime.datetime.now()
    
    def __str__(self):
        return self.pname+'--'+self.wtext+'--'+str(self.lastTime)+'--'+str(self.time)


if __name__=="__main__":
    t=0
    info= GetActivityInformation()
    info.start()
    info.frenquency=4
    PersistenceThread=PersistenceThread()
    PersistenceThread.start()
    while True:
        lock=Lock()
        lock.acquire()
        t=t+len(entryList)
        PersistenceThread.SaveToLocal(entryList)
        print("totalEntry:"+str(info.totalEntry)+",totalSaved:"+str(t))
        entryList=[]
        lock.release()
       
        time.sleep(5)


    
