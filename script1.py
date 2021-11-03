"""
первый скрипт
"""
n = 10
a = 0
b = 1
f = [a]
for i in range(n):
    temp = a
    a = b
    b += temp
    f.append(a)
print("fi number for {} is {}".format(n, a))

