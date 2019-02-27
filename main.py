import time
import win32gui
import win32con
import subprocess
import os

import updatehtml
import getdata

htmlpath = 'webpage/index.html'
bmppath = 'img/wallpaper.bmp'
imgwidth = 3840
imgheight = 2160

def render():
    updatehtml.update()
    cmd = 'wkhtmltoimage'
    cmd += ' --crop-w '+str(imgwidth)
    cmd += ' --crop-h '+str(imgheight)
    cmd += ' --width '+str(imgwidth)
    cmd += ' --height '+str(imgheight)
    cmd += ' --javascript-delay '+str(200)
    cmd += ' '+htmlpath+' '+bmppath
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE, shell = True)
    p.wait()
    t0 = time.clock()
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, os.getcwd()+'/'+bmppath, 1+2)
    print('set wallpaper time used:', time.clock() - t0)

def refreshdata():
    getdata.getdata()
    
b1 = True
b2 = True
refreshdata()
while True:
    time.sleep(0.2)
    localtime = time.localtime(time.time())

    
    if localtime[5]==0 or localtime[5]==30:
        if b1:
            render()
            b1 = False
    else:
        b1 = True
    
    if localtime[4]%2==0 and localtime[5]==0 and b2:
        if b2:
            refreshdata()
            b2 = False
    else:
        b2 = True
