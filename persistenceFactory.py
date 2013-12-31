import sqlite3
class ab_persistence:
    def SaveToLocal(self):
        raise NotImplementedError("Must be Implented")
class persistenceSqlite(ab_persistence):
    #summary every hours
    def SaveToLocal(self,entryList):
        conn=sqlite3.connect("db.db3")
        c=conn.cursor()
        entryListTuple=[]
        for entry in entryList:
            entryListTuple.append((entry.pname,entry.wtext,entry.lastTime,entry.time))
        c.executemany('insert into Entry values(?,?,?,?)',entryListTuple)
        entryList=[]
        conn.commit()
        conn.close()
                        
def CreatePersistence(ptype):
    if ptype=="sqlite":
        return persistenceSqlite()
    else:
         raise NotImplementedError("No support yet")
    
