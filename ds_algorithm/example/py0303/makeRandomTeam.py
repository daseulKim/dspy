#-*- coding: utf-8 -*-
import datetime
import random
# n명 중 m 명을 뽑아 팀 만들기

inputUsers = ["Sophia", "Anne", "Peter", "Johnny"]
kakaoFriends = ["Apeach", "Ryan", "Con", "Muzi", "Jay-G", "Frodo", "Neo", "Tube"]
bt21 = ["Shooky", "RJ", "Chimmy", "Mang", "Koya", "Tata"]
niniz = ["Cob","Bbanya", "Angmond", "Jordy", "Kero", "Berony", "Scappy", "Penda"]
sample = ["Tom", "Jerry", "Mike"]

def random_pop(users):
    randomNum = random.randrange(0, len(users))
    pop = users[randomNum]
    del users[randomNum]
    return pop

def make_random_couple(users, m):
    st = datetime.datetime.now()
    n = len(users) // m
    for i in range(0, n):
        team = []
        for j in range(0, m):
            team.append(random_pop(users))
        print i+1,"팀 ",team

    # for i in range(0, len(users) % m):
    if len(users) == 1:
        print random.randrange(1, n+1), "팀에서 깍두기 한 명 껴주는거로~! ",users[0]
    if len(users) > 1:
        print "남은 사람들끼리 팀하세요~ ",users
    # print "소요시간:", datetime.datetime.now() - st
    return 0

members = kakaoFriends+niniz+sample
memberCount = 2
print len(members), "명 중 ", memberCount, "명 씩 팀만들기"
make_random_couple(members, memberCount)
