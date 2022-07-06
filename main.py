import sys
import time

print(sys.getrecursionlimit())
sys.setrecursionlimit(200000)


class Tree:

    def __init__(self, data):
        self.children = []
        self.data = data
        self.h = 1
        self.probel = '_|'

    def height(self):
        h = 1
        for el in self.children:
            h = max(h, 1 + el.height())

        self.h = h
        return h

    def print(self):
        print(self.probel,'data of tree ', self.data, '  N children = ',len(self.children))
        for el in self.children:
            el.probel = self.probel*2
            el.print()


def add(dic, node):
    todel = []
    keys = [ind for ind in dic.keys() if dic[ind] == node.data]
    for ind in keys:
        node.children.append(Tree(ind))
        todel.append(ind)
    for el in todel:
        dic.pop(el)


def add_all(dic, node):
    add(dic, node)
    if len(dic) == 0: return 0
    for el in node.children:
        if len(dic) == 0: return 0
        add_all(dic, el)
    return 0


def height0(stroka, ind, glubina):
    el = stroka[ind]
    h = 1
    while el != -1:
        if glubina[el] > 0: return h + glubina[el]
        el = stroka[el]
        h += 1
    return h


def height(stroka, n):
    h = 1
    glubina = [0] * n
    ind = 0
    for _ in stroka:
        glub = height0(stroka, ind, glubina)
        glubina[ind] = glub
        h = max(h, glub)
        ind += 1
    return h




if __name__ == '__main__':
    stroka = input("type str for tree ")
    if stroka == '': stroka = '9 7 5 5 2 9 9 9 2 -1'
    time0 = time.time()
    n = len(stroka)
    stroka = [int(x) for x in stroka.split()]

    print(f'time after input {time.time() - time0:.6f}')
    print('height of tree = ', height(stroka, n))
    print(f'time for height of tree {time.time() - time0:.6f}')


    posminone = stroka.index(-1)
    tr = Tree(posminone)
    dic = dict((i,j) for i,j in list(enumerate(stroka)))
    add_all(dic,tr)
    tr.print()
    print('height of tree = ',tr.height())
    print(f'time for height of tree {time.time() - time0:.6f}')


