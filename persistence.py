import sqlite3,os
class ab_persistence:
    def SaveToLocal(self):
        raise NotImplementedError("Must be Implented")
class persistenceSqlite(ab_persistence):
    #summary every hours
    def SaveToLocal(self,entryList):
        dbfile=os.path.dirname( __file__)+"\db.db3"
        print(dbfile)
        conn=sqlite3.connect(dbfile)
        c=conn.cursor()
        entryListTuple=[]
        '''for entry in entryList:
            currentItem=(entry.pname,entry.wtext)
            c.execute('select * from Entry where processName=? and title=?',currentItem)
            existedItem=c.fetchone()
            print(existedItem)
            if   existedItem is not None:
                entry.lastTime+=existedItem.lastTime
                
                print(c.fetchone())
            else:
                entryListTuple.append((entry.pname,entry.wtext,entry.lastTime,entry.time))
           
INSERT OR REPLACE INTO entry (processname, title, duration,starttime) 
  VALUES (  'pythonw.exe', 
            'tt13',
            COALESCE((SELECT duration+5 FROM entry WHERE processname='pythonw.exe' and title='tt13'),0)
            ,COALESCE((SELECT starttime FROM entry WHERE processname='pythonw.exe' and title='tt13'), datetime('now'))
          );
'''
            #print (entryListTuple)
        #if pname and wtitle are same, then update duration
        c.executemany(  '''
                          INSERT OR REPLACE INTO entry (processname, title, duration,starttime) 
                           VALUES (?,?,COALESCE((SELECT duration+? FROM entry WHERE processname=? and title=?),0)
                         ,COALESCE((SELECT starttime FROM entry WHERE processname=? and title=?), ?)
                  );
''',[(item.pname,item.wtext,item.lastTime,item.pname,item.wtext,item.pname,item.wtext,item.time) for item in entryList])
        #c.executemany('insert into Entry values(?,?,?,?)',entryListTuple)
        conn.commit()
        conn.close()
    # [(str(keywords[i]), date, time, position[i]) for i in range(20)]
                        
def CreatePersistence(ptype):
    if ptype=="sqlite":
        return persistenceSqlite()
    else:
         raise NotImplementedError("No support yet")
    
