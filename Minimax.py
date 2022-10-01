import math

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def minimaxTree(isMax, tree):
    if tree.right == None and tree.left == None:
        return tree.value
    
    if isMax:
        v = max(
            minimaxTree(False, tree.left) if tree.left is not None else float('-inf'),
            minimaxTree(False, tree.right) if tree.right is not None  else float('-inf')
        )
        return v
    else:
        v = min(
            minimaxTree(True,tree.left) if tree.left is not None else float('inf'),
            minimaxTree(True, tree.right) if tree.right is not None else float('inf')
        )
        return v


# t_X -> terminal node x
t_1 = Node(3)
t_2 = Node(5)
t_3 = Node(2)
t_4 = Node(9)
t_5 = Node(12)
t_6 = Node(5)
t_7 = Node(23)
t_8 = Node(23)

root = Node(float('-inf'))

# l_X_Y -> 
#         X: Level
#         Y: Node/Leaf
l_1_1 = Node(float('inf'))
l_1_2 = Node(float('inf'))

l_2_1 = Node(float('-inf'))
l_2_2 = Node(float('-inf'))
l_2_3 = Node(float('-inf'))
l_2_4 = Node(float('-inf'))

# link nodes to parent
l_1_1.left = l_2_1
l_1_1.right = l_2_2
l_1_2.left = l_2_3
l_1_2.right = l_2_4
l_2_1.left = t_1
l_2_1.right = t_2
l_2_2.left = t_3
l_2_2.right = t_4
l_2_3.left = t_5
l_2_3.right = t_6
l_2_4.left = t_7
l_2_4.right = t_8

#link root
root.left = l_1_1
root.right = l_1_2


#run 
print('#'*20)
print('the optimal value is: {}'.format(minimaxTree(True, root)))
print('#'*20)
