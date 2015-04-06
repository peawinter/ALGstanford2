# data format
# weight, length
class Solution1():
    
    def readData(self):
        # import the data
        file = open('clustering1.txt', 'r')
        # file = open('test.txt', 'r')
        lines = file.readlines()
        self.cnt = int(lines[0])
        self.edgeDict = {}
        for line in lines[1:]:
            newop = map(int, line.split(' '))
            self.edgeDict[(newop[0] - 1, newop[1] - 1)] = newop[-1]
        self.edgeDict
    
    def MST(self):
        edgeLst = sorted(self.edgeDict, key=self.edgeDict.get)
        track = range(self.cnt)
        dist = 0
        for edge in edgeLst:
            if track[edge[0]] != track[edge[1]]:
                tmp = track[edge[1]]
                for idx in range(self.cnt):
                    if track[idx] == tmp:
                        track[idx] = track[edge[0]]
                dist += self.edgeDict[edge]
        return dist
    
    def KCluster(self, k = 4):
        edgeLst = sorted(self.edgeDict, key=self.edgeDict.get)
        track = range(self.cnt)
        n_cluster = self.cnt
        for edge in edgeLst:
            if track[edge[0]] != track[edge[1]]:
                if n_cluster > k:
                    tmp = track[edge[1]]
                    for idx in range(self.cnt):
                        if track[idx] == tmp:
                            track[idx] = track[edge[0]]
                    n_cluster -= 1
                else:
                    return self.edgeDict[edge]
        return None

class Solution2():
    
    def __init__(self):
        self.A = []
        for i in range(24):
            op = ['0'] * 24
            op[i] = '1'
            self.A.append(int(''.join(op), 2))
        for i in range(1, 24):
            for j in range(i):
                op = ['0'] * 24
                op[i], op[j] = '1', '1'
                self.A.append(int(''.join(op), 2))
        print self.A
    
    def readData(self):
        # import the data
        file = open('clustering_big.txt', 'r')
        lines = file.readlines()
        self.cnt = map(int, lines[0].split(' '))
        self.data = {}
        for line in lines[1:]:
            op = int(''.join(line.split(' ')[:-1]), 2)
            self.data[op] = op
    
    def allNeighbor(self, node):
        return [node ^ a for a in self.A]
        
    def Three(self):
        merge_cnt = 0
        node_cnt = 0
        for node in self.data:
            nodeFather = self.data[node]
            while nodeFather != self.data[nodeFather]:
                nodeFather = self.data[nodeFather]
                self.data[node] = nodeFather
            neighbors = self.allNeighbor(node)
            for ngb in neighbors:
                if ngb in self.data:
                    ngbFather = self.data[ngb]
                    while ngbFather != self.data[ngbFather]:
                        ngbFather = self.data[ngbFather]
                        self.data[ngb] = ngbFather
                    if ngbFather != nodeFather:
                        self.data[ngbFather] = nodeFather
                        self.data[ngb] = nodeFather
                        merge_cnt += 1
            node_cnt += 1
            if node_cnt % 1000 == 0:
                print node_cnt
        print merge_cnt, node_cnt
        
if __name__ == '__main__':
    # sol1 = Solution1()
    # sol1.readData()
    # print sol1.KCluster(4)
    
    # print output1
    # output2 = sol1.two(data)
    # print output2
    
    sol2 = Solution2()
    sol2.readData()
    sol2.Three()
    # sol2.three(data2)