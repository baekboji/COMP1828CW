class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    class Locator(HeapPriorityQueue. Item):
        slots = _index # add index as additional field

    def init (self, k, v, j):
        super( ). init (k,v)
        self. index = j


    def swap(self, i, j):
        super( ). swap(i,j) # perform the swap

    def bubble(self, j):
        if j > 0 and self. data[j] < self. data[self. parent(j)]:
            self. upheap(j)
        else:

            def dijstras_algorithm(g, src):
                d = {}  # d[v] is upper bound from s to v
                cloud = {}  # map reachable v to its d[v] value
                pq = AdaptableHeapPriorityQueue()  # vertex v will have key d[v]
                pqlocator = {}  # map from vertex to its pq locator

                # for each vertex v of the graph, add an entry to the priority queue, with
                # the source having distance 0 and all others having infinite distance
                for v in g.vertices():
                    if v is src:
                        d[v] = 0
                    else:
                        d[v] = float('inf')  # syntax for positive infinity
                        pqlocator[v] = pq.add(d[v], v)  # save locator for future updates

                while not pq. is empty():
                    key, u = pq.remove
                    min()
                    cloud[u] = key  # its correct d[u] value
                    del pqlocator[u]  # u is no longer in pq
                    for e in g.incident edges(u):  # outgoing edges (u,v)
                        v = e.opposite(u)
                        if v not in cloud:
                            # perform relaxation step on edge (u,v)
                            wgt = e.element()
                            if d[u] + wgt < d[v]:  # Better path to v?
                                d[v] = d[u] + wgt  # update the distance
                                pq.update(pqlocator[v], d[v], v)  # update the pq entry

            return cloud  # only includes reachable vertices
            self. downheap(j)
