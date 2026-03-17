def bishal(num):
    n = len(num)
    for i in range(n):
        min_idx = i
        for b in range(i+1, n):
            if num[b] < num[min_idx]:
                min_idx = b
        num[i], num[min_idx] = num[min_idx], num[i]
    return num


num = [98, 54, 34, 664, 353, 353]
print(bishal(num))
