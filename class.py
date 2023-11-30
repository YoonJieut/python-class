result = 0

def add1(num) :
  global result
  result += num
  return result


# print(add1(3));
# print(add1(4));


class Calculator :
  def __init__(self):
    self.result = 0
  
  def add(self, num):
    self.result += num
    return self.result
  
cal1 = Calculator()
cal2 = Calculator()


# print(cal1.add(3))
# print(cal2.add(45))
# print(cal2.add(5))


# ------------------------------

# class FourCal :
#   def setdata(self, first, second):
#     self.first = first
#     self.second = second
    
#   def add(self):
#     result = self.first + self.second
#     return result
#   def mul(self):
#     result = self.first * self.second
#     return result
#   def sub(self):
#     result = self.first - self.second
#     return result
#   def div(self):
#     result = self.first / self.second
#     return result

# b = FourCal()
# b.setdata(4,2)
# print(b.first, b.second)
# print("add메서드 호출",b.add())
# print("mul메서드 호출",b.mul())
# print("sub메서드 호출",b.sub())
# print("div메서드 호출",b.div())


#! Constructor 생성자
#?setdata를 실행하지 않으면 메서드가 작동되지 않는다. 그 이유는 객체변수에 있었다.
#전재 조건이 first, second라는 객체의 변수가 필요했기 때문에 작동하지 않는 것

#js의 클래스가 set과 get객체를 통해 초기값을 저장하듯
#py의 클래스도 초깃값 설정이 필요이 필요할 때 사용하는 방법이 있다.
#! __init__ 초기화라는 뜻의 언더스코어를 2개 연결한 모습이 보인다.
#* 이것은 이름만 작성해도 클래스를 선언함과 동시에 초기값을 세팅해주는 메서드이자 생성자가 되는 것이다.
# 너무 편한데...??

class FourCal :
  def __init__(self, first, second):
    self.first = first
    self.second = second
    
  def add(self):
    result = self.first + self.second
    return result
  def mul(self):
    result = self.first * self.second
    return result
  def sub(self):
    result = self.first - self.second
    return result
  def div(self):
    result = self.first / self.second
    return result

c = FourCal(6,4)
print(c.add())





