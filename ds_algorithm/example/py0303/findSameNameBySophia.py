#-*- coding: utf-8 -*-
# n명의 사람 이름 중에서 같은 이름을 찾아 집합으로 만들어 돌려주는 알고리즘
import datetime

# set 이 중복을 허용하지 않으므로, list 에있는 이름들을 set에 하나씩 넣고 전 후 갯수가 변하지 않으면 중복된 이름으로 판단.
# O(n)
def find_same_name(names):
    st = datetime.datetime.now()
    temp = set()
    for x in names:
        before = len(temp)
        temp.add(x)
        after = len(temp)
        if before == after:
            print "중복", x

    print "소요시간:", datetime.datetime.now() - st
    return 0
