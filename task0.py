t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    count_negative = a.count(-1)
    count_zero = a.count(0)
    
    count = count_zero + 2 * count_negative
    if count_negative % 2 == 1 and count_zero == 0:
        count += 1
        
    print(count)
