a = 0
b = []
with open("mass.txt", "r") as x:
    for mass in x:
        current = int(mass)//3 - 2
        b.append(current)
        current = current//3 - 2
        while (current > 0):
            b.append(current)
            current = current//3 - 2

    print(sum(b))



"""
INPUT_FILE = 'mass.txt'

def main():
    with open(INPUT_FILE) as file:
        module_masses = [int(mass) // 3 - 2 for mass in file.readline()]
    print(sum(module_masses))

if __name__ == '__main__':
    main()
"""


#with open('input.txt','r') as f:
    #inp = list(map(int,f.readline().split(',')))
