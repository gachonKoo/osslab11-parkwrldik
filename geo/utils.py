import math

def calculate_distance(coord1, coord2):
    """
    두 좌표 간의 유클리드 거리를 계산하는 함수.
    
    Parameters:
    coord1, coord2: 각각 (x, y) 형식의 튜플
    
    Returns:
    거리 (float)
    """
    x1, y1 = coord1
    x2, y2 = coord2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance
