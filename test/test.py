import unittest

import main


class Test(unittest.TestCase):

    def shouldSayHello(self):
        self.assertEqual('Hello World', main.main('run'))

    def shouldSayGoodbye(self):
        self.assertEqual('Goodbye', main.main('test'))

    def shouldNotFailForNone(self):
        self.assertEqual('Hello World', main.main(None))


if __name__ == '__main__':
    unittest.main()
