class Node:
    def __init__(self, value):
        self.value = value
        self.nodes = []
        

def minimaxTreeAlphaBetaPruning(isMax, tree,alpha,beta):
    if len(tree.nodes) == 0:
        return tree.value

    if isMax:
      best = float('-inf')
      for node in tree.nodes:
        v = minimaxTreeAlphaBetaPruning(False, node,alpha,beta)
        best = max(best,v)
        alpha = max(best,alpha)
        if beta <= alpha:
          #check no more, we got max
          break
      tree.value = best
      return best
    else:
      best = float('inf')
      for node in tree.nodes:
        v = minimaxTreeAlphaBetaPruning(True, node,alpha,beta)
        best = min(best,v)
        beta = min(best,beta)
        if beta <= alpha:
          #check no more, we got min
          break
      tree.value = best
      return best


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

root.nodes.extend([l_1_1, l_1_2])

l_2_1 = Node(float('-inf'))
l_2_2 = Node(float('-inf'))
l_2_3 = Node(float('-inf'))
l_2_4 = Node(float('-inf'))

# link nodes to parent
l_1_1.nodes.extend([l_2_1, l_2_2])
l_1_2.nodes.extend([l_2_3, l_2_4])

l_2_1.nodes.extend([t_1, t_2])
l_2_2.nodes.extend([t_3, t_4])
l_2_3.nodes.extend([t_5, t_6])
l_2_4.nodes.extend([t_7, t_8])


# run
print('#' * 20)
print('the optimal value is: {}'.format(minimaxTreeAlphaBetaPruning(True, root,float('-inf'),float('inf'))))
print('#' * 20)
