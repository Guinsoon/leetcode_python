import re

# sentence = input()

pat = '\w+[\-]?'


a = re.findall(pat, "i am &**#@    a--student age is 20-yeas & @ oum")
print(a)