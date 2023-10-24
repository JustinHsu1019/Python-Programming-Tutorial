# 作業: 猜數字遊戲

# import 和 random 非學生已知範圍，要先把這兩行程式碼給學生，並稍加解釋
import random
secret_number = random.randint(1, 100)

print("歡迎來到猜數字遊戲!")
print("我已經選擇了一個 1 到 100 之間的數字。")

guess = 0
while guess != secret_number:
    guess = int(input("請猜一個數字: "))
    
    if guess < secret_number:
        print("太小了!")
    elif guess > secret_number:
        print("太大了!")
    else:
        print("恭喜你猜對了!")
