from enum import Enum
from src.htmlnode import HTMLNode, LeafNode,ParentNode
from src.inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes)

from src.textnode import TextNode, TextType,text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    OLIST = "ordered_list"
    ULIST = "unordered_list"
    

def markdown_to_block(markdown):
    split_md = markdown.split("\n\n")
    res = []
    for i in split_md:
        if i == "":
            continue
        i = i.strip()
        res.append(i)
    return res

def block_to_blockType(block):
    lines = block.split('\n')
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].endswith("```"):
        return BlockType.CODE
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f'{i}. '):
                return BlockType.PARAGRAPH
            i = i + 1
        return BlockType.OLIST
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    return BlockType.PARAGRAPH




def block_to_html_node(block):
    b_type = block_to_blockType(block)
    if b_type == BlockType.CODE:
        return code_to_htmlnode(block)
    elif b_type == BlockType.PARAGRAPH:
        return paragraph_to_htmlnode(block)
    elif b_type == BlockType.HEADING:
       return heading_to_htmlnode(block)
    elif b_type == BlockType.OLIST:
       return olist_to_htmlnode(block)
    elif b_type == BlockType.ULIST:
        return ulist_to_htmlnode(block)
    elif b_type == BlockType.QUOTE:
       return quote_to_htmlnode(block)
    else:
        raise Exception('can\'t find BlockType')

def text_to_children(block):
    text = []
    textnodes = text_to_textnodes(block)
    for textnode in textnodes:
        textnode = text_node_to_html_node(textnode)
        text.append(textnode)
    return text

def list_to_children(block):
    res = []
    blocktype = block_to_blockType(block)
    text_list = block.split("\n")
    for t in text_list:
        if BlockType.OLIST == blocktype:
            if t == "":
                continue
            else:
                text = t[3:]
                value = text_to_children(text)
                res.append(ParentNode('li',value))
        elif BlockType.ULIST == blocktype :
            if t == "":
                continue
            else:
                text = t[2:]
                value = text_to_children(text)
                res.append(ParentNode('li',value))
    return res

def paragraph_to_htmlnode(block):
    b_text = " ".join(block.split("\n"))
    b_children = text_to_children(b_text)
    return ParentNode('p',b_children)
def heading_to_htmlnode(block):
    level = 0
    for char in block:
        if char == "#":
            level +=1
    if level + 1 > len(block):
        raise ValueError('Invalid heading')
    b_text = block[level+1:]
    b_children = text_to_children(b_text)
    return ParentNode(f'h{level}',b_children)
def olist_to_htmlnode(block):
    b_children = list_to_children(block)
    return ParentNode('ol',b_children)
def ulist_to_htmlnode(block):
    b_children = list_to_children(block)
    return ParentNode('ul',b_children)
def quote_to_htmlnode(block):
    lines = block.split('\n')
    new = []
    for line in lines:  
        if not line.startswith(">"):
            raise ValueError('not a quote')
        new_line = line[2:]
        new.append(new_line)
    content = " ".join(new)
    children = text_to_children(content)
    return ParentNode('blockquote',children)
def code_to_htmlnode(block):
    block = block[4:]
    block = block[:-3]
    textnode = TextNode(block, TextType.CODE)
    b_children = text_node_to_html_node(textnode)
    return ParentNode('pre',[b_children])


def markdown_to_html_node(markdown):
    blocks = markdown_to_block(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)

def extract_title(md):
    blocks = markdown_to_block(md)
    if blocks[0].startswith("# "):
        return blocks[0][2:]
    else:
        raise Exception('Does not have a title')