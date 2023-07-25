# data type :
#     int , float ,complex ,str,
#     byte , bytearray , None

# data structure: 
    # list , tuple , 
    # set , frozenset ,
    # dict , range 
    
# a = 1
# arr = [1,2,3] # list - array 
# list - tartibli elementlar toplami 
# tuple - tartibli o'zgarmas elementlar to'plami 
# set - unikal elementlar toplami # print(set("assa"))
# frozenset - unikal o'zgarmas  elementlar toplami
# dict - kalit orqali murojat qilinadigan element tolpami  
# range - sonlar oraligi 

# dict 
# d = dict(name="John", age=30)
# print(d) # {'name': 'John', 'age': 30}
# print(d["name"]) # John

# d = {"username":"chaplin","age":40, "skills":["python", "javascript"]}
# print(d)
# print(d.get("username")) # chaplin

# d["salary"] = 500
# country = {"country":"USA"}
# d.update(country)
# print(d)

# d = {"username":"chaplin","age":40, "skills":["python", "javascript"]}
# del d["username"]
# print(d) # {'age': 40, 'skills': ['python', 'javascript']}
 
# d["username"] = "goblin"
# print(d)

# d.pop("username") # siz korsatgan kalit boyicha elementni ochiradi
# print(d) # {'age': 40, 'skills': ['python', 'javascript']}
# d.popitem() # eng oxirgi elementni ochiradi
# print(d) # {'age': 40}

# print(d["country"]) # KeyError: 'country'
# print(d.get("country")) # None
# for elem in d.items():
#     print(elem) # tuple korinishida element olish

# for k in d.keys():
#     print(k) # faqat dict kalitlari olinadi 

# for v in d.values():
#     print(v) #faqat dict qiymatlari larini olish

# for i in d:
#     print(i) #faqat dict kalitlarini olish

# task 1 
# alpha = "abcdef"
# numbers = range(1,7)
# shu ikkala qiymatlardan foydalanib alohida dict hosil qiling 
# namuna : {"a":1, "b":2 .... }
# dict1={}
# for i in range(6):
#     dict1[alpha[i]]=numbers[i]
# dict1=dict.fromkeys(alpha,0)
# print(dict1)


# task 2 
# d = {"one":230,"two":120,"three":560,"four":410,"five":320}
# d lugatidan eng katta ikita elementni olib alohida lugat qilib yozing
# l=sorted(d.values())
# dict2={}
# for k in d.keys():
#     if l[-1]==d[k] or l[-2]==d[k]:
#         dict2[k]=d[k]
        
# print(dict2)
# task 3
d1={
    '5':5
}
print(d1)