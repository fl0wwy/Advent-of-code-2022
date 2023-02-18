class RPS:
    throws = {'A':1,'B':2,'C':3}
    def __init__(self) -> None:
        self.score = 0
    def play(self,throw,cheat):
        adv = cheat
        if throw == 'Y':
            throw = 'B'
        elif throw == 'X':
            throw = 'A'
        elif throw == 'Z':
            throw = 'C'        
        
        if adv == 'A':
            if throw == 'B':
                self.score += self.throws['B'] + 6
            elif throw == 'A':
                self.score += self.throws['A'] + 3
            elif throw == 'C':
                self.score += self.throws['C'] + 0
        elif adv == 'B':
            if throw == 'B':
                self.score += self.throws['B'] + 3
            elif throw == 'A':
                self.score += self.throws['A'] + 0
            elif throw == 'C':
                self.score += self.throws['C'] + 6
        elif adv == 'C':
            if throw == 'B':
                self.score += self.throws['B'] + 0
            elif throw == 'A':
                self.score += self.throws['A'] + 6
            elif throw == 'C':
                self.score += self.throws['C'] + 3        
    
    def __str__(self) -> str:
        return str(self.score)          

test = RPS()

with open('Advent of code D2/input.txt', 'r') as file:
    inp = file.read()
    inp = inp.splitlines()

for i in inp:
    test.play(i[2],i[0])

print(test)




        


