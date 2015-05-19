import unittest
from histogram_class import Histogram


class Test_Histogram(unittest.TestCase):

    def test_add_to_histogram(self):
        h = Histogram()
        h.add("Apache")
        h.add("Apache")
        h.add("IIS")

        self.assertTrue(h.count("Apache") == 2)
        self.assertTrue(h.count("IIS") == 1)

    def test_get_dict(self):
        h = Histogram()
        h.add("Apache")
        h.add("Apache")
        h.add("IIS")
        wanted_result = {"Apache": 2, "IIS": 1}
        self.assertEqual(h.get_dict(), wanted_result)


if __name__ == '__main__':
    unittest.main()
