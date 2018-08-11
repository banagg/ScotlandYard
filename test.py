import collections
sgraph = {}
def map():
    global sgraph
    cord_node = []
    arr = []
    with open('SCOTMAP.txt','r') as f:
        for line in f:
            list = []
            for word in line.split():
                list.append(word)
            cord = tuple(list)
            cord_node.append(cord)
    graph = {}
    for i in range(470):
        u = cord_node[i][0]
        v = cord_node[i][1]
        w = cord_node[i][2]
        graph.setdefault(u,[]).append((v,w))
    sgraph = collections.OrderedDict(sorted(graph.items()))
   # print(sgraph)
map()

def poss_moves(curr_pos):
    global sgraph
    lis = []
    #length = len(sgraph[curr_pos])
    lis = sgraph[curr_pos]
    return lis
list = poss_moves('123')
print(list)


    

                          

