from panda import Panda
from panda_social_network import PandaSocialNetwork
from panda_social_network import PandaAlreadyThere, PandaAlreadyFriends
import unittest


class TestPandaSocialNetwork(unittest .TestCase):

    def setUp(self):
        self.network = PandaSocialNetwork()
        self.peshko = Panda("Peshko", "peshko@pandaemail.com", "male")
        self.marto = Panda("Marto", "marto@pandaemail.com", "male")

    def test_create_social_network(self):
        self.assertTrue(isinstance(self.network, PandaSocialNetwork))

    def test_add_panda(self):
        self.network.add_panda(self.peshko)

        with self.assertRaises(PandaAlreadyThere):
            self.network.add_panda(self.peshko)

    def test_has_panda(self):
        self.network.add_panda(self.peshko)
        self.assertTrue(self.network.has_panda(self.peshko))

    def test_make_friends(self):
        self.network.make_friends(self.peshko, self.marto)

        self.assertTrue(self.peshko in self.network.network_dict.keys())

        self.assertTrue(self.peshko in self.network.network_dict[self.marto])
        self.assertTrue(self.marto in self.network.network_dict[self.peshko])

    def test_pandas_already_friends(self):
        self.network.make_friends(self.peshko, self.marto)

        with self.assertRaises(PandaAlreadyFriends):
            self.network.make_friends(self.marto, self.peshko)

    def test_are_pandas_friends(self):
        self.network.make_friends(self.peshko, self.marto)

        self.assertTrue(self.network.are_friends(self.peshko, self.marto))

    def test_friends_of(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        mina = Panda("Mina", "mina@pandamail.com", "female")
        self.assertFalse(self.network.friends_of(ivo))

        self.network.make_friends(self.peshko, self.marto)
        self.network.make_friends(self.peshko, mina)
        self.assertEqual(self.network.friends_of(self.peshko), [self.marto, mina])

    def test_connection_level(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        mina = Panda("Mina", "mina@pandamail.com", "female")
        tony = Panda("Tony", "tony@pandamail.com", "female")

        self.network.make_friends(ivo, tony)
        self.network.make_friends(self.marto, ivo)
        self.network.make_friends(self.marto, self.peshko)
        self.network.make_friends(self.peshko, mina)
        self.network.make_friends(mina, tony)

        self.assertEqual(self.network.connection_level(ivo, mina), 2)

    def test_connection_level_circle(self):
        ivo = Panda("Ivo", "ivo@pandamail.com", "male")

        self.network.make_friends(self.marto, ivo)
        self.network.make_friends(self.marto, self.peshko)
        self.network.make_friends(ivo, self.peshko)

        self.assertEqual(self.network.connection_level(ivo, self.peshko), 1)

    def test_are_pandas_connected(self):
        self.network.make_friends(self.peshko, self.marto)
        self.assertTrue(self.network.connection_level(self.peshko, self.marto) != 0)

        ivo = Panda("Ivo", "ivo@pandamail.com", "male")
        self.assertFalse(self.network.connection_level(self.peshko, ivo) != 0)

    def test_how_many_gender_in_network(self):
        tony = Panda("Tony", "tony@pandamail.com", "female")
        self.network.make_friends(self.marto, self.peshko)
        self.network.make_friends(self.peshko, tony)

        self.assertEqual(self.network.how_many_gender_in_network(1, self.peshko, "female"), 1)


if __name__ == '__main__':
    unittest.main()
