"""
배열이 주어졌을 때 이 배열을 이용하여 이진 트리를 만든다
이때 각 노드의 값이 자식 노드의 평균 값에 해당하도록
최소한으로 수정했을 때 수정 횟수
"""
class Solution:
    # 트리 형태의 배열로 만들어 보기 쉽게 정리함
    def make_tree(self,arr):

        list_list = []
        end = 1
        while len(arr) > 0:
            list = []
            for i in range(end):
                remove_value = arr.pop(0)
                list.append(remove_value)
            print(list)
            list_list.append(list)
            end = end * 2
            for j in list:
                if j == "#":
                    end -= 2
        return list_list
    # 트리 형태에서 각 부모 노드가 자식 노드의 평균 값인지 구한다
    def check_tree(self,arr):
        copy_list = arr.copy()
        cnt = 0
        null_cnt = 0
        list = self.make_tree(arr)
        num_cnt = len(copy_list) - len(list[-1])

        for i in range(num_cnt):
            left = 2 * i + 1 - null_cnt
            right = 2 * i + 2 - null_cnt
            if copy_list[i] == "#":
                null_cnt += 2
            elif copy_list[left] == "#" or copy_list[right] == "#":
                pass
            elif copy_list[i] != (copy_list[left] +copy_list[right])/2:
                cnt += 1
                #print(i,left,right)
        return cnt


sol = Solution()
arr = [2,0,2,"#","#",0,2,"#","#",0,1,"#","#",0,1,"#","#",0,1]
print(sol.check_tree(arr))
