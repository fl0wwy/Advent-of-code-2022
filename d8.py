with open('D8/INPUT.txt', 'r') as file:
    r = file.read()
    r = r.splitlines()

# Adding all trees that are on the edge of the grid to the visible trees variable
trees = (len(r[0]) -2) * 2
for i in range(len(r)):
    trees += 2

def row(n,iteration):
    """A function that takes a number(n) and a string(iteration) and iteraters over the string characters.
    if it finds a tree value that is larger or equal to that of the number(n), 
    returns a tuple with False and the number of iterations,
    else return a tuple with True and the number of iterations"""
    n = int(n)
    l = 0
    for i in iteration:
        l += 1
        if int(i) >= n:
            return (False,l)
    return (True,l)    
def column(n,iteration,index):
    """A function that takes a number(n), a list(iteration) and and index(index) and iteraters over the list of strings.
    if the character in the specific index of the string is larger or equal to that of the number(n), 
    returns a tuple with False and the number of iterations,
    else return a tuple with True and the number of iterations"""
    n = int(n)
    l = 0
    for i in iteration:
        l += 1
        if int(i[index]) >= n:
            return (False,l)
    return (True,l)       

# Now we iterate over the list of trees, skipping all the edges.
# For part 1, we check if any of our functions return True. if so, 
# that means the tree is visible from one of the directions at least. therefore we increase the amount of visible trees by 1.
# For part 2, we declare an empty var called "Highest score", replacing its value each time a higher one is calculated.
highest_scenic = 0
for i in r:
    if i == r[0] or i == r[-1]:
        continue
    ind = r.index(i)
    c = -1
    for n in i:
        c += 1
        if c == 0 or c == len(i) - 1:
            continue
        # Starting from index below that of (n) iterating backwards to index 0
        if row(n,i[c-1::-1])[0] == True:
            trees += 1
        # Starting after (n) until the end of the string    
        elif row(n,i[c+1::])[0] == True:   
            trees += 1
        # Starting from the string before (i) and iterating backwards to r[0], with the index of (n) as the function variable   
        elif column(n,r[ind-1::-1],c)[0] == True:
            trees += 1
        # Starting after the string (i) until the last string, with the index of (n) as the function variable   
        elif column(n,r[ind+1::],c)[0] == True:
            trees += 1 
        # Part 2
        # To calculate the scenic score, we multiply all the iterations of each function,
        # which tells us how many trees each function passed before terminating.
        scenic_score = row(n,i[c-1::-1])[1] * row(n,i[c+1::])[1] * column(n,r[ind-1::-1],c)[1] * column(n,r[ind+1::],c)[1]  
        if scenic_score > highest_scenic:
            highest_scenic = scenic_score           
                                           
print(trees)
print(highest_scenic)



    





