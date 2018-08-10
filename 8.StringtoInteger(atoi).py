class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX =  2147483647
        INT_MIN = -2147483648
        result = 0
        
        if not str:
            return result
        i=0
        while i<len(str) and str[i].isspace():
            i+=1
        if len(str)==i:
            return result
        sign=1
        if str[i]=="+":
            i+=1
        elif str[i]=="-":
            sign=-1
            i+=1
        
        while i<len(str) and '0'<=str[i]<='9':
            if result>(INT_MAX-int(str[i]))/10:
                return INT_MAX if sign>0 else INT_MIN
            result=result*10+int(str[i])
            i+=1
        return result*sign
            

if __name__ == "__main__":
    # assert Solution().myAtoi(" -1123") == -1123
    # assert Solution().myAtoi("222222222222222") == 2147483647
    print(Solution().myAtoi("-91283472332"))