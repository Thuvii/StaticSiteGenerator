from src.textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT or node.text_type == TextType.LINK or node.text_type == TextType.IMAGE :
            new_nodes.append(node)
            continue
        else:
            split_node = []
            split_text = node.text.split(delimiter)
            if len(split_text) % 2 == 0:
                raise Exception('no delimiter')
            for i in range(len(split_text)):
                if split_text[i] =="":
                    continue
                if i % 2 == 0:
                    split_node.append(TextNode(split_text[i],TextType.TEXT))
                else:
                    split_node.append(TextNode(split_text[i],text_type))
        new_nodes.extend(split_node)
    return new_nodes
def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = []
        image_info = extract_markdown_images(node.text)
        if image_info is None or image_info == []:
            new_nodes.append(node)
        else:
            images.extend(image_info)
            curr_text = node.text
            for i in range(len(images)):
                alt_text = images[i][0]
                url = images[i][1]
                sections = curr_text.split(f"![{alt_text}]({url})", 1)
                text_before = sections[0]
                text_after = sections[1]
                if text_before =="":
                    new_nodes.append(TextNode(alt_text,TextType.IMAGE,url))
                else:
                    new_nodes.append(TextNode(text_before,TextType.TEXT,None))
                    new_nodes.append(TextNode(alt_text,TextType.IMAGE,url))
                curr_text = text_after
            if curr_text:
                 new_nodes.append(TextNode(curr_text,TextType.TEXT,None))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = []
        image_info = extract_markdown_links(node.text)
        if image_info is None or image_info == []:
            new_nodes.append(node)
        else:
            images.extend(image_info)
            curr_text = node.text
            for i in range(len(images)):
                alt_text = images[i][0]
                url = images[i][1]
                sections = curr_text.split(f"[{alt_text}]({url})", 1)
                text_before = sections[0]
                text_after = sections[1]
                if text_before =="":
                    new_nodes.append(TextNode(alt_text,TextType.LINK,url))
                else:
                    new_nodes.append(TextNode(text_before,TextType.TEXT,None))
                    new_nodes.append(TextNode(alt_text,TextType.LINK,url))
                curr_text = text_after
            if curr_text:
                 new_nodes.append(TextNode(curr_text,TextType.TEXT,None))
    return new_nodes
def text_to_textnodes(text):
    text_nodes = [TextNode(text,TextType.TEXT)]
    text_nodes = split_nodes_delimiter(text_nodes,"**",TextType.BOLD,)
    text_nodes = split_nodes_delimiter(text_nodes,"_",TextType.ITALIC,)
    text_nodes = split_nodes_delimiter(text_nodes,"`",TextType.CODE,)
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)
    return text_nodes

    
    
