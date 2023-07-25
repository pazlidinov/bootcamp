# k=int(input('k..'))
# n=int(input('n..'))

# for i in range(n):
#     print(k)
#     print('>>')
#     if i%5==0:
#         print(i)
# print(5)


# a=int(input('a...'))
# b=int(input('b...'))
# for i in range(a, b+1):
#     print(i)
# print('soni..',b+1-a)


# 11
# n=int(input('n...'))
# s=0
# for i in range(n, 2*n+1):
#     s+=i**2
# print('javob:',s)

# a=0
# a+=1  #a=a+1
# a-=1   #a=a-1
# a*=2   #a=a*2
# a/=2   #a=a/2
# a//=2   #a=a//2
# a%=2   #a=a%2
# a**=2   #a=a**2

# print(a)



# 13
# n=int(input('n..'))
# s=0
# j=1.1
# for i in range(n):
#     s+=j*(-1)**i
#     j+=0.1
# print(s)


# n=int(input('n..'))
# s=0
# for i in range(1, n+1):
#     s+=2*i-1
# print(s)


# a=[]
# for i in range(5):
#     a.append(int(input()))
# print(a)

# task 1 
# userdan n sonini qabul qiling 0 dan n gacha bo'lgan sonlarni 1 qatorda orasida probellar bilan chiqaring
# agar son toq bolsa undan keyin  1 ta probel juft bolsa 2 ta probel bilan chiqadi
# input : 5
# output : 1 2  3 4  5
# n= int(input('n...'))
# print("".join([str(x) + "  " if x % 2 == 0 else str(x) + " " for x in range(1 ,n+1)]))
# s=''
# for i in range(1, n+1):
#     if i%2==0:
#         s+=str(i)+'  '
#     else:
#         s+=str(i)+' '
# print(s)

# n = int(input("n"))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(str(i) + "  " , end="")
#     else:
#         print(str(i) + " " , end="")
        
# task 2 
# 0 dan user kiritgan songacha bolgan barcha 7 raqami aralashgan sonlarni ekranga chiqaring 
# input : 20
# output : 7 17 

# n=int(input('n>>>'))

# for i in range(n):
#     if '7' in str(i):
#         print(i)

# '5' in [6,7,9,5]
# '5' in '1318'



# [4,65,23,89,7]
# [4,65,23,89,0]

# task 3 
# arr = [1,4,5,6,8,7,9,9,2,45,3,2,1,5,87,9,6,4,5,65,4,8,89,545] # 3
# massivda necha marta 5 soni ishtirok etganini toping
# ox ahmedov


# print([1,4,5,6,8,7,9,9,2,45,3,2,1,5,87,9,6,4,5,65,4,8,89,545].count(5))

# n=[1,2,3,5,5,2,25,2,22]
# s=0
# for i in range(len(n)):
#     if n[i]%5==0:
#         s+=1
# print(s)



# len([i for i in [1,23,5,25,3] if i%5==0])




# input: 2 6

a=int(input('a..'))
b=int(input('b..'))
s=0
for i in range(a,b+1):
    s+=1
    for j in range(s):
        print(i)

























