-- create unique index uq_entry on entry(processName,title)
-- delete from entry
INSERT OR REPLACE INTO entry (processname, title, duration,starttime) 
  VALUES (  'pythonw.exe', 
            'tt13',
            COALESCE((SELECT duration+5 FROM entry WHERE processname='pythonw.exe' and title='tt13'),0)
            ,COALESCE((SELECT starttime FROM entry WHERE processname='pythonw.exe' and title='tt3'), datetime('now'))
          );
          select * from entry
       