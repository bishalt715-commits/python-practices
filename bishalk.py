def bishal(num):
    a = num
    results = 0

    while a > 0:
        bt = a % 10
        results = (results * 10) + bt
        a = a // 10

    return num == results


num = int(input("Enter a number: "))
print(bishal(num))
