
from src.areColumsValid import areColumnsValid
from src.isSquareMatrix import isSquareMatrix
from src.areRowsValid import areRowsValid
from src.areElementsIntegers import areElementsIntegers


def checkSudoku(sudoku):
    assert isinstance(sudoku, list)
    return (
        isSquareMatrix(sudoku)
        and areElementsIntegers(sudoku)
        and areRowsValid(sudoku)
        and areColumnsValid(sudoku)
    )
### CASOS TEST ###

if __name__ == "__main__":

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        else:
            print(attr, " => ", checkSudoku(casosTest.__dict__[attr]))