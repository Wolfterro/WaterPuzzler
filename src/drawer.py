from colored import fore, style


class Drawer(object):
    def __init__(self):
        self.rows = 3
        self.columns = 8
        self.limiter = "ꓕ"

        super(Drawer, self).__init__()

    def draw(self, row_data):
        self.__print_delimiter("up")
        for x in row_data:
            self.__print_line(line=self.__get_current_line(row_data=x))
        self.__print_delimiter("down")

    def draw_puzzle_option(self, puzzle_option, label):
        self.__print_delimiter(direction="up")
        self.__print_line(line=self.__get_current_line(row_data=puzzle_option), label=label)
        self.__print_delimiter(direction="down")

    def draw_div(self, text):
        value = "    " + "—————— {} ".format(text) + "—" * (((self.columns * 4) + 4) - len(text))
        print(value)

    def draw_lights(self, cleared=False):
        red_light = "{}◉{}".format(
            fore.RED,
            style.RESET
        )
        green_light = "{}◉{}".format(
            fore.GREEN,
            style.RESET
        )
        print("{}".format(red_light if not cleared else "○"))
        print("{}".format(green_light if cleared else "○"))
        print()

    def draw_selection_choices(self):
        print("Which wave range will you adjust?")
        print("[A] - Wave A")
        print("[B] - Wave B")
        print("[C] - Wave C")
        print("[Q] - Quit")

    def draw_interaction_choices(self):
        print("Move to which direction?")
        print("[L] - Left")
        print("[R] - Right")
        print("[C] - Check")
        print("[Q] - Return")

    # "Private" Methods
    # -----------------
    def __print_line(self, line, label=None):
        value = "⎸" + line + self.limiter + "⎹"
        if label:
            value = "{} - ".format(label) + value
        else:
            value = "    " + value

        if label == "A":
            block = "{}█{}".format(
                fore.RED,
                style.RESET
            )
        elif label == "B":
            block = "{}█{}".format(
                fore.YELLOW,
                style.RESET
            )
        elif label == "C":
            block = "{}█{}".format(
                fore.CYAN,
                style.RESET
            )
        else:
            block = "█"

        value = value.replace("█", block)
        print(value)

    def __print_delimiter(self, direction):
        delimiter = "_" if direction == "up" else "‾"
        value = delimiter * ((self.columns * 5) + 4)
        value = "    " + value

        print(value)

    def __get_current_line(self, row_data):
        line = ""
        for x in range(1, self.columns * 2 + 1):
            if x % 2 == 0:
                if type(row_data) == dict:
                    value = row_data.get("{}".format(x), 0)
                else:
                    value = row_data[(x // 2) - 1]

                line += "█" * value
                line += " " * (4 - value)

                continue

            line += self.limiter

        return line
