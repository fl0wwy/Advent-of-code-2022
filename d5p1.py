stacks= ['F,H,M,T,V,L,D','P,N,T,C,J,G,Q,H','H,P,M,D,S,R','F,V,B,L','Q,L,G,H,N','P,M,R,G,D,B,W','Q,L,H,C,R,N,M,G','W,L,C','T,M,Z,J,Q,L,D,R']
for i in stacks:
    ind = stacks.index(i)
    i=i.split(',')
    stacks[ind] = i 
    
with open('D5/input.txt', 'r') as file:
    r = file.read()
    r = r.splitlines()

#part 1
for i in r:
    i = i.split(' ')
    for n in range(int(i[1])):
        stacks[int(i[5])-1].insert(0,stacks[int(i[3])-1][0])
        stacks[int(i[3])-1].pop(0)

st = []
for i in stacks:
    st.append(i[0])
print(''.join(st))






