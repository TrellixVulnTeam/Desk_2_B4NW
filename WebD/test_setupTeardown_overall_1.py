# import pytest-ordering
import pytest, time

def delay():
    time.sleep(10)
    # for i in range(1000):
    #     print(i)
def setup():
    print("in setup")
def teardown():
    print("in teardown")

def setup_function():
    print("in setup_function")
def teardown_function():
    print("in teardown_function")

def setup_module():
    print("in setup_module")
def teardown_module():
    print("in teardown_module")

def test_05_a():
    print("test_5 starts")

def test_04_a():
    print("test_4 starts")

@pytest.mark.run(order=2)
def test_02_a():
    print("test_2 starts")
@pytest.mark.run(order=1)
def test_01_a():
    print("test_01 starts")
@pytest.mark.run(order=3)
def test_03_a():
    print("test_3 starts")
    # time.sleep(10)
    print("calling delay()")
    delay()


    print("time is up")

def test_06_a():
    print("test_6 starts")
if __name__ == "__main__":
    pytest.main(["-s", "-v", "test_setupTeardown_overall_1.py"])




if __name__=="__main__":
    pytest.main(["-s", "-v", "test_setupTeardown_overall_1.py"])
#
# C:\Users\jsun\Documents\Desk_2\venv_3.7.2\Scripts\python.exe "C:\Program Files\JetBrains\PyCharm Community Edition 213.4631.9\plugins\python-ce\helpers\pycharm\_jb_pytest_runner.py" --path C:/Users/jsun/Documents/Desk_2/WebD/test_setupTeardown_overall_1.py
# Testing started at 4:26 PM ...
# Launching pytest with arguments C:/Users/jsun/Documents/Desk_2/WebD/test_setupTeardown_overall_1.py --no-header --no-summary -q in C:\Users\jsun\Documents\Desk_2\WebD
#
# ============================= test session starts =============================
# collecting ... collected 6 items
#
# test_setupTeardown_overall_1.py::test_01_a in setup_module
# in setup_function
# in setup
# PASSED                        [ 16%]test_01 starts
# in teardown
# in teardown_function
#
# test_setupTeardown_overall_1.py::test_02_a in setup_function
# in setup
# PASSED                        [ 33%]test_2 starts
# in teardown
# in teardown_function
#
# test_setupTeardown_overall_1.py::test_03_a in setup_function
# in setup
# PASSED                        [ 50%]test_3 starts
# calling delay()
# time is up
# in teardown
# in teardown_function
#
# test_setupTeardown_overall_1.py::test_05_a in setup_function
# in setup
# PASSED                        [ 66%]test_5 starts
# in teardown
# in teardown_function
#
# test_setupTeardown_overall_1.py::test_04_a in setup_function
# in setup
# PASSED                        [ 83%]test_4 starts
# in teardown
# in teardown_function
#
# test_setupTeardown_overall_1.py::test_06_a in setup_function
# in setup
# PASSED                        [100%]test_6 starts
# in teardown
# in teardown_function
# in teardown_module
#
#
# ============================= 6 passed in 10.05s ==============================
#
# Process finished with exit code 0



