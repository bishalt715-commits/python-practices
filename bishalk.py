# creating a basic function to check the number is armstrong number or not
def bishal(num):
    a = num
    total = 0
    hero = (len(str(num)))

    while a > 0:
        bt = a % 10
        total = (bt ** hero) + total
        a = a // 10

    return total == num


num = int(input("Enter a number: "))
print(bishal(num))
