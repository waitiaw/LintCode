from typing import (
    List,
)
#Hard-3871
class Solution:
    """
    @param nums: An integer array
    @param queries: A two-dimensional array
    @return: Sum of special evenly-spaced elements in array
    """
    # queries에 첫번쨰 index 값에 두번째 index값을 더해가면서 값을 누적시켜주는 코드
    def solve(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        result = []
        # 첫번째 index와 증가하는 index를 추출
        for query in queries:
            total = 0
            index = query[0]
            add_index = query[1]
            # while문을 통해서 nums의 길이를 넘지 않는 선에서 index를 증가하면서 값을 더한다.
            while index < len(nums):
                value = nums[index]
                total += value
                index += add_index
            result.append(total)
        return result


sol = Solution()
arr_num = [0,1, 2, 3, 4, 5, 6, 7]
arr_queries = [[0, 3], [5, 1], [4, 2]]
print(sol.solve(arr_num, arr_queries))