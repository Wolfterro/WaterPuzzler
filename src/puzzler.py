class Puzzler(object):
    def __init__(self):
        self.A = [4, 2, 4, 2, 0, 4, 2, 0] # 2 x 0, 3 x 2, 3 x 4 - Not sure yet if that's relevant
        self.B = [0, 0, 2, 2, 2, 4, 0, 2] # 3 x 0, 4 x 2, 1 x 4 - Not sure yet if that's relevant
        self.C = [4, 0, 2, 2, 0, 2, 2, 0] # 3 x 0, 4 x 2, 1 x 4 - Not sure yet if that's relevant

        super(Puzzler, self).__init__()

    # "Private" Methods
    # -----------------
    def shift_left(self, puzzle_option):
        puzzle_option.append(puzzle_option.pop(0))

    def shift_right(self, puzzle_option):
        puzzle_option.insert(0, puzzle_option.pop(-1))
