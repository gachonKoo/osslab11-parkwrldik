import geo.utils as utils  # geo.utils 모듈 가져오기

# 빗변 길이 계산 (a=3, b=4)
a, b = 3, 4
c = utils.hypotenuse(a, b)  # hypotenuse 함수 호출
print('c =', c)

# 원의 넓이 계산 (반지름 r=10)
r = 10
area = utils.circle_area(r)  # circle_area 함수 호출
print('area =', area)
