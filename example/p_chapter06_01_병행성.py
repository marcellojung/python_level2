# Chapter06-01
# 병행성(Concurrency)
# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# 반복 가능한 이유? -> iter(x) 함수 호출
t = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# for 반복
for c in t:
    print(c)

print()

# while 반복

w = iter(t)

while True: # 종료조건있을 때 까지 반복
    try: # 예외조건 
        print(next(w))
    except StopIteration: # break 조건 
        break

print()

from collections import abc

# 반복형 확인 3가지 알아야 합니다!
print(dir(t))
#직접 찾아야함 ㅎㅎㅎ
print(hasattr(t, '__iter__'))
# t가 iter를 가지고 있는지 확인하는 함수 has attribute
#true
print(isinstance(t, abc.Iterable))
#상속을 받았는지 확인 
#true 
print()
print()

# next 사용
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        #magic method로 next 구현 
        # print('Called __next__')
        try:
            word = self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration.')
        self._idx += 1
        return word

    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wi = WordSplitIter('Do today what you could do tomorrow')

print(wi)
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
print(next(wi))
# print(next(wi))

print()
print()

# Generator 패턴
# 1.지능형 리스트, 딕셔너리, 집합 -> 데이터 양 증가 후 메모리 사용량 증가 -> 제네레이터 사용 권장
# 2.단위 실행 가능한 코루틴(Coroutine) 구현과 연동
# 3.작은 메모리 조각 사용

class WordSplitGenerator:
    def __init__(self, text):
        self._text = text.split(' ')
    
    def __iter__(self):
        # print('Called __iter__')
        for word in self._text:
           yield word # 제네레이터
        return
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)


wg = WordSplitGenerator('Do today what you could do tomorrow')

wt = iter(wg)

print(wt)
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
print(next(wt))
# print(next(wt))

print()
print()