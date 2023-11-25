import json
# 创建一个 Python 对象实例
letter_lis = []

# # 将对象序列化为二进制字节流并保存到文件
# with open('example.pkl', 'wb') as f:
base_letter = ord('a')

# 保存基本字母
for i in range(26):
    letter_lis.append(chr(base_letter+i))

# 保存数字
base_num = ord('0')
for i in range(10):
    letter_lis.append(chr(base_letter+i))

# 保存希腊字母
#1. lambda
letter_lis.append([r'\lambda'])
letter_lis.append([r'\sigma '])
letter_lis.append([r'\alpha '])
letter_lis.append([r'\beta '])
letter_lis.append([r'\gamma '])
letter_lis.append([r'\epsilon '])

with open('symbols.json', 'w',  encoding = 'utf-8') as f:
    json.dump(letter_lis, f)

