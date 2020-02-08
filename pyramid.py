#!/usr/bin/env python3
"""Print a pyramid to the terminal
A pyramid of height 3 would look like:
--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter

#  raises error if the height is not at least 1.
def print_pyramid(height):
    """Print a pyramid of a given height
    :param int rows: total height
    """
    if height < 1:
        raise "rows must be at least 1"
    width = (height * 2) - 1
    margin = round(width / 2) - 1
    row_counter = 0

    # Build one row at a time.
    while row_counter < height:
        col_counter = 0
        row = ""
        margin_counter = margin
        equal_sign_count = width - 2 * margin_counter

        #  Build a row one column at a time.
        while col_counter < width:
            if margin_counter > 0:
                margin_counter = margin_counter - 1
                row = row + "-"
            elif equal_sign_count > 0:
                row = row + "="
                equal_sign_count = equal_sign_count - 1
            else:
                row = row + "-"
            col_counter = col_counter + 1
        print(row)
        row_counter = row_counter + 1
        margin = round(width / 2) - row_counter - 1



##   number of rows is input on the command line.
if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, type=int, help="Number of rows")
    args = parser.parse_args()
    print_pyramid(args.rows)
