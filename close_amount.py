

class CLOSE_AMOUNT:
    """a value to show the code how much its closed in
    """

    def __init__(self, initial_amount):
        self.close_amount = initial_amount

    def get_close_amount(self):
        return self.close_amount

    def set_close_amount(self, num):
        self.close_amount = num
