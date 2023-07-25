# set
# print(type(a))
# print(a)
# for i in a:
#     print(i)



# a.add(44)
# a.add(334)
# print(a)

# d={55,66,77,1}
# a.update(d)
# print(a)
# a.update(88)
# print(a)




# a={'ss',334,'ddd',7878,1}
# print(a)
# a.remove(0)
# a.discard(0)
# a.pop()
# a.clear()
# del a
# print(a)


# a={55,66,88,77}
# b={44,55,66,99}
# c=a.union(b)
# a.intersection_update(b)
# c=a.intersection(b)
# print(c)


# task1
# string qiymatlardan iborat tuple hosilqilinadi va har bir elementni oxirgi belgisini chiqaring
# input: ('abc','def')
# output: c, f

# task 2
# musbat va manfiy sonlardan iborat set hosil qilinsin va har bir qiymatni musbatga aylantirib ekranga chiqarilsin

# a={2,-7,8,-10}
# for i in a:
#     print(abs(i), end=" ")
    
# task 3
# sonlardan iborat tuple hosil qilinsin, tupleda bir xil qiymatlar mavjud va tartibsiz holda, bu qiymatlarni bir xillarini tashlab va tartiblangan holda chiqaring.
# input: (9,9,8,56,23,23)
# output: 8,9,23,56

# a=(9,9,8,56,23,23)
# b=set(a)
# c=list(b)
# c.sort()
# print(c)



# task 4
# tuple hosil qiling, unda bir xillari mavjud bo'lgan son va so'zlardan iborat, sonlarni alohida so'zlarni alohida ajratib oling, o'zshash qiymatlar olinmasin
# input: (5,'a','b',4,'b',5)
# output: 5,4
#         a,b 


# a=(5,'a','b',4,'b',5)
# a=set(a)
# b=[]
# d=[]
# for i in a:
#     if type(i)==int:
#         b.append(i)
#     else:
#         d.append(i)
# print(b,d)

