s = "i list Python"
s01 = s.upper()
print(s01) #대문자
print(s) #소문자
print(s.lower())
print(s.swapcase())
print(s.capitalize())
print(s.title())

print(s*3)
print(s+s)
s = 'I Like Python. I Like Java Also'

print(s.find("Like"))
print(s.find("Like", 5))
print(s.find("Like", 5, 40))

print(s.find("JS"))

print(s.rfind("Like"))

#print(s.index("to"))

print(s.startswith("I Like"))
print(s.startswith("I Like", 2))

print(s.endswith("Also"))
print(s.endswith("Java",0,26))

#편집과 치환
s = '   spam and ham    '
print(s.strip())
print(s.rstrip())
print(s.lstrip())

s = '<><abc><><defg><><>'
print(s.strip('<>'))

s = 'Hello Java Java java'
print(s.replace( 'Java', 'Python'))

print("=============")

s = 'king and queen'

print(s.center(60))
print(s.center(60, '-'))
print(s.ljust(60, '-'))
print(s.rjust(60, '-'))

print("1234".isdigit())
print("abcdefg한".isdigit())
print("abcD".islower())
print("ABCD".isupper())

print("\n\n".isspace())
print('    '.isspace())
print(''.isspace())

print('20'.zfill(10))
print('1234'.zfill(10))

print('===========================')
#공백 - 문자열이 모두 공백이면 true
print(" ".isspace())
print("".isspace())

print("            a           ".isspace())
