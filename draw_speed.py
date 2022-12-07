class DRAW_SPEED:
    def __init__(self, initial_amount):
        """A flag to check if the speed powerup exists

        Args:
            initial_amount (_type_): _description_
        """
        self.draw_speed = initial_amount

    def get_draw_speed(self):
        return self.draw_speed

    def set_draw_speed(self, bool):
        self.draw_speed = bool
