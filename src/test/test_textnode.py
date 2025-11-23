import unittest

from src.textnode import (TextNode, TextType,text_node_to_html_node)


class TestTextNode(unittest.TestCase):
    #TEST TextNode
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_eq_false2(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node2", TextType.TEXT)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode('helooooooooooooo',TextType.LINK,'https://www.boot.dev')
        outPut = repr(node)
        testOutPut = "TextNode(helooooooooooooo,link,https://www.boot.dev)"
        self.assertEqual(outPut,testOutPut)
    
    
    # test text_node_to_html_node()
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    def test_text2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'b')
        self.assertEqual(html_node.value, "This is a text node")
    def test_text3(self):
        node = TextNode("this is a image", TextType.IMAGE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, 'img')
        self.assertEqual(html_node.value, None)
        self.assertNotEqual(html_node.props, None)
    
    
                

if __name__ == "__main__":
    unittest.main()