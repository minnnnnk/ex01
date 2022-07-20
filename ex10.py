str1 = "FirstString"
str2 = "SecondString"

print(str1[0])
print(str1 + str(10)) #print(str1 + 10) 은 안됨 --> 문자열 + 문자열

print(str1 + str2)
print(str1*3)
print(str1[2])
print(str2[2:5]) #[이상:미만]
print(str2[1:9:2]) #[이상:미만:증가]
print(len(str2))

print(str1[:])
print(str1[-6: -2])

print(str1[::-1])

name = '우영후'
name2 = name[::-1]

print(name)
print(name2)
'''if('토마토' == name[::-1]):
 print("aaa")'''


