### создать список из трёх любых элементов
print("\n--- создать список из трёх любых элементов ---")
lst1 = [i for i in range(3)]
lst1.sort()
print("содержимое первого списка: {}".format(lst1))

lst2 = []
lst2.append('fi2rst')
lst2.append('se3cond')
lst2.append('th1ird')
lst2.sort(key=lambda c2: c2[2])
print("содержимое второго списка с сортировкой по 3му символу: {}".format(lst2))

### создать словарь из трёх пар ключ-значение
print("\n--- создать словарь из трёх пар ключ-значение ---")
dct1 = {1: "hello", 2: "world", 3: "!"}
print("содержимое словаря: {} {} {}".format(dct1[1], dct1[2], dct1[3]))

### создать множество из трёх элементов
print("\n--- создать множество из трёх элементов ---")
set1 = {1, 2, 3, 1}
print("множество (отсутствуют дубли): {}".format(set1))

### из списка получить элемент с индексом 1
print("\n--- из списка получить элемент с индексом 1 ---")
print("элемент с индексом 1 из списка lst2: {}".format(lst2[1]))

### написать условие if с двумя блоками elif и блоком else
print("\n--- написать условие if с двумя блоками elif и блоком else ---")
if lst2[1][2].isnumeric():
    k = int(lst2[1][2])
else:
    print("it is not numeric")
    k = None

if k == 1:
    str1 = "one"
elif k == 2:
    str1 = "two"
elif k == 3:
    str1 = "three"
else:
    str1 = None

print("нашли символ '{}'".format(str1))

### написать цикл while
print("\n--- написать цикл while ---")
lst3 = [1, 2, 5, "привет"]
i = 0
while i < len(lst3):
    print(lst3[i])
    i += 1
### создать список из трёх элементов и распечатать его элементы с помощью цикла for
print("\n--- создать список из трёх элементов и распечатать его элементы с помощью цикла for ---")
for l in lst3:
    print(l)

### распечатать числа от 0 до 5
print("\n--- распечатать числа от 0 до 6 ---")
for i in range(6):
    print(i)

### создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass'
print("\n--- создать строку 'TEST', если в ней есть буква 'E', напечатать 'pass' ---")
s = 'TEST'
if s.find('E'):
    print("pass")