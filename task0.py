t = int(input())
for _ in range(t):
    n = int(input())
    
    a = list(map(int, input().split()))
    
    count_negative = a.count(-1)
    count_zero = a.count(0)
    
    min_operations = count_zero
    
    if count_negative % 2 != 0:
        min_operations += 2
        
    print(min_operations)
