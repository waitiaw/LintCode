from typing import (
    List,
)
#Hard-1879
class Solution:
    """
    @param nums: the input array
    @param target: the target number
    @return: return the target pair
             we will sort your return value in output
    """
    # 리스트에서 두 값을 더했을때 target이 되는 경우 찾기
    def two_sum_v_i_i(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        # 현재 값에서 target이 되려면 더하거나 빼야하는 값을 찾음
        for i in range(len(nums)):
            success_sum = []
            value = target - nums[i]
            for j in range(len(nums)):
                # 현재 값의 부호에 따라 값을 더하거나 빼줌
                if nums[j] == value and i <j:
                    success_sum.append(i)
                    success_sum.append(j)
            if success_sum != []:
                result.append(success_sum)
        return result
arr_input = [0,-1,2,-3,4]
target_input = 1
sol = Solution()
print(sol.two_sum_v_i_i(arr_input,target_input))