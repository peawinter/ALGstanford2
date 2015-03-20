# data format
# weight, length

import Queue

class Solution1():
    
    def readData(self):
        # import the data
        file = open('jobs.txt', 'r')
        lines = file.readlines()
        cnt = int(lines[0])
        data = []
        for line in lines[1:]:
            newop = line.split(' ')
            data.append(map(int, newop))
        return data
    
    def one(self, data):
        data = sorted(data, key = lambda x: (x[0] - x[1], x[0]), reverse = True)
        print data[:10]
        curr_time = 0
        output = 0
        for row in data:
            curr_time += row[1]
            output += curr_time * row[0]
        return output
    
    def two(self, data):
        data = sorted(data, key = lambda x: x[0]/float(x[1]), reverse = True)
        print data[:10]
        curr_time = 0
        output = 0
        for row in data:
            curr_time += row[1]
            output += curr_time * row[0]
        return output

class Solution2():
    
    def readData(self):
        # import the data
        file = open('edges.txt', 'r')
        lines = file.readlines()
        self.cnt = map(int, lines[0].split(' '))
        data = {}
        for line in lines[1:]:
            newline = (map(int, line.split(' ')))
            data[frozenset(newline[0:2])] = newline[2]
        return data
    
    def three(self, data):
        visited = set([1])
        output = 0
        while len(visited) < self.cnt[0]:
            neighbor = {key: value for (key, value) in data.items() if len(key - visited) == 1}
            visited = visited | min(neighbor, key = neighbor.get)
            output += min(neighbor.values())
            print len(visited), output
        return output

if __name__ == '__main__':
    sol1 = Solution1()
    data = sol1.readData()
    output1 = sol1.one(data)
    print output1
    output2 = sol1.two(data)
    print output2
    
    # sol2 = Solution2()
    # data2 = sol2.readData()
    # sol2.three(data2)