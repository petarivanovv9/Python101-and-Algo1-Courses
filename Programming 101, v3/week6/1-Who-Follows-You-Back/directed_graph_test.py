import unittest
from directed_graph import DirectedGraph
from directed_graph import AlreadyThere
from directed_graph import CantFollowYourself


class Test_DirectedGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()

    def test_add_node(self):
        self.graph.add_node("Pesho")
        self.assertTrue("Pesho" in self.graph.nodes.keys())

        with self.assertRaises(AlreadyThere):
            self.graph.add_node("Pesho")

    def test_add_edge(self):
        self.graph.add_edge("Pesho", "Kriso")
        self.assertEqual(self.graph.nodes["Pesho"], {"Kriso"})
        self.assertEqual(self.graph.nodes["Kriso"], set())

        with self.assertRaises(CantFollowYourself):
            self.graph.add_edge("Pesho", "Pesho")

    def test_get_neighbours_for(self):
        self.graph.add_edge("Pesho", "Kriso")
        self.graph.add_edge("Pesho", "Mincho")
        self.graph.add_edge("Kriso", "Mincho")
        self.assertEqual(self.graph.nodes["Pesho"], set(["Kriso", "Mincho"]))
        self.assertEqual(self.graph.nodes["Kriso"], set(["Mincho"]))
        self.assertEqual(self.graph.nodes["Mincho"], set())

    def test_path_between(self):
        self.graph.add_edge("Pesho", "Kriso")
        self.graph.add_edge("Pesho", "Mincho")
        self.graph.add_edge("Kriso", "Mincho")
        self.graph.add_edge("Mincho", "Choko")
        self.graph.add_node("Strahil")

        self.assertFalse(self.graph.path_between("Kriso", "Pesho"))
        self.assertTrue(self.graph.path_between("Pesho", "Choko"))
        self.assertTrue(self.graph.path_between("Pesho", "Mincho"))
        self.assertFalse(self.graph.path_between("Pesho", "Strahil"))

    def test_are_connected(self):
        pass


if __name__ == '__main__':
    unittest.main()
