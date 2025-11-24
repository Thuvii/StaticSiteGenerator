from src.textnode import *
from src.inline_markdown import *
from src.markdown_block import *
from src.htmlnode import *
from src.copy_static import *
from src.generate_page import *
import re
import os
from pathlib import Path

path_content = "./content/"
path_public = "./public/"
static_path = "./static"
path_public = "./public"
def main():
    if os.path.exists(static_path):
        shutil.rmtree(path_public)
    copy_folder("./static","./public")
    generate_page_recursive(path_content,"template.html",path_public)
    # print(os.listdir(path_content))
 


if __name__ == "__main__":
    main()
    
    
    
    