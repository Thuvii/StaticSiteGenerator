from src.textnode import *
from src.inline_markdown import *
from src.markdown_block import *
from src.htmlnode import *
import re


def main():
    md ="""
>value1
>value2
"""
    
    print(markdown_to_html_node(md))
      
    


        
  
    
if __name__ == "__main__":
    main()
    
    
    
    