import unittest
from HTMLNode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_node_creation(self):
        node = HTMLNode(tag="div", value="Hello, World!", props={"class": "greeting"})
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Hello, World!")
        self.assertEqual(node.props, {"class": "greeting"})

    def test_props_to_html(self):
        node = HTMLNode(tag="input", props={"type": "text", "value": "Sample"})
        self.assertEqual(node.props_to_html(), ' type="text" value="Sample"')

    def test_repr(self):
        node = HTMLNode(tag="span", value="Hello", props={"class": "text"})
        self.assertEqual(repr(node), "HTMLNode(tag=span, value=Hello, children=[], props={'class': 'text'})")

if __name__ == "__main__":
    unittest.main()
