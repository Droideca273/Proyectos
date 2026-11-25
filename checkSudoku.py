
from src.columnasValidas import areColumnsValid
from src.esMatrizCuadrada import isSquareMatrix
from src.filasValidas import areRowsValid
from src.sonElementosEnteros import areElementsIntegers


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