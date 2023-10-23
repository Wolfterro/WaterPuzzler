#!/usr/bin/env python3
from src.drawer import Drawer
from src.puzzler import Puzzler

def main():
    # row_data = [
    #     # Top
    #     {
    #         "2": 2,
    #         "4": 0,
    #         "6": 0,
    #         "8": 0,
    #         "10": 0,
    #         "12": 0,
    #         "14": 2,
    #         "16": 0,
    #     },
    #     # Middle
    #     {
    #         "2": 2,
    #         "4": 0,
    #         "6": 2,
    #         "8": 2,
    #         "10": 0,
    #         "12": 2,
    #         "14": 2,
    #         "16": 4,
    #     },
    #     # Bottom
    #     {
    #         "2": 4,
    #         "4": 2,
    #         "6": 4,
    #         "8": 2,
    #         "10": 2,
    #         "12": 4,
    #         "14": 4,
    #         "16": 4,
    #     }
    # ]
    drawer = Drawer()
    puzzler = Puzzler()

    row_data = puzzler.get_row_data_from_options()

    drawer.draw_div("Sample")
    drawer.draw(row_data=row_data)

    drawer.draw_div("Options")
    drawer.draw_puzzle_option(puzzler.A, "A")
    drawer.draw_puzzle_option(puzzler.B, "B")
    drawer.draw_puzzle_option(puzzler.C, "C")

    drawer.draw_div("Result")
    drawer.draw(row_data=row_data)

if __name__ == '__main__':
    main()
