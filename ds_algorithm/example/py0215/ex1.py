#-*- coding: utf-8 -*-
# 1부터 n까지 연속한 숫자의 제곱의 합

import datetime
import example.py0209.sumAtoB as dsSum

def squareSum(n):
    sum= 0
    st = datetime.datetime.now()
    for x in range(n+1):
        sum += x**2

    print "1 계산 끝 ",datetime.datetime.now()-st
    return sum

def squareSum2(n):
    st = datetime.datetime.now()
    sum = ((n+1)**3 -1 -3*dsSum.gausSumAtoB(1,n)-n)/3
    print "2 계산 끝 ",datetime.datetime.now()-st
    return sum

print squareSum(100)
print squareSum2(100)

