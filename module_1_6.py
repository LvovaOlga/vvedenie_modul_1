my_dict={'Olga':1998, 'Oleg':2003, 'Vlad':2014}
print(my_dict)
print(my_dict['Olga'])
my_dict['Jerry']=2024
print(my_dict)
my_dict.update({'Alex':1977, 'Jess':1908})
print(my_dict)
print(my_dict.get('Olga'))
del my_dict['Olga']
print(my_dict)
a = my_dict.pop('Vlad')
print(a)
print(my_dict.items())

my_set={1,2.3,'hi',1,2.5,3}
print(my_set)
print(my_set.add(6))
print(my_set.add(7))
print(my_set.remove(1))
print(my_set)