import pytest
test_user_data = ["linda", "sai", "tom"]
@pytest.fixture(scope='module')
def login(request):
    user=request.param
    print(f"{user}")
    return user

# run 'login' as a function, and test_user_data as its argument
@pytest.mark.parametrize('login', test_user_data, indirect=True)
def test_cart(login):
    usera = login
    print(f"user is {usera}")
    assert usera



if __name__ == "__main__":
    pytest.main(["-s", '-v', "test_with_fixture_7.py"])

