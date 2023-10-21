# 作業: 找出串列中的最大值和最小值

# 給定一個數字串列
numbers = [56, 23, 78, 12, 90, 33, 47]

# 初始化最大值和最小值為串列的第一個元素
max_value = numbers[0]
min_value = numbers[0]

# 使用 for 迴圈遍歷串列，找出最大值和最小值
for num in numbers:
    if num > max_value:
        max_value = num
    if num < min_value:
        min_value = num

print("串列中的最大值是: " + max_value)
print("串列中的最小值是: " + min_value)
