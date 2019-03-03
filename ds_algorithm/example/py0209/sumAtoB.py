#-*- coding: utf-8 -*-
# 입력: 시작, 끝
# 출력: 시작부터 끝까지 모든 수의 합
import datetime

def sumAtoB(a, b):
    st = datetime.datetime.now()
    print "sumAtoB > ", a,"부터 ",b,"까지 모든 수의 합 "
    tmp = 0
    for x in range(a, (b-a+3)):
        tmp+=x
    print "< sumAtoB 계산 끝 ", datetime.datetime.now()-st
    return tmp

# print sumAtoB(1,10)
# print sumAtoB(1,100)
# print sumAtoB(1,1000)

def gausSumAtoB(a, b):
    st = datetime.datetime.now()
    # print "gausSumAtoB > ", a,"부터 ",b,"까지 모든 수의 합 "
    result = 0
    if (b-a+1)%2==0:
        result= (b-a+1)*(b+a)/2
    else:
        # print (b-a+1)//2, ",", (b+a), ",", (b-a+1)//2*(b+a)
        result= (b-a+1)//2*(b+a)+(b+a)/2

    # print "< gausSumAtoB 계산 끝 ",datetime.datetime.now()-st
    return result

# gausSumAtoB(1, 10**8)
# sumAtoB(1,10**8)
# print sumAtoB(2,5)
# print gausSumAtoB(2,5)
# print sumAtoB(2,6)
# print gausSumAtoB(2,6)
# print sumAtoB(2,7)
# print gausSumAtoB(2,7)

# 2,3,4,5,6
# 5//2 = 2
# 2+6 3+5 +4

