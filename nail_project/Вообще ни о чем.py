import random

def pretty___print(mesto):
    print("-"*10)
    for row in mesto:
        print(*row)
    print("-" * 10)

def get_number_from_index(i, j):
    return i*4+j+1

def get_empty_list(mesto):
    empty = []
    for i in range(4):
        for j in range(4):
            if mesto[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty

def get_index_from_number(num):
    num-=1
    x,y = num//4, num%4
    return x,y

def insert_2_or_4(mesto,x,y):
    if random.random()<=0.75:
        mesto[x][y]=2
    else:
        mesto[x][y]=4
    return mesto

mesto = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
pretty___print(mesto)
print(get_empty_list(mesto))

