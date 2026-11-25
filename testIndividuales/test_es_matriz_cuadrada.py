import pytest
from src.esMatrizCuadrada import esMatrizCuadrada
import casosTest.casosTestSudoku as casosTest


@pytest.mark.es_cuadrado
@pytest.mark.parametrize(
    "sudoku, sano",
    [
        (casosTest.correcto, True),
        (casosTest.incorrect, True),
        (casosTest.incorrect2, True),
        (casosTest.incorrect3, True),
        (casosTest.incorrect4, True),
        (casosTest.incorrect5, True),
        (casosTest.sudoku_booleanos, True),
        (casosTest.sudoku_fuera_de_rango, True),
        (casosTest.sudoku_valido_9x9, True),
        ],
)
def test_check_cuadrado(sudoku, sano):
    assert esMatrizCuadrada(sudoku) == sano