# X and O

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0

def pr_xo(n):
    print(f'| {n[0]} | {n[1]} | {n[2]} |')
    print(f'| {n[3]} | {n[4]} | {n[5]} |')
    print(f'| {n[6]} | {n[7]} | {n[8]} |')

pr_xo(l)
def check(n):
    if n[0] == 'x' and n[1] == 'x' and n[2] == 'x':
        return 1
    elif n[0] == 'o' and n[1] == 'o' and n[2] == 'o':
        return 0
    elif n[3] == 'x' and n[4] == 'x' and n[5] == 'x':
        return 1
    elif n[3] == 'o' and n[4] == 'o' and n[5] == 'o':
        return 0
    elif n[6] == 'x' and n[7] == 'x' and n[8] == 'x':
        return 1
    elif n[6] == 'o' and n[7] == 'o' and n[8] == 'o':
        return 0
    elif n[0] == 'x' and n[3] == 'x' and n[6] == 'x':
        return 1
    elif n[0] == 'o' and n[3] == 'o' and n[6] == 'o':
        return 0
    elif n[1] == 'x' and n[4] == 'x' and n[7] == 'x':
        return 1
    elif n[1] == 'o' and n[4] == 'o' and n[7] == 'o':
        return 0
    elif n[2] == 'x' and n[5] == 'x' and n[8] == 'x':
        return 1
    elif n[2] == 'o' and n[5] == 'o' and n[8] == 'o':
        return 0
    elif n[0] == 'x' and n[4] == 'x' and n[8] == 'x':
        return 1
    elif n[0] == 'o' and n[4] == 'o' and n[8] == 'o':
        return 0
    elif n[2] == 'x' and n[4] == 'x' and n[6] == 'x':
        return 1
    elif n[2] == 'o' and n[4] == 'o' and n[6] == 'o':
        return 0


while count <= 8:
    x = int(input('В какую клетку ходить будем? (x): '))
    l[x - 1] = 'x'
    pr_xo(l)
    if check(l) == 1:
        exit(print('Победили крестики !'))
    count += 1

    if count >= 8:
        exit(print('Ничья !'))

    o = int(input('В какую клетку ходить будем? (o): '))
    l[o - 1] = 'o'
    pr_xo(l)
    if check(l) == 0:
        exit(print('Победили нолики !'))
    count += 1