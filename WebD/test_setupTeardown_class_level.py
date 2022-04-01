import pytest

class Test_ABC:

    def setup_class(self):
        print("\n--- setup starts---")

    def teardown_class(self):
        print("*** teardown ----")

    def test_b(self):
        print("\n^^^ test_b ^^^")
        assert 1

    def test_a(self):
        print("\n^^^ test_a ^^^")
        assert 2

if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_setupTeardown_function_level.py"])
