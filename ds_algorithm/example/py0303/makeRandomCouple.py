#-*- coding: utf-8 -*-
import datetime
import random

# n명 중 두 명을 뽑아 짝짓기

inputUsers = ["Sophia", "Anne", "Peter", "Johnny"]
kakaoFriends = ["Apeach", "Ryan", "Con", "Muzi", "Jay-G", "Frodo", "Neo", "Tube"]
bt21 = ["Shooky", "RJ", "Chimmy", "Mang", "Koya", "Tata"]
niniz = ["Cob","Bbanya", "Angmond", "Jordy", "Kero", "Berony", "Scappy", "Penda"]
sample = ["Tom", "Jerry", "Mike"]

def make_random_couple(users):
    st = datetime.datetime.now()
    while len(users) != 0:
        idx1 = random.randrange(0, len(users))
        user1 = users[idx1]
        del users[idx1]
        if len(users) == 0:
            print "Sorry, You are alone... ", user1
        else:
            idx2 = random.randrange(0, len(users))
            user2 = users[idx2]
            del users[idx2]
            print "Couple : ", user1, "and ", user2
    print "소요시간:", datetime.datetime.now() - st
    return 0

print len(kakaoFriends), "명"
make_random_couple(kakaoFriends)

print len(inputUsers), "명"
make_random_couple(inputUsers)

print len(sample), "명"
make_random_couple(sample)