t = int(input())
for _ in range(t):
    words = input().split()
    short_forms = words[0][0] + words[1][0] + words[2][0]
    print(short_forms.upper())
