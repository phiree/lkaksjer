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
        for entry in entryList:
            entryListTuple.append((entry.pname,entry.wtext,entry.lastTime,entry.time))
        c.executemany('insert into Entry values(?,?,?,?)',entryListTuple)
        conn.commit()
        conn.close()
                        
def CreatePersistence(ptype):
    if ptype=="sqlite":
        return persistenceSqlite()
    else:
         raise NotImplementedError("No support yet")
    
