import pyautogui                 #pip install pyautogui
from PIL import Image, ImageGrab #pip install pillow
import time

def hit(key):
    pyautogui.press(key)

def isCollide(data):
    for i in range(365,380): #birds
            for j in range(345,360):
                if data[i,j]<100:
                    hit("down")
                    return

    for i in range(325,345): #cactus
            for j in range(410,485):
                if data[i,j]<100:
                    hit("up")
                    return
    return
    

if __name__ == "__main__":
    print("NONSTOP DINO GAME ABOUT TO START IN 3 SECONDS")
    time.sleep(3)
    hit('up')
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)