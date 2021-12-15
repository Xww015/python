number = int(input("请输入一个数以得到该数的简写序数(x∈+∞)："))
new_number = number % 100
number_list_1 = (1, 21, 31, 41, 51, 61, 71, 81, 91)
number_list_2 = (2, 22, 32, 42, 52, 62, 72, 82, 92)
number_list_3 = (3, 23, 33, 43, 53, 63, 73, 83, 93)


if number <= 0:
    print("输出错误!")
elif new_number in number_list_1:
    print(f"\n该数的简写序数为：{number}st")
elif new_number in number_list_2:
    print(f"\n该数的简写序数为：{number}nd")
elif new_number in number_list_3:
    print(f"\n该数的简写序数为：{number}rd")
else:
    print(f"\n该数的简写序数为：{number}th")
