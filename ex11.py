age = 3333
do = 23
str1 = "현재 온도는 %d 도 입니다." % do
str2 = "오늘은 %s년 %d월 %d일 입니다" %("2022",7,15)
area = 76.483

print(str1)
print(str2)
print("제 나이는 %d살 입니다" % age)
print("원의 넓이는 %f 입니다"% area)

print("제 나이는 %10d살 입니다" %age)
print("제 나이는 %-10d살 입니다" % age)
print("원의 넓이는 %7.5f 입니다"% area)
print("원의 넓이는 %-20.1f 입니다"% area)

print("수수료는 %d%% 입니다" %20)

print("=====================================")
age = 25

print("제 나이는 {0}살입니다" .format(25))
print("제 나이는 {0}살입니다" .format("스물다섯"))
print("제 나이는 {0}살입니다" .format(age))
print("오늘은 {0}년 {1}월 {2}일 입니다" .format("2022", 7, 15))
print("오늘은 {year}년 {month}월 {day}일 입니다." .format(year="2022", month=7, day=15))

print("오늘은 {0:<10}년 {1:>10}월 {2:^10}일 입니다".format("2022", 7, 15))
