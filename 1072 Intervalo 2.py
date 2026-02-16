n = int(input())
dento = 0
out = 0

for i in range(n):
    x = int(input())
    if x >= 10 and x <= 20:
        dento += 1
    else:
        out += 1
        
print(f"{dento} in")
print(f"{out} out")
