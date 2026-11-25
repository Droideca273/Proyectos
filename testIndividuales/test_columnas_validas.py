import pytest
from src.columnasValidas import columnasValidas
import casosTest.casosTestSudoku as casosTest


@pytest.mark.columnas_validas
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
        (casosTest.sudoku_valido_9x9, True),
    ],
)
def test_check_columnas(sudoku, sano):
    assert columnasValidas(sudoku) == sano