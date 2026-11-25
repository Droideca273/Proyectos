from src.checkSudoku import checkSudoku
import casosTest.casosTestSudoku as casosTest

for attr in sorted(casosTest.__dict__):
    if attr.startswith('__'):
        pass
    else:
        print(attr, " => ", checkSudoku(casosTest.__dict__[attr]))