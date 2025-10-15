#task1

num = int(input("Enter the number of operations: "))

for _ in range(num):
    x = int(input("Enter the x: "))
    n = int(input("Enter the n: "))
    
    arr = []
    for i in range(n):
        if i % 2 == 0:
            arr.append(x)
            
        else:
            arr.append(-x)
            
    print(sum(arr))
