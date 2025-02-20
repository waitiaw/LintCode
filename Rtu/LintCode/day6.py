class LFUCache:
    """
    @param: capacity: An integer
    """
    # 데이터 베이스에 저장 (용량 초과시 사용량이 적은 key를 제거)
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.repeat = []
        self.freq = []

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # 용량이 가득 찼을때
        if len(self.cache) >= self.capacity:
            for key_value in self.cache:
                self.repeat.append(self.freq.count(key_value[0]))
            min_index = self.repeat.index(min(self.repeat))
            del self.cache[min_index]

        # 동일한 key가 존재할때 추가 X
        arr = []
        for check_key in self.cache:
            if check_key[0] == key:
                return False
        arr.append(key)
        arr.append(value)
        self.cache.append(arr)
        print(self.cache)

    """
    @param: key: An integer
    @return: An integer
    """
    # get하면 freq 배열에 key 값을 추가한다.
    def get(self, key):
        for i in self.cache:
            if i[0] == key:
                result = i[1]
                self.freq.append(i[0])
                return print(result)
        return print(-1)


if __name__ == "__main__":
    sol = LFUCache(3)
    sol.set(2,2)
    sol.set(1,1)
    sol.get(2)
    sol.get(1)
    sol.get(2)
    sol.set(3,3)
    sol.set(4,4)
    sol.get(3)
    sol.get(2)
    sol.get(1)
    sol.get(4)

