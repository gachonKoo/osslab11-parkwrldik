from geo import utils

def main():
    # 표준 입력을 통해 좌표를 입력받기
    x1, y1 = map(float, input("첫 번째 좌표 (x1, y1): ").split())
    x2, y2 = map(float, input("두 번째 좌표 (x2, y2): ").split())

    # calculate_distance 함수 호출
    distance = utils.calculate_distance((x1, y1), (x2, y2))
    print(f"계산된 거리: {distance}")

if __name__ == "__main__":
    main()
