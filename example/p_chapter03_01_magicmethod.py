# Chapter03-01
# 파이썬 심화
# Special Method(Magic Method)
# 참조 : https://docs.python.org/3/reference/datamodel.html#special-method-names
# 파이썬의 핵심 -> 시퀀스(Sequence), 반복(Iterator), 함수(Functions), 클래스(Class)

# 기본형
print(int)
print(float)
#이게 클래스 였구나.....

# 모든 속성 및 메소드 출력
print(dir(int))
'''['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
<class 'int'>'''
# int class 안에 __add__의 메소드가 있다. 외부에는 +가 내부에는 __add_로 호출되는 것이다.
print(dir(float))
print()
print()

n = 10

# 사용
print(n + 100)
print(n.__add__(100)) # 내부적으로 이게 호출됨

# print(n.__doc__)
print(n.__bool__(), bool(n))
print(n * 100, n.__mul__(100))

print()
print()

# 클래스 예제1
class Fruit:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def __str__(self):
        return 'Fruit Class Info : {} , {}'.format(self._name, self._price)

    def __ge__(self, x):
        print('Called >> __ge__ Method.')
        if self._price >= x._price:
            return True
        else:
            return False

    def __le__(self, x):
        print('Called >> __le__ Method.')
        if self._price <= x._price:
            return True
        else:
            return False

    def __sub__(self, x):
        print('Called >> __sub__ Method.')
        return self._price - x._price

# 인스턴스 생성
s1 = Fruit('Orange', 7500)
s2 = Fruit('Banana', 3000)

# 매직메소드 출력
print(s1 >= s2)
print(s1 <= s2)
print(s1 - s2)
print(s2 - s1)
print(s1)
print(s2)
