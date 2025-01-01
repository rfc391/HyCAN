
import unittest
import os
from utils import read_file, write_file

class TestUtils(unittest.TestCase):
    def test_read_file(self):
        with open('test_file.txt', 'w') as f:
            f.write('Hello, World!')
        content = read_file('test_file.txt')
        self.assertEqual(content, 'Hello, World!')
        os.remove('test_file.txt')

    def test_write_file(self):
        write_file('test_write.txt', 'Testing write operation.')
        with open('test_write.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, 'Testing write operation.')
        os.remove('test_write.txt')
