import sys

def MBST(a):
    #create binary tree and mirror by switching the left and right child values
    btlist = []
    for i in range(len(a)):
        btlist.append(BT(a[i][0], a[i][2], a[i][1]))
    #nested for-loops to link each node to its child node(s)
    for i in range(len(btlist)):
        for j in range(len(btlist)):
            if btlist[i]._left == btlist[j]._value:
                btlist[i]._left = btlist[j]
            if btlist[i]._right == btlist[j]._value:
                btlist[i]._right = btlist[j]
    #identify the root from the given tree
    values = []
    child = []
    for i in range(len(a)):
        values.append(int(a[i][0]))
        if a[i][1] != 'x':
            child.append(int(a[i][1]))
        if a[i][2] != 'x':
            child.append(int(a[i][2]))
    root = list(set(values)-set(child))
    rootindex = values.index(root[0])
    #since in-order traversal of binary search trees are sorted lists, sort the list of values
    values.sort()
    #build binary search tree by performing in-order traversal of original mirrored binary tree 
    #and replacing the original value at each node with the sorted value 
    BST(btlist[rootindex], values)
    #perform pre-order traversal of binary search tree
    result = []
    preorder(btlist[rootindex], result)
    return " ".join(str(x) for x in result)

class BT:
    def __init__(self, v, left, right):
        self._value = v
        self._left = left
        self._right = right
    
def BST(n, temp):
    if n != 'x':
        BST(n._left, temp)
        n._value = temp[0]
        temp.pop(0)
        BST(n._right, temp)
        
def preorder(n, temp):
    if n != 'x':
        temp.append(n._value)
        preorder(n._left, temp)
        preorder(n._right, temp)


num_line = int(sys.stdin.readline())
for _ in range(num_line):
    a = [s.split(':') for s in sys.stdin.readline().split()]
    print(MBST(a))