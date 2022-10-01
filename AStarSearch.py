def aStarAlgo(start_node, stop_node):     
        open_set = {start_node}     #frontier
        closed_set = set()          #explored
        g = {}                      #heuristic value
        parents = {}

        g[start_node] = 0
        parents[start_node] = start_node
        while len(open_set) > 0:
            n = None
 
            #node with lowest f() is found

            for v in open_set:
                if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
                    n = v
             
            if n == stop_node or Graph_nodes[n] == None:
                pass
            else:
                for (m, weight) in get_neighbors(n):
                    if m not in open_set and m not in closed_set:
                        open_set.add(m)
                        parents[m] = n
                        g[m] = g[n] + weight
         
                    else:
                        if g[m] > g[n] + weight:
                            #update g(m)
                            g[m] = g[n] + weight
                            #change parent of m to n
                            parents[m] = n
                             
                            #if m in closed set,remove and add to open
                            if m in closed_set:
                                closed_set.remove(m)
                                open_set.add(m)
 
            if n == None:
                print('Path does not exist!')
                return None
 
            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                path = []
 
                while parents[n] != n:
                    path.append(n)
                    n = parents[n]
 
                path.append(start_node)
 
                path.reverse()
 
                print('Path found: {}'.format(path),end='')
            
                return path
 
 
            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_set.remove(n)
            closed_set.add(n)
 
        print('Path does not exist!')
        return None
         
#define fuction to return neighbor and its distance
#from the passed node
def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None

def heuristic(n):
    H_dist = {
        'Arad' : 366,
        'Bucharest' : 0,
        'Craiova' : 160,
        'Drobeta' : 242,
        'Eforei' : 161,
        'Fragaras' : 176,
        'Giu' : 77,
        'Hirsova' : 151,
        'Iasi' : 226,
        'Lugoj' : 244,
        'Mehadia' : 241,
        'Neamt'  : 234,
        'Oradea' : 380,
        'Pitesti' : 100,
        'Rim' : 193,
        'Sibiu' : 253,
        'Timisoara' : 329,
        'Urz' : 80,
        'Vaslui' : 199,
        'Zerind' : 374
    }
    print(n)
    return H_dist[n]


Graph_nodes = {
    'Arad' : [('Zerind',75),('Timisoara',118),('Sibiu',140)],
    'Zerind' : [('Arad',75),('Oradea',71)],
    'Oradea' : [('Zerind',71),('Sibiu',151)],   
    'Timisoara' : [('Arad',118),('Lugoj',111)],
    'Lugoj' : [('Timisoara',111),('Mehadia',70)],
    'Mehadia' : [('Lugoj',70),('Drobeta',75)],
    'Drobeta' : [('Mehadia',75),('Criova',120)],
    'Criova' : [('Drobeta',120),('Rim',146),('Pitesti',138)],
    'Rim' : [('Criova',146),('Pitesti',97),('Sibiu',80)],
    'Sibiu' : [('Arad',140),('Oradea',151),('Fragaras',99),('Rim',80)],
    'Fagaras' : [('Sibiu',99),('Becharest',211)],
    'Bucharest' : [('Fagaras',211),('Pitesti',101),('Giu',90),('Urz',85)],
    'Giu' : [('Bucharest',90)],
    'Urz' : [('Bucharest',85),('Vaslui',142),('Hirsova',98)],
    'Hirsova' : [('Urz',98),('Eforie',86)],
    'Eforie' : [('Hirsova',86)],
    'Vaslui' : [('Urz',142),('Iasi',92)],
    'Iasi' : [('Neamt',87),('Vaslui',92)],
    'Neamt' : [('Iasi',87)],
    'Pitesti' : [('Rim',97),('Criova',138),('Bucharest',110)]
}

aStarAlgo('Arad', 'Rim')
