class Calc:
  def __init__(self):
    self.result = 0

  def add(self, num):
    self.result += num
    return self.result
  
cal1 = Calc()
cal2 = Calc()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(1))
print(cal2.add(2))