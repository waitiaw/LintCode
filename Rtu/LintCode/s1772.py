class Solution:
    """
    @param n: the range of element is in [1,n]
    @return: return the number of good collections
    """
    # 첫번째 인덱스 값 x에 대하여 2x,3x 해당하는 수를 제외한 리스트 조합 만들기
    def number_of_collections(self, n: int) -> int:
        cnt = 1
        print([])
        # write your code here
        for i in range(1,n+1):
            list = []
            list.append(i)
            for j in range(1,n+1):
                if i < j and j != 2*i and j != 3*i:
                    list.append(j)
            list_list = self.find_combinations_with_first(list)
            cnt += len(list_list)
            print(list_list)
        print(cnt)

    # 길이가 r인 조합 만들기
    def get_combinations(self,arr, r):
        if r == 0:
            return [[]]
        if not arr:
            return []

        with_first = self.get_combinations(arr[1:], r - 1)

        without_first = self.get_combinations(arr[1:], r)

        with_first = [[arr[0]] + comb for comb in with_first]
        return with_first + without_first

    # 길이가 r-1인 조합에 첫번쨰 인덱스 값 더하기
    def find_combinations_with_first(self,arr):
        first_value = arr[0]
        result = []

        for r in range(1, len(arr) + 1):
            combinations = self.get_combinations(arr[1:], r-1)
            for comb in combinations:
                result.append([first_value] + comb)

        return result


sol = Solution()
sol.number_of_collections(5)