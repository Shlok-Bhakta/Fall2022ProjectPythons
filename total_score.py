
class TOTAL_SCORE:
    def __init__(self, initial_blue=0, initial_yellow=0):
        self.blue_score = initial_blue
        self.yellow_score = initial_yellow

    def get_blue_score(self):
        return self.blue_score

    def set_blue_score(self, num):
        self.blue_score = num

    def get_yellow_score(self):
        return self.yellow_score

    def set_yellow_score(self, num):
        self.yellow_score = num
