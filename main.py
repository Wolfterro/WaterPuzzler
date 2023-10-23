#!/usr/bin/env python3
from src.drawer import Drawer
from src.puzzler import Puzzler

def main():
    row_data = [
        # Top
        {
            "0": 0,
            "2": 2,
            "4": 0,
            "6": 0,
            "8": 0,
            "10": 0,
            "12": 0,
            "14": 2,
            "16": 0,
        },
        # Middle
        {
            "0": 2,
            "2": 2,
            "4": 0,
            "6": 2,
            "8": 2,
            "10": 0,
            "12": 2,
            "14": 2,
            "16": 2,
        },
        # Bottom
        {
            "0": 4,
            "2": 4,
            "4": 2,
            "6": 4,
            "8": 2,
            "10": 2,
            "12": 4,
            "14": 4,
            "16": 4,
        }
    ]

    drawer = Drawer()
    drawer.draw(row_data=row_data)

    puzzler = Puzzler()
    drawer.draw_puzzle_option(puzzler.A, "A")
    drawer.draw_puzzle_option(puzzler.B, "B")
    drawer.draw_puzzle_option(puzzler.C, "C")


if __name__ == '__main__':
    main()