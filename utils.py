# 1. 选择单个字符，构建字典
# 构造字典集合，保存需要的字符到latex的转化
import json
import random
import time

# 使用系统时间作为种子
random.seed(time.time())

class Symbols(object):
    def __init__(self, file_path):
        self.symbols_lis = []
        self.file_path = file_path
        with open(self.file_path, 'r') as f:
            self.symbols_lis = json.load(f)
        self.len = len(self.symbols_lis)
    def choice(self):
        # 随机选择返回一个字母
        return "".join(random.choice(self.symbols_lis))
    def UpAndDowns(self):
        # 之后用于生成随机的上下标，扩充当前的symbols
        upp = self.choice()
        down = self.choice() 
        return upp, down
        

class Operation(object):
    def __init__(self, file_path):
        self.operation_lis = []
        self.file_path = file_path
        self.len = len(self.operation_lis)
        with open(self.file_path, 'r') as f:
            self.operation_lis = json.load(f)
    def choice(self):
        # 随机选择返回一个关系操作，同时要返回操作数的类型
        operation_list = self.operation_lis
        cls_opes = list(operation_list.keys())
        # 关系类型的数目
        num_cls_opes = len(list(operation_list.keys()))
        kind = cls_opes[random.choice(list(range(num_cls_opes)))]

        return random.choice(list(operation_list[kind])), kind

# 构造公式，这里是通过将所有的符号进行拼接得到，相当于拼接一个字符串。
class Formula(object):
    def __init__(self, operation, symbol):
        self.operation = operation
        self.symbol = symbol
    def create(self,  num_operations):
        # num_operations表示操作数的个数
        # 不同的公式块需要用{}来连接
        # 这里应该要进行递归生成公式
        # 这里需要通过判断当前的操作符需要几个操作数
        if num_operations==0:
            return "".join(self.symbol.choice())
        else:
            ope, kind = self.operation.choice()
            str_formula = ""
            # 一元操作数
            random_number = random.random()
            ratio = 0.1
            if kind =="0" and random_number<ratio:  # 设置一定的跳过比例
                # 如果为sum可能选择是否添加上下标
                if ope=='\sum ':
                    str_right = self.create(num_operations-1)
                    upper, down = self.symbol.UpAndDowns()
                    str_formula = "".join([ope, f'_{down}', f'^{upper}',str_right])
            # 二元操作数的情况
            elif kind == "1" or random_number>=ratio:
                str_left = self.create(num_operations-1)
                str_right = self.create(num_operations-1)
                # 拼接字符串
                # str_formula = '{'+str_left+ope+str_right+'}'
                str_formula = "".join([str_left,ope,str_right])
            return str_formula
            
    
