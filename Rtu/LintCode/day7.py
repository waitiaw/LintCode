
class Solution:
    """
    @param n: the length of the string.
    @param k: the kth Lexicographically smallest that result should be.
    @return: return the kth Lexicographically smallest string.
    """
    # a,b,c를 이용해 만들 수 있는 조합 중 인접한 index의 값이 다르며 특정 번지수에 있는 값을 찾는 것
    def kth_string(self, n: int, k: int) -> str:
        string_set = ["a","b","c"]
        string_make = self.add_value(n,string_set)
        print(string_make)
        if k == 0:
            return None
        else:
            return print(string_make[k-1])
    # 만들 수 있는 모든 경우의 수를 체크
    def add_value(self, n, arr):
        result = ["a", "b", "c"]
        if n == 1:
            return result
        check_arr = []
        for i in arr:
            for j in result:
                if i[-1] != j:
                    check_arr.append(i+j)
        n -= 1
        if n == 0:
            return []
        elif n == 1:
            return check_arr
        else:
            return self.add_value(n,check_arr)

sol = Solution()
arr=["a", "b", "c"]
sol.kth_string(3,6)