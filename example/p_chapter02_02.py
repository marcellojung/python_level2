# Chapter02-02
# 파이썬 심화
# 객체 지향 프로그래밍(OOP) -> 코드의 재사용, 코드 중복 방지 등
# 클래스 상세 설명
# 클래스 변수, 인스턴스 변수

# 클래스 재 선언
class Car():
    """
    Car Class
    Author : Kim
    Date : 2019.11.08
    """

    # 클래스 변수 : 모든 인스턴스가 공유하는 변수 
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))

    def __del__(self):
        Car.car_count -= 1


# Self 의미
car1 = Car('Ferrari', {'color' : 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# ID 확인
print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

'''1611045121328
1611045121040
1611045121184
False
False
이렇게 car1,car2,car3의 인스턴스는 각각 다른 아이디를 가진다. 이를 매핑해주는것이 self이다.
'''

# dir & __dict__ 확인
#오브젝트 변수를 보고 싶을 때
#dir은 상위로부터 상속받은 모든 값들을 보여줌. 그러나 실제 값들은 보여주지 않음
#__dict__는 key,value값들을 상세하게 보여준다., 
print(dir(car1))
print(dir(car2))

print()
print()
## key, value로 보고 싶을 때 
print(car1.__dict__)
print(car2.__dict__)

# Doctring : 미리 약속된 주석임. 
print(Car.__doc__)
print()

# 실행
car1.detail_info()
car2.detail_info()

# 에러
# Car.detail_info()
Car.detail_info(car1)
Car.detail_info(car2)
#class 확인 : 붕어빵 틀은 똑같으니까/ car1,car2,car3는 car가 몸통이다. 
# 비교
print(car1.__class__, car2.__class__)
print(id(car1.__class__) == id(car3.__class__))

print()

# 인스턴스 변수
# 직접 접근(PEP 문법적으로 권장X)
print(car1._company, car2._company)
print(car2._company, car3._company)

print()
print()

# 클래스 변수

# 접근
print(car1.car_count)
print(car2.car_count)
print(Car.car_count)

print()
print()


# 공유 확인
print(Car.__dict__)
print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

# 인스턴스 네임스페이스 없으면 상위에서 검색
# 즉, 동일한 이름으로 변수 생성 가능(인스턴스 검색 후 -> 상위(클래스 변수, 부모 클래스 변수))
del car2

print(car1.car_count)
print(Car.car_count)