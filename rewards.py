
class REWARDS():
    def __init__(self, initial_blue=0, initial_yellow=0):
        self.blue_reward = initial_blue
        self.yellow_reward = initial_yellow

    def get_blue_reward(self):
        return self.blue_reward

    def set_blue_reward(self, num):
        self.blue_reward = num

    def get_yellow_reward(self):
        return self.yellow_reward

    def set_yellow_reward(self, num):
        self.yellow_reward = num
