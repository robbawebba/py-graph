from collections import deque

class Vertex:
  def __init__(self,key):
      self.id = key
      self.adjacent = {}
  # Adds the given vertex number to the list of adjacent vertices
  def addNeighbor(self,nbr,weight=0):
      self.adjacent[nbr] = weight

  def __str__(self):
      return str(self.id) + ' Adjacent To: ' + str([x.id for x in self.adjacent])

  def getConnections(self):
      return self.adjacent.keys()

  def getId(self):
      return self.id

  def getWeight(self,nbr):
      return self.adjacent[nbr]

class Graph:
    def __init__(self, dir = False):
        self.vertList = {} # list of vertices in the graph
        self.degrees = {} # list of the degrees of each vertex in the graph
        self.numVertices = 0 # number of vertices in the graph
        self.numEdges = 0 # number of edges in the graph
        self.directed = dir # boolean of whether the graph is directed or not
        self.entry = {} # list of entry times for each vertex
        self.exit = {} # list of exit times for each vertex
        self.discovered = {} # list of vertices that have been discovered
        self.processed = {} # list of vertices whose edges have been fully processed
        self.time = 0 # keeps track of search time for entry and exi

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        self.degrees[key] = 0
        return newVertex

    def getVertex(self,key):
        if key in self.vertList:
            return self.vertList[key]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def __str__(self):
        return str(self.numEdges) +"edges, " + str(self.numVertices) + " vertices: "+ str([x for x in self.vertList])

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        if self.directed == False: # We must add the double edge for undirected
            self.vertList[t].addNeighbor(self.vertList[f], cost)
            self.degrees[t] += 1
        self.vertList[f].addNeighbor(self.vertList[t], cost)
        self.degrees[f] += 1
        self.numEdges = self.numEdges + 1

    def getVertices(self):
        return self.vertList.keys()

    def sumDegrees(self):
        return sum(self.degrees.values())

    def printGraph(self):
        print self
        for v in self.vertList:
            print self.getVertex(v)

    def showHandshakeLemma(self):
        print "Sum of degrees = " + str(self.sumDegrees())
        print "2*|E|          = " + str(2*self.numEdges)


    def __iter__(self):
        return iter(self.vertList.values())

def dfs(g, root):
    parent = {}
    successor = 0 # successor vertex for recursion
    g.discovered[root] = True #discovered value of current root to true
    g.time += 1
    g.entry[root] = g.time #set entry time of vertex

    #if desired, do some vertex processing here

    #get list of adjacent vertices to the root
    adj = g.getVertex(root).adjacent.keys()
    while adj: #while there are still unexplored vertices adjacent to the root
        successor = adj.pop() # get a vertex adjacent to the root
        if successor.id not in g.discovered.keys():
            # if successor is not in list of possibly discovered vertices,
            # add it to the known list as undiscovered. This is pretty much a
            # check for null because I was getting an error. The important condition
            # is two lines down
            g.discovered[successor.id] = False #
        if not g.discovered[successor.id]: #if the successor has not been discovered
            parent[successor.id] = root # add root as parent to successor
            #process the edge (root,successor) if desired
            dfs(g, successor.id, parent) #recursively explore further down tree
        # elif ((not g.processed[successor.id] and g.parent[root] != successor.id) or g.directed):
            # This is a back edge!
            # In order to find cycles (one of the applications of dfs),you
                # should process the edge here: process_edge(root, successor)

    # if you want to process the root vertex some more, do it here!
        # e.g. process_vertex_late(root, successor)

    g.time +=1
    g.exit[root] = g.time # set the exit time of the graph
    g.processed[root] = True
    if g.numVertices == len(g.processed): # if all vertices of graph have been processed
        # We're done with the dfs!
        # clear some of the global variables to be used in future searches
        g.time = 0
        g.discovered = {}
        g.processed = {}
        parent[root] = -1 # add the original graph root to list of parents as -1
        return parent

def bfs(g, root):
    parent={}
    queue = deque() #double-ended queue (we will be pushing with append(), and popping with popleft())
    curr = 0 #current node we're working on
    successor = 0 # node adjacent to/descendant of curr

    parent[root] = -1 # add the original graph root to list of parents as -1
    queue.append(root) # add the starting root node to the queue
    g.discovered[root] = True # label the root node as discovered
    while queue: # while the queue is not empty
        curr = queue.popleft() #set curr to first node in the queue
        #If you want, you could process curr here! e.g. process_vertex_early(curr)
        g.processed[curr] = True # label curr as processed
        adj = g.getVertex(curr).adjacent.keys() #get the list of nodes adjacent to curr
        while adj: #while there are still adjacent nodes in the list
            successor = adj.pop() #get next adjacent node in list
            # if successor is not in list of possibly processed vertices,
            # add it to the known list as unprocessed.
            if successor.id not in g.processed.keys():
                g.processed[successor.id] = False
            # if successor is not in list of possibly discovered vertices,
            # add it to the known list as undiscovered.
            if successor.id not in g.discovered.keys():
                g.discovered[successor.id] = False
            #if not g.processed[successor.id] or g.directed:
                # here you could do some edge processing, depending on what you
                # are trying to accomplish
            if not g.discovered[successor.id]: # if the node has not yet been discovered
                queue.append(successor.id) # add node to queue of nodes to explore
                g.discovered[successor.id] = True #label node as discovered
                parent[successor.id] = curr #set the parent of successor to curr
        # here, after the loop of exploring nodes adjacent to curr, you can
        # process the current vertex curr again if you want
    if g.numVertices == len(g.processed): # if all vertices of graph have been processed
        # We're done with the dfs!
        # clear some of the global variables to be used in future searches
        g.discovered = {}
        g.processed = {}
        return parent

def findShortestPath(g, source, target, parents):
    if source == target or target == -1:
        return 0
    else:
        return 1 + findShortestPath(g, source, parents[target], parents)
