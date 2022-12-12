import unittest

from main import main


class Test(unittest.TestCase):

    def shouldSayHello(self):
        self.assertEqual('Hello World', main('run'))

    def shouldSayGoodbye(self):
        self.assertEqual('Goodbye', main('test'))

    def shouldNotFailForNone(self):
        self.assertEqual('Hello World', main(None))


if __name__ == '__main__':
    unittest.main()
