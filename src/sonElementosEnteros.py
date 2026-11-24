def sonElementosEnteros(sudoku):
    assert isinstance(sudoku, list)
    for fila in sudoku:
        for columna in fila:
            if type(columna) != int:
                return False
    return True
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
            print(attr, " => ", sonElementosEnteros(casosTest.__dict__[attr]))
            # mismo codigo que getattr(module, attr)
            # es necesario añadir el espacio de nombres del modulo:
            # casosTestSudoku.irregular