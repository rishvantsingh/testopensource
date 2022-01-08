import unittest
import cotu


class TestHW(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(cotu.hello_world(), "hello world")

    def test_hello_world_on_jenkins(self):
        self.assertEqual(cotu.hello_world(), "hello jenkins")

if __name__ == '__main__':
    unittest.main()
