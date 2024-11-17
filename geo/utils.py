import math  # math 모듈 사용

# 피타고라스 정리를 이용한 빗변 길이 계산
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

# 원의 넓이 계산
def circle_area(radius):
    return math.pi * radius**2  # math.pi를 사용하여 더 정확한 계산
