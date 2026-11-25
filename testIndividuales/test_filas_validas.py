import pytest
from src.filasValidas import filasValidas
import casosTest.casosTestSudoku as casosTest

@pytest.mark.filas_validas
@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto, True),
        (casosTest.incorrect, False),
        (casosTest.incorrect2, True),
        (casosTest.incorrect3, False),
        (casosTest.incorrect4, False),
        (casosTest.incorrect5, False),
        (casosTest.sudoku_booleanos, False),
        (casosTest.sudoku_fuera_de_rango, False),
        (casosTest.sudoku_valido_9x9, True),
    ],
)
def test_check_filas(sudoku, sano):
    assert filasValidas(sudoku) == sano