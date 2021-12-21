import copy
import random
# Consider using the modules imported above.

class Hat:
    #kwargs will be our dictionary for all the parameters passed in
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)    
        #print(self.contents)

    def draw(self, number):
        
        all_removed = []
        
        #If the number of balls to draw exceeds the avaliable quantitiy, return all the balls.
        if(number > len(self.contents)):
            return self.contents
        #This will loop for the amount specified by number
        for i in range(number):
            # This will remove a ball at random from self.contents list using pop()
            removed = self.contents.pop(int(random.random() * len(self.contents)))
            all_removed.append(removed)
        return all_removed
    
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        #Using the ipmorted copy library for "freezing" the expected_balls dict
        expected_balls_copy = copy.deepcopy(expected_balls)
        
        #Same deep copy here so that hat_copy does not change with hat
        hat_copy = copy.deepcopy(hat)
        colours_gotten = hat_copy.draw(num_balls_drawn)
        
        for colours in colours_gotten:
            if(colour in expected_balls_copy):
                expected_balls_copy[colour]-=1
        
    return None