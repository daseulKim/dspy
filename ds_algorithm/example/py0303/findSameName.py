#-*- coding: utf-8 -*-
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘
import datetime

# 다음꺼랑 비교 O(n^2)
def find_same_name(names):
    st = datetime.datetime.now()
    n = len(names)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if names[i] == names[j]:
                print "중복", names[i]

    print "소요시간:", datetime.datetime.now() - st
    return 0

