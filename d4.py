with open('Advent of Code D4/input.txt', 'r') as file:
    r = file.read()
    r = r.splitlines()

final = 0
for i in r:
    i = i.split(',')
    c = [m.split('-') for m in i]
    r1 = [str(n) for n in range(int(c[0][0]),int(c[0][1])+1)]
    r1 = ''.join(r1)
    r2 = [str(n) for n in range(int(c[1][0]),int(c[1][1])+1)]
    r2 = ''.join(r2)
    if r1 in r2 or r2 in r1:
        final +=1
       


print(final)
