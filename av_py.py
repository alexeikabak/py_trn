
In [6]: cyc = ['a', 'b', 'c']
In [7]: print(cyc)
['a', 'b', 'c']

In [8]: print(cyc[1])
b

In [9]: cyc.append('k')

In [10]: print(cyc)
['a', 'b', 'c', 'k']

In [11]: del cyc[2]

In [12]: print(cyc)
['a', 'b', 'k']

In [18]: cyc.remove('k')

In [19]: print(cyc)
['a', 'b']

In [20]: cars = ['porsche', 'audi', 'subaru' 'bmw', 'citroen']

In [21]: print(cars)
['porsche', 'audi', 'subaru', 'citroen']

In [22]: print(sorted(cars))
['audi', 'citroen', 'porsche', 'subaru']

In [23]: print('\nSortedList')

In [26]: spisok = ['odin', 'vtoroy', 'troi', 'cht']

In [27]: for spis in spisok:
    ...:     print(spis)
    ...:     exit()
    ...:
odin
vtoroy
troi
cht

In [6]: setup = 'a duck goes into a bar'

In [7]: setup.capitalize()
Out[7]: 'A duck goes into a bar'

In [8]: setup.title()
Out[8]: 'A Duck Goes Into A Bar'

In [12]: setup.upper()
Out[12]: 'A DUCK GOES INTO A BAR'

In [15]: list1 = ['coral', 'splash', 'axe', 'xia']

In [16]: list2 = ['sass', 'less']

In [17]: list1 += list2

In [18]: list1
Out[18]: ['coral', 'splash', 'axe', 'xia', 'sass', 'less']

In [19]: 'xia' in list1
Out[19]: True

In [21]: list1
Out[21]: ['coral', 'splash', 'axe', 'xia', 'sass', 'less']

In [22]: separator = ' * '

In [23]: joined = separator.join(list1)

In [24]: joined
Out[24]: 'coral * splash * axe * xia * sass * less'

In [25]: dell = "wysiwig"

In [26]: len(dell)
Out[26]: 7

In [27]: dell.count('i')
Out[27]: 2

In [28]: digi = [1,8,4,7,3,7,2,0]

In [29]: min(digi)
Out[29]: 0

In [30]: max(digi)
Out[30]: 8

In [31]: sum(digi)
Out[31]: 32

In [32]: print(sorted(digi))
[0, 1, 2, 3, 4, 7, 7, 8]

In [33]: print("Aloha, " + full.name.title() + "!")




























