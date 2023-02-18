with open('D6/input.txt', 'r') as file:
    r = file.read()

def char(r,count):
    i = 0
    while i != len(r):
        calc = r[i:i+count:]
        for w in calc:
            if calc.count(w) > 1:
                i+=1
                break
            else:
                if calc.index(w) == count-1:
                    return i + count
                else:
                    continue    
#part 1
print(char(r,4))
#part 2
print(char(r,14))


            
