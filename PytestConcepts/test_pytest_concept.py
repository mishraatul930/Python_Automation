import pytest

def test_m():
    a = 3
    b = 4
    assert a+1 == 4, "Assert Failed"
    assert a == b,"Assert false both are not equal"

@pytest.mark.login
def test_m2():
    name = "selenium"
    assert name.upper() == "SELENIUM","Assert is failing"


def test_m3():
    assert True

@pytest.mark.login
def test_m4():
    assert False

def test_m5():
    assert 100 == 100

@pytest.mark.login
def test_m6():
    assert "atul" == "ATUL"

#how to run entire suite marker - py.test -m marker_name
#how to run file specific marker - py.test directory_name/file_name -m marker_name
#how to run tests in parallel py.test -n 5
#how to run file specific parallel tests - py.test directory_name/file_name -n 5
#5 in above comments is the number of workers# Activate virtualenv (PowerShell)