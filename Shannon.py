import math
from decimal import *

# 设置decimal精度
getcontext().prec = 6

# 信源数据类
class num_data():
    def __init__(self, n, p):
        self.n = n
        self.p = p

# 手动输入数据
def input_num():
    n = int(input('请输入信源符号的个数:'))
    p = []
    for i in range(1, n + 1):
        c = input('请输入第' + str(i) + '个信源符号的概率:')
        p.append(float(c))
    return num_data(n, p)

# 测试用数据1
def insert_num1():
    n = 4
    p = [0.1, 0.2, 0.3, 0.4]
    return num_data(n, p)

# 测试用数据2
def insert_num2():
    n = 12
    p = [0.243807, 0.159758, 0.106511, 0.085204, 0.053253, 0.053253, 0.053253, 0.053253,  0.053253, 0.053253,  0.042602,  0.042602]
    return num_data(n, p)

# 降序排序
def sort_num(p):
    p.sort(reverse=True)
    return p

# 计算累加概率
def sum_num(n, p):
    p_sum =[]
    for i in range(n):
        if i == 0:
            p_sum.append(0)
        else:
            p_sum.append(Decimal(p_sum[i - 1]) + Decimal(p[i - 1]))
    msg = '累加概率：'
    for i in p_sum:
        msg = msg + '  ' + str('{:g}'.format(float(i)))
    print(msg)
    return p_sum

# 编码
def coding(n, p, p_len):
    code={}
    for i in range(n):
        code[str(p[i])] = '0.'
        b = p[i]
        for j in range(p_len[i]):
            b = b * 2
            if b > 1:
                code[str(p[i])] = code[str(p[i])] + str(1)
                b = b - 1
            else:
                code[str(p[i])] = code[str(p[i])] + str(0)
    for each in code:
        code[each] = code[each][2:]
    
    list = sorted(code.items(), key = lambda d:d[0])
    num_code = []
    for key,value in list:
        num_code.append(value)
    return num_code

# 优化算法（for循环非常多，待优化）
def improve_a(num_code, n):
    e = []
    for i in range(len(num_code)):
        d = []
        for j in range(len(num_code)):
            if i != j:
                flag = 0
                c = [len(num_code[i]), len(num_code[j])]
                for k in range(1, min(c) + 1):
                    if str(num_code[i][k-1:k]) != str(num_code[j][k-1:k]):
                        d.append(k)
                        flag = 1
                        break
                if flag == 0:
                    print('0')
                    d.append(min(c) + 1)
        e.append(max(d))
    return e

# 优化完的编码
def order_a(e, num_code, n):
    for i in range(n):
        num_code[i] = num_code[i][:e[i]]
    return num_code

# 改进算法
def improve_b(num_code_a):
    num_code_b = sorted(num_code_a, key = lambda i:len(i), reverse = False)
    return num_code_b

# 求平均码长
def get_length(n, num_code, p):
    m = []
    a = 0
    for i in range(n):
        m.append(len(num_code[i]))
        a = a + len(num_code[i]) * float(p[i])
    print('码字长度：' + str(m))
    return a

# 主函数
def main():
    sym = int(input('请进行您的选择:\n    1.使用手动输入数字\n    2.使用内置测试数据[0.1, 0.2, 0.3, 0.4]\n    3.使用内置测试数据[0.243807, 0.159758, 0.106511, 0.085204, 0.053253, 0.053253, 0.053253, 0.053253,  0.053253, 0.053253,  0.042602,  0.042602]\n'))
    if sym == 1:
        input_temp = input_num()
        n = input_temp.n
        p = sort_num(input_temp.p)
    elif sym == 2:
        input_temp = insert_num1()
        n = input_temp.n
        p = sort_num(input_temp.p)
    elif sym == 3:
        input_temp = insert_num2()
        n = input_temp.n
        p = sort_num(input_temp.p)
    else:
        return

    print('信源符号概率：'+ str(p))
    p_sum = sum_num(n, p)
    b = 0
    p_len = []
    for i in range(n):
        p_len.append(int(math.log(p[i], 2) * (-1) + 0.9999))
        b = b + (-1) * p[i] * (math.log(p[i], 2))
    print('信源熵：' + '%.5s' % str(b))

    num_code = coding(n, p_sum, p_len)
    print('\n采用香农编码后：')
    print(num_code)
    a0 = get_length(n, num_code, p)
    print('平均码长：' + '%.5s' % str(a0 / n))
    print('平均信息传输率:' + '%.5s' % str(b / a0))

    e = improve_a(num_code, n)
    num_code_a = order_a(e, num_code, n)
    print('\n采用优化算法后：')
    print(num_code_a)
    a1 = get_length(n, num_code_a, p)
    print('平均码长：' + '%.5s' % str(a1 / n))
    print('平均信息传输率:' + '%.5s' % str(b / a1))

    num_code_b = improve_b(num_code_a)
    print('\n采用改进算法后：')
    print(num_code_b)
    a2 = get_length(n, num_code_b, p)
    print('平均码长：' + '%.5s' % str(a2 / n))
    print('平均信息传输率:' + '%.5s' % str(b / a2))

# 该运行啦
if __name__ == '__main__':
    main()