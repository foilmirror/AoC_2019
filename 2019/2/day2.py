def intcode(noun, verb):
    with open('program.txt','r') as f:
        inp = list(map(int,f.readline().split(',')))

    inp[1] = noun
    inp[2] = verb
    index = 0
    while inp[index] != 99:
        if inp[index] == 1:
            inp[inp[index+3]] = inp[inp[index+1]] + inp[inp[index+2]]
        elif inp[index] == 2:
            inp[inp[index+3]] = inp[inp[index+1]] * inp[inp[index+2]]
        else:
            print('failure')
            break
        index += 4

    return(inp[0])

for y in range(0,99):
    for x in range(0,99):
        if (intcode(x,y) == 19690720):
            print(100 * x + y)
            exit(0)
print("failed")
