# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
#

if __name__ == '__main__':
    # \n 换行
    # 一个\t占四个制表位，\t前如果不是新的制表位则会在已站制表位字符后填充空格至满四格
    # \r 是回车，会清掉前面所占一行的字符
    # \b 是回退一格，删掉上一格的字符
    # \ 在输出时会默认为转义字符 \\时会去掉一个\
    # print('a\na\ta\ra\ba\\\\a\'a\"aaaa')

    # 原字符，不希望字符串中的转义字符起作用，就使用原字符，就是在字符串之前加上r或R，但要注意字符串尾部不能是单个\为结尾
    # print(r'a\na')

    # 输出文本文件到目录xxx  ， a+
    # fp=open('D:/pySoft/text.txt','a+')
    # print('a1',file=fp)
    # fp.close()

    # chr： 解析二进制数字转为汉字，0b：指出后方是二进制数字,0o：表示八进制，0x：表示十六进制
    # ord：解析汉字转为十进制数字
    # print(chr(0b100111001011000))
    # print(ord('乘'))

    # 变量中包含 ：id：是地址，type：类型，value：值
    # name = 'Joey'
    # print(name)
    # print('id',id(name))
    # print('类型',type(name))

    # 多个值陆续指向同一个地址则会修改该地址的值
    # name = 'Joey'
    # print(name)
    # print('id',id(name))
    # name = 'Joey1'
    # print(name)
    # print('id',id(name))

    # 浮点数运算因二进制底层问题导致不精确，故引入decimal
    # from decimal import Decimal
    # print(Decimal('1.1')+Decimal('2.2'))

    # 布尔类型 True = 1.False = 0
    # 字符串类型 单引号、双引号、三引号（三引号可以换行）：""" aaa """ 或  ‘’‘ aaa '''
    # str()：可将其他类型转换成字符串类型、
    # int()：可转成int类型，但在截取浮点数时会省略掉小数部分，而且在截取字符串类型的小数时会报错
    # print(int("1.5"))
    # float()：可将其他类型转成float类型

    # 输入函数input()获取用户输入的值
    # print(int(input('加数1')) + int(input('加数2')))

    # 运算符 + 加、- 减、 * 乘、/ 除、// 整除、% 取模(取余运算)、** 幂运算、、、
    # print(2//3) 被除数如果小于除数则为0
    # print(2**3) 表示2的三次方
    # print(-9//-4) 负负得正
    # print(-9//4) 或 print(9//-4)  一正一负的整除公式，向下取整
    # print(9%-4)  -3 公式 余数 = 被除数-除数*商   9-(-4)*(-3)   9-12 = -3
    # print(-9%4)   3                         -9-(4)*(-3)   -9+12 = 3
    # print(4%-9)  无论数值大小。只要是一正一负，取余的值跟随除数状态，除数为负则结果为负，否则反之

    # 链式解包赋值 &交换变量值(若是变量之间交换则是直接交换的地址)
    # a,b=10,20
    # print(a,b,id(a),id(b))
    # a,b = b,a
    # print(a,b,id(a),id(b))

    # 比较运算符: >,<,>=,<=,!=,== 比值,is 比id(地址), 相反是 is not
    # a=10
    # b=10
    # print(a == b,id(a),id(b))
    # print(a is b,id(a),id(b))

    # 逻辑运算符: and, or, not, in, not in
    # a = 'helloworld'
    # print('w' in a)
    # print('a' not in a)

    # 位运算符:  位与 &  对应数位都是1 结果数位才是1 否则为0, 位或 | 对应数位都是0 结果数位才是0 否则为1 , 左移位运算符 << 高位溢出舍弃 低位补0, 右移位运算符 >> 地位溢出舍弃 高位补0
    # print(330<<1)

    # 运算符优先级 (**  *,/,//,%  +-),(<<  >>,&,|),(>,<,<=,>=,==,!=),(and,or),(=)

    # 一下都为False
    # print(bool(False))#
    # print(bool(0))#
    # print(bool(0.0))#
    # print(bool(None))#
    # print(bool(''))#
    # print(bool(""))#
    # print(bool([]))# 空列表
    # print(bool(list()))# 空列表
    # print(bool(()))# 空元组
    # print(bool(tuple()))# 空元组
    # print(bool({}))# 空字典
    # print(bool(dict()))# 空字典
    # print(bool(set()))# 空集合

    # 条件表达式 支持链式表达
    # if 1 == 0:
    #     print(True)
    # elif 2 >= 1 >= 0 >= -1 >= -10:
    #     print(1)
    # else:
    #     print(False)

    # 省略式写法
    # print(1 if 1 > 0 else 0)

    # 省略结构 在没思路或没打算写的时候可以用pass占位
    # if 1 > 0:
    #     pass
    # else:
    #     pass

    # range(stop):0-stop数，stop为10 时 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 默认步长间隔1
    #  range(start,stop,step) step为步长
    # print(list(range(1, 10, 2)))

    # while 循环
    # a = 0
    # total = 0
    # while a <= 100:
    #     total += a if not (a % 2) else 0
    #     a += 1
    # print(total)

    # for-in 可是字符串 可是列表
    # for i in 'Python':
    #     print(i)

    # break: 可在for 或while 中使用结束循环， continue: 跳出当前循环
    # for i in range(0, 100, 2):
    #     if i == 60:
    #         continue
    #     if i > 50:
    #         break
    #     print(i)

    # else 可以和 for 和 while 搭配使用  在break生效后else会失效
    # for i in range(100):
    #     if i < 10:
    #         print(i)
    #         i += 1
    # else:
    #     print('a')

    # for i in range(1, 10):
    #     for j in range(1, i + 1):
    #         print(i, '*', j, '=', i * j, end='\t')
    #     print()

    # list 列表 正向索引为0开始到列表结束，逆向索引为尾端-1开始到列表起始位置，任意数据类型可混存，可以存重复数据 且是可变序列
    lst1 = [1, 2, '3', True, 0.1, "Python"]
    lst2 = list({222, 444, 5555, 'tttt'})
    # print(id(lst1))
    # print(id(lst2))
    # print(lst1.index(1))
    # print(lst1[-1])

    # 如果查找的不存在则抛异常
    # print(lst1.index('hello'))

    # 可设置start，stop
    # print(lst1.index('Python', 3, 6))

    # 列表切片 无论是正索引还是负索引，都要从左开始往右结束截取
    # print(lst1[-4:-1:1])
    # print(lst1[1:3:1])
    # print(lst1[::])  # 参数均可省略 ，起始默认是0，结束默认是列表长N，步长默认是1

    # print(lst1[::-1])  #当步长是-1时则倒序输出列表
    # print(1 in lst1)
    # print(1 not in lst1)
    # lst1.append(4)  # 在列表尾部添加一个元素，假如用append 添加一个列表，则将这个列表作为一个元素添加到尾端
    # print(lst1)
    # lst1.extend(lst2)  # 该函数是将列表2中的每个元素无序添加到列表1中
    # print(lst1)
    # lst1.insert(1, 90)  # 在指定的位置上添加一个元素，原本索引位置会往后移
    # print(lst1)
    # lst1[1:] = lst2   # 切片无序覆盖起始位后方元素
    # lst1[:1] = lst2   # 切片无序覆盖结束索引前的元素并添加到起始所引位
    # print(lst1)
    # lst1.remove(2)  # 删除一个元素，重复元素只删除第一个，元素不存在则报ValueError
    # print(lst1)
    # lst1.pop(1)  # 根据索引移除元素，如果索引位置不存在则会抛异常，如果不指定参数将删除列表中的最后一个元素
    # lst3 = lst1[1:3]  # 切片删除，会产生一个新列表
    # lst1[1:3] = []  # 指定索引位置切片删除 用空列表替代
    # lst1.clear() # 清空所有列表
    # del lst1  # 直接删除列表 再次引用将报未定义参数
    # lst1[1:3] = [100, 200, 300, 400, 500]  # 替换指定位置的元素，并添加新元素，并将索引后移
    # lst1.sort(reverse=True)  # 地址不会修改，在原列表修改,True 是降序排序，False是升序排序，默认是False升序排序
    # lst4 = sorted(lst1, reverse=True)  # 将新建一个新的对象,True 是降序排序，False是升序排序

    # lst5 = [i*10 for i in range(1, 10)]  # 利用range和for-in 列表生成式
    # print(lst5)

    # 字典：Java中Map类似 key不可以重复 value可以重复，值都是无序的  ，且是可变序列
    # 字典中的key必须是不可变对象，字典可以动态伸缩，字典浪费内存较大，是利用空间换时间的数据结构
    # scores = {'张三': '666', '李四': 98, '李四': 22}  # 假如有多个key则会被后方的key覆盖
    # print(scores)
    # key可以是数字,也可以是布尔类型(当key中存在数字且和布尔类型转换值一样时，布尔类型会被转换成为数字，并且value会被覆盖)
    scores = {'张三': '666', '李四': 98, 1: 22, False: 'aaa', True: "aaa", 0: 1}
    # print(scores)
    # print(scores['张三'])  # 取值的一种方式 不常用，因为未找到key时会报错
    # print(scores.get('张三', 99))  # 常用取值（不会报错），右侧可输入默认值，未找到时可取默认值
    # print('张三' in scores)
    # print('张三' not in scores)
    # del scores['张三a']  # 删除指定的key-value 若不存在值则报KeyError
    # scores.clear()  # 清空字典的元素
    # print(scores)
    # scores['陈六'] = 90  # 新增或修改元素
    # scores.keys()  # 获取所有的key
    # scores.values()  # 获取所有的values
    # list(scores.keys())  # 可直接转成列表
    # items = scores.items()  # 获取所有的key,value对
    # print(items,type(items))  # 类型为元组
    # lst6 = list(items)
    # print(lst6,type(lst6))  # 转换之后的列表元素是由元组组成

    # 遍历字典
    # for i in scores:
    #     print(i,scores[i],scores.get(i))

    # keys = ['a', 'b', 'c']
    # values = [1, 2, 3]
    # scores1 = {k.upper(): v for k, v in zip(keys, values)}  # 字典生成式（打包两个列表为字典） k.upper()函数 可以为大写key
    # print(scores1)

    # 元组 为不可变序列 ，不可增删改  跟列表相似但是用小括号 ,也可混存不同类型元素
    # t0 = ()  # 空元组
    # t0 = tuple()  # 空元组
    # t1 = 1, 2, 23, 'qa'
    # t2 = (1, 2, 23, 'qa')
    # print(t1)
    # t3 = tuple((1, 2, 23, 'qa'))
    # t4 = (1,)  # 只包含一个元素的元组需要小括号和都好结构
    # t5 = (1, [33, 44], 2)
    # t5[1].append(22)  # 元组不可休

    # set集合 无序的、不重复的、
    s = {1, 2, 3, 4, 5, 65, 7}
    print(s)
    s1 = set('1')
    s2 = set((1, 2, 3, 4, 5, 6))
    s3 = set({1, 2, 3, 4, 5, 6})
    s4 = set([1, 2, 3, 4, 5, 6])
    s5 = {}
    s6 = set()
    print(s1)
    print(s2)
    print(s3)
    print(s4)















