immutable_var= 1,[2,3],'pen', True
print(immutable_var)
immutable_var[1][0]=5
print(immutable_var)
immutable_var= (1,[2,3],'pen', True) +(7,8)
print(immutable_var)
immutable_var= ((1,[2,3],'pen', True) +(7,8))*3
print(immutable_var)

mutable_list=[1,'pen',True]
print(mutable_list)
mutable_list[0]='pencil'
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
mutable_list.extend('baby')
print(mutable_list)
mutable_list.extend(['baby',2])
print(mutable_list)
mutable_list.remove('pen')
print(mutable_list)
