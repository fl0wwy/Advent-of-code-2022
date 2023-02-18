with open('Advent of Code D1/input.txt', 'r') as file:
    r = file.read()
    r = r.splitlines()

nextelf = 0
top = []
for i in r:
    if i == '':
        top.append(nextelf)
        nextelf = 0
        continue
    nextelf += int(i)

l = []
for i in range(3):
    l.append(max(top))
    top.remove(max(top))

print(sum(l))    
    


