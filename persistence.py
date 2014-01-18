import sqlite3,os
class ab_persistence:
    def SaveToLocal(self):
        raise NotImplementedError("Must be Implented")
    
class persistenceSqlite(ab_persistence):
    def SaveToLocal(self,entryList):
        dbfile=os.path.dirname( __file__)+"\db.db3"
        conn=sqlite3.connect(dbfile)
        c=conn.cursor()
        c.executemany(''' INSERT OR REPLACE INTO entry (processname, title, duration,starttime) 
                          VALUES(?
                                 ,?
                                 ,COALESCE((SELECT duration+? FROM entry WHERE processname=? and title=?),0)
                                 ,COALESCE((SELECT starttime FROM entry WHERE processname=? and title=?), ?)
                                );'''
                      ,[(item.pname
                         ,item.wtext
                         ,item.lastTime
                         ,item.pname
                         ,item.wtext
                         ,item.pname
                         ,item.wtext
                         ,item.time)
                        for item in entryList])
        conn.commit()
        conn.close()
                        
def CreatePersistence(ptype):
    if ptype=="sqlite":
        return persistenceSqlite()
    else:
         raise NotImplementedError("No support yet")
    
