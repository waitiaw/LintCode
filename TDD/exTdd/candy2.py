class Candy2:
    def __init__(self):
        self.count_of_candies = 0

    def give_candies(self,child):
        if len(child) == 0:
            self.count_of_candies = 0
        else:
            self.count_of_candies = 1
        return self.count_of_candies