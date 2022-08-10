import unittest
class testman( unittest.TestCase):
    def test_godse(self):
        list=("python", "java", "sql")
        self.assertIn("java",list)

if __name__== "__main__":

    unittest.main()

