import time
import datetime
import numpy as np
import cv2
import mss
import mss.tools
import threading

startScreen = None
stgScreen = 340
stgWrong = 670

def listenAwaking():
    curtime = datetime.datetime.now()
    while True:
        time.sleep(1)
        diff = (datetime.datetime.now()- curtime).total_seconds()
        #print("clock : "+str(diff))
        if diff < 1:
            while True:
                try:
                    global startScreen
                    time.sleep(0.1)
                    startScreen = getCurrentScreen()
                    handleScreen()
                    break
                except:
                    pass
        curtime = datetime.datetime.now()

def getCurrentScreen():
    try:
        with mss.mss() as sct:
            region = {"top":495,"left":615,"width":210,"height":70}
            img = sct.grab(region)
            mss.tools.to_png(img.rgb,img.size,output="current.png")
        image = cv2.imread("current.png")
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)
        return image
    except Exception as e:
        pass

def capture():
    cam = cv2.VideoCapture(0)
    s, img = cam.read()
    if s:
        cv2.namedWindow("cam-test",cv2.WINDOW_AUTOSIZE)
        now = datetime.datetime.now()
        cv2.imwrite("captures/"+str(now)+".jpg",img)


def handleScreen():
    while True:
        try:
            cur = getCurrentScreen()
            diff = cv2.absdiff(startScreen,cur)
            
            histg = cv2.calcHist([diff],[0],None,[256],[0,256])
            std = np.std(histg).item()
            #print(std)
            if std < stgWrong and std > stgScreen:
                print("Password Is Wrong! Taked Photo From Webcam...")
                capture()
                time.sleep(0.6)
            elif std < stgScreen:
                print("Password True...")
                break
        except Exception as e:
            pass

thr = threading.Thread(target=listenAwaking)
thr.start()
