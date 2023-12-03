import cv2
import numpy as np
import fruit
import globalvariables as gv
import buffer
class Vision:
    def __init__(self):
        self.screenshot = None
        self.buffer = buffer.Buffer(5,[[],[]])
        
    def setScreenshot(self,screenshot):
        self.screenshot = screenshot
        
    def getScreenshot(self):
        return self.screenshot
    def getColorSum(self,src,x,y,rad):
        height, width = src.shape
        all = 0.0
        sum = 0.0
        for ix in range(max(x-rad,0),min(x+rad+1,width)):
            for iy in range(max(y-rad,0),min(y+rad+1,height)):
                if (ix-x)**2 + (iy-y)**2 <= rad**2:
                    sum += src[iy,ix]/255.0
                    all += 1.0
        return sum/all

    def getCircles(self,src,color):
        def getCircleTemp(src,color):
            circles = cv2.HoughCircles(src,cv2.HOUGH_GRADIENT,1,17,param1=10,param2=7,minRadius=5,maxRadius=0)
            src = cv2.bitwise_not(src)
            result = []
            if circles is not None:
                circles = np.uint16(np.around(circles))
                for i in circles[0,:]:
                    i[0] = int(i[0])
                    i[1] = int(i[1])
                    try:
                        if src[i[1],i[0]] == 255:
                            continue
                    except:
                        continue
                    for thrad in range(len(gv.fruitRadius)-1):
                            if i[2] < (gv.fruitRadius[thrad] + gv.fruitRadius[thrad+1])/2:
                                try:
                                    col = color[i[1],i[0]]
                                except:
                                    continue
                                
                                min_color_error = np.sum([abs(t) for t in (gv.fruitcolor[thrad] - col)])
                                min_thrad = thrad
                                if thrad+1!=len(gv.fruitcolor):    
                                    t2 = np.sum([abs(t) for t in (gv.fruitcolor[thrad+1] - col)])
                                    if(min_color_error > t2):
                                        min_color_error = t2
                                        min_thrad = thrad + 1
                                if thrad!=0:    
                                    t2 = np.sum([abs(t) for t in (gv.fruitcolor[thrad-1] - col)])
                                    if(min_color_error > t2):
                                        min_color_error = t2
                                        min_thrad = thrad - 1
                                
                                
                                if min_color_error > 80:
                                    break
                                if min_thrad == 0 or self.getColorSum(src,i[0],i[1],gv.fruitRadius[min_thrad]-2) <= 0.03 - 0.02*gv.fruitRadius[min_thrad]/108:
                                    result.append( fruit.Fruit(len(result),min_thrad,i[0],i[1]) )
                                break
            return result
        arrcircles = getCircleTemp(src,color)
        filteredresult = []
        for i in range(len(arrcircles)):
            error = False
            fruitA = arrcircles[i]
            for j in range(len(arrcircles)): 
                fruitB = arrcircles[j]
                if i!=j and fruitB.radius > fruitA.radius and fruitB.include(fruitA):
                    error = True
                    break
            if error:
                continue
            filteredresult.append(fruit.Fruit(len(filteredresult),fruitA.radindex,fruitA.x,fruitA.y))
        return filteredresult
        
        
    def isStable(self):
        firstitem = self.buffer.top()
        firstarrCircles = firstitem[0]
        firstmatBinary = firstitem[1]
        for item in self.buffer.list():
            arrCircles = item[0]
            matBinary = item[1]
            if(len(firstarrCircles) != len(arrCircles)):
                return False
            try:
                matDiff = cv2.absdiff(matBinary,firstmatBinary)
                if np.average(matDiff) > 90:
                    return False
            except:
                return False
        return True
    def drawCircles(self,src,circles):
        for circle in circles:
            _x = circle.x
            _y = circle.y
            _r = circle.radius
            src = cv2.circle(src,(_x,_y),_r,(0,255,0),2)
            src = cv2.circle(src,(_x,_y),2,(0,255,255),3)
        return src
    def calculateMap(self):
        matSrc = self.screenshot
        matSrc = cv2.resize(matSrc,dsize=(301,528))
        matMask = cv2.bitwise_not(cv2.inRange(matSrc,(155,220,220), (176,253,255)))
        matBinary = cv2.bitwise_and(matMask, matMask, mask=matMask)
        matBinaryNextFruit = matBinary[5:75,115:186]
        matBinaryContainer = matBinary[76:486,:]
        matContainer = matSrc[76:486,:]
        matNextFruit = matSrc[5:75,115:186]

        arrCircles = self.getCircles(matBinaryContainer,matContainer)
        arrNextFruits = self.getCircles(matBinaryNextFruit,matNextFruit)
        
        nextFruit = None
        if (len(arrNextFruits) != 0):
            nextFruit = arrNextFruits[0].radindex
        if gv.DEBUG:
            if(nextFruit != None):
                cv2.putText(matContainer,"nextFruit="+gv.fruitlabels[int(nextFruit)],(0,20),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,0,0),1)
            dy = 0
            for circle in arrCircles:
                cv2.putText(matContainer,gv.fruitlabels[circle.radindex]+":"+str(circle.x) + "," + str(circle.y),(0,50 + dy),cv2.FONT_HERSHEY_SIMPLEX,0.3,(255,0,0),1)
                dy += 20
            matContainer = self.drawCircles(matContainer,arrCircles)
            matNextFruit = self.drawCircles(matNextFruit,arrNextFruits)
            cv2.imshow("NextFruit",matNextFruit)
            cv2.imshow("Container",matContainer)
            cv2.imshow("Binary",matBinaryContainer)
        self.buffer.push([arrCircles,matBinaryContainer])
        return arrCircles, nextFruit
    def printImage(self,src):
        cv2.imshow("Game AI template by hjabo",src)
    
    def waitKey(self,mill):
        cv2.waitKey(mill)