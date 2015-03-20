# your code goes here
# import the data
import urllib2  
url = 'http://spark-public.s3.amazonaws.com/algo1/programming_prob/IntegerArray.txt'
file = urllib2.urlopen(url)
data = []
for line in file:
    data.append(int(line))

# Tiral data
# data = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# build the function
class Solution():
    def inverCount(self, data):
    	if len(data) <= 1:
    		return [data, 0]
    	if len(data) == 2:
    		if data[0] > data[1]:
    			return [data[::-1], 1]
    		return [data, 0]
    	[data1, count1] = self.inverCount(data[ : len(data)/2])
    	[data2, count2] = self.inverCount(data[len(data)/2 : ])
    	idx1, idx2 = 0, 0
    	newData = []
    	count = 0
    	while idx1 < len(data1) and idx2 < len(data2):
    		if data1[idx1] < data2[idx2]:
    			newData += [data1[idx1]]
    			idx1 += 1
    		else:
    			newData += [data2[idx2]]
    			idx2 += 1
    			count += len(data1) - idx1
    	if idx1 == len(data1):
    		newData += data2[idx2:]
    	else:
    		newData += data1[idx1:]
        return [newData, count1 + count2 + count]

sol = Solution()
[data, b] = sol.inverCount(data)
print b
