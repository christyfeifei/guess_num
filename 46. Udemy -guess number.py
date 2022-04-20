import random
r = random.randint(1, 100)  # 自動生成一個數字(答案)

while True:
    num = input('請猜數字:')
    num = int(num)  # 不要忘記轉成整數
    if num == r:
        print('你答對了!')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
