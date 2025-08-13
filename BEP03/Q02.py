'''2. Usando as mesmas variáveis (x = 10, y = 5, z = 10), avalie as seguintes
expressões:
a) (x > y) E (z == x)
b) (y < x) OU (z != 10)
c) NÃO (x == z)
d) ((x * 2) > 20) E ((y - 1) == 4)'''

x = 10
y =5
z = 10

print("a) (x > y) E (z == x)")
if (x>y) & z ==x:
    print("true")
else: print("false")

print("b) (y < x) OU (z != 10)")
if (y<x) | (z != 10):
    print("true")
else: print("false")

print("c) NÃO (x == z)")
if not (x==z):
    print("true")
else: print("false")

print("d) ((x * 2) > 20) E ((y - 1) == 4)")
if ((x * 2) > 20) and ((y - 1) == 4):
    print("true")
else: print("false")