import pytest

class Test_abc:
    # if condition is True; xfail is enabled
    # otherwise, xfail is disabled
    # 2>1 is True --> xfail enabled
    @pytest.mark.xfail(2>1, reason="Expected failure")
    def test_a(self):
        print("\ntest_a is running")
        assert 3 != 3

    def test_b(self):
        print("\ntest_b is running")
        assert 1 != 3

if __name__ == "__main__":
    pytest.main(["-s", '-v', "test_with_fixture_6.py"])

