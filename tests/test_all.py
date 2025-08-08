import unittest
from my_toolkit.math_ops.basic import add, divide
from my_toolkit.string_ops.utils import reverse_string
from my_toolkit.file_ops.file_handler import write_to_file, read_from_file

class TestToolkit(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_reverse(self):
        self.assertEqual(reverse_string("abc"), "cba")

    def test_file_ops(self):
        filename = "test.txt"
        content = "Test"
        write_to_file(filename, content)
        self.assertEqual(read_from_file(filename), content)

if __name__ == "__main__":
    unittest.main()
