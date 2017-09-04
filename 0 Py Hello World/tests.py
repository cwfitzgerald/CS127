import unittest
import helloworld


class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        self.assertEqual(helloworld.get_hello(), "Hello World!")

if __name__ == "__main__":
    unittest.main()
