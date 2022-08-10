import unittest
@classmethod
def setupmodule ():
    print("allow applications")
def teardownmodule():
    prtint("complite application")
class search_testing (unittest.TestCase):
    @classmethod
    def setup (self):
         print("all applications")\
    @classmethod
    def teardown(self):
        print("logout applications")
    def test_google(self):
        print("this is google method")


if __name__ == "__main__":
    unittest.main()