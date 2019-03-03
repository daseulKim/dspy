#-*- coding: utf-8 -*-
import datetime

# n명 중 두 명을 뽑아 짝을 짓는다고 할 때, 짝을 지을 수 있는 모든조합을 출력

inputUsers = ["Sophia", "Anne", "Peter", "Johnny"]
kakaoFriends = ["Apeach", "Ryan", "Con", "Muzi", "Jay-G", "Frodo", "Neo", "Tube"]
bt21 = ["Shooky", "RJ", "Chimmy", "Mang", "Koya", "Tata"]
niniz = ["Cob","Bbanya", "Angmond", "Jordy", "Kero", "Berony", "Scappy", "Penda"]
sample = ["Tom", "Jerry", "Mike"]

def case_of_make_couple(ussers):
    st = datetime.datetime.now()

    n = len(ussers)
    for i in range(0, n-1):
        for j in range(i+1, n):
            print ussers[i], " - ", ussers[j]

    print "소요시간:", datetime.datetime.now() - st
    return 0

case_of_make_couple(sample)
print "kakaoFriends ", len(kakaoFriends)
case_of_make_couple(kakaoFriends)
print "niniz ", len(niniz)
case_of_make_couple(niniz)
print "bt21 ", len(bt21)
case_of_make_couple(bt21)