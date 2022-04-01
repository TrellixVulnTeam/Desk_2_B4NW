import pytest
import time
# import instafail

def setup_module(self):
    print("\n--- setup starts---")


def teardown_module(self):
    print("*** teardown ----")

class Test_ABC:


    def test_b(self):
        print("\n^^^ test_b ^^^")
        assert 1==1

    def test_a(self):
        print("\n^^^ test_a ^^^")
        time.sleep(10)
        assert 2==1
    def test_c(self):
        print("\n^^^ test_c ^^^")
        assert 1==3
    def test_d(self):
        print("\n^^^ test_d ^^^")
        assert 1==4
    def test_e(self):
        print("\n^^^ test_e ^^^")

        time.sleep(15)
        assert 1

if __name__ == "__main__":
    pytest.main(["-s", "-v", "--tb=auto", "test_setupTeardown_module_level.py"])

# collecting ... collected 2 items
#
# test_setupTeardown_module_level.py::Test_ABC::test_b
# --- setup starts---
# PASSED              [ 50%]
# ^^^ test_b ^^^
#
# test_setupTeardown_module_level.py::Test_ABC::test_a PASSED              [100%]
# ^^^ test_a ^^^
# *** teardown ----