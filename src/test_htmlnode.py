import unittest
from HTMLNode import HTMLNode
from HTMLNode import leafNode
from HTMLNode import ParentNode
from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node


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

    def test_leaf_to_html_p(self):
        node = leafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a(self):
        node = leafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = leafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = leafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = leafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_parent_to_html_no_tag(self):
        child_node = leafNode("span", "child")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError) as context:
            parent_node.to_html()
        self.assertEqual(str(context.exception), "Parent nodes must have a tag")

    def test_text_node_to_html_node_text(self):
        text_node = text_node_to_html_node(
            TextNode("This is a text node", TextType.TEXT)
        )
        self.assertEqual(text_node.to_html(), "This is a text node")        
    def test_text_node_to_html_node_bold(self):
        text_node = text_node_to_html_node(
            TextNode("This is a bold node", TextType.BOLD)
        )
        self.assertEqual(text_node.to_html(), "<strong>This is a bold node</strong>")
    def test_text_node_to_html_node_italic(self):
        text_node = text_node_to_html_node(
            TextNode("This is an italic node", TextType.ITALIC)
        )
        self.assertEqual(text_node.to_html(), "<em>This is an italic node</em>")
    def test_text_node_to_html_node_code(self):
        text_node = text_node_to_html_node(
            TextNode("This is a code node", TextType.CODE)
        )
        self.assertEqual(text_node.to_html(), "<code>This is a code node</code>")
    def test_text_node_to_html_node_link(self):
        text_node = text_node_to_html_node(
            TextNode("This is a link node", TextType.LINK, "https://www.boot.dev")
        )
        self.assertEqual(
            text_node.to_html(),
            '<a href="https://www.boot.dev">This is a link node</a>',
        )
    def test_text_node_to_html_node_image(self):
        text_node = text_node_to_html_node(
            TextNode("This is an image node", TextType.IMAGE, "https://www.boot.dev/image.png")
        )
        self.assertEqual(
            text_node.to_html(),
            '<img src="https://www.boot.dev/image.png" alt="This is an image node">',
        )

if __name__ == "__main__":
    unittest.main()
