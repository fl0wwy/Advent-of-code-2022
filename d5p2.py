#part 2
stacks= ['F,H,M,T,V,L,D','P,N,T,C,J,G,Q,H','H,P,M,D,S,R','F,V,B,L','Q,L,G,H,N','P,M,R,G,D,B,W','Q,L,H,C,R,N,M,G','W,L,C','T,M,Z,J,Q,L,D,R']
for i in stacks:
    ind = stacks.index(i)
    i=i.split(',')
    stacks[ind] = i 
    
with open('D5/input.txt', 'r') as file:
    r = file.read()
    r = r.splitlines()

for i in r:
    i = i.split(' ')
    for n in reversed(range(int(i[1]))):
        if int(i[1]) == 1:
            stacks[int(i[5])-1].insert(0,stacks[int(i[3])-1][0])
            stacks[int(i[3])-1].pop(0)
        else:
            stacks[int(i[5])-1].insert(0,stacks[int(i[3])-1][n])
            stacks[int(i[3])-1].pop(n)


it = []
for i in stacks:
    it.append(i[0])
print(''.join(it))