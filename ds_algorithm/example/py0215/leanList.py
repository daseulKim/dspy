#-*- coding: utf-8 -*-


a = [5,6,7,8,9]
print a
print "뒤에서 두번째 ", a[-2]
print "a 의 길이 ", len(a)

print "a.append(10)", a.append(10), a
print "뒤에서 두번째 ", a[-2]
print "a 의 길이 ", len(a)

print "a.insert(-1, 4)", a.insert(-1, 4), a
print "뒤에서 두번째 ", a[-2]
print "a 의 길이 ", len(a)

print "a.pop()", a.pop(), a
print "뒤에서 두번째 ", a[-2]
print "a 의 길이 ", len(a)

print "5 in a ", 5 in a
print "5 not in a ", 5 not in a


