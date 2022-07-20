#type() --> 자료형 리턴

#참이나 거짓을 나타내는 True , False 두 상수를 갖는다
a = 1
b = a<10
print(b)

#True -> 1, False -> 0
a = True + True
print(a)

print(1 == True)
print(0 == True)
print(0 == False)


#특이한 케이스
b1 = True
b2 = False

print(b1 + 10) #1+10 = 11
print(b2 + 10) #0+10 = 10
print(True + True) #1+1 = 2
print(True - 2) #1-2 = -1
