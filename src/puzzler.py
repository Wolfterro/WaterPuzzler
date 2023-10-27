import random


class Puzzler(object):
    TOP = 0
    MIDDLE = 1
    BOTTOM = 2

    def __init__(self):
        self.A = [4, 2, 4, 2, 0, 4, 2, 0] # 2 x 0, 3 x 2, 3 x 4 - Not sure yet if that's relevant
        self.B = [0, 0, 2, 2, 2, 4, 0, 2] # 3 x 0, 4 x 2, 1 x 4 - Not sure yet if that's relevant
        self.C = [4, 0, 2, 2, 0, 2, 2, 0] # 3 x 0, 4 x 2, 1 x 4 - Not sure yet if that's relevant

        super(Puzzler, self).__init__()

    def get_row_data(self, sample=None):
        row_data = [
            # Top
            {},
            # Middle
            {},
            # Bottom
            {},
        ]
        for x in range(1, 8 + 1):
            if sample:
                data = [sample[self.TOP][x - 1], sample[self.MIDDLE][x - 1], sample[self.BOTTOM][x - 1]]
            else:
                data = [self.A[x - 1], self.B[x - 1], self.C[x - 1]]

            data.sort()
            row_index = x * 2

            row_data[self.TOP][str(row_index)] = data[self.TOP]
            row_data[self.MIDDLE][str(row_index)] = data[self.MIDDLE]
            row_data[self.BOTTOM][str(row_index)] = data[self.BOTTOM]

        return row_data

    def get_sample(self):
        sample = self.__shufle_sample_options()
        row_data = self.get_row_data(sample=sample)
        return row_data

    def shift_left(self, puzzle_option):
        puzzle_option.append(puzzle_option.pop(0))

    def shift_right(self, puzzle_option):
        puzzle_option.insert(0, puzzle_option.pop(-1))

    def get_seed(self, shift_seed=False):
        if shift_seed:
            return random.choice(range(0, 2))

        return random.choice(range(0, 99))

    def compare(self, row_data, sample):
        top = row_data[self.TOP] == sample[self.TOP]
        middle = row_data[self.MIDDLE] == sample[self.MIDDLE]
        bottom = row_data[self.BOTTOM] == sample[self.BOTTOM]

        return top and middle and bottom

    # "Private" Methods
    # -----------------
    def __shufle_sample_options(self):
        sample_A = self.A.copy()
        sample_B = self.B.copy()
        sample_C = self.C.copy()

        for sample in [sample_A, sample_B, sample_C]:
            seed = self.get_seed()
            shift_dir = self.get_seed(shift_seed=True)

            for rotation in range(seed):
                if shift_dir % 2 == 0:
                    self.shift_right(puzzle_option=sample)
                    continue

                self.shift_left(puzzle_option=sample)

        return [sample_A, sample_B, sample_C]
