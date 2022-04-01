import pytest

@pytest.fixture()
def need_data():
    print("\nfixture: need_data is called")
    return [100,200,300]

@pytest.mark.usefixtures('need_data')
class Test_ABC:
    def test_1(self, need_data):
        print(f"\nneed_data is of {type(need_data)}")
        print("starting test_1")
        assert need_data != 1, "Fail, need_data==1"

    # def test_2(self):
    #     print("\ncalling test_2")

if __name__ == "__main__":
    pytest.main(["-s", '-v', "test_with_fixture_2.py"])

