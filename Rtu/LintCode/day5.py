class Solution:
    """
    @param n: an integer
    @param m: an integer
    @param p: an integer
    @return: return an integer
    """
    # super-948 n 배열일 때 추가 필요
    # 배열에 해당하는 값이 모두 소수인지 확인
    def remove_num(self,result_arr):
        for a in result_arr:
            if self.find_prime(a) == True:
                return True
        return False
    # 소수 찾기
    def find_prime(self, value):
        for k in range(2, value):
            if value % k == 0:
                return False
        return True

    # 사용가능한 숫자 배열
    def use_num(self,max_num):
        num_list = []
        for num in range(1,max_num+1):
            num_list.append(num)
        return num_list
    # 만들 수 있는 모든 경우의 배열을 생성
    def arr_basic(self, count_num, max_num, comb_num, sum_num):
        result2 = []
        if count_num == 0:
            return None
        for i in comb_num:
            for j in range(1,max_num+1):
                result1 = []
                if isinstance(i, list):
                    result1.extend(i)
                else:
                    result1.append(i)
                result1.append(j)
                sum = 0
                for m in result1:
                    sum += m
                # 배열의 합이 p의 배수거나 배열에 소수가 포함되어 있으면 result2에 저장
                if sum%sum_num == 0 and self.remove_num(result1) == True:
                    result2.append(result1)
        count_num -= 1
        if count_num == 1:
            print(result2)
            return result2
        else:
            return self.arr_basic(count_num, max_num, result2, sum_num)
    # 최종 배열의 길이를 확인
    def sequence_count(self, n: int, m: int, p: int) -> int:
        arr_sequence = self.use_num(m)
        result = self.arr_basic(n,m,arr_sequence, p)
        return print(len(result))


sol = Solution()
n = 2
m = 5
p = 4
sol.sequence_count(n,m,p)
