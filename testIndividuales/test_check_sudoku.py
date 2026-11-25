import pytest
from src.checkSudoku import checkSudoku
import casosTest.casosTestSudoku as casosTest


@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto, True),
        (casosTest.incorrect, False),
        (casosTest.incorrect2, False),
        (casosTest.incorrect3, False),
        (casosTest.incorrect4, False),
        (casosTest.incorrect5, False),
        (casosTest.sudoku_booleanos, False),
        (casosTest.sudoku_fuera_de_rango, False),
        (casosTest.sudoku_valido_9x9, False),
    ],
)
def test_check_sudoku(sudoku, sano):
    assert checkSudoku(sudoku) == sano