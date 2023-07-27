# lambda arg:expression
# x=lambda a:a+10
# print(x(5))

# d=lambda a,b:a+b
# print(d(5,20))
# print(d(6,2))
# print(d(5,10))
# print(d(9,1))
# print(d(5,20))


# def myfunc(n):
#     return lambda x: x**n

# fun1=myfunc(3) #lambda x:x**3

# print(fun1(2))

# def func():
#     pass 
# x = lambda x: x ** 2  

# map() , filter() , zip() 
# map - siz korsatgan function ni ketma-ketlikdagi elementlarni har biriga qollaydi va alohida ketma-ketlik tarzida qaytaradi

# def pow_num(x):
#     return x ** 2
# m = map(pow_num,[1,2,3,4,5])
# print(m) # print<map object at 0x0000006B69A328E0>
# print(list(m)) # [1, 4, 9, 16, 25]

# print(list(map(lambda x:x**2,[1,2,3,4,5]))) # [1, 4, 9, 16, 25]

# filter - siz korsatgan ketma-ketlikdagi elementlarni siz korsatgan shartlar boyicha filterlab alohida ketma-ketlik qilib qaytaradi 
# arr = [1,21,3,4,5,69,87,5,23,17,3,60,6,4,11,2,3,5,10]
# res = []
# for i in arr:
#     if i > 20:
#         res.append(i)
# print(res) # [21, 69, 87, 23, 60]
# def filter_twenty(x):
#     if x > 20:
#         return x
    
# f = filter(filter_twenty, arr)
# print(f) # <filter object at 0x000000AC5E063C70>
# print(list(f)) # [21, 69, 87, 23, 60]
# print(list(filter(lambda x: x > 20,arr))) # [21, 69, 87, 23, 60]

# zip - siz korsatgan kemta-ketliklardan har biridan bittadan elementlarni olib alohida tuple hosil qilib qaytaradi 

# abc = "abcdef"
# nums = [1,2,3,4,5,6]
# z = zip(abc,nums)
# print(z) # <zip object at 0x0000008A61A5D200>
# print(list(z)) # [('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5), ('f', 6)]

# d = {}
# for k,v in zip(abc,nums):
#     d.update({k:v})
# print(d) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# print({k:v for k,v in zip(abc,nums)}) # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

# l = lambda x: "harf" if type(x) == str else "son"
# print(l(10)) # son
# print(l("xarip")) # harf


# task 1
# test_str = "afds32f65sdf4sd6f54s68fsd"
# test_str da  harflarni alohida massivga va sonlarni alohida massivga yozuvchi filter function yozing


# decorator - biror bir functionni ishiga ozgartirish kirituvchi yoki u ishga tushishidan avval biror bir ishni qilib beruvchi function ga aytiladi  
#  decorator - oddiy founksiyalarni o'zgartiruvchi funksiya
# password = "1234"
# username = input("Usernamer \n")
# user_password = input("Password \n")

# def is_authenticated(func):
#     if user_password == password:
#         return func
#     else:
#         return lambda :"Authorization fail !"    
    
# @is_authenticated
# def login():    
#     return f"Welcome back ! {username}"

# @is_authenticated
# def contact():
#     print("Welcome to contact page !")

# print(login())

# recursion  - funksiya ozini ozi chaqirganida  

# def recursion(x):
#     x -= 1
#     print(x)
#     if x <= 0:
#         print("The end !")
#     else:
#         recursion(x)

# # recursion(100) # RecursionError
# recursion(10)
# def fak(n):
#     if n<=1:
#         return n
#     else:
#         return n*fak(n-1)
    
# print(fak(10))
















# def kv(a,b):
#     if b==0:
#         return 1
#     elif b==1:
#         return a
#     else:
#         return a*kv(a,b-1)

# print(kv(2,3))

p=int(input('padez>>'))
q=int(input('qavat>>'))
s=int(input('kv soni>>'))

n=int(input('kvartira>>'))

for i in range(p):
    for j in range(q):
        for k in range(1,s+1):
            if (i*q*s)+j*s+k==n:
                print(f'{i+1} padez {j+1} qavat {k}-xonadon')
                









