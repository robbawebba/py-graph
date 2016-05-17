from graph import *
import string
maxVertices = 1000

vertexPrompt = "Enter a positive vertex ID, or 0 if done: "

edgePrompts = [\
"Enter the first vertex ID of an edge, or 0 if done: ",\
"Enter the id of the second vertex of the edge: "
]

source = None
target = None
index = 0
vertexKeepGoing = True;
edgeKeepGoing = True;

g = Graph();


##############################################
##           example graph data             ##
##############################################
#                     1                      #
#                    /\                      #
#                   4  2                     #
#                  /\   \                    #
#                 9  \   3 ---10             #
#                  \  \   \     \            #
#                   `--6---5    11 ---12     #
#                           \        /       #
#                            7---8--'        #
##############################################
# add vertices
for i in range(1,12):
    g.addVertex(i)
# Add edges
g.addEdge(1,4)
g.addEdge(1,2)
g.addEdge(4,9)
g.addEdge(4,6)
g.addEdge(9,6)
g.addEdge(6,5)
g.addEdge(2,3)
g.addEdge(3,5)
g.addEdge(3,10)
g.addEdge(10,11)
g.addEdge(11,12)
g.addEdge(5,7)
g.addEdge(7,8)
g.addEdge(8,12)

##############################################
## Command Line Prompts for nodes and edges ##
##      make sure to comment out the        ##
##        sample graph code above!          ##
##############################################
# #input vertex info for graph
# while vertexKeepGoing and index < maxVertices:
#     stdin = input(vertexPrompt)
#     if int(stdin) > 0:
#         g.addVertex(int(stdin))
#         index+=1
#     elif int(stdin) == 0:
#         vertexKeepGoing = False
#     else:
#         print "Enter a positive number please."
#
#
# while edgeKeepGoing:
#     stdin = input(edgePrompts[0])
#     if int(stdin) > 0:
#         second = input(edgePrompts[1])
#         g.addEdge(int(stdin), int(second))
#     elif int(stdin) == 0:
#         edgeKeepGoing = False
#     else:
#         print "Enter a positive number please."
print ""
print "printing graph..."
g.printGraph()
print ""

# print "Starting DFS..."
# parents = dfs(g, 1)
# print parents

print "Starting BFS..."
parents = bfs(g, 1)
print parents

print "The shortest path between 1 and 9 is of length " + str(findShortestPath(g, 1, 9, bfs(g,1)))
