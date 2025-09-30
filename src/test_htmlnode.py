import unittest
from Block_types import (
    markdown_to_html_node,
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)
from textnode import TextNode, TextType


class Testextract_title(unittest.TestCase):
    def test_extract_title(self):
        from main import extract_title

        self.assertEqual(extract_title("# Hello World"), "Hello World")
        self.assertEqual(extract_title("#   Leading and trailing spaces   "), "Leading and trailing spaces")
        self.assertEqual(extract_title("# Title with # in it #"), "Title with # in it #")
        self.assertEqual(extract_title("# Title with special characters !@#$%^&*()"), "Title with special characters !@#$%^&*()")
        self.assertEqual(extract_title("# 1234567890"), "1234567890")
        self.assertEqual(extract_title("# Title with emojis 😊🚀"), "Title with emojis 😊🚀")

        with self.assertRaises(Exception) as context:
            extract_title("No title here")
        self.assertTrue("No title found" in str(context.exception))

        self.assertEqual(extract_title("## Subtitle\n# Main Title"), "Main Title")
        self.assertEqual(extract_title("# First Title\n# Second Title"), "First Title")
        self.assertEqual(extract_title("# Title\nSome other text\n# Another Title"), "Title")

        self.assertEqual(extract_title("   # Indented Title"), "Indented Title")
        self.assertEqual(extract_title("#TitleWithoutSpace"), "TitleWithoutSpace")

        self.assertEqual(extract_title("### Not a title\n# Actual Title"), "Actual Title")

        self.assertEqual(extract_title("# "), "")
        self.assertEqual(extract_title("#    "), "")

        self.assertEqual(extract_title(""), "Untitled")
        self.assertEqual(extract_title("\n\n\n"), "Untitled")
        self.assertEqual(extract_title("   \n   \n# Title After Blank Lines"), "Title After Blank Lines")
        self.assertEqual(extract_title("# Title with newline\nin it"), "Title with newline")                                
        self.assertEqual(extract_title("# Title with tab\tin it"), "Title with tab\tin it")
        self.assertEqual(extract_title("# Title with multiple   spaces"), "Title with multiple   spaces")
        self.assertEqual(extract_title("# Title with mixed # characters # and #"), "Title")
if __name__ == "__main__":
    unittest.main()
