class Coin:
    def __init__(self):
        self.coin_winner = True

    def coin_game(self, num):
        num = int(num)
        if num % 3 == 0:
            self.coin_winner = False
        else:
            self.coin_winner = True

        return self.coin_winner
num = input("동전의 갯수를 입력하시오")
result = Coin().coin_game(num)
print(result)