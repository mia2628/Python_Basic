#Exercise package
#basketball, badminton modules
#basketball, badminton say "hurryup"

# from Exercise import basketball # Exercise 패키지에서 basketball 모듈을 갖고와줘
# from Exercise import badminton # Exercise 패키지에서 badminton 모듈을 갖고와줘

from Exercise import * # 모두 갖고와줘

#b1 = basketball.Basketball()
#b1.coach()

#b2 = badminton.Badminton()
#b2.coach()

b1 = Basketball()
b1.coach()

b2 = Badminton()
b2.coach()
