class DRAW_SLOW:
    def __init__(self, initial_amount):
        """a flag for checking if the slow powerup exists

        Args:
            initial_amount (_type_): _description_
        """
        self.draw_slow = initial_amount

    def get_draw_slow(self):
        return self.draw_slow

    def set_draw_slow(self, bool):
        self.draw_slow = bool
