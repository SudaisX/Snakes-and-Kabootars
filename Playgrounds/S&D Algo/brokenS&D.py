from Playgrounds.dsa import Queue


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        for p in range(len(self.queue)):
            if self.queue[p][1] < priority:
                self.queue.insert(p, (item, priority))
                return
        self.queue.append((item, priority))

    def dequeue(self):
        return self.queue.pop(0)[0]

    def is_empty(self):
        return self.queue == []


def BFS_(self, start):
    queue = Queue()
    queue.enQueue(start)
    visited = []

    while not(queue.is_empty()):
        current = queue.deQueue()
        for neighbour in self.getNeighbours(current):
            if neighbour not in visited:
                queue.enQueue(neighbour)
        visited.append(current)
    return visited


def MinRolls(move, N):
    visited = [False]*N
    queue = PriorityQueue()

    visited[0] = True

    queue.enqueue(0, 0)  # (node, dist)

    while not(queue.is_empty()):
        qe = queue.dequeue(0)
        v = qe.v

        if v == N - 1:
            break
        j = v+1
        while j <= v+6 and j < N:

            if visited[j] is False:

                a
