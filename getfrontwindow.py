from win32gui import *
from win32process import *
from psutil import *
from platform import *
def wininfoFactory():
    if system()=="Windows":
        return windowInfo()
    elif system()=="Linux":
        raise NotImplementedError("not for linux yet")
    else:
         raise NotImplementedError("unkown platform")
class ab_windowInfo:
    def GetFrontWindowInfo():
        pass
class windowInfo(ab_windowInfo):
    def GetFrontWindowInfo(self):
            hwnd=GetForegroundWindow()
            pinfo= GetWindowThreadProcessId(hwnd)
            pname=''
            try:
                pname=Process(pinfo[1]).name
            except:
                pname='errwhengetname'

            wtext=GetWindowText(hwnd)
            return pname,wtext
if __name__=="__main__":
    wi=windowInfo()
    print(wi.GetFrontWindowInfo())
