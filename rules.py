import collections
import random
# initialize game engine
def start():
    cord_node = []
    arr = []
    with open('SCOTPOS.txt','r') as f:
        for line in f:
            list = []
            for word in line.split():
                list.append(word)
            cord = tuple(list)
            cord_node.append(cord)          

    start_station = [103,112,34,155,94,117,132,53,174,198,50,91,26,29,141,13,138,197]
    num = 6
    random_start = random.sample(start_station, num)
    start1 = random_start[0]
    start2 = random_start[1]
    start3 = random_start[2]
    start4 = random_start[3]
    start5 = random_start[4]
    mr_x = random_start[5]

    cord1 = (cord_node[start1][1],cord_node[start1][2])
    x1 =int(cord1[0])
    y1 = int(cord1[1])
    arr.append((x1,y1))

    cord2 = (cord_node[start2][1],cord_node[start2][2])
    x2 =int(cord2[0])
    y2 = int(cord2[1])
    arr.append((x2,y2))


    cord3 = (cord_node[start3][1],cord_node[start3][2])
    x3 =int(cord3[0])
    y3 = int(cord3[1])
    arr.append((x3,y3))


    cord4 = (cord_node[start4][1],cord_node[start4][2])
    x4 =int(cord4[0])
    y4 = int(cord4[1])
    arr.append((x4,y4))


    cord5 = (cord_node[start5][1],cord_node[start5][2])
    x5 =int(cord5[0])
    y5 = int(cord5[1])
    arr.append((x5,y5))

    cord_mr_x = (cord_node[mr_x][1],cord_node[mr_x][2])
    xx =int(cord_mr_x[0])
    yx = int(cord_mr_x[1])
    arr.append((xx,yx))
    return arr

sgraph = {}
def map():
    global sgraph
    cord_node = []
    global sgraph
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
    print(sgraph)
#map()

def poss_moves(curr_pos):
    global sgraph
    lis = []
    #length = len(sgraph[curr_pos])
    lis = sgraph[curr_pos]
    return lis
#list = poss_moves('123')
#print(list)
