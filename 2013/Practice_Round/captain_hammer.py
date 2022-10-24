from math import pi, asin

t = int(input())

for i in range(t):
    data = input().split()
    v = data[0]
    d = data[1]
    res = 90*asin(9.8*int(d)/(int(v)*v))/pi
    print(f"Case # {i+1}: {res:.7f}")