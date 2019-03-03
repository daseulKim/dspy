#-*- coding: utf-8 -*-
import math

# 입력: 실수 a
# 출력: a의 절대값

def abs_sign(a): # 절대값
    if a>=0:
        return a
    else:
        return -a

def abs_square(a): # 제곱근
    b = a*a
    return math.sqrt(b)

print 3, abs_sign(3), abs_sign(-3), abs_square(-3)