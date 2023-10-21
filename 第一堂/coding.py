# 實作Code

# 1. 基本輸入輸出
name = input("請輸入你的名字: ")
print("你好,", name + "!")

# 2. 基本數學運算
num1 = int(input("請輸入第一個數字: "))
num2 = int(input("請輸入第二個數字: "))

print("兩數之和是:", num1 + num2)
print("兩數之差是:", num1 - num2)
print("兩數之積是:", num1 * num2)
print("兩數之商是:", num1 / num2)
print("兩數相除的餘數是:", num1 % num2)

# 3. 基本字串處理
str1 = input("請輸入第一段文字: ")
str2 = input("請輸入第二段文字: ")

print("字串合併:", str1 + str2)
print("字串反轉:", str1[::-1])
print("轉換為大寫:", str1.upper())
print("轉換為小寫:", str1.lower())
print("字串長度:", len(str1))

# 4. 條件判斷
if '1' == '1':
    print("1")
elif '2' != '2':
    print("2")
else:
    print("3")

# 5. 兩數比大小
if num1 > num2:
    print(num1, "是較大的數字")
elif num1 < num2:
    print(num2, "是較大的數字")
else:
    print("兩個數字相等")
