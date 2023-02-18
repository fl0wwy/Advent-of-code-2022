with open('D9/input.txt', 'r') as file:
    commands = file.read().splitlines()


class RopeEdge():
    def __init__(self,name,head) -> None:
        self.name = name
        self.head = head
        self.position = [0,0]
    def move(self,steps,direction):
        if direction == 'U':
            self.position[1] += steps
        elif direction == 'D':
            self.position[1] -= steps
        elif direction == 'L':
            self.position[0] -= steps
        else:
            self.position[0] += steps
    def follower(self):
        if self.head.position[1] > self.position[1]:       
            while abs(self.head.position[1] - self.position[1]) >= 2:
                if self.head.position[0] > self.position[0]:        
                    while abs(self.head.position[0] - self.position[0]) >= 1:
                        self.move(1,'R')
                elif self.head.position[0] < self.position[0]:  
                    while abs(self.head.position[0] - self.position[0]) >= 1:
                        self.move(1,'L')       
                self.move(1,'U')
        
        elif self.head.position[1] < self.position[1]:
            while abs(self.head.position[1] - self.position[1]) >= 2:
                if self.head.position[0] > self.position[0]:        
                    while abs(self.head.position[0] - self.position[0]) >= 1:
                        self.move(1,'R')
                elif self.head.position[0] < self.position[0]:  
                    while abs(self.head.position[0] - self.position[0]) >= 1: 
                        self.move(1,'L')
                self.move(1,'D')                         
        
        if self.head.position[0] > self.position[0]:        
            while abs(self.head.position[0] - self.position[0]) >= 2:
                if self.head.position[1] > self.position[1]:        
                    while abs(self.head.position[1] - self.position[1]) >= 1:
                        self.move(1,'U')
                elif self.head.position[1] < self.position[1]:  
                    while abs(self.head.position[1] - self.position[1]) >= 1: 
                        self.move(1,'D')
                self.move(1,'R')
        
        elif self.head.position[0] < self.position[0]:
            while abs(self.head.position[0] - self.position[0]) >= 2:
                if self.head.position[1] > self.position[1]:        
                    while abs(self.head.position[1] - self.position[1]) >= 1:
                        self.move(1,'U')
                elif self.head.position[1] < self.position[1]:  
                    while abs(self.head.position[1] - self.position[1]) >= 1: 
                        self.move(1,'D')
                self.move(1,'L')                  

def part_1():
    head = RopeEdge('Head',None)
    tail = RopeEdge('Tail',head)
    tail_positions = set()
    
    for command in commands:
        direction, steps = command.split()
        for i in range(int(steps)):
            head.move(1,direction)
            tail.follower()
            tail_positions.add(tuple(tail.position)) 
    return len(tail_positions)    

def part_2():
    tail_positions = set()
    head = RopeEdge('Head',None)
    knots = [RopeEdge(str(n),None) for n in reversed(range(1,10))]
    for x in knots:
        ind = knots.index(x)
        try:
            x.head = knots[ind+1]
        except IndexError:
            x.head = head   
    for command in commands:
        direction, steps = command.split()
        for i in range(int(steps)):
            head.move(1,direction)
            for l in reversed(knots):
                l.follower()
            tail_positions.add(tuple(knots[0].position))
    return len(tail_positions)

print(part_1())
print(part_2()) 
      

            



                  

           
    