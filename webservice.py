from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import numpy as np
import base64
import cv2
class WebService:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://suikagame.com/")
        self.canvas = self.driver.find_element(By.XPATH,'//*[@id="canvasDiv"]')
        
    def getScreenshot(self):
        canvas_base64 = self.canvas.screenshot_as_base64
        nparr = np.frombuffer(base64.b64decode(canvas_base64), np.uint8)
        matResult = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return matResult
    
    def dropFruit(self,x): # x is percentage, 0<x<100
        ac = ActionChains(self.driver)
        ac.move_to_element(self.canvas).move_by_offset((x-49)*(self.canvas.size["width"])/101,10).click().perform()