#password generator
import random
symbols=['@','!','#','$','%','&']
num=['1','2','3','4','5','6','7','8','9','0']
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
password=[]
print("welcome to password generator")
s=int(input("how many symbols u want"))
n=int(input("how many numbers u want"))
a=int(input("how many alphabets u want"))
for i in range(s):
    password+=random.choice(symbols)
for i in range(n):
    password+=random.choice(num)
for i in range(a):
    password+=random.choice(alpha)
random.shuffle(password)
ur_password=""
for char in password:
    ur_password+=char
print(ur_password)





