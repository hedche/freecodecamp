import copy
import random
# Consider using the modules imported above.

class Hat:
    #kwargs will be our disctionary for all the parameters passed in
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)    
        #print(self.contents)

    def draw(self, number):
        all_removed = []
        # If the number of balls to draw exceeds the avaliable quantitiy, return all the balls.
        if(number > len(self.contents)):
            return self.contents
        
        # This will remove a ball at random from self.contents list using pop()
        for i in range(number):
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            all_removed.append(removed)
        return all_removed
    
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    return None