size = int(input('Max = '))

sum = 0

for v in range(1 : size+1) :
    if v % 3 == 0 or v % 5 == 0 :
        sum += v
print(sum)
