#-*- coding: utf-8 -*-

print("Hello ds!") # test
print "hi"

a = 5**2
b = 5/2
c = 5//2
d = 5%2
arr = [a,b,c,d]

for x in arr:
    if x%2 ==0:
        print x, "짝수"
    else:
        print x, "홀수"

print "1부터 10까지 출력"
for x in range(10):
    print x+2
for x in range(1,11,1):
    print x
i = 1
while i<=10:
    print i
    i+=1


