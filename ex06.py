#복소수

#복소수 타입의 객체는 실수부+허수부로 나뉘며 허수부에는 j 또는 J를 숫자 뒤에 붙인다
a = 4+5j
print(type(a))
print(isinstance(a, complex))

a= 4+5j
b= 7-2j
print(a+b)
print(b.real,b.imag)

c= 4
d= 5.4
print(complex(c))
print(complex(d))


