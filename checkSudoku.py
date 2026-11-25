
from src.columnasValidas import columnasValidas
from src.esMatrizCuadrada import esMatrizCuadrada
from src.filasValidas import filasValidas
from src.sonElementosEnteros import sonElementosEnteros


def checkSudoku(sudoku):
    assert isinstance(sudoku, list)
    return (
        esMatrizCuadrada(sudoku)
        and sonElementosEnteros(sudoku)
        and filasValidas(sudoku)
        and columnasValidas(sudoku)
    )
### CASOS TEST ###

if __name__ == "__main__":

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        else:
            print(attr, " => ", checkSudoku(casosTest.__dict__[attr]))