# 10.1

# 아무 내용 없는 클래스랑 example 객체 생성
class thing:
    pass


example = thing()

# 출력한다
print(thing)  # result: <class '__main__.thing'>
print(example)  # <__main__.thing object at 0x0000023C02B0FBD0>


# 10.2 Thing2 클래스 만들고 letters 객체를 만들고 출력하기
class thing2:
    letters = 'abc'


print(thing2.letters)  # result: abc


# 10.3
# things3 클래스를 만들고 인스턴스 객체의 letters 출력한다.

class things3:
    pass


last = things3()
last.letter = 'xyz'
print(last.letter)  # result: xyz
