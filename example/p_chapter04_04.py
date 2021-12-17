# Chapter04-04
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화

# immutable Dict 수정 불가능한 dictionary 만들기
from types import MappingProxyType

d = {'key1': 'value1'}

# Read Only
#d는 수정가능하고 d_frozen은 수정 불가능 
d_frozen = MappingProxyType(d)

print(d, id(d))
print(d_frozen, id(d_frozen))
print(d is d_frozen, d == d_frozen)

# 수정 불가
# d_frozen['key1'] = 'value2'

d['key2'] = 'value2'

print(d)

print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

# 추가
s1.add('Melon')

# 추가 불가
# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
#바이트 코드 -> 파이썬 인터프리터 
#dis모듈을 활용하면 바이트코드가 어떻게 생성되는지 알 수 있다
from dis import dis

print('------')
print(dis('{10}'))

print('------')
print(dis('set([10])'))

print()
print()
'''------ 집합 직접 선언이 더 좋다..ㅎㅎ
  1           0 LOAD_CONST               0 (10)
              2 BUILD_SET                1
              4 RETURN_VALUE
None
------
  1           0 LOAD_NAME                0 (set)
              2 LOAD_CONST               0 (10)
              4 BUILD_LIST               1
              6 CALL_FUNCTION            1
              8 RETURN_VALUE
None'''
# 지능형 집합(Comprehending Set)
#unicodedate 모듈 에서 name 함수만 가져옴 
from unicodedata import name

print('------')

print({name(chr(i), '') for i in range(0,256)})