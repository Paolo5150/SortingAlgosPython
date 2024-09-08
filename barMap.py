import time
from typing import List
import matplotlib.patches
import matplotlib.transforms as transforms

# Animation for a bar: defined by the bar to move, and the target X value
class AnimationEvent:
    def __init__(self, barPatch: matplotlib.patches.Rectangle,  targetX: int) -> None:
        self.barPatch = barPatch
        self.targetX = targetX
        self.direction = 1;
        self.lastTime = time.time()
        self.completed = False
        if targetX < self.barPatch.get_x():
            self.direction = -1


    def hasReachedTarget(self):
        if self.direction == 1:
                if self.barPatch.get_center()[0] >= self.targetX:
                    return True
    
        if self.direction == -1:
                if self.barPatch.get_center()[0] <= self.targetX:
                    return True
        return False
    
    def update(self, speed = 1):
        nowTime = time.time()
        delta = nowTime - self.lastTime
        self.lastTime = nowTime

        if not self.hasReachedTarget():
             self.barPatch.set_x(self.barPatch.get_x() + (self.direction * delta * speed)) #set speed here
             self.barPatch.set_color('red')
        else:

             self.barPatch.set_color('blue')

             self.barPatch.set_x(self.targetX -  self.barPatch.get_width() * 0.5)
             self.completed = True        

# Manages graph bar animations
class BarMap:
    def __init__(self, barDictionary) -> None:
        self.barDictionary = barDictionary
        self.allAnimations : List[AnimationEvent] = []

    def MoveBarByYValue(self, barValue: int, targetXValue):
        self.allAnimations.append(AnimationEvent(self.barDictionary[barValue], targetX= targetXValue))

    def GetBarCenterXForValue(self, value):
         return self.barDictionary[value].get_center()[0]

    def HasAnimations(self):
         return len(self.allAnimations) > 0
    
    def SetColorForValue(self, value, color):
         self.barDictionary[value].set_color(color)
    
    def IsIdle(self):
         return len(self.allAnimations) == 0
    
    #Automaticall adds 2 animation that swap the bars of 2 given values
    #The two values are the Ys of the bars
    def AnimateSwap(self, first, second):
        self.MoveBarByYValue(first, self.GetBarCenterXForValue(second))
        self.MoveBarByYValue(second, self.GetBarCenterXForValue(first))
         

    def Update(self, barSpeed = 1):
        #print(f"Animations {len(self.allAnimations)}")
        for anim in self.allAnimations:
            anim.update(barSpeed)
            if anim.completed:
                 self.allAnimations.remove(anim)






