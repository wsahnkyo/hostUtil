import os
import shutil
import sys
def createHost():
    pass

def moveHost(filapath):
    if filapath:
        # hostName = str(ip) + "-" + "hosts"
        shutil.copyfile(filapath,"C:\Windows\System32\drivers\etc\hosts")
def readHost():
    file = open("C:\Windows\System32\drivers\etc\hosts","r",encoding="utf-8")
    content = file.read()
    print(content)
    file.close()

if __name__ == "__main__":
    ip = sys.argv[1]
    moveHost(ip)