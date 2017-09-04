import unittest
import helloworld


class TestHelloWorld(unittest.TestCase):
    def test_output(self):
        self.assertEqual(helloworld.create_hello(), "Hello World!")

if __name__ == "__main__":
    unittest.main()
