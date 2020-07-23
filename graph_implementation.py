from collections import defaultdict
import heapq as hq

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.result_list = list()
        self.nodes = set()
        self.head = -1

    def __str__(self):
        to_print = "["
        for u in self.graph:
            to_print += str(u) + ": " + str(self.graph[u])
        return to_print + "]"

    def size(self):
        return len(self.graph)

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.nodes.add(u)
        self.nodes.add(v)


    def DFSUtil(self, v, visited, result_list, bias=0):
        #visited[v-bias] = True
        print("function called")
        visited.append(self.head)
        #print(v, end = ' ')
        result_list.append(str(v))
        for i in self.graph[v]:
            if i not in visited:
                self.DFSUtil(i, visited, result_list, bias)

    def DFS(self, v):
        #visited = [False] * (len(self.graph))
        visited = []
        result_list = list()
        self.DFSUtil(v, visited, result_list, v)
        print(result_list)
        return result_list

    def grow_tree(self, v, res, visited):
        # from the original graph, expand it by adding the children of its children
        visited.append(v)
        children = self.graph[v]
        #print("children of node " + str(v) + ": " + str(children))
        #res[v].append(children)
        if len(children) > 0:
            for vertex in children:
                if vertex not in visited:
                    res.addEdge(v, vertex)
                    visited.append(vertex)
                    self.grow_tree(vertex, res, visited)
        return res

    def isReachable(self, start, end):
        # returns whether there is a path between two given nodes in the current graph
        visited = []

        # Create a queue for BFS
        queue = []
        hq.heappush(queue, start)
        #queue.append(start)
        visited.append(start)
        iter = 0
        while len(queue) > 0:
            #print("Been Called " + str(iter) + " times.")
            iter += 1
            n = hq.heappop(queue)
            if n == end:
                print("start node: "  + str(start) + ", end node: " + str(end))
                return True

            for i in self.graph[n]:
                try:
                    elem = visited[i]
                except:
                    visited.append(i)
                    hq.heappush(queue, i)
        return False


    def find(self, u):
        # find all the children of a given node
        return self.graph[u]

    def growSubtree(self, v):
        # from the original graph, create a subgraph with v as starting node + all of its children
        res = Graph()
        res.head = v
        visited = []
        return self.grow_tree(v, res, visited)

    def bestFirstSearch(self, start, end, edges_network):
        node_queue = []
        visited = []
        hq.heappush(node_queue, (0, start))
        while(len(node_queue) > 0):
            u = hq.heappop(node_queue)
            print(u[1])
            if u[1] == end:
                return node_queue
            for neighbour in self.graph[u[1]]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    l2_dist =  edges_network.loc[(edges_network["start_node_id"] == int(u[1])) & (edges_network["end_node_id"] == int(neighbour))]["l2_dist"].values[0]
                    hq.heappush(node_queue, (l2_dist, neighbour))
                visited.append(u)
        return 0

