multipl = 1
for i in list(range(1,11)):
    if i % 2 == 2:
        continue
    multipl += i
else:
    print(multipl)
