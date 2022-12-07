class IS2P:
    def __init__(self, initial_val=True):
        """checks if the game is 1 player

        Args:
            initial_val (bool, optional): _description_. Defaults to True.
        """
        self.blue_score = initial_val

    def get_2p(self):
        return self.blue_score

    def set_2p(self, val: bool):
        self.blue_score = val
