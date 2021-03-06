class Person:
  def __init__(self, name, grad, score, port, vol, act):
    self.name = name
    self.grad = grad
    self.score = score
    self.port = port
    self.vol = vol
    self.act = act

  def say_hello(self):
    print("안녕하세요 저는 " + self.name + " 입니다.")

  def check_graduate(self):
    if self.score >= "130":
      if self.port == "O":
        if self.vol >= "150":
          print("졸업여부 : " + "True")
        else:
          print("졸업여부 : " + "False")
      else:("졸업여부 : " + "False")
    else:
      print("졸업여부 : " + "False")

  def school_grade(self):
    print("수강학점 : " + self.score + "점")

  def portfolio(self):
    print("포트폴리오 제출여부 : " + self.port)

  def volunteer(self):
    print("봉사시간 : " + self.vol)

  def active(self):
    print(self.act + "는(은) 놀고 자빠졌습니다.")


Seong = Person("허윤성", "", "128", "O", " 150", "Seong")
Seong.say_hello()
Seong.check_graduate()
Seong.school_grade()
Seong.portfolio()
Seong.volunteer()
Seong.active()

class Lab(Person):
  def experience(self, exp):
    self.exp = exp
    print(self.exp + "는(은) 스웨덴을 여행중입니다. ")

class Programmer(Person):
  def program(self, tool):
    self.tool = tool
    print(self.tool + "는(은) e-mail client를 개발중입니다. ")

scott = Lab("scott", "", "130", "O", "150", "")
scott.say_hello()
scott.check_graduate()
scott.school_grade()
scott.portfolio()
scott.volunteer()
scott.experience("scott")
scott.program("scott")


Amily = Programmer("Amily", "", "150", "O", "160", "")
Amily.say_hello()
Amily.check_graduate()
Amily.school_grade()
Amily.portfolio()
Amily.volunteer()
Amily.experience("Amily")
Amily.program("Amily")
