# 生成公式数据集
from utils import *


if __name__=='__main__':
    num_operation = 3
    n_samples = 1000
    symbols = Symbols('./symbols.json')
    operations = Operation('./factorys.json')
    fomula = Formula(operation=operations, symbol=symbols)
    with open('train.txt', 'w') as f:
        for i in range(n_samples):
            result = fomula.create(num_operation)
            f.write(result)
            f.write('\n')