# Chapter05-01
# 일급 함수(일급 객체)
# 파이썬 함수 특징
# 1.런타임 초기화 
# 2.변수 할당 가능
# 3.함수 인수 전달 가능
# 4.함수 결과 반환 가능(return)

# 함수 객체
def factorial(n):
    '''factorial function-> n:int '''
    if n == 1:
        return 1
    return n * factorial(n-1) # 재귀 함수

class A:
    pass

print(factorial(5))
#5 * 4 * 3 * 2 * 1
print(factorial.__doc__)
#factorial function-> n:int 
print(type(factorial),type(A))
#print(dir(factorial))
#일개 함수가 le, repr, gt 이런게 있음
print(set(sorted(dir(factorial))) - set(sorted(dir(A))) )
#함수 - class -> 함수는 객체 취급을 하고 있다. 
#{'__call__', '__defaults__', '__closure__', '__qualname__', '__globals__', '__kwdefaults__', '__get__', '__annotations__', '__code__', '__name__'}
print(factorial.__name__)
print(factorial.__code__) # file 위치까지 알 수 있다. 함수가 정의된 위치도.

print()
print()

# 변수 할당
var_func = factorial

print(var_func)
print(var_func(10))
print(map(var_func, range(1,11)))
print(list(map(var_func, range(1,6))))


# 함수 인수 전달 및 함수로 결과 반환 -> 고위 함수(Higher-order function)
# map, filter, reduce 등
print(list(map(var_func, filter(lambda x: x % 2, range(1,6)))))
print([var_func(i) for i in range(1,6) if i % 2])

print()
print()

# reduce()
from functools import reduce
from operator import add

print(reduce(add, range(1,11))) # 누적
print(sum(range(1,11)))


# 익명함수(lambda)
# 가급적 주석 작성
# 가급적 함수 사용
# 일반 함수 형태로 리팩토링 권장
print(reduce(lambda x, t: x + t, range(1,11)))

print()
print()

# Callable : 호출 연산자 -> 메소드 형태로 호출 가능한지 확인
# 호출 가능 확인
print(callable(str), callable(list), callable(var_func), callable(3.14))

from inspect import signature

sg = signature(var_func)

print(sg)
print(sg.parameters)

print()
print()

# partial 사용법 : 인수 고정 -> 콜백 함수에 사용
from operator import mul
from functools import partial

print(mul(10,10))

# 인수 고정
five = partial(mul, 5)

# 고정 추가
six = partial(five, 6)

print(five(10))
print(six())
print([five(i) for i in range(1,11)])
print(list(map(five, range(1,11))))