from panda import Panda
from panda import WrongEmailError
import unittest


class TestPanda(unittest .TestCase):

    def setUp(self):
        self.peshko_panda = Panda("Peshko", "peshko@pandaemail.com", "male")

    def test_create_new_panda(self):
        self.assertTrue(isinstance(self.peshko_panda, Panda))

        with self.assertRaises(WrongEmailError):
            self.marto_panda = Panda("Marto", "martopandaemail.com", "male")

    def test_get_name(self):
        self.assertEqual(self.peshko_panda.name, self.peshko_panda.get_name())

    def test_get_gender(self):
        self.assertEqual(
            self.peshko_panda.gender, self.peshko_panda.get_gender())

    def test_get_email(self):
        self.assertEqual(
            self.peshko_panda.email, self.peshko_panda.get_email())

    def test_is_male(self):
        self.assertTrue(self.peshko_panda.is_male())

    def test_is_female(self):
        self.assertFalse(self.peshko_panda.is_female())

    def test_equal_objects(self):
        peshko_panda_2 = Panda("Peshko", "peshko@pandaemail.com", "male")
        self.assertEqual(self.peshko_panda, peshko_panda_2)

    def test_object_to_str(self):
        peshko_panda_2 = Panda("Peshko", "peshko@pandaemail.com", "male")
        message = "My panda with name {} is with email {} and gender {}".format(
            peshko_panda_2.name, peshko_panda_2.email, peshko_panda_2.gender)

        self.assertEqual(str(peshko_panda_2), message)

    def test_object_to_hash(self):
        self.assertTrue(int(hash(self.peshko_panda)))


if __name__ == '__main__':
    unittest.main()
