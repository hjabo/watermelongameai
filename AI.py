import vision
import webservice
import fruit
import time
import random

class Agent:
    def __init__(self, web):
        self.web = web

    
    def algo1(self, fruits, next):
        fruits.sort()

        if 9 in fruits:
            for i in fruits:
                if i.radindex == 9:
                    big = i
            if big.x >= 0 and big.x <= 125:
                print("test1")
                if next == 4:
                    self.web.dropFruit(90)
                    return
               
                same_fruits = [x for x in fruits if x.radindex == next]
                for f in same_fruits:
                    print("t1")
                    upper_fruits = [i for i in fruits 
                                    if i.radius != f.radius
                                    if i.y < f.y
                                    if (i.x + i.radius >= f.x and i.x - i.radius < f.x - f.radius)
                                    or (i.x - i.radius <= f.x and i.x + i.radius > f.x + f.radius)]
                    if upper_fruits:
                        print(upper_fruits[0].radius, upper_fruits[0].x, upper_fruits[0].y, f.radius, f.x, f.y)
                    if not upper_fruits:
                        print("t2", upper_fruits)
                        self.web.dropFruit(f.x / 3)
                        return  
            
                self.web.dropFruit(40)
                return
                            
            if big.x >= 126 and big.x <= 175:
                print("test2")
                if next == 4:
                    self.web.dropFruit(90)
                    return
               
                same_fruits = [x for x in fruits if x.radindex == next]
                for f in same_fruits:
                    print("t1")
                    upper_fruits = [i for i in fruits 
                                    if i.radius != f.radius
                                    if i.y < f.y
                                    if (i.x + i.radius >= f.x and i.x - i.radius < f.x - f.radius)
                                    or (i.x - i.radius <= f.x and i.x + i.radius > f.x + f.radius)]
                    if upper_fruits:
                        print(upper_fruits[0].radius, upper_fruits[0].x, upper_fruits[0].y, f.radius, f.x, f.y)
                    if not upper_fruits:
                        print("t2", upper_fruits)
                        self.web.dropFruit(f.x / 3)
                        return  
            
                self.web.dropFruit(40)
                return
              
            if big.x >= 176 and big.x <= 301:
                print("test3")
                if next == 4:
                    self.web.dropFruit(1)
                    return
               
                same_fruits = [x for x in fruits if x.radindex == next]
                same_fruits.reverse()
                for f in same_fruits:
                    print("t1")
                    upper_fruits = [i for i in fruits 
                                    if i.radius != f.radius
                                    if i.y < f.y
                                    if (i.x + i.radius >= f.x and i.x - i.radius < f.x - f.radius)
                                    or (i.x - i.radius <= f.x and i.x + i.radius > f.x + f.radius)]
                    if upper_fruits:
                        print(upper_fruits[0].radius, upper_fruits[0].x, upper_fruits[0].y, f.radius, f.x, f.y)
                    if not upper_fruits:
                        print("t2", upper_fruits)
                        self.web.dropFruit(f.x / 3)
                        return  
            
                self.web.dropFruit(60)
                return
        



        elif 8 in fruits:
            for i in fruits:
                if i.radindex == 8:
                    big = i
            if big.x >= 0 and big.x <= 100:
                if next == 4:
                    self.web.dropFruit(90)
                    return
               
                same_fruits = [x for x in fruits if x.radindex == next]
                for f in same_fruits:
                    print("t1")
                    upper_fruits = [i for i in fruits 
                                    if i.radius != f.radius
                                    if i.y < f.y
                                    if (i.x + i.radius >= f.x and i.x - i.radius < f.x - f.radius)
                                    or (i.x - i.radius <= f.x and i.x + i.radius > f.x + f.radius)]
                    if upper_fruits:
                        print(upper_fruits[0].radius, upper_fruits[0].x, upper_fruits[0].y, f.radius, f.x, f.y)
                    if not upper_fruits:
                        print("t2", upper_fruits)
                        self.web.dropFruit(f.x / 3)
                        return  
            
                self.web.dropFruit(1)
                return
                            
            if big.x >= 101 and big.x <= 200:
                if next == 4:
                    self.web.dropFruit(90)
                    return
               
                same_fruits = [x for x in fruits if x.radindex == next]
                for f in same_fruits:
                    print("t1")
                    upper_fruits = [i for i in fruits 
                                    if i.radius != f.radius
                                    if i.y < f.y
                                    if (i.x + i.radius >= f.x and i.x - i.radius < f.x - f.radius)
                                    or (i.x - i.radius <= f.x and i.x + i.radius > f.x + f.radius)]
                    if upper_fruits:
                        print(upper_fruits[0].radius, upper_fruits[0].x, upper_fruits[0].y, f.radius, f.x, f.y)
                    if not upper_fruits:
                        print("t2", upper_fruits)
                        self.web.dropFruit(f.x / 3)
                        return  
            
                self.web.dropFruit(1)
                return  
            if big.x >= 201 and big.x <= 301:
                if next == 4:
                    self.web.dropFruit(1)
                    return
               
                same_fruits = [x for x in fruits if x.radindex == next]
                same_fruits.reverse()
                for f in same_fruits:
                    print("t1")
                    upper_fruits = [i for i in fruits 
                                    if i.radius != f.radius
                                    if i.y < f.y
                                    if (i.x + i.radius >= f.x and i.x - i.radius < f.x - f.radius)
                                    or (i.x - i.radius <= f.x and i.x + i.radius > f.x + f.radius)]
                    if upper_fruits:
                        print(upper_fruits[0].radius, upper_fruits[0].x, upper_fruits[0].y, f.radius, f.x, f.y)
                    if not upper_fruits:
                        print("t2", upper_fruits)
                        self.web.dropFruit(f.x / 3)
                        return  
            
                self.web.dropFruit(95)
                return
        


        else:
            if next == 4:
                self.web.dropFruit(90)
                return
               
            same_fruits = [x for x in fruits if x.radindex == next]
            for f in same_fruits:
                print("t1")
                upper_fruits = [i for i in fruits 
                                if i.radius != f.radius
                                if i.y < f.y
                                if (i.x + i.radius >= f.x and i.x - i.radius < f.x - f.radius)
                                or (i.x - i.radius <= f.x and i.x + i.radius > f.x + f.radius)]
                if upper_fruits:
                    print(upper_fruits[0].radius, upper_fruits[0].x, upper_fruits[0].y, f.radius, f.x, f.y)
                if not upper_fruits:
                    print("t2", upper_fruits)
                    self.web.dropFruit(f.x / 3)
                    return  
            
            self.web.dropFruit(1)
            return              
    
    