from typing import (
    List,
)

from numpy.ma.extras import row_stack


class Solution:
    """
    @param arr: the arr
    @param target: the target
    @return: the sum of paths
    """
    # 2차원 배열에서 이동 가능한 경로 중에서 이동 경로에 있는 모든 값의 Xor 값이 Target인 경로의 갯수
    def move_pos(self,pos,col,row,arr):
        max_col = len(arr) - 1
        max_row = len(arr[0]) -1
        if max_col < col or max_row < row:
            return
        new_pos = pos + [arr[col][row]]

        if col == max_col and row == max_row:
            print(new_pos)
            result = self.xor_check(new_pos)
            print(result)
            return new_pos

        self.move_pos(new_pos, col+1, row, arr)
        self.move_pos(new_pos, col, row+1, arr)

    def xor_check(self,result_arr):
        result = 0
        for i in result_arr:
            result ^= i
        return result

    def xor_sum(self, arr: List[List[int]], target: int) -> int:
        print(self.move_pos([],0,0,arr))

sol = Solution()
arr = [[2,1,5],[7,10,0],[12,6,4]]
target =11
print(sol.move_pos([],0,0,arr))
#print(sol.xor_check(arr[0]))
#print(sol.xor_sum(arr,6))
