import unittest

from communicate.email import send
from process import ProcessByPID


class EmailTest(unittest.TestCase):
    def test_default(self):
        send('test@test.com', ProcessByPID(1))


if __name__ == '__main__':
    unittest.main()
