import pytest


def setup(): # same as setup_function()
    print("\n--- setup_function starts---")
def teardown(): # same as teardown_function()
    print("*** teardown_function ----")


def test_b():
    print("\n^^^ test_b ^^^")
    assert 1

def test_a():
    print("\n^^^ test_a ^^^")
    assert 2

if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_setupTeardown_function_level_1.py"])

# collecting ... collected 2 items
#
# test_setupTeardown_function_level_2.py::test_b
# --- setup_function starts---
# PASSED                    [ 50%]
# ^^^ test_b ^^^
# *** teardown_function ----
#
# test_setupTeardown_function_level_2.py::test_a
# --- setup_function starts---
# PASSED                    [100%]
# ^^^ test_a ^^^
# *** teardown_function ----