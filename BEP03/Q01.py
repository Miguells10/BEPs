from ftplib import print_line


class Q01:
   ''' 1.
    Considere as variáveis
    x = 10, y = 5 e z = 10.
    Determine se as seguintes expressões
    são Verdadeiras  ou Falsas:
    a) x > y
    b) x <= z
    c) y == x
    d) x != z
    e) (x + y) > (z * 2)'''

   x = 10
   y = 5
   z = 10

   print("a) x > y")
   if (x>y):
       print_line("X é maior")
   else: print("y é maior")

   print("b) x <= z")
   if x<=z:
       print_line("true")
   else:print("false")

   print("c) y == x")
   if y==x:
       print_line("true")
   else:print("false")

   print("d) x != z")
   if x!=z:
       print_line("true")
   else:print("false")

   print("(x + y) > (z * 2)")
   if (x + y) > (z * 2):
       print_line("true")
   else:print("false")

