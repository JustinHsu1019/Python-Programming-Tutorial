# 實作Code

# Python 入門 - 第二堂課

# 課前小考
score = int(input("請輸入您的分數："))

if 90 <= score <= 100:
    print("優秀")
elif 80 <= score <= 89:
    print("良好")
elif 70 <= score <= 79:
    print("一般")
elif 60 <= score <= 69:
    print("及格")
elif 0 <= score <= 59:
    print("不及格")
else:
    print("無效的分數")

# 1. 介紹串列
fruits = ["apple", "banana", "cherry", "date"]
print("水果串列:", fruits)
print("串列的第一個元素:", fruits[0])

# 添加元素到串列
fruits.append("grape")
print("添加後的串列:", fruits)

# 刪除串列中的元素
fruits.remove("date")
print("刪除後的串列:", fruits)

# 修改串列中的元素
fruits[1] = "blueberry"
print("修改後的串列:", fruits)

# 獲得串列長度
fruits_length = len(fruits)
print("水果串列的長度是:", fruits_length)

# 2. for 迴圈
print("\n使用 for 迴圈列印水果:")
for fruit in fruits:
    print(fruit)

# 使用 range() 函數與 for 迴圈
print("\n使用 range() 函數與 for 迴圈列印數字:")
for i in range(5):
    print(i)

# 3. while 迴圈
print("\n使用 while 迴圈列印水果:")
index = 0
while index < len(fruits):
    print(fruits[index])
    index += 1

# 4. 串列切片
print("\n使用切片取得串列的部分元素:")
print(fruits[1:3])

# 5. 串列中的數字加總
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = 0
index = 0
while index < len(numbers):
    sum_of_numbers += numbers[index]
    index += 1
print("\n串列中的數字加總是:", sum_of_numbers)

# 6. 串列推導式
print("\n使用串列推導式生成新串列:")
squared_numbers = [x**2 for x in numbers]
print("原始數字串列:", numbers)
print("平方後的數字串列:", squared_numbers)

# 7. 串列排序
print("\n使用內建函數對串列進行排序:")
numbers.sort()
print("排序後的數字串列:", numbers)
