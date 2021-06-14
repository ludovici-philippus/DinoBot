import pyautogui
from time import sleep
from PIL import ImageGrab
from PIL import ImageOps
from numpy import *
#83, 83, 83
#pyautogui.mouseInfo()
class DinoBot:
    def __init__(self):
        self.dino = (725, 455)
        self.restart_buttom = (963, 434)
        self.main()
    
    def start_game(self):
        pyautogui.moveTo(self.restart_buttom)
        pyautogui.click()

    def image_grab(self):
        box = (self.dino[0]+55, self.dino[1], self.dino[0] + 145, self.dino[1] + 5)
        image = ImageGrab.grab(box)
        grayImage = ImageOps.grayscale(image)
        a = array(grayImage.getcolors())
        return a.sum()
    
    def jump(self, color):
        if color != 697: 
            sleep(.0175) 
            pyautogui.press("space")
           
     
    def main(self):
        sleep(3)
        self.start_game()
        sleep(.2)
        while True:
            self.image_grab()
            self.jump(self.image_grab())
    
bot = DinoBot()
