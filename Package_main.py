#Exercise package
#basketball, badminton modules
#basketball, badminton say "hurryup"

# from Exercise import basketball # Exercise 패키지에서 basketball 모듈을 갖고와줘
# from Exercise import badminton # Exercise 패키지에서 badminton 모듈을 갖고와줘

# from Exercise import * # 모두 갖고와줘

#b1 = basketball.Basketball()
#b1.coach()

#b2 = badminton.Badminton()
#b2.coach()

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Scott")
location = geolocator.geocode("Seoul, South Korea")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)