import unittest

class test_sample(unittest.TestCase):

    def setUp(self):
        print('setup')

    def tearDown(self):
        print('tearDown')

    @unittest.skipIf(0 < 1, "demonstrating skipping")
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    @unittest.expectedFailure
    def test_upper_f(self):
        self.assertEqual('foo'.upper(), 'FOZ')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()