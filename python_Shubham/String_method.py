#day6-string method

# print(dir(str))

#string methods
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

#how to find use of any method.

# s1 = "python"
# print(help(s1.isalnum))  #to check use of methods details information.
#
# s1 = "python"
# print(help(s1.isupper))


# s1 = "python"
# print(s1.isalnum())   #True


#
# txt="this is the python programming"
# x = txt.find("h",4,10) # it is find what is index of given letter.
# print(x)   #9

#find
# txt = "one two one is number, in one two digit"
# x = txt.replace('one','three')
# y = txt.replace('one','three',1)
# print(x)  #three two three is number, in three two digit
# print(y)  #three two one is number, in one two digit


