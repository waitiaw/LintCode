class Solution:
    """
    @param n: the range of element is in [1,n]
    @return: return the number of good collections
    """
    def number_of_collections(self, n: int) -> int:
        # write your code here
        for i in range(1,n+1):
            list = []
            list.append(i)
            for j in range(1,n+1):
                if i < j and j != 2*i and j != 3*i:
                    list.append(j)
            print(list)

sol = Solution()
sol.number_of_collections(6)