n = int(input())
s = n % 60
m = (n % 3600) // 60
h = n // 3600

print(f"{h}:{m}:{s}")