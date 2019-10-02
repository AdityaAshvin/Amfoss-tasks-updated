def value():
 a = int(value())
 d = 0
 for k in range(1,a):
    row = vlaue().split()
    d = d+ (int(row[k]) - int(row[a-1-k]))
 print(abs(d))
