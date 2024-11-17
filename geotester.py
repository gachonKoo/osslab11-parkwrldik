from geo import utils

def main():
    # 테스트할 좌표 설정
    coord1 = (0, 0)
    coord2 = (3, 4)
    
    # calculate_distance 함수 테스트
    distance = utils.calculate_distance(coord1, coord2)
    print(f"{coord1}와 {coord2} 사이의 거리: {distance}")

if __name__ == "__main__":
    main()
