from textnode import TextNode, TextType
from HTMLNode import leafNode, ParentNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return leafNode(tag=None, value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return leafNode(tag="strong", value=text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return leafNode(tag="em", value=text_node.text)
    elif text_node.text_type == TextType.CODE:
        return leafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.LINK:
        return leafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return leafNode(tag="img", props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"Unknown TextType: {text_node.text_type}")