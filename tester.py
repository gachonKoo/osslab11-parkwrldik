from geo.utils import add, subtract

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    print("add() 테스트 성공")

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 1) == -1
    print("subtract() 테스트 성공")

if __name__ == "__main__":
    test_add()
    test_subtract()
    print("모든 테스트 성공")
