from queue import PriorityQueue
class State(object):
    def __init__(self, value, parent,start, goal):
        self.neighbours=[]
        self.parent=parent
        self.value=value
        self.dist=0
        if parent:
            self.path=parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path=[value]
            self.start=start
            self.goal=goal
        def GetDist(self):
            pass
        def neighbourss(self):
            pass
class State_String(State):
    def __init__(self, value, parent, start=0, goal=0):
        super(State_String, self).__init__(value, parent, start, goal)
        self.dist= self.GetDist()
    def GetDist(self):
        if self.value ==self.goal:
            return 0
        dist = 0
        for i in range(len(self.goal)):
            letter=self.goal[i]
            dist +=abs(i - self.value.index(letter))
        return dist
    def neighbourss(self):
        if not self.neighbours:
            for i in range(len(self.goal)-1):
                val= self.value
                val=val[:i] + val[i+1]+val[i]+val[i+2:]
                neighbour = State_String(val, self)
                self.neighbours.append(neighbour)
class Astar:
    def __init__(self, start, goal):
        self.path=[]
        self.visitedQueue= []
        self.priorityQueue=PriorityQueue()
        self.start=start
        self.goal=goal
    def Solve(self):
        startState= State_String(self.start, 0, self.start, self.goal)
        count=0
        self.priorityQueue.put((0, count, startState))
        while(not self.path and self.priorityQueue.qsize()):
            closestneighbour=self.priorityQueue.get()[2]
            closestneighbour.neighbourss()
            self.visitedQueue.append(closestneighbour.value)
            for neighbour in closestneighbour.neighbours:
                if neighbour.value not in self.visitedQueue:
                    count+=1
                    if not neighbour.dist:
                        self.path=neighbour.path
                        break
                    self.priorityQueue.put((neighbour.dist, count, neighbour))
        if not self.path:
            print("Impossible")
        return self.path
start1 = input("Input Your start value: ")
goal1 = input("Input Your goal: ")
a=Astar(start1, goal1)
a.Solve()
for i in range(len(a.path)):
    print("%d"%i+") " + a.path[i])
