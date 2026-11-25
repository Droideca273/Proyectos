import pytest
from src.sonElementosEnteros import sonElementosEnteros
import casosTest.casosTestSudoku as casosTest


@pytest.mark.numeros_validos
@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto, True),
        (casosTest.incorrect, True),
        (casosTest.incorrect2, True),
        (casosTest.incorrect3, True),
        (casosTest.incorrect4, False),
        (casosTest.incorrect5, False),
        (casosTest.sudoku_booleanos, False),
        (casosTest.sudoku_fuera_de_rango, True),
        (casosTest.sudoku_valido_9x9, True),
    ],
)
def test_check_numeros_validos(sudoku, sano):
    assert sonElementosEnteros(sudoku) == sano