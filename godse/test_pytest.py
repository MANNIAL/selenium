import pytest

@pytest.fixture()
def setup():
    print(":this is setup ")
def testmethod(setup):
    print("this is test method")
def testmethod1(setup):
    print("this is test method1")