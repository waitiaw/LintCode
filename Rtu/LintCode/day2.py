from typing import (
    List,
)
#Harr-1858
class Solution:
    """
    @param boxes: An array
    @return: the number of boxes
    """
    #def sort_box(self,):
    # 상자 안에 상자를 포개서 관리할때 가장 많이 포갤 수 있는 경우의 수
    def max_boxes(self, boxes: List[List[int]]) -> int:
        box_sort = []
        result = 1
        # 가로와 길이 작은 값을 0번 index로 저장하고 정렬해준다.
        for i in boxes:
            box = []
            box_length = i[0]
            box_weight = i[1]
            if box_length <= box_weight:
                box.append(box_length)
                box.append(box_weight)
            elif box_length > box_weight:
                box.append(box_weight)
                box.append(box_length)
            box_sort.append(box)
        box_sort = sorted(box_sort)
        # 현재 상자보다 큰 상자를 탐색하는 작업을 반복(다음 상자를 찾으면 그 상자를 기준으로 다시 탐색)
        for i in range(len(boxes) -1):
            if box_sort[i][0] < box_sort[i+1][0] and box_sort[i][1] < box_sort[i+1][1]:
                result += 1
                i += i -1
                pass

        return result


#boxList = [[5,4],[6,4],[6,7],[2,3]]
boxList = [[1,5],[6,2]]
sol = Solution()
print(sol.max_boxes(boxList))