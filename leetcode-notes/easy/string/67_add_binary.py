'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
'''


# Mine 
def binary2decimal(a, counter):
    if len(a) == 0:
        return 0
    i = a[-1]
    return int(i) * 2**counter + binary2decimal(a[:-1], counter+1)


def decimal2binary(a):
    res = ""
    while a > 1:
        r = a%2
        res = str(r) + res
        a = a // 2
    res = str(a) + res
    return res

class Solution:        
    def addBinary(self, a: str, b: str) -> str:
        sum_decimal = binary2decimal(a, 0) + binary2decimal(b, 0)
        return decimal2binary(sum_decimal)


# Others
class Solution:
    def addBinary(self, a, b):
        if len(a)==0: return b
        if len(b)==0: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1],b[0:-1]),'1')+'0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1],b[0:-1])+'0'
        else:
            return self.addBinary(a[0:-1],b[0:-1])+'1'

