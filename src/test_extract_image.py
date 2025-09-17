import unittest
from HTMLNode import HTMLNode
from textnode import TextNode, TextType
from Extract_image import extract_markdown_images
from Extract_image import extract_markdown_links

def test_extract_markdown_images():
    text = "Here is an image: ![Alt text](https://www.example.com/image.png) in the text."
    nodes = extract_markdown_images(text)
    expected_nodes = [
        TextNode("Here is an image: ", TextType.TEXT),
        TextNode("Alt text", TextType.IMAGE, "https://www.example.com/image.png"),
        TextNode(" in the text.", TextType.TEXT),
    ]
    assert nodes == expected_nodes

def test_extract_markdown_links():
    text = "Here is a link: [Link text](https://www.example.com) in the text."
    nodes = extract_markdown_links(text)
    expected_nodes = [
        TextNode("Here is a link: ", TextType.TEXT),
        TextNode("Link text", TextType.LINK, "https://www.example.com"),
        TextNode(" in the text.", TextType.TEXT),
    ]
    assert nodes == expected_nodes

def test_extract_markdown_images_no_images():
    text = "This text has no images."
    nodes = extract_markdown_images(text)
    expected_nodes = [TextNode("This text has no images.", TextType.TEXT)]
    assert nodes == expected_nodes  

def test_extract_markdown_links_no_links():
    text = "This text has no links."
    nodes = extract_markdown_links(text)
    expected_nodes = [TextNode("This text has no links.", TextType.TEXT)]
    assert nodes == expected_nodes      
def test_extract_markdown_images_multiple_images():
    text = "Image one: ![Alt1](https://example.com/img1.png) and Image two: ![Alt2](https://example.com/img2.png)."
    nodes = extract_markdown_images(text)
    expected_nodes = [
        TextNode("Image one: ", TextType.TEXT),
        TextNode("Alt1", TextType.IMAGE, "https://example.com/img1.png"),
        TextNode(" and Image two: ", TextType.TEXT),
        TextNode("Alt2", TextType.IMAGE, "https://example.com/img2.png"),
        TextNode(".", TextType.TEXT),
    ]
    assert nodes == expected_nodes
def test_extract_markdown_links_multiple_links():
    text = "Link one: [Link1](https://example.com/link1) and Link two: [Link2](https://example.com/link2)."
    nodes = extract_markdown_links(text)
    expected_nodes = [
        TextNode("Link one: ", TextType.TEXT),
        TextNode("Link1", TextType.LINK, "https://example.com/link1"),
        TextNode(" and Link two: ", TextType.TEXT),
        TextNode("Link2", TextType.LINK, "https://example.com/link2"),
        TextNode(".", TextType.TEXT),
    ]
    assert nodes == expected_nodes
def test_extract_markdown_images_edge_cases():
    text = "![Alt text](https://example.com/image.png)![Another image](https://example.com/image2.png)"
    nodes = extract_markdown_images(text)
    expected_nodes = [
        TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png"),
        TextNode("Another image", TextType.IMAGE, "https://example.com/image2.png"),
    ]
    assert nodes == expected_nodes