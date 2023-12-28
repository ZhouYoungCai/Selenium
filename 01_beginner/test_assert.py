# content of my_assertion.py
def test_assertion():
    assert [1, 2, 3] == [1, 2, 4], "left is [1,2,3], right is [1,2,4]"

if __name__ == '__main__':
    test_assertion()
