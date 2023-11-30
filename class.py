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

class FourCal :
  def setdata(self, first, second):
    self.first = first
    self.second = second

b = FourCal()
b.setdata(4,2)
print(b.first, b.second)




