class Calc:
  def __init__(self):
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result
  
cal1 = Calc()
cal2 = Calc()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(1))
# print(cal2.add(2))

# 상속은 인자로 넣으면 된다.

class SetNumber:
  def __init__ (self, first, second):
    self.first = first
    self.second = second  
    self.result = 0

class ADD(SetNumber):
  def addFS(self):
    self.result = self.first + self.second

instance = ADD(4,5) #클레스를 호출할 땐, 변수 즉, 메모리를 할당해주어야 한다. 
print(instance.addFS()) # 이후 객체 점접근법을 활용해서 메서드를 실행한다. // 실행문은 none이 나온다.
print(instance.result) # 콘솔에 결과를 출력한 결과 9가 바르게 나오게 된다.
