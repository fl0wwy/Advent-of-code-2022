with open('Advent of Code D1/input.txt', 'r') as file:
    r = file.read()
    r = r.splitlines()

currentelf = 0
nextelf = 0

for i in r:
    if i == '':
        if currentelf < nextelf:
            currentelf = nextelf
        nextelf = 0
        continue
    nextelf += int(i)    
            
print(currentelf)
            
