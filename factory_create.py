# 制造函数算子
import json
# -----------------一元操作数-----------------------------
relation_lis_1 = [] 


# 求和
relation_lis_1.append(r'\sum ')

# -------------二元操作数-------------------------------
relation_lis_2 = []

# 加
relation_lis_2.append('+ ')
# 减
relation_lis_2.append('- ')
# 数乘
relation_lis_2.append(r'\times ')
# # 除
# relation_lis.append('\frac{}{}')


relations = {0:relation_lis_1, 1:relation_lis_2}

# relations = {1:relation_lis_2}
with open('factorys.json', 'w',  encoding = 'utf-8') as f:
    json.dump(relations, f)