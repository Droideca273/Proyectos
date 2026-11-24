import sys

sys.path.append("..")

from src.esMatrizCuadrada import esMatrizCuadrada
from src.sonElementosEnteros import sonElementosEnteros
from src.filasValidas import filasValidas
from src.columnasValidas import columnasValidas

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
    import sys

    sys.path.append("..")

    import casosTest.casosTestSudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        # Scan namespace keys (or enumerate) del objeto modulo checkCuadrado
        # Asi podemos añadir todos los casos que queramos
        # en la unidad cassTestSudoku sin modificar este codigo
        if attr.startswith("__"):
            pass
            # Skip atributo
        else:
            print(attr, " => ", checkSudoku(casosTest.__dict__[attr]))
            # mismo codigo que getattr(module, attr)
            # es necesario añadir el espacio de nombres del modulo:
            # casosTestSudoku.irregular