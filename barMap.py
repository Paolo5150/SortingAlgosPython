from typing import List
import matplotlib.patches
import matplotlib.transforms as transforms

# Animation for a bar: defined by the bar to move, and the target X value
class AnimationEvent:
    def __init__(self, barPatch: matplotlib.patches.Rectangle,  targetX: int) -> None:
        self.barPatch = barPatch
        self.targetX = targetX
        self.direction = 1;
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
    
    def update(self):

        if not self.hasReachedTarget():
             #translation = transforms.Affine2D().translate(self.direction * 0.0005, 0)
             #self.barPatch.set_transform(translation + self.barPatch.get_transform())
             self.barPatch.set_x(self.barPatch.get_x() + (self.direction * 0.05))
             self.barPatch.set_color('red')
        else:
             print('reached')
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

    def HasAnimations(self):
         return len(self.allAnimations) > 0
    
    def IsIdle(self):
         return len(self.allAnimations) == 0

    def Update(self):
        for anim in self.allAnimations:
            anim.update()
            if anim.completed:
                 self.allAnimations.remove(anim)






