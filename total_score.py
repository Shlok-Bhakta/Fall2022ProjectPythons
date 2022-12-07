
class TOTAL_SCORE:
    def __init__(self, initial_blue=0, initial_yellow=0):
        """makes a global object to store the snakes' scores

        Args:
            initial_blue (int, optional): _description_. Defaults to 0.
            initial_yellow (int, optional): _description_. Defaults to 0.
        """
        self.blue_score = initial_blue
        self.yellow_score = initial_yellow

    def get_blue_score(self):
        """gets the blue score

        Returns:
            _type_: _description_
        """
        return self.blue_score

    def set_blue_score(self, num):
        """sets the blue score

        Args:
            num (_type_): _description_
        """
        self.blue_score = num

    def get_yellow_score(self):
        """get the yellow score

        Returns:
            _type_: _description_
        """
        return self.yellow_score

    def set_yellow_score(self, num):
        """set the yellow score

        Args:
            num (_type_): _description_
        """
        self.yellow_score = num
