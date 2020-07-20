from django.test import TestCase
import time

x = time.localtime()
print(x)
namsinh = 2019
a = x[0] - namsinh
print(a)

age =3
txt = 'tuoi {}'
print(txt.format(age))

abc = {'a':'b'}
# print(bool(abc))

abc['a']='c'
abc['them'] = 'test'
abc.pop('a')
print(abc)

i = 1
while i < 6:
  print(i)
  i += 1