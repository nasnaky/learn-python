a = True
if  a :
    print("집에")
print("가고")
print("싶다")


a = False
if a:
    print("참")
else :
    print("거짓")

a= 0
if a == 0 :
    print("참")
else:
    print("거짓")
 
a= 1
b=0
if a or b == 0:
    print("참")

if not a == 0:
    print('거짓')

if a and b == 1:
    print("참")

else:
    print("거짓")

a =[1,2,3,4]
if 1 in a :
    print("참")

a = 0
if a ==1:
    print("참")
elif a == 0:
    print("참")
else :
    print("거짓")

message = '노아'
score = 20
if score >= 60:
    message = "success"
else:
    message = "failure"

message = "success" if score >= 60 else "failure"  
print(message)  