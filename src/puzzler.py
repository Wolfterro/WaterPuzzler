class Puzzler(object):
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2

    def __init__(self):
        self.A = [4, 2, 4, 2, 0, 4, 2, 0] # 2 x 0, 3 x 2, 3 x 4 - Not sure yet if that's relevant
        self.B = [0, 0, 2, 2, 2, 4, 0, 2] # 3 x 0, 4 x 2, 1 x 4 - Not sure yet if that's relevant
        self.C = [4, 0, 2, 2, 0, 2, 2, 0] # 3 x 0, 4 x 2, 1 x 4 - Not sure yet if that's relevant

        super(Puzzler, self).__init__()

    def get_row_data_from_options(self):
        row_data = [
            # Top
            {},
            # Middle
            {},
            # Bottom
            {},
        ]
        for x in range(1, 8 + 1):
            data = [self.A[x - 1], self.B[x - 1], self.C[x - 1]]
            data.sort()
            row_index = x * 2

            row_data[self.TOP][str(row_index)] = data[self.TOP]
            row_data[self.MIDDLE][str(row_index)] = data[self.MIDDLE]
            row_data[self.BOTTOM][str(row_index)] = data[self.BOTTOM]

        return row_data

    # "Private" Methods
    # -----------------
    def shift_left(self, puzzle_option):
        puzzle_option.append(puzzle_option.pop(0))

    def shift_right(self, puzzle_option):
        puzzle_option.insert(0, puzzle_option.pop(-1))
