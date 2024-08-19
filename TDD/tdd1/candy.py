from encodings.punycode import selective_find


class Candy:
    def __init__(self):
        self.count_of_candies = 0

    def give_candies(self, child):

        if len(child) == 0:
            self.count_of_candies = 0
        else:
            self.count_of_candies = len(child)
            for i in range(len(child) - 1):
                if child[i+1] > child[i]:
                    self.count_of_candies += 1

        return self.count_of_candies

input_str = input("사탕을 받으러 온 아이들의 정보를 입력해주세요")
arr = list(map(int, input_str.split()))

count = Candy().give_candies(arr)
print("총 사용한 Candy : ", count)
