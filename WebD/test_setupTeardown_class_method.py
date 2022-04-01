import pytest

class Test_ABC:

    def setup_method(self): # same as setup()
        print("\n--- setup_method starts---")

    def teardown_method(self): # same as teardown()
        print("*** teardown_method ----")

    def test_b(self):
        print("\n^^^ test_b ^^^")
        assert 1

    def test_a(self):
        print("\n^^^ test_a ^^^")
        assert 2

if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_setupTeardown_function_level.py"])

# collecting ... collected 2 items
#
# test_setupTeardown_class_method.py::Test_ABC::test_b
# --- setup_method starts---
# PASSED              [ 50%]
# ^^^ test_b ^^^
# *** teardown_method ----
#
# test_setupTeardown_class_method.py::Test_ABC::test_a
# --- setup_method starts---
# PASSED              [100%]
# ^^^ test_a ^^^
# *** teardown_method ----