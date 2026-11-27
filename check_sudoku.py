
from src.are_columns_valid import are_columns_valid
from src.are_elements_integers import are_elements_integers
from src.are_rows_valid import are_rows_valid
from src.is_square_matrix import is_square_matrix


def checkSudoku(sudoku):
    assert isinstance(sudoku, list)
    return (
        is_square_matrix(sudoku)
        and are_elements_integers(sudoku)
        and are_rows_valid(sudoku)
        and are_columns_valid(sudoku)
    )
### CASOS TEST ###

if __name__ == "__main__":
    import sys
        
    sys.path.append("../")

    import casosTest.casos_test_sudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        else:
            print(attr, " => ", checkSudoku(casosTest.__dict__[attr]))