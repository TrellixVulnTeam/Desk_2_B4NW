import pytest

@pytest.fixture()
def my_setup():
    print("\nRun before test functions")
    yield
    print("\nRun after test function")

@pytest.mark.xfail()
def test_a(my_setup):
    print("\nRunning test_a")
    assert 2 == 5

@pytest.mark.usefixtures("my_setup")
def test_b():
    print("\nRunning test_b")
    assert 2 == 2

if __name__ == "__main__":
    pytest.main(["-s", '-v', "test_with_fixture_yield.py"])

