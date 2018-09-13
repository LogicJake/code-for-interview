class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
       	# listall = [[0 for col in range(((len(s)//(numRows*2-2))+1)*2)] for row in range(numRows)]
        # print(listall[0].__len__())
        if numRows == 1:
        	return s
        listall = []
        rule = []
        for x in range(0,numRows):
        	rule.append(x)
        for x in range(0,numRows-2):
        	rule.append(numRows-x-2)
        for x in range(0,numRows):
        	listall.append([])
        for x in range(0,len(s)):
        	temp = listall[rule[x%(numRows*2-2)]]
        	temp.append(s[x])
        	listall[rule[x%(numRows*2-2)]] = temp
       	res = ''
        for x in range(0,numRows):
        	res += ''.join(listall[x])
        return res
b = Solution()
print(b.convert("PAYPALISHIRING", 3))