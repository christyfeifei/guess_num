import random
start = input('請決定起始數字:')
end = input('請決定結束數字:')
start = int(start)
end = int(end)

r = random.randint(start, end)  # 自動生成一個數字(答案)
count = 0

while True:
    count += 1  # count = count + 1
    num = input('請猜數字:')
    num = int(num)  # 不要忘記轉成整數
    if num == r:
        print('你答對了!')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('這是你猜的第', count, '次')
