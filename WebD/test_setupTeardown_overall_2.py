def setup():
    print("in setup")


class TestDemo:
    def setup_class(self):
        print("\nin setup_class")
    def teardown_class(self):
        print("in teardown_class")

    def setup_method(self):
        print("\nin setup_method")
    def teardown_method(self):
        print("in teardown_method")

    def teardown(self):
        print("in teardown")

    def test_1(self):
        print("test_1 starts")
    def test_2(self):
        print("test_2 starts")
    def test_3(self):
        print("test_3 starts")
