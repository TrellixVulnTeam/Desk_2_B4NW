import pytest

@pytest.fixture(params=[1,2,3])
def need_data(request):
    return request.param

class Test_abc:
    def test_a(self, need_data):
        print("\ntest_a is running")
        assert need_data != 3

if __name__ == "__main__":
    pytest.main(["-s", '-v', "test_with_fixture_5.py"])

