class IS2P:
    def __init__(self, initial_val=True):
        self.blue_score = initial_val

    def get_2p(self):
        return self.blue_score

    def set_2p(self, val: bool):
        self.blue_score = val
