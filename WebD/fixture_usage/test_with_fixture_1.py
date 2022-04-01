import pytest

@pytest.fixture()
def need_data():
    d = 10
    print(f"data is {d}")
    return d

class Test_ABC:
    def test_1(self, need_data):
        print(f"\nneed_data is of {type(need_data)}")
        print("starting test_1")
        assert need_data != 1, "Fail, need_data==1"

if __name__ == "__main__":
    pytest.main(["-s", '-v', "test_with_fixture_1.py"])