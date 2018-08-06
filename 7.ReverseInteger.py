class Solution(object):
    def reverse_number(self,x):
        if x < 0:
                return -self.reverse_number(-x)

        result = 0
        while x:
            result = result * 10 + x % 10
            x //= 10
        return result if result <= 0x7fffffff else 0  # Handle overflow.

if __name__ == "__main__":
    print(Solution().reverse_number(354))
