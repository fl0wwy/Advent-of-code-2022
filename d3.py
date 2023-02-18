#Part 1
with open('Advent of code D3/input.txt', 'r') as file:
    r = file.read()
    r = r.splitlines()

lowercase = [chr(i) for i in range(97,123)]
uppercase = [chr(i) for i in range(65,91)]

lower_val = list(enumerate(lowercase, start=1))
upper_val = list(enumerate(uppercase, start=27))

lower_val.extend(upper_val)
vals = {m[1]:m[0] for m in lower_val}

prio = 0
for i in r:
    half = len(i) // 2
    for l in i[:half:]:
        if l in i[half::]:
            prio += vals[l]
            i = i.replace(l,'')

# print(prio)

#Part 2
groups = []

while True:
    if len(r) == 0:
        break
    for i in r[0]:
        if i in r[1] and i in r[2]:
            groups.append(i)
            for c in range(3):
                r.pop(0)
            break    

prio2 = 0
for i in groups:
    prio2 += vals[i]

print(prio2)

           

    

    






