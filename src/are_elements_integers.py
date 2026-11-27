
def are_elements_integers(sudoku):
    assert isinstance(sudoku, list)
    for fila in sudoku:
        for columna in fila:
            if type(columna) != int:
                return False
    return True


### CASOS TEST ###

if __name__ == "__main__":
    import sys
    
    sys.path.append("../")
    
    import casosTest.casos_test_sudoku as casosTest

    for attr in sorted(casosTest.__dict__):
        if attr.startswith("__"):
            pass
        else:
            print(attr, " => ", are_elements_integers(casosTest.__dict__[attr]))
