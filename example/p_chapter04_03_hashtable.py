# Chapter04-03
# 파이썬 심화
# 시퀀스형
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
'''key에 value를 저장하는 구조. 키값의 연산결과에 따라 직접 접근이 가능한 구조.
key 값을 해싱함수 -> 해휘 주소 --> key에 대한 value 참조 '''
# Dict -> Key 중복 허용 X, Set -> 중복 허용 X
# Dict 및 Set 심화


# Dict 구조
print(__builtins__.__dict__)

print()
print()

# Hash 값 확인
t1 = (10, 20, (30, 40, 50))
#tuple은 수정이 불가능하다. 고유하다. 
t2 = (10, 20, [30, 40, 50])


print( hash(t1)) #: 고유하기 때문에 값이 나온다.
# print(hash(t2)) # 예외
#TypeError: unhashable type: 'list'
print()
print()

# Dict Setdefault 예제
#tuple 형식을 딕셔너리 형태로 변경하는 2가지 방법입니다. setdefault로 변경하면 빠르게 변경 가능합니다. 
#딕셔너리의 중요한 기능 중 하나가 바로 키-값 쌍 추가입니다. 다음과 같이 딕셔너리에 키-값 쌍을 추가하는 메서드는 2가지가 있습니다.
#setdefault: 키-값 쌍 추가

source = (('k1', 'val1'),
            ('k1', 'val2'),
            ('k2', 'val3'),
            ('k2', 'val4'),
            ('k2', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use setdefault
#tuple을 dictionary로 변경하는 방법 
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k : v for k , v in source}

print(new_dict3)

print()
print()