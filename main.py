#!/usr/bin/env python
#-*-coding: utf-8 -*-

import psutil,os,time,datetime
from config import *
from  GetFrontWindow import *
from threading import *
from persistence import *

class GetActivityInformation(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.stopped=False
        self.frenquency=frequency_readprocess
        self.preProcess=''
        self.totalEntry=0
        self.entryList=entryList
        self.myLock=myLock
       
    def run(self):
        while not self.stopped:
            time.sleep(self.frenquency)
            frontWindowInfo=wininfoFactory().GetFrontWindowInfo()
            pname=frontWindowInfo[0]
            wtext=frontWindowInfo[1]
            self.lastTime=self.frenquency
            self.preProcess=pname
            re=RecordEntry()
            re.pname=pname
            re.wtext=wtext
            re.lastTime=self.lastTime
            self.myLock.acquire()
            self.entryList.append(re)
            self.totalEntry+=1
            self.myLock.release()

class PersistenceThread(Thread):
    '''save entry to server'''
    def __init__(self):
        Thread.__init__(self)
        self.t=0
        self.entryList=entryList
        self.repeatFrenquency=frequency_savetolocal
    def run(self):
        while True:
            myLock.acquire()
            self.t=self.t+len(self.entryList)
            PersistenceThread.SaveToLocal(self.entryList)
            del self.entryList[:]
            myLock.release()
            time.sleep(self.repeatFrenquency)
    def SaveToLocal(self,entryList):
        CreatePersistence("sqlite").SaveToLocal(entryList)

class RecordEntry:
    def __init__(self):
       
       self.time=datetime.datetime.now()
       pass
       self.pname=''
       self.wtext=''
       self.lastTime=0
    
    def __str__(self):
        return self.pname+'--'+self.wtext+'--'+str(self.lastTime)+'--'+str(self.time)

if __name__=="__main__":
    myLock=Lock()
    entryList=[]
    info= GetActivityInformation()
    info.start()
    PersistenceThread=PersistenceThread()
    PersistenceThread.start()

    
    


    
