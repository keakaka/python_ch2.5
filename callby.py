# call by reference 이지만, 내부에서 변경하더라도 변경되지 않는다. ( Immutable 객체일 때 )
def f(i):
    i = 20


def f2(seq):
    seq[0] = 0



a = 10
f(a)
print(a)

# 파라미터가 sequence type( immutable )인 경우 내부 변경 시 오류
# a = (1, 2, 3)
# f2(a)

a = [1, 2, 3]
f2(a)
print(a)

